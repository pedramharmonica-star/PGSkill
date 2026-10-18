#!/usr/bin/env python3
"""Read one indexed official source on demand; do not republish source documents."""
import argparse,gzip,html.parser,json,pathlib,re,subprocess,tempfile,urllib.parse,urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
class TextParser(html.parser.HTMLParser):
 def __init__(self,article=False):
  super().__init__();self.skip=0;self.parts=[];self.article=article;self.depth=0;self.inside=not article
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if self.article and not self.inside and tag=='div' and 'parent' in attrs.get('class','').split():self.inside=True;self.depth=1
  elif self.article and self.inside and tag=='div':self.depth+=1
  if not self.inside:return
  if tag in ('script','style'):self.skip+=1
  if not self.skip and tag in ('p','div','h1','h2','h3','h4','li','tr','br','pre'):self.parts.append('\n')
  if not self.skip and tag in ('td','th'):self.parts.append(' | ')
 def handle_endtag(self,tag):
  if not self.inside:return
  if tag in ('script','style'):self.skip=max(0,self.skip-1)
  if not self.skip and tag in ('p','div','li','tr','pre'):self.parts.append('\n')
  if self.article and tag=='div':
   self.depth-=1
   if self.depth==0:self.inside=False
 def handle_data(self,data):
  if self.inside and not self.skip:self.parts.append(data)
 def text(self):return re.sub(r'\n[ \t]*\n+', '\n\n', ''.join(self.parts)).strip()

def permitted(url):
 p=urllib.parse.urlsplit(url)
 return p.scheme=='https' and (p.hostname in ('help.payamgostar.com','developer.payamgostar.com') or (p.hostname=='raw.githubusercontent.com' and any(p.path.startswith(prefix) for prefix in ('/1stco/PayamGostarDocs/','/1stco/PayamGostarApiSamples/'))))
class SourceRedirectHandler(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  if not permitted(newurl):raise ValueError('Redirect outside source allowlist')
  return super().redirect_request(req,fp,code,msg,headers,newurl)

def read(row,latest=False):
 errors=[]
 urls=[row.get('live_read_url') or row.get('read_url'),row.get('live_fallback_url')] if latest else [row.get('read_url'),row.get('fallback_url')]
 for url in dict.fromkeys(urls):
  if not url:continue
  if not permitted(url):errors.append('Source outside allowlist');continue
  try:
   request=urllib.request.Request(urllib.parse.quote(url,safe=':/?=&%'),headers={'User-Agent':'PayamGostarKnowledgeResearch/1.0'})
   with urllib.request.build_opener(SourceRedirectHandler()).open(request,timeout=40) as r:
    if not permitted(r.url):raise ValueError('Redirect outside source allowlist')
    b=r.read(20*1024*1024+1);ctype=r.headers.get('Content-Type','')
   if len(b)>20*1024*1024:raise ValueError('Source exceeds 20 MiB limit')
   if b.startswith(b'PK\x03\x04'):raise ValueError('Binary Office/archive attachment: use the appropriate document reader; this reader supports text, HTML and PDF.')
   if b.startswith(b'%PDF'):
    with tempfile.TemporaryDirectory() as tmp:
     path=pathlib.Path(tmp)/'source.pdf';path.write_bytes(b)
     result=subprocess.run(['pdftotext','-layout',str(path),'-'],capture_output=True,check=True)
     text='\n'.join(f'\n[PDF page {i}]\n{p}' for i,p in enumerate(result.stdout.decode('utf8','replace').split('\f'),1) if p.strip())
   elif 'raw.githubusercontent.com' not in url and ('html' in ctype or b.lstrip().startswith(b'<')):
    parser=TextParser(article='rendercontent' in url);parser.feed(b.decode('utf-8-sig','replace'));text=parser.text()
    if 'rendercontent' in url and not re.search(r'<div[^>]+class="[^"]*\bparent\b',b.decode('utf8','replace')):raise ValueError('Article body missing; shell is not evidence')
   else:text=b.decode('utf-8-sig','replace')
   if not text.strip():raise ValueError('Empty source text')
   return url,text
  except Exception as exc:errors.append(f'{url}: {type(exc).__name__}: {exc}')
 raise RuntimeError('\n'.join(errors))
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('source_id');p.add_argument('--latest',action='store_true',help='Read the current official repository branch when a live URL is indexed. This does not prove deployment availability.');p.add_argument('--offset',type=int,default=0);p.add_argument('--max-chars',type=int,default=30000);a=p.parse_args()
 if a.offset<0 or not 1<=a.max_chars<=100000:p.error('Invalid text range')
 rows=[json.loads(line) for path in sorted((ROOT/'references/source-index').glob('*.jsonl.gz')) for line in gzip.decompress(path.read_bytes()).decode('utf-8').splitlines() if line.strip()];row=next((r for r in rows if r['id']==a.source_id),None)
 if row is None:p.error('Unknown source ID; use search_kb.py first')
 try:url,text=read(row,latest=a.latest)
 except Exception as exc:p.exit(1,str(exc)+'\n')
 end=a.offset+a.max_chars
 print(json.dumps({'id':row['id'],'source_class':row['source'],'indexed_status':row['status'],'title':row['title'],'citation_url':row['url'],'actual_read_url':url,'latest_requested':a.latest,'pinned_snapshot':bool(re.search(r'raw\.githubusercontent\.com/[^/]+/[^/]+/[0-9a-f]{40}/',url)),'offset':a.offset,'total_chars':len(text),'next_offset':end if end<len(text) else None,'text':text[a.offset:end],'notice':'Check actual_read_url and pinned_snapshot. Re-reading a pinned repository commit does not refresh its content; use --latest and check current official indexes for freshness. A static PDF URL may still be an old document. PDF RTL tables need visual verification when ambiguous.'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
