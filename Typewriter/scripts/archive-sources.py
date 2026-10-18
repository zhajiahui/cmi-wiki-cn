from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json,hashlib,time
BASE=Path(__file__).resolve().parents[1]
repo=json.loads((BASE/'sources/repository-tree.json').read_text(encoding='utf-8-sig'))
REF=repo['ref'];PREFIX='documentation/versioned_docs/version-0.8.0/'
files=[f for f in repo['files'] if f['path'].startswith(PREFIX)]
files += [f for f in repo['files'] if f['path'] in ['documentation/docusaurus.config.ts','documentation/sidebars.js','documentation/versions.json'] or f['path'].startswith('documentation/src/components/')]
def download(row):
    relative=row['path'].removeprefix('documentation/')
    dest=BASE/'sources/repository'/relative
    if dest.exists() and dest.stat().st_size==row['size']:return relative
    dest.parent.mkdir(parents=True,exist_ok=True)
    for attempt in range(3):
        try:
            r=requests.get(f'https://raw.githubusercontent.com/gabber235/Typewriter/{REF}/{row["path"]}',timeout=(20,90));r.raise_for_status()
            if len(r.content)!=row['size']:raise ValueError('Content size mismatch')
            dest.write_bytes(r.content);return relative
        except Exception:
            if attempt==2:raise
            time.sleep(1)
with ThreadPoolExecutor(max_workers=8) as pool:
    results=list(pool.map(download,files))
(BASE/'sources/source-info.json').write_text(json.dumps({'project':'Typewriter','version':'0.8.0','repository':'https://github.com/gabber235/Typewriter','commit':REF,'source_prefix':PREFIX,'source_files':len(files),'bytes':sum(f['size'] for f in files)},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'archived_files':len(results),'bytes':sum(f['size'] for f in files)},ensure_ascii=False))
