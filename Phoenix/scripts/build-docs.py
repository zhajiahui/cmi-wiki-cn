"""Build the Phoenix translations from archived source and reviewed overrides."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
from bs4 import BeautifulSoup
import json,re,posixpath,yaml,hashlib
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'Phoenix'
PROJECTS={'Phoenix':'phoenix/','MMOItems':'mmoitems/','MMOCore':'mmocore/','MMOInventory':'mmoinventory/','MMOProfiles':'mmoprofiles/','MythicLib':'mythiclib/','BountyHunters':'bounty-hunters/','Contracts':'contracts/'}
pages=json.loads((BASE/'sources/pages.json').read_text(encoding='utf-8'))
units=json.loads((BASE/'sources/units.json').read_text(encoding='utf-8'))
unit_id={u['source']:u['id'] for u in units}
draft=json.loads((BASE/'sources/draft.json').read_text(encoding='utf-8'))
labels={}
for line in (BASE/'sources/review/titles.tsv').read_text(encoding='utf-8-sig').splitlines():
 if '\t' in line:
  en,zh=line.split('\t',1);labels[en]=zh
review={}
for f in sorted((BASE/'sources/review').glob('*.json')):review.update(json.loads(f.read_text(encoding='utf-8')))
manual=json.loads((BASE/'sources/review/technical-review.json').read_text(encoding='utf-8'));review.update(manual)
translations={str(u['id']):review.get(str(u['id']),draft.get(str(u['id']))) for u in units}
def polish(text,source):
    parts=re.split(r'(`+[^`\n]*`+|\]\([^\n]*?\)|<[^>]+>)',text)
    replacements={'健康状况':'生命值','健康值':'生命值','健康':'生命值','球员':'玩家','暴徒':'生物','产卵':'生成','库存':'物品栏','班级':'职业','主要职业':'主职业','主要课程':'主职业','派对':'队伍','爱好者':'增益效果','级别':'等级','调平':'升级','操作栏':'动作栏','物品知识':'物品描述','法杖精神':'法杖精魂','食谱':'配方','滴答':'刻','蜱虫':'刻','蜱':'刻','弹丸':'投射物','潜影贝子弹':'潜影贝导弹','您':'你','你将需要':'需要','你需要首先':'先','点击此处了解更多':'详见此处'}
    for i in range(0,len(parts),2):
        for en,zh in replacements.items():parts[i]=parts[i].replace(en,zh)
        if re.search(r'\bcast(?:ing|able)?\b',source,re.I) and not re.search(r'Java|type cast|class cast',source,re.I):parts[i]=parts[i].replace('可浇注物','可施放').replace('铸造','施放')
        if re.search(r'\bticks?\b',source,re.I):parts[i]=parts[i].replace('刻度','刻')
        if re.search(r'\bprofiles?\b',source,re.I) and not re.search(r'\bconfig(?:uration)?\b',source,re.I):parts[i]=parts[i].replace('配置文件','档案')
        if re.search(r'\bstatistics\b',source,re.I) and not re.search(r'\bvanilla\b',source,re.I):parts[i]=parts[i].replace('统计数据','属性').replace('统计信息','属性')
    result=''.join(parts)
    if '``' not in source:result=result.replace('``','` `')
    return result
for u in units:
    key=str(u['id'])
    if translations[key] is not None and key not in manual:translations[key]=polish(translations[key],u['source'])

missing=[u['id'] for u in units if translations[str(u['id'])] is None]
if missing:raise ValueError('Missing translations: '+str(missing))
assets=json.loads((BASE/'sources/all-assets.json').read_text(encoding='utf-8'))
asset_map={(a['project'],a['url']):a for a in assets}
normalize=lambda p:unquote(p).removesuffix('.html').rstrip('/') or '/'
by_path={normalize(p['path']):p for p in pages};bad_links=[]
for p in pages:
 en=(ROOT/p['project']/p['english']).read_text(encoding='utf-8');p['anchors']=set(re.findall(r'\{#([^}]+)\}',en))
def destination(p):return PROJECTS[p['project']]+p['file']
def local_url(url,current):
 part=urlsplit(url)
 if (current['project'],url) in asset_map:
  target=PROJECTS[current['project']]+asset_map[(current['project'],url)]['file']
 elif part.netloc.lower() in {'docs.phoenixdevt.fr','www.docs.phoenixdevt.fr'}:
  target_page=by_path.get(normalize(part.path))
  if not target_page:
   bad_links.append({'page':current['url'],'target':url,'reason':'target not in source site'});return url
  if part.fragment and unquote(part.fragment) not in target_page['anchors']:
   bad_links.append({'page':current['url'],'target':url,'reason':'anchor absent in source'});return url
  target=destination(target_page)
 else:return url
 result=posixpath.relpath(target,posixpath.dirname(destination(current)))
 if part.fragment:result+='#'+part.fragment
 return result
def clean_title(text):return re.sub(r'^[^A-Za-z0-9]+','',text).strip()
def title_for(p):
 raw=clean_title(p['title']);t=labels.get(raw,raw)
 if p['path']=='/archive/dead-link':return '失效链接归档页'
 if p['path']=='/archive/mmocore-convert-to-sql':return '迁移到 SQL（归档）'
 if p['path']=='/archive/mmocore-def-stat-values':return '默认属性值（归档）'
 if p['path']=='/archive/new-custom-blocks':return '自定义方块（归档）'
 if p['project']=='Contracts':return 'Contracts'
 return t
def source_cells(line):
    saved=[]
    def keep(m):saved.append(m[0]);return 'PHXTABLETOKEN'+str(len(saved)-1)+'END'
    masked=re.sub(r'`+[^`]*`+',keep,line)
    cells=[v.strip() for v in re.split(r'(?<!\\)\|',masked.strip().strip('|'))]
    return [re.sub(r'PHXTABLETOKEN(\d+)END',lambda m:saved[int(m[1])],v) for v in cells]
FROZEN={'Type','Parameter','Alias','Aliases','Default','Default Value','Command','Permission','Placeholder','Getter','Setter','Method','Subvariable','Config Key','Identifier','Code','Color Code','Tag','Formula','Variable'}
manifests={project:[] for project in PROJECTS}
for page in pages:
 project=page['project'];table_headers=[];en=(ROOT/project/page['english']).read_text(encoding='utf-8');out=[];inside=False;fence='';used=[]
 for line in en.splitlines():
  m=re.match(r'^(`{3,})',line)
  if m:
   if not inside:inside=True;fence=m[1]
   elif line.strip()==fence:inside=False
   out.append(line);continue
  if line.startswith('|') and re.match(r'^\|[ \-:|]+$',line) and out:
   table_headers=source_cells(previous_source)
  previous_source=line
  if inside or not line.strip() or re.fullmatch(r'[\s|:*-]+',line) or re.match(r'^\s*<(?:/?(?:video|source|iframe|details)\b|a[ >])',line):out.append(line);continue
  m=re.match(r'^(\s*(?:#{1,6} |[-*] |\d+\. )?)(.*?)(\s*\{#[^}]+\})?$',line)
  leading,text,anchor=m.groups()
  if not text:out.append(line);continue
  uid=unit_id[text];value=translations[str(uid)];used.append(uid)
  raw_label=clean_title(text)
  if raw_label in labels:value=labels[raw_label]
  # Source markup is structure, rather than text that a translation service may drop.
  if text.startswith('>') and not value.startswith('>'):value='> '+value
  if text.startswith('|'):
   if not value.startswith('|'):value='| '+value
   if not value.endswith('|'):value+=' |'
  if text.startswith('|'):
   original_cells=source_cells(text);translated_cells=source_cells(value)
   if len(original_cells)!=len(translated_cells):raise ValueError('Table cell count changed: '+str(uid))
   if table_headers and len(table_headers)==len(original_cells):
    for column,(raw,header) in enumerate(zip(original_cells,table_headers)):
     if header in FROZEN or re.fullmatch(r'[a-z][a-z0-9_./:*%-]*',raw):translated_cells[column]=raw
    value='| '+' | '.join(translated_cells)+' |'
  value=value.replace('您','你')
  # Escape inline pipe characters for the Markdown table parser, preserving displayed code.
  if text.startswith('|'):value=re.sub(r'`([^`]+)`',lambda m:'`'+m[1].replace('|','\\|')+'`',value)
  out.append(leading+value+(anchor or ''))
 body='\n'.join(out)+'\n'
 title=title_for(page)
 if re.match(r'^# [^\n]*$',body,re.M):
  def heading(m):
   anchor=re.search(r'\s*\{#[^}]+\}$',m[0]);return '# '+title+(anchor[0] if anchor else '')
  body=re.sub(r'^# [^\n]*$',heading,body,count=1,flags=re.M)
 else:body='# '+title+'\n\n'+body
 blocks=re.split(r'(^`{3,}[^\n]*\n[\s\S]*?^`{3,}\s*$)',body,flags=re.M)
 for i in range(0,len(blocks),2):
  blocks[i]=re.sub(r'(?<=\]\()[^\n]*?(?=\))',lambda m:local_url(m[0],page),blocks[i])
  blocks[i]=re.sub(r'((?:src|poster)=")([^"]+)',lambda m:m[1]+local_url(m[2],page),blocks[i])
 body=''.join(blocks)
 if page['project']=='Phoenix' and page['file']=='index.md':
  for project_name,project_prefix in PROJECTS.items():
   if project_name!='Phoenix':body=body.replace('## '+project_name+'\n','## ['+project_name+']('+posixpath.relpath(project_prefix+'index.md','phoenix')+')\n')
 body+='\n---\n\n原文：['+page['title']+']('+page['url']+') · 原文归档：2026-10-19\n'
 meta={'title':title,'source':page['url'],'source_snapshot':'2026-10-19'}
 content='---\n'+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False)+'---\n\n'+body
 output=ROOT/project/'docs'/page['file'];output.parent.mkdir(parents=True,exist_ok=True);output.write_text(content,encoding='utf-8')
 manifests[project].append({'title':title,'file':page['file'],'source':page['url'],'source_key':page['key'],'source_sha256':page['sha256'],'translation_units':used})
site=json.loads((BASE/'sources/site-data.json').read_text(encoding='utf-8'))
def nav_item(node):
 raw=clean_title(node.get('text',''));name=labels.get(raw,raw);children=[]
 if node.get('link'):
  p=by_path.get(normalize(node['link']))
  if p:children.append({name:p['file']})
 for child in node.get('items',[]):children.extend(nav_item(child))
 if node.get('items'):return [{name:children}]
 return children
def navfiles(items):
 for item in items:
  for value in item.values():
   if isinstance(value,list):yield from navfiles(value)
   else:yield value
for project,prefix in PROJECTS.items():
 rows=manifests[project]
 if project=='Phoenix':nav=[{'前言':'index.md'},{'官方文档维护说明':'site-maintenance.md'},{'失效链接归档页':'archive/dead-link.md'}]
 else:
  nav=[]
  for node in site['themeConfig']['sidebar'].get('/'+prefix,[]):nav.extend(nav_item(node))
  included=set(navfiles(nav));extra=[p for p in rows if p['file'] not in included]
  archives=[{p['title']:p['file']} for p in extra if p['file'].startswith('archive/')]
  categories=[{p['title']:p['file']} for p in extra if not p['file'].startswith('archive/')]
  if categories:nav.append({'分类目录':categories})
  if archives:nav.append({'归档文档':archives})
 config={'site_name':project+' 中文文档','site_url':'https://zhajiahui.github.io/cmi-wiki-cn/'+prefix,'theme':{'name':'material','language':'zh','font':False},'plugins':[{'search':{'lang':['zh','en']}}],'markdown_extensions':['admonition','attr_list','md_in_html','tables',{'toc':{'permalink':True}},'pymdownx.details','pymdownx.superfences'],'nav':nav,'docs_dir':'docs','site_dir':'.cache/site'}
 (ROOT/project/'mkdocs.yml').write_text(yaml.safe_dump(config,allow_unicode=True,sort_keys=False),encoding='utf-8')
 (ROOT/project/'sources/manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 selected=[{'id':u['id'],'source':u['source'],'zh':translations[str(u['id'])]} for u in units if project in u['projects']]
 (ROOT/project/'sources/translations.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(BASE/'sources/link-issues.json').write_text(json.dumps(bad_links,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pages':sum(map(len,manifests.values())),'projects':{p:len(r) for p,r in manifests.items()},'source_link_issues':len(bad_links)},ensure_ascii=False,indent=2))
