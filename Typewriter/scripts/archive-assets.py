"""Archive images and original example/video files referenced by the translated docs."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from concurrent.futures import ThreadPoolExecutor,as_completed
import hashlib,json,re,requests,time,shutil
BASE=Path(__file__).resolve().parents[1]
COMMIT=json.loads((BASE/'sources/source-info.json').read_text(encoding='utf-8-sig')).get('commit','9b0a087150c594120d6b89b158f3402bb9d85142')
urls=set()
for path in (BASE/'sources/en').rglob('*.md'):
    text=path.read_text(encoding='utf-8')
    for m in re.finditer(r'!\[[^\]]*\]\(([^\n]+?)\)|<(?:video|source)[^>]*\bsrc="([^"]+)"|\[[^\]]*\]\(([^\n]+?\.(?:json|zip|png|gif|mp4|webm|jpg|avif|riv))\)',text):
        urls.add(next(x for x in m.groups() if x))
manifest={};errors=[]
def fetch(url):
    parts=urlsplit(url);name=unquote(parts.path.rsplit('/',1)[-1]);digest=hashlib.sha256(url.encode()).hexdigest()[:12]
    file='assets/'+digest+'-'+name
    target=BASE/'docs'/file;target.parent.mkdir(exist_ok=True,parents=True)
    if '/documentation/' in url and parts.netloc=='raw.githubusercontent.com':
        source=BASE/'sources/repository'/url.split('/documentation/',1)[1]
        if not source.is_file():raise ValueError('Source missing: '+str(source))
        if not target.exists():shutil.copyfile(source,target)
    elif not target.exists():
        for attempt in range(3):
            try:
                r=requests.get(url,timeout=45);r.raise_for_status();target.write_bytes(r.content);break
            except Exception:
                if attempt==2:raise
                time.sleep(1)
    data=target.read_bytes()
    return url,{'file':file,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
with ThreadPoolExecutor(max_workers=8) as pool:
    jobs={pool.submit(fetch,u):u for u in urls}
    for f in as_completed(jobs):
        try:u,row=f.result();manifest[u]=row
        except Exception as exc:errors.append({'url':jobs[f],'error':str(exc)})
(BASE/'sources/assets.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(BASE/'sources/asset-errors.json').write_text(json.dumps(errors,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'assets':len(manifest),'bytes':sum(x['bytes'] for x in manifest.values()),'errors':errors},ensure_ascii=False))
if errors:raise SystemExit(1)
