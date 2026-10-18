"""Archive every compiled page from the official Phoenix documentation site."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlsplit
from collections import Counter
from bs4 import BeautifulSoup
import requests, re, json, hashlib, threading
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'Phoenix'; ORIGIN='https://docs.phoenixdevt.fr'
PROJECTS={'mmoitems':'MMOItems','mmocore':'MMOCore','mmoinventory':'MMOInventory','mmoprofiles':'MMOProfiles','mythiclib':'MythicLib','bounty-hunters':'BountyHunters','contracts':'Contracts'}
ARCHIVES={'mi-stat-config-fmt':'MMOItems','new-custom-blocks':'MMOItems','mmocore-anticheats':'MMOCore','mmocore-convert-to-sql':'MMOCore','mmocore-def-stat-values':'MMOCore'}
state=threading.local()
def session():
 if not hasattr(state,'s'):state.s=requests.Session()
 return state.s
def read_json_var(text,name):
 m=re.search(r'window\.'+re.escape(name)+r'=JSON.parse\(("(?:[^"\\]|\\.)*")\)',text)
 if not m:raise ValueError('Missing official site data: '+name)
 return json.loads(json.loads(m[1]))
home=session().get(ORIGIN+'/',timeout=40);home.raise_for_status();home.encoding='utf-8'
hashes=read_json_var(home.text,'__VP_HASH_MAP__');site=read_json_var(home.text,'__VP_SITE_DATA__')
(BASE/'sources/site-data.json').write_text(json.dumps(site,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(BASE/'sources/page-hashes.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def get_page(key):
 path=key[:-3].replace('_','/')
 if path=='index':path=''
 elif path.endswith('/index'):path=path[:-5]
 if path=='readme':path='README'
 url=ORIGIN+'/'+path
 group=path.split('/')[0]
 project=PROJECTS.get(group,'Phoenix')
 if group=='archive':project=ARCHIVES.get(path.split('/')[-1],'Phoenix');filename='archive/'+path.split('/')[-1]+'.md'
 elif group in PROJECTS:filename=path[len(group):].strip('/') or 'index';filename=filename+'.md'
 else:filename='index.md' if not path else ('site-maintenance.md' if path=='README' else path+'.md')
 target=ROOT/project/'sources/live'/key.replace('.md','.html')
 if target.exists():data=target.read_bytes();status=200;headers={}
 else:
  for attempt in range(3):
   try:
    r=session().get(url,timeout=(15,50));r.raise_for_status();data=r.content;status=r.status_code;headers=dict(r.headers);break
   except Exception:
    if attempt==2:raise
  target.write_bytes(data)
 soup=BeautifulSoup(data,'html.parser');main=soup.select_one('main') or soup.select_one('.VPHome')
 if not main:raise ValueError('No main document: '+url)
 title=soup.title.get_text().removesuffix(' | Phoenix Wiki') if soup.title else ''
 return {'key':key,'project':project,'path':'/'+path,'url':url,'file':filename,'html':str(target.relative_to(ROOT/project)).replace('\\','/'),'title':title,'hash':hashes[key],'sha256':hashlib.sha256(data).hexdigest(),'main_chars':len(main.get_text()),'etag':headers.get('ETag'),'last_modified':headers.get('Last-Modified')}
rows=[];errors=[]
with ThreadPoolExecutor(max_workers=6) as pool:
 jobs={pool.submit(get_page,k):k for k in hashes}
 for n,f in enumerate(as_completed(jobs),1):
  try:rows.append(f.result())
  except Exception as e:errors.append({'key':jobs[f],'error':str(e)[:250]})
  if n%40==0 or n==len(jobs):print('Archived',n,'/',len(jobs),flush=True)
rows.sort(key=lambda r:r['key'])
(BASE/'sources/pages.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for project in ['Phoenix']+list(PROJECTS.values()):
 selected=[r for r in rows if r['project']==project]
 (ROOT/project/'sources/pages.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n',encoding='utf-8') if project!='Phoenix' else None
(BASE/'sources/archive.json').write_text(json.dumps({'source':ORIGIN,'snapshot_date':'2026-10-19','pages':len(rows),'site_data_sha256':hashlib.sha256(home.content).hexdigest(),'projects':dict(Counter(r['project'] for r in rows)),'errors':errors},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pages':len(rows),'projects':dict(Counter(r['project'] for r in rows)),'empty_pages':[r['url'] for r in rows if r['main_chars']<5],'errors':errors},ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
