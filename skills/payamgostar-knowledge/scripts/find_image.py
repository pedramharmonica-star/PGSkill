#!/usr/bin/env python3
"""Find help-center screenshots by topic.

Usage: python3 find_image.py "<query>" [--top 8] [--json]
Searches references/kb-images-index.csv (alt text, section, article title, nearby text, path).
Prints id, repo path (kb-assets/..., from the PGSkill repo root), public URL and context.
Standard library only.
"""
import csv, json, math, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "..", "references", "kb-images-index.csv")

def toks(s):
    s = s.lower().replace("‌", " ").replace("ي", "ی").replace("ك", "ک")
    return [t for t in re.split(r"[^\w]+", s) if len(t) > 1]

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); return
    top = int(a[a.index("--top") + 1]) if "--top" in a else 8
    as_json = "--json" in a
    q = toks(a[0])
    rows = list(csv.DictReader(open(INDEX, encoding="utf-8")))
    fields = lambda r: (r["alt"] + " ") * 3 + (r["section"] + " ") * 2 + r["article_title"] + " " + r["context"] + " " + r["source_path"].replace("/", " ").replace("-", " ")
    docs = [collections.Counter(toks(fields(r))) for r in rows]
    df = collections.Counter(t for d in docs for t in set(d))
    N = len(docs)
    scored = []
    for r, d in zip(rows, docs):
        s = sum((1 + math.log(d[t])) * math.log(1 + N / df[t]) for t in q if d[t])
        if s: scored.append((s, r))
    scored.sort(key=lambda x: -x[0])
    seen, out = set(), []
    for s, r in scored:
        if r["id"] in seen: continue
        seen.add(r["id"]); out.append(dict(r, score=round(s, 2)))
        if len(out) >= top: break
    if as_json:
        print(json.dumps(out, ensure_ascii=False, indent=1)); return
    for r in out:
        print(f"[{r['score']}] {r['id']}  {r['image']}  ({r['width']}x{r['height']})")
        print(f"    مقاله: {r['article_title']} › {r['section']}  ·  alt: {r['alt'] or '—'}")
        print(f"    URL عمومی: {r['public_url']}")
        print(f"    متن نزدیک: {r['context'][-160:]}\n")

if __name__ == "__main__":
    main()
