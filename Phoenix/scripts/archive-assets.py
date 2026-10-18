"""Save native source images without resampling or changing their formats."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from concurrent.futures import ThreadPoolExecutor,as_completed
import json,re,requests,hashlib,base64,threading
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'Phoenix'
items=json.loads((BASE/'sources/asset-urls.json').read_text(encoding='utf-8'));state=threading.local()
def download(info):
 project,url=info['project'],info['url'];key=hashlib.sha256(url.encode()).hexdigest()[:12]
 if not hasattr(state,'session'):state.session=requests.Session()
 if url.startswith('data:'):
  header,payload=url.split(',',1);data=base64.b64decode(payload) if ';base64' in header else unquote(payload).encode();ctype=header[5:].split(';')[0];name='embedded.'+ctype.split('/')[-1]
 else:
  r=state.session.get(url,timeout=(15,45));r.raise_for_status();data=r.content;ctype=r.headers.get('Content-Type','').split(';')[0];name=unquote(urlsplit(url).path).rsplit('/',1)[-1]
  if not ctype.startswith(('image/','video/','audio/')):raise ValueError('Not media: '+ctype+' '+url)
 name=re.sub(r'[^A-Za-z0-9_.-]','-',name)
 file='assets/'+key+'-'+name
 target=ROOT/project/'docs'/file;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
 return {**info,'file':file,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'content_type':ctype}
rows=[];errors=[]
with ThreadPoolExecutor(max_workers=6) as pool:
 jobs={pool.submit(download,i):i for i in items}
 for n,f in enumerate(as_completed(jobs),1):
  try:rows.append(f.result())
  except Exception as e:errors.append({'project':jobs[f]['project'],'url':jobs[f]['url'][:180],'error':str(e)[:200]})
  if n%30==0 or n==len(jobs):print('Assets',n,'/',len(jobs),flush=True)
rows.sort(key=lambda i:(i['project'],i['url']))
(BASE/'sources/all-assets.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for p in sorted({i['project'] for i in items}):
 (ROOT/p/'sources/assets.json').write_text(json.dumps([i for i in rows if i['project']==p],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'assets':len(rows),'bytes':sum(r['bytes'] for r in rows),'errors':errors},ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
