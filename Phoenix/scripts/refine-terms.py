"""Refine gameplay vocabulary in cached drafts; never changes executable examples."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import re,json
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'Phoenix'
namespace={'__file__':str(BASE/'scripts/draft-translations.py')}
exec((BASE/'scripts/draft-translations.py').read_text(encoding='utf-8-sig').split('pending=[]')[0],namespace)
units=namespace['units'];draft=namespace['draft'];terms=dict(namespace['TERMS'])
terms.update({'class':'职业','classes':'职业','profession':'副职业','professions':'副职业','attribute':'基础属性','attributes':'基础属性','attribute points':'基础属性点','attribute point':'基础属性点','health':'生命值','maximum health':'最大生命值','mobs':'生物','mob':'生物','buffs':'增益效果','buff':'增益效果','leveling':'升级','level':'等级','levels':'等级','experience':'经验','exp':'经验','particle effects':'粒子效果','particles':'粒子','loots':'掉落物','loot':'掉落物','party':'队伍','parties':'队伍','profiles':'档案','profile':'档案','caste':'施法者','caster':'施法者'})
term_re=re.compile(r'\b(?:'+'|'.join(re.escape(k) for k in sorted(terms,key=len,reverse=True))+r')\b',re.I)
natural={'built-in':'内置','main-class':'主职业','class-based':'按职业划分','stamina-based':'以耐力为资源的','magicka-based':'以魔法为资源的','non-skill':'非技能','out-of-combat':'脱离战斗','off-combat':'脱离战斗','non-player':'非玩家','non-vanilla':'非原版','cross-server':'跨服','case-sensitive':'区分大小写','case-insensitive':'不区分大小写','right-click':'右键点击','right-clicking':'右键点击','left-click':'左键点击','left-clicking':'左键点击','one-time':'一次性','real-time':'实时','third-party':'第三方','user-friendly':'易于使用'}
tech=namespace['TECH']
def mask(text):
 saved=[]
 def save(value):
  key='ZXQ'+str(len(saved)).zfill(4)+'QXZ';saved.append(value);return ' '+key+' '
 text=tech.sub(lambda m:save(natural.get(m[0].lower(),m[0])),text)
 text=term_re.sub(lambda m:save(terms[m[0].lower()]),text)
 return text,saved
namespace['mask']=mask
reviews=json.loads((BASE/'sources/review/technical-review.json').read_text(encoding='utf-8'))
selected=[]
for u in units:
 z=draft.get(str(u['id']),'')
 if str(u['id']) in reviews or not z:continue
 if all('_api' in p for p in u['pages']):continue
 if re.search(r'Java class|extends|implements|constructor|Bukkit class',u['source'],re.I):continue
 if re.search(r'\b(?:class(?:es)?|professions?|attributes?|profiles?)\b',u['source'],re.I) or re.search('班级|球员|暴徒|产卵|健康|调平|专业|派对|爱好者|库存|主要课程',z) or re.search(r'%[^%]*[A-Za-z][^%]*\s[^%]*%',re.sub(r'`[^`]+`','',u['source'])):selected.append(u)
result={};out=BASE/'sources/review/terminology-refinement.json';existing=json.loads(out.read_text(encoding='utf-8')) if out.exists() else {};selected=[u for u in selected if str(u['id']) not in existing]
print('Gameplay vocabulary refinement',len(selected),flush=True)
with ThreadPoolExecutor(max_workers=6) as pool:
 jobs={pool.submit(namespace['translate'],[u]):u for u in selected}
 for n,f in enumerate(as_completed(jobs),1):
  try:result.update(f.result())
  except Exception as exc:print('REVIEW MANUALLY',jobs[f]['id'],str(exc)[:100],flush=True)
  if n%25==0 or n==len(jobs):
   out.write_text(json.dumps({**existing,**result},ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('Refined',n,'/',len(jobs),flush=True)
