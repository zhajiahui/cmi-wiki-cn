"""Cache translation drafts with code, links, identifiers and numbers protected.
Reviewed edits belong in sources/review/ and are applied by build-docs.py.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import requests,json,re,time,threading
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'Phoenix'
units=json.loads((BASE/'sources/units.json').read_text(encoding='utf-8'))
OUT=BASE/'sources/draft.json';draft=json.loads(OUT.read_text(encoding='utf-8')) if OUT.exists() else {}
TERMS={
 'permission nodes':'权限节点','permission node':'权限节点','player profiles':'玩家档案','player profile':'玩家档案','character slots':'角色栏位','character slot':'角色栏位',
 'crafting stations':'合成站','crafting station':'合成站','crafting recipes':'合成配方','crafting recipe':'合成配方','item tiers':'物品品质','item tier':'物品品质','item sets':'物品套装','item set':'物品套装','item lore':'物品描述','lore format':'描述格式',
 'damage mitigation':'伤害减免','damage indicators':'伤害显示','damage indicator':'伤害显示','on-hit effects':'命中效果','on-hit effect':'命中效果','stat modifiers':'属性修正器','stat modifier':'属性修正器','item modifiers':'物品修饰器','item modifier':'物品修饰器',
 'critical strike chance':'暴击几率','critical strike power':'暴击伤害','critical strikes':'暴击','critical strike':'暴击','critical hits':'暴击','critical hit':'暴击','attack damage':'攻击伤害','attack speed':'攻击速度','max health':'最大生命值',
 'ender-chest':'末影箱','ender chest':'末影箱','main hand':'主手','off hand':'副手','mainhand':'主手','offhand':'副手','skill trees':'技能树','skill tree':'技能树',
 'soulbound':'灵魂绑定','reforging':'重铸','reforge':'重铸','deconstruction':'分解','deconstruct':'分解','custom durability':'自定义耐久度','durability':'耐久度','cooldowns':'冷却时间','cooldown':'冷却时间',
 'placeholders':'占位符','placeholder':'占位符','inventories':'物品栏','inventory':'物品栏','players':'玩家','player':'玩家','permissions':'权限','permission':'权限','weapons':'武器','weapon':'武器','consumables':'消耗品','consumable':'消耗品',
 'stats':'属性','stat':'属性','skills':'技能','skill':'技能','mana':'魔力','stamina':'耐力','bounties':'悬赏','bounty':'悬赏','contracts':'委托','contract':'委托','targeters':'目标选择器','targeter':'目标选择器','vanilla':'原版','knockback':'击退',
 'lore':'描述','armors':'盔甲','armor':'护甲','items':'物品','item':'物品'
}
NAMES=['Phoenix','MMOItems','MMOCore','MMOInventory','MMOProfiles','MythicLib','BountyHunters','Contracts','Minecraft','Bukkit','SpigotMC','Spigot','Paper','Purpur','MythicMobs','MythicCrucible','PlaceholderAPI','LuckPerms','ItemsAdder','Oraxen','Nexo','CoreTools','Fabled','Heroes','SkillAPI','ProtocolLib','Vault','WorldGuard','WorldEdit','Citizens','BungeeCord','Velocity','MySQL','SQLite','MariaDB','Redis','YAML','JSON','Java','Kotlin','VitePress','Vue','TeamCity','Discord','GitLab','Gitlab','GitHub','Polymart','RPG','MMORPG','NBT','NMS','JDK','Maven','Gradle','SQL','API','UUID','GUI','ID','PvP','PvE','PvM','AoE']
TECH=re.compile(r'`+[^`\n]*`+|\]\([^\n]*?\)|<[^>\n]+>|\b(?:'+ '|'.join(re.escape(n) for n in sorted(NAMES,key=len,reverse=True))+r')\b|%[^%\s`\n]+%|\b[a-zA-Z][\w]*(?:[._-][\w*]+)+\b|(?<![\w])(?:-?\d+(?:\.\d+)*(?:%|[a-zA-Z]+)?)(?![\w])|\b(?:true|false|null)\b')
TERM_RE=re.compile(r'\b(?:'+'|'.join(re.escape(k) for k in sorted(TERMS,key=len,reverse=True))+r')\b',re.I)
def mask(text):
 saved=[]
 def save(value):
  key='ZXQ'+str(len(saved)).zfill(4)+'QXZ';saved.append(value);return ' '+key+' '
 # Protect existing technical syntax first, then freeze established Chinese terms.
 text=TECH.sub(lambda m:save(m[0]),text)
 text=TERM_RE.sub(lambda m:save(TERMS[m[0].lower()]),text)
 return text,saved
state=threading.local()
def translate(batch):
 if not hasattr(state,'s'):state.s=requests.Session()
 packed=[];tokens={}
 for u in batch:
  text,saved=mask(u['source']);packed.append(text);tokens[u['id']]=saved
 for attempt in range(4):
  try:
   r=state.s.get('https://translate.googleapis.com/translate_a/single',params={'client':'gtx','sl':'en','tl':'zh-CN','dt':'t','q':'\n\n'.join(packed)},timeout=(15,45));r.raise_for_status()
   text=''.join(v[0] for v in r.json()[0]);parts=re.split(r'\n\s*\n',text.strip());result={}
   if len(parts)!=len(batch):
    if len(batch)>1:
     for u in batch:result.update(translate([u]))
     return result
    parts=[text]
   for u,value in zip(batch,parts):
    saved=tokens[u['id']];found=re.findall(r'ZXQ\s*(\d+)\s*QXZ',value,re.I)
    if sorted(map(int,found))!=list(range(len(saved))):continue
    value=re.sub(r'\s*ZXQ\s*(\d+)\s*QXZ\s*',lambda m:saved[int(m[1])],value,flags=re.I)
    value=value.replace('播放器','玩家').replace('服务器端','服务端')
    result[str(u['id'])]=value.strip()
   if len(result)==len(batch):return result
   if len(batch)>1:
    for u in batch:
     if str(u['id']) not in result:result.update(translate([u]))
    return result
  except Exception:
   if attempt==3:raise
  time.sleep(attempt+1)
 raise ValueError('Draft token recovery failed: '+str([u['id'] for u in batch]))
review={}
for f in (BASE/'sources/review').glob('*.json'):review.update(json.loads(f.read_text(encoding='utf-8')))
pending=[]
for u in units:
 if str(u['id']) in draft or str(u['id']) in review:continue
 masked,_=mask(u['source']);clean=re.sub(r'ZXQ\d+QXZ|[^A-Za-z]','',masked)
 if not clean:draft[str(u['id'])]=re.sub(r'\s*ZXQ(\d+)QXZ\s*',lambda m:mask(u['source'])[1][int(m[1])],masked).strip()
 else:pending.append(u)
batches=[];batch=[];size=0
for u in pending:
 cost=len(mask(u['source'])[0])
 if size+cost>2000 and batch:batches.append(batch);batch=[];size=0
 batch.append(u);size+=cost
if batch:batches.append(batch)
if OUT.exists() and len(pending)<500:batches=[[u] for u in pending]
print('Draft batches',len(batches),'units',len(pending),flush=True)
with ThreadPoolExecutor(max_workers=6) as pool:
 jobs={pool.submit(translate,b):b for b in batches}
 for n,f in enumerate(as_completed(jobs),1):
  try:draft.update(f.result())
  except Exception as exc:print('FAILED',[u['id'] for u in jobs[f]],str(exc)[:180],flush=True)
  if n%10==0 or n==len(jobs):
   OUT.write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('Draft',n,'/',len(jobs),'units',len(draft),'/',len(units),flush=True)
OUT.write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for project in sorted({p for u in units for p in u['projects']}):
 terms='en\tzh-CN\n'+'\n'.join(k+'\t'+v for k,v in TERMS.items())+'\n'
 (ROOT/project/'terminology.tsv').write_text(terms,encoding='utf-8')
if any(str(u['id']) not in draft and str(u['id']) not in review for u in units):raise SystemExit(1)
