#!/usr/bin/env python3
"""Rebuild references/kb from the official docs repo.
Usage: python3 convert_kb.py <PayamGostarDocs clone> <out dir> [commit]
Strips images/HTML, redacts credentials, groups articles by menu section, writes _index.json."""
import os,re,sys,json,collections
SRC=sys.argv[1]  # clone of https://github.com/1stco/PayamGostarDocs
OUT=sys.argv[2]  # e.g. references/kb
COMMIT=sys.argv[3] if len(sys.argv)>3 else 'e6143c66b1746f251ae840745e7fe070607aee10'
BLOB=f'https://github.com/1stco/PayamGostarDocs/blob/{COMMIT}/'
os.makedirs(OUT,exist_ok=True)
def clean(t):
    t=re.sub(r'!\[[^\]]*\]\([^)]*\)','',t)                    # md images
    t=re.sub(r'data:[a-z/+]+;base64,[A-Za-z0-9+/=]+','',t)
    t=re.sub(r'<(img|video|source|iframe)[^>]*>','',t,flags=re.I)
    t=re.sub(r'<br\s*/?>','\n',t,flags=re.I)
    t=re.sub(r'</?(p|div|span|center|font|b|strong|i|u|sup|sub|a|details|summary|figure|figcaption)[^>]*>','',t,flags=re.I)
    t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    t=re.sub(r'\[([^\]]+)\]\((?!http)[^)]*\)',r'\1',t)        # relative links -> text
    t=re.sub(r'&nbsp;',' ',t)
    t=re.sub(r'(?im)(password|username|پسورد|رمز عبور)\s*[:：]\s*\S[^\n/]*','\\1: [حذف‌شده]',t)
    t=re.sub(r'[ \t]+\n','\n',t); t=re.sub(r'\n{3,}','\n\n',t)
    return t.strip()
def ver(name):
    m=re.search(r'(\d+\.\d+(?:\.\d+)*)',name); return m.group(1) if m else ''
groups=collections.defaultdict(list); index=[]
for dp,ds,fs in os.walk(SRC):
    ds[:]=[d for d in ds if d!='.git']
    for f in sorted(fs):
        if not f.endswith('.md') or f in('README.md',): continue
        p=os.path.join(dp,f); rel=os.path.relpath(p,SRC)
        if rel.startswith('Other/') and f in ('test.md','MyTest.md','PicTest.md','Sample.md','Alovoiptest.md'): continue
        raw=open(p,encoding='utf-8',errors='replace').read()
        body=clean(raw)
        if len(body)<40: continue
        m=re.search(r'^#\s+(.+)$',body,re.M)
        title=(m.group(1).strip() if m else f[:-3]).strip('# ')
        parts=rel.split('/')
        # group: top + second (+third for big sections)
        if parts[:3]==['Help','Settings','Personalization-crm'] and len(parts)>4:
            g='-'.join(parts[:4]) if parts[3]!='Overview' else '-'.join(parts[:5])
        elif parts[0]=='Help' and parts[1] in ('Settings','Integrated-bank','Management-and-reports','Marketing') and len(parts)>3:
            g='-'.join(parts[:3])
        else:
            g='-'.join(parts[:2]) if len(parts)>2 else parts[0]
        g=re.sub(r"[^A-Za-z0-9\-]",'',g)
        v=ver(rel)
        # demote headings inside article by 2 levels
        body=re.sub(r'^(#{1,4})\s',lambda mm:'#'*(len(mm.group(1))+2)+' ',body,flags=re.M)
        groups[g].append((rel,title,v,body))
        index.append({'file':g+'.md','path':rel,'title':title,'doc_version':v,'chars':len(body),'url':BLOB+rel})
for g,arts in groups.items():
    out=[f'# مستندات رسمی پیام‌گستر — {g}','',f'منبع: مخزن رسمی 1stco/PayamGostarDocs (commit {COMMIT[:12]}، ۱۴۰۵/۰۶/۱۴) — متن مقاله‌های help.payamgostar.com/docs. تصاویر حذف شده‌اند؛ جزئیات داخل تصویر در این متن نیست.','']
    for rel,title,v,body in arts:
        out.append(f'## {title}')
        out.append(f'`مسیر سند: {rel}`' + (f' · `نسخه سند: {v}`' if v else '') + f' · [منبع]({BLOB}{rel})')
        out.append(''); out.append(re.sub(r'^###\s+'+re.escape(title)+r'\s*\n','',body,count=1)); out.append('')
    open(os.path.join(OUT,g+'.md'),'w').write('\n'.join(out))
json.dump(index,open(os.path.join(OUT,'_index.json'),'w'),ensure_ascii=False,indent=0)
sz=sorted(((os.path.getsize(os.path.join(OUT,g+'.md')),g,len(a)) for g,a in groups.items()),reverse=True)
print(len(index),'articles',len(groups),'files', sum(s for s,_,_ in sz),'bytes')
for s,g,n in sz[:12]: print(s,n,g)
