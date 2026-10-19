"""Render only fully reviewed MythicMobs pages and retain every source link/code example."""
from pathlib import Path
from collections import Counter
from urllib.parse import urlsplit,unquote
import json,re,posixpath,yaml,hashlib,sys
from markdown.extensions.toc import slugify_unicode,unique
from markdown import Markdown
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'MythicMobs';CACHE=BASE/'sources/wiki/translation'
units={u['id']:u for u in json.loads((CACHE/'translation-units.json').read_text('utf-8'))}
docs=json.loads((CACHE/'document-slots.json').read_text('utf-8'));coverage=json.loads((BASE/'sources/wiki-coverage.json').read_text('utf-8'))
titles=json.loads((CACHE/'page-titles.json').read_text('utf-8'))
translations={};origins={}
for path in sorted((CACHE/'reviewed').rglob('*.json')):
 data=json.loads(path.read_text('utf-8'))
 for key,value in data.items():
  if key in translations and translations[key]!=value:raise ValueError('Conflicting reviewed translations: '+key)
  translations[key]=value;origins[key]=str(path.relative_to(CACHE))

literal_reviews={}
for path in sorted((CACHE/'literal-reviews').glob('*.json')):
 for item in json.loads(path.read_text('utf-8')):
  key=(item['file'],item['part_index'])
  if key in literal_reviews:raise ValueError('Duplicate literal prose review: '+str(key))
  literal_reviews[key]=item

def protected(s):return Counter(re.findall(r'ZZURL\d+ZZ|<[A-Za-z_&#0-9/][^<>\n]*>|\*\*(?:<=|>=|<|>|=)\*\*|%[^%\s]+%|\b(?:true|false|null)\b|(?<![A-Za-z0-9_])-?\d+(?:\.\d+)*(?![A-Za-z0-9_])',s))
token_review_path=CACHE/'token-review-exceptions.json'
token_reviews=json.loads(token_review_path.read_text('utf-8')) if token_review_path.is_file() else {}
errors=[]
for key,value in translations.items():
 if key not in units:continue
 source=units[key]['source'];missing=protected(source)-protected(value)
 if key in token_reviews:
  exception=token_reviews[key]
  if exception['source']!=source or not exception.get('reason'):raise ValueError('Invalid prose keyword review: '+key)
  missing-=Counter(exception['tokens'])
 inline=lambda s:Counter(m[2] for m in re.finditer(r'(?<!`)(`{1,2})([^`\n]+)\1(?!`)',s))
 if missing:errors.append({'id':key,'kind':'protected tokens lost','tokens':dict(missing),'origin':origins[key]})
 if inline(source)-inline(value):errors.append({'id':key,'kind':'inline code lost','tokens':list((inline(source)-inline(value)).elements()),'origin':origins[key]})
if errors:
 (CACHE/'review-errors.json').write_text(json.dumps(errors,ensure_ascii=False,indent=2)+'\n','utf-8')
 print(json.dumps({'review_errors':errors[:25]},ensure_ascii=False,indent=2));raise SystemExit(1)
ready=[d for d in docs if all('id' not in p or p['id'] in translations for p in d['parts'])]
ready_paths={d['file'] for d in ready};aliases=coverage['aliases'];aliasfold={url.casefold():file for url,file in aliases.items()}
assets_path=BASE/'sources/wiki/assets.json';assets=json.loads(assets_path.read_text('utf-8')) if assets_path.is_file() else []
asset_map={r['url']:r['file'] for r in assets if r['status']=='archived'}
anchors={};heading_anchor_fills={};manifest=[];link_issues=[]
for d in docs:
 ids=set();fills={};used=set()
 for i,part in enumerate(d['parts']):
  if not re.fullmatch(r'#{1,6} ',part.get('text','')):continue
  title_part=d['parts'][i+1];tail=d['parts'][i+2]['text']
  source_title=title_part.get('text',units.get(title_part.get('id'),{}).get('source',''))
  for n,url in enumerate(title_part.get('tokens',[])):source_title=source_title.replace('ZZURL'+str(n).zfill(3)+'ZZ',url)
  explicit=re.search(r'\{\s*#([^}\s]+)\s*\}',tail)
  if explicit:anchor=explicit[1];used.add(anchor)
  else:
   md=Markdown(extensions=['toc']);md.convert(part['text']+source_title)
   anchor=unique(md.toc_tokens[0]['id'],used)
   fills[i+2]=' {#'+anchor+'}'+tail
  ids.add(anchor)
 anchors[d['file']]=ids;heading_anchor_fills[d['file']]=fills

def localize(url,d):
 if url in asset_map:return posixpath.relpath(asset_map[url],posixpath.dirname(d['file']))
 p=urlsplit(url);base=url.split('#',1)[0].rstrip('/')
 target=aliases.get(base) or aliasfold.get(base.casefold())
 if not target or target not in ready_paths:return url
 if p.fragment and unquote(p.fragment) not in anchors[target]:
  link_issues.append({'source':d['source_url'],'target':url,'reason':'原文片段与目标章节不对应，保留官方链接'});return url
 value=posixpath.relpath(target,posixpath.dirname(d['file']))
 if p.fragment:value+='#'+p.fragment
 return value

def rewrite_links(text,d):
 if d['file']=='wiki/spawners.md' and '](/commands and permissions)' in text:
  text=text.replace('](/commands and permissions)','](https://wiki.mythiccraft.io/commands%20and%20permissions)')
  link_issues.append({'source':d['source_url'],'target':'https://wiki.mythiccraft.io/commands%20and%20permissions','reason':'原文含空格的根相对地址；保留官方根站地址并编码空格，不猜测替换目标页面'})
 # Keep code fences and inline code byte-for-byte, including URLs used in examples.
 saved=[]
 def keep(m):saved.append(m[0]);return 'LITERALCODEBLOCK'+str(len(saved)-1)+'END'
 text=re.sub(r'^([ \t]*(?:>\s*)?)(`{3,}|~{3,})[^\n]*\n[\s\S]*?^\1\2\s*$',keep,text,flags=re.M)
 text=re.sub(r'(?<!`)(`{1,2})([^`\n]+)\1(?!`)',keep,text)
 text=re.sub(r'(\]\()([^\s)]+)(\))',lambda m:m[1]+localize(m[2],d)+m[3],text)
 text=re.sub(r'\b(src|poster)="([^"]+)"',lambda m:m[1]+'="'+localize(m[2],d)+'"',text)
 return re.sub(r'LITERALCODEBLOCK(\d+)END',lambda m:saved[int(m[1])],text)

for d in ready:
 out=[]
 for part_index,part in enumerate(d['parts']):
  if 'text' in part:
   if part_index in heading_anchor_fills[d['file']]:out.append(heading_anchor_fills[d['file']][part_index]);continue
   review=literal_reviews.get((d['file'],part_index))
   if review:
    if review['source']!=part['text'] or protected(review['source'])-protected(review['translation']) or inline(review['source'])-inline(review['translation']):raise ValueError('Literal prose source mismatch: '+d['file'])
    out.append(review['translation'])
   else:out.append(part['text'])
   continue
  value=translations[part['id']]
  if d['file']=='wiki/skills/math.md' and units[part['id']]['source']=='Function':value='函数'
  for n,token in enumerate(part.get('tokens',[])):value=value.replace('ZZURL'+str(n).zfill(3)+'ZZ',token)
  out.append(value)
 body=''.join(out);body=rewrite_links(body,d)
 title_review=titles[d['file']]
 if title_review['source']!=d['source_title']:raise ValueError('Source page title changed: '+d['file'])
 title=title_review['translation']
 first_heading=re.match(r'^#\s+(.*?)(?:\s*\{#[^}]+\})?\s*$',body.splitlines()[0])
 if not first_heading or first_heading[1]!=title:body='# '+title+'\n\n'+body
 meta={'title':title,'source_url':d['source_url'],'source_kind':'official-wiki','translation_review':'reviewed','source_version':coverage['version']}
 content='---\n'+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False)+'---\n\n'+body.rstrip()+'\n'
 target=BASE/'docs'/d['file'];target.parent.mkdir(parents=True,exist_ok=True);target.write_text(content,'utf-8',newline='\n')
 manifest.append({'file':d['file'],'title':title,'source_url':d['source_url'],'source_file':d['source_file'],'source_sha256':d['source_sha256'],'translation_review':'reviewed'})
(BASE/'sources/wiki-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n','utf-8',newline='\n')
labels={'mobs':'生物','skills':'技能','items':'物品','drops':'掉落物','guides':'使用指南','changelogs':'更新记录','examples':'示例','config':'配置','troubleshooting':'排错','wiki-editors-resources':'Wiki 编辑资料','enum':'枚举参考','mechanics':'技能机制','conditions':'条件','targeters':'目标选择器','triggers':'触发器','auras':'光环','effects':'效果','particles':'粒子','placeholders':'占位符','tags':'标签','ai':'AI','goals':'AI 行为','targets':'AI 目标','droptypes':'掉落类型'}
def wiki_nav(prefix,rows):
 direct=[row for row in rows if posixpath.dirname(row['file'])==prefix]
 children={}
 for row in rows:
  rest=row['file'][len(prefix)+1:]
  if '/' in rest:children.setdefault(rest.split('/')[0],[]).append(row)
 absorbed={}
 for name in children:
  for row in direct:
   if row['file']==prefix+'/'+name+'.md':absorbed[name]=row
 nav=[]
 for row in direct:
  if row in absorbed.values():continue
  label='文档目录' if row['file']=='wiki/index.md' else row['title']
  nav.append({label:row['file']})
 for name,nested in children.items():
  entries=wiki_nav(prefix+'/'+name,nested)
  if name in absorbed:entries.insert(0,{absorbed[name]['title']:absorbed[name]['file']})
  nav.append({labels.get(name,name):entries})
 return nav
nav=wiki_nav('wiki',manifest)
(BASE/'sources/wiki-nav.yml').write_text(yaml.safe_dump(nav,allow_unicode=True,sort_keys=False),'utf-8',newline='\n')
coverage['translation_status']=[{'file':d['file'],'source_url':d['source_url'],'status':'translated' if d['file'] in ready_paths else 'pending','pending_units':len({p['id'] for p in d['parts'] if 'id' in p and p['id'] not in translations})} for d in docs]
coverage['translated_pages']=len(ready);coverage['pending_pages']=len(docs)-len(ready)
(BASE/'sources/wiki-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n','utf-8',newline='\n')
(BASE/'sources/wiki/link-issues.json').write_text(json.dumps(link_issues,ensure_ascii=False,indent=2)+'\n','utf-8',newline='\n')
print(json.dumps({'reviewed_units':len(translations),'all_units':len(units),'fully_translated_pages':len(ready),'pending_pages':len(docs)-len(ready),'retained_source_link_issues':len(link_issues)},ensure_ascii=False,indent=2))
