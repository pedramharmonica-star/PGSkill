#!/usr/bin/env python3
"""Search source cards locally. Standard library only; no network or mutations."""
import argparse,collections,gzip,json,math,pathlib,re,unicodedata
ROOT=pathlib.Path(__file__).resolve().parents[1]
TRANS=str.maketrans('يكىةؤإأۀ۱۲۳۴۵۶۷۸۹۰٠١٢٣٤٥٦٧٨٩','یکیهوااه12345678900123456789')
def normalize(s):
 s=unicodedata.normalize('NFKC',s).translate(TRANS).lower().replace('\u200c',' ')
 s=re.sub(r'[\u064b-\u065f\u0670ـ]','',s)
 for a,b in [('پیشفاکتور','پیش فاکتور'),('یکبار','یک بار'),('تائید','تایید')]:s=s.replace(a,b)
 return s
def tokens(s):return re.findall(r'[^\W_]+',normalize(s))
def load_sources():
 return [json.loads(line) for path in sorted((ROOT/'references/source-index').glob('*.jsonl.gz')) for line in gzip.decompress(path.read_bytes()).decode('utf-8').splitlines() if line.strip()]
def load_cards():
 return {row['id']:row['text'] for path in sorted((ROOT/'references/card-index').glob('*.jsonl.gz')) for row in map(json.loads,gzip.decompress(path.read_bytes()).decode('utf-8').splitlines())}
def read_card(source_id):
 row=next((r for r in load_sources() if r['id']==source_id),None)
 if row is None:raise ValueError('Unknown source ID')
 card=next((r for r in map(json.loads,gzip.decompress((ROOT/row['card']).read_bytes()).decode('utf-8').splitlines()) if r['id']==source_id),None)
 if card is None:raise ValueError('Source card missing')
 return {**row,'text':card['text']}
def search(query,source=None,limit=8):
 rows=load_sources();cards=load_cards()
 rows=[r for r in rows if r.get('card') and ((r.get('source')!='community') if source is None else r.get('source')==source)]
 terms=[t for t in tokens(query) if t not in {'به','از','در','با','برای','و','یا','آیا','است','را'}]
 if not terms:return []
 docs=[];df=collections.Counter()
 for r in rows:
  text=cards[r['id']];ts=collections.Counter(tokens(text));df.update(ts.keys());docs.append((r,text,ts))
 n=len(docs);avg=sum(sum(ts.values()) for _,_,ts in docs)/max(n,1);out=[]
 for r,text,ts in docs:
  length=sum(ts.values());score=0;matched=0
  for term in set(terms):
   f=ts[term]
   if f:
    matched+=1;score+=math.log(1+(n-df[term]+.5)/(df[term]+.5))*f*2.2/(f+1.2*(.25+.75*length/max(avg,1)))
  if not matched:continue
  title=normalize(r.get('title',''))
  score+=sum(1.5*math.log(1+(n-df[t]+.5)/(df[t]+.5)) for t in set(terms) if t in title)
  score*=(matched/len(set(terms)))**3
  if r.get('status')=='pdf_text_indexed' and not r.get('primary_api_document'):score*=.8
  if r.get('source')=='community':score*=.4
  if r.get('status') in ['navigation_only','media_only']:score*=.5
  if r.get('status') in ['fetch_error','parse_error']:score*=.15
  out.append((score,r,text))
 out.sort(key=lambda x:(-x[0],x[1]['id']))
 unique=[];seen=set()
 for score,r,text in out:
  key=r.get('repository_source_id') or (r['id'] if r['id'].startswith('repo-') else r.get('text_sha256',r['id']))
  if key in seen:continue
  seen.add(key);unique.append((score,r,text))
  if len(unique)==limit:break
 return [{'score':round(s,3),**r,'read_card_command':'python scripts/search_kb.py --card '+r['id'],'preview':text[:1600]} for s,r,text in unique]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('query',nargs='?');p.add_argument('--card',help='Read one complete indexed card by source ID');p.add_argument('--source',choices=['help','release','developer','community']);p.add_argument('--limit',type=int,default=8);a=p.parse_args()
 if a.card:
  if a.query:p.error('Use either a query or --card')
  try:result=read_card(a.card)
  except ValueError as exc:p.error(str(exc))
 elif a.query:
  if not 1<=a.limit<=50:p.error('--limit must be between 1 and 50')
  result={'query':a.query,'results':search(a.query,a.source,a.limit),'note':'Read complete cards with --card SOURCE_ID and verify official source text before detailed or contractual claims.'}
 else:p.error('Provide a query or --card SOURCE_ID')
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
