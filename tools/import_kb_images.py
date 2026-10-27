#!/usr/bin/env python3
"""Import the screenshots of the official help center into PGSkill (read-only on the source).

Usage (from repo root):
  python3 tools/import_kb_images.py <clone of 1stco/PayamGostarDocs> [commit]

Reads the source clone only; never writes to it. Produces:
  kb-assets/kb-images/<source path>.webp       every image that an article references (WebP, max 1600 px wide)
  kb-assets/image-map.json                      {article path: {raw reference: image id}} for convert_kb.py
  skills/payamgostar-knowledge/references/kb-images-index.csv
                                                one row per (image, article): id, repo path, public URL,
                                                article, section heading, alt text, nearby text, size
Then run convert_kb.py to rebuild references/kb with image markers.
"""
import csv, json, os, re, sys, urllib.parse
from PIL import Image

SRC = os.path.abspath(sys.argv[1])
COMMIT = sys.argv[2] if len(sys.argv) > 2 else 'e6143c66b1746f251ae840745e7fe070607aee10'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'kb-assets')
IMG_OUT = os.path.join(OUT, 'kb-images')
INDEX = os.path.join(ROOT, 'skills', 'payamgostar-knowledge', 'references', 'kb-images-index.csv')
RAW = f'https://raw.githubusercontent.com/1stco/PayamGostarDocs/{COMMIT}/'
MAXW, QUALITY = 1600, 80
SKIP_MD = ('test.md', 'MyTest.md', 'PicTest.md', 'Sample.md', 'Alovoiptest.md', 'README.md')

imgs, by_base = {}, {}
for dp, ds, fs in os.walk(SRC):
    ds[:] = [d for d in ds if d != '.git']
    for f in fs:
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            rel = os.path.relpath(os.path.join(dp, f), SRC)
            imgs[rel.lower()] = rel
            by_base.setdefault(f.lower(), []).append(rel)

RX = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)|<img[^>]*?src=["\']([^"\']+)["\'][^>]*>', re.I)
RAW_RX = re.compile(r'https?://raw\.githubusercontent\.com/1stco/PayamGostarDocs/[^/]+/(.+)', re.I)
GH_RX = re.compile(r'https?://github\.com/1stco/PayamGostarDocs/(?:blob|raw)/[^/]+/(.+)', re.I)

def resolve(md_rel, ref):
    ref = ref.strip().split(' "')[0].strip('<>').split('#')[0].split('?')[0]
    if ref.startswith('data:'): return None, 'data'
    m = RAW_RX.match(ref) or GH_RX.match(ref)
    if m:
        cand = os.path.normpath(urllib.parse.unquote(m.group(1)))
    elif ref.startswith('http'):
        return None, 'external'
    else:
        cand = os.path.normpath(os.path.join(os.path.dirname(md_rel), urllib.parse.unquote(ref)))
    if cand.lower() in imgs: return imgs[cand.lower()], 'ok'
    base = os.path.basename(cand).lower()
    if len(by_base.get(base, [])) == 1: return by_base[base][0], 'basename'
    return None, 'missing'

def plain(s):
    s = re.sub(r'<[^>]+>', ' ', s); s = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s); s = re.sub(r'[*_`>#|]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def out_path(src_rel):
    p = re.sub(r'\s+', '_', os.path.splitext(src_rel)[0]) + '.webp'
    return p.replace('\\', '/')

ids, rows, amap, stats = {}, [], {}, {'ok': 0, 'basename': 0, 'missing': 0, 'external': 0, 'data': 0}
for dp, ds, fs in os.walk(SRC):
    ds[:] = sorted(d for d in ds if d != '.git')
    for f in sorted(fs):
        if not f.endswith('.md') or f in SKIP_MD: continue
        md_rel = os.path.relpath(os.path.join(dp, f), SRC)
        text = open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()
        title = (re.search(r'^#\s+(.+)$', text, re.M) or [None, f[:-3]])[1].strip('# ').strip()
        for m in RX.finditer(text):
            alt = (m.group(1) or '').strip()
            ref = m.group(2) or m.group(3)
            src_rel, st = resolve(md_rel, ref)
            stats[st] += 1
            if not src_rel: continue
            if src_rel not in ids:
                ids[src_rel] = f'IMG-{len(ids) + 1:04d}'
            iid = ids[src_rel]
            amap.setdefault(md_rel, {})[ref] = iid
            before = text[:m.start()]
            heads = re.findall(r'^#{1,6}\s+(.+)$', before, re.M)
            ctx = plain(before[-700:])[-220:]
            rows.append({'id': iid, 'image': 'kb-assets/kb-images/' + out_path(src_rel), 'source_path': src_rel,
                         'public_url': RAW + urllib.parse.quote(src_rel), 'article': md_rel, 'article_title': title,
                         'section': plain(heads[-1]) if heads else title, 'alt': alt, 'context': ctx})

os.makedirs(IMG_OUT, exist_ok=True)
sizes = {}
for src_rel, iid in ids.items():
    dst = os.path.join(IMG_OUT, out_path(src_rel))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im = Image.open(os.path.join(SRC, src_rel))
    if im.mode not in ('RGB', 'RGBA'): im = im.convert('RGBA')
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    sizes[iid] = im.size
    if not os.path.exists(dst):
        im.save(dst, 'WEBP', quality=QUALITY, method=4)
for r in rows:
    r['width'], r['height'] = sizes[r['id']]

json.dump({'commit': COMMIT, 'images': {iid: 'kb-assets/kb-images/' + out_path(s) for s, iid in ids.items()},
           'refs': amap}, open(os.path.join(OUT, 'image-map.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
with open(INDEX, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
videos = [os.path.relpath(os.path.join(dp, f), SRC) for dp, ds, fs in os.walk(SRC) if '.git' not in dp
          for f in fs if f.lower().endswith('.mp4')]
print(json.dumps({'unique_images': len(ids), 'references': len(rows), 'resolution': stats,
                  'all_images_in_source': len(imgs), 'videos_not_imported': videos}, ensure_ascii=False, indent=1))
