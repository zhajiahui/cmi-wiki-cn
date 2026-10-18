"""Create a cached translation draft. Reviewed overrides are maintained separately."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import json,re,requests,time,hashlib
BASE=Path(__file__).resolve().parents[1]
units=json.loads((BASE/'sources/units.json').read_text(encoding='utf-8'))
OUT=BASE/'sources/draft.json'
draft=json.loads(OUT.read_text(encoding='utf-8')) if OUT.exists() else {}
TOKEN=re.compile(r'\btypewriter\.[A-Za-z0-9_./*]+|%typewriter_[^%]+%|\b(?:Typewriter|Basic Adapter|BasicExtension|EntityExtension|PacketEvents|PlaceholderAPI|Vault|MythicMobs|Paper|Spigot|Bukkit|Minecraft|Playit\.gg|MiniMessage|Rive|Kotlin|Gradle)\b|`+[^`\n]*`+|!?\[|\]\([^\n]*?\)|\*\*|(?<!\w)\*(?!\s)|(?<!\s)\*(?!\w)|<[^>]+>')
def mask(s):
    saved=[]
    def sub(m):
        k=len(saved);saved.append(m.group());return ' ZXQ'+str(k).zfill(3)+'QXZ '
    return TOKEN.sub(sub,s),saved

def translate(batch):
    packed=[];saved={}
    for u in batch:
        masked,tokens=mask(u['source']);saved[u['id']]=tokens
        packed.append(masked)
    for attempt in range(5):
        try:
            r=requests.get('https://translate.googleapis.com/translate_a/single',params={'client':'gtx','sl':'en','tl':'zh-CN','dt':'t','q':'\n\n'.join(packed)},timeout=45)
            r.raise_for_status();text=''.join(x[0] for x in r.json()[0])
            parts=re.split(r'\n\s*\n',text.strip());result={}
            if len(parts)!=len(batch):
                if len(batch)>1:
                    for u in batch:result.update(translate([u]))
                    return result
                parts=[text]
            for u,value in zip(batch,parts):
                uid=u['id'];tokens=saved[uid]
                found=re.findall(r'ZXQ\s*(\d+)\s*QXZ',value,flags=re.I)
                if sorted(map(int,found))!=list(range(len(tokens))):continue
                value=re.sub(r'\s*ZXQ\s*(\d+)\s*QXZ\s*',lambda m:tokens[int(m[1])],value,flags=re.I).strip()
                result[str(uid)]=value
            if len(result)==len(batch):return result
            if len(batch)>1:
                for u in batch:
                    if str(u['id']) not in result:result.update(translate([u]))
                return result
        except Exception:
            if attempt==4:raise
        time.sleep(1+attempt)
    raise RuntimeError('Unrecoverable translation tokens: '+str([u['id'] for u in batch]))
pending=[u for u in units if str(u['id']) not in draft]
batches=[];batch=[];size=0
for u in pending:
    if size+len(u['source'])>1400 and batch:batches.append(batch);batch=[];size=0
    batch.append(u);size+=len(u['source'])
if batch:batches.append(batch)
print('Draft batches:',len(batches),flush=True)
with ThreadPoolExecutor(max_workers=8) as pool:
    jobs={pool.submit(translate,b):b for b in batches}
    for n,f in enumerate(as_completed(jobs),1):
        try:draft.update(f.result())
        except Exception as exc:print('FAILED', [u['id'] for u in jobs[f]],str(exc),flush=True)
        if n%10==0 or n==len(jobs):
            OUT.write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            print('Draft',n,'/',len(jobs),'units',len(draft),'/',len(units),flush=True)
OUT.write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if any(str(u['id']) not in draft for u in units):raise SystemExit(1)
