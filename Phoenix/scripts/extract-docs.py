"""Extract full document bodies while keeping code, anchors, tables and media."""
from pathlib import Path
from urllib.parse import urljoin,urlsplit
from collections import Counter
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'Phoenix'
pages=json.loads((BASE/'sources/pages.json').read_text(encoding='utf-8'))
class Converter(MarkdownConverter):
 def __init__(self,*args,**kw):super().__init__(*args,**kw);self.blocks=[]
 def convert_hN(self,n,el,text,parent_tags):
  output=super().convert_hN(n,el,text,parent_tags)
  anchor=el.get('id')
  return output.rstrip()+' {#'+anchor+'}\n\n' if anchor else output
 def convert_pre(self,el,text,parent_tags):
  parent=el.parent;language=''
  while parent and parent.name not in ['main','body']:
   for cls in parent.get('class',[]):
    if cls.startswith('language-'):language=cls[9:]
   if language:break
   parent=parent.parent
  content=el.get_text();fence='`'*max(3,max([len(m[0])+1 for m in re.finditer(r'`+',content)]+[3]))
  block=fence+language+'\n'+content+('' if content.endswith('\n') else '\n')+fence
  key='PHXCODEBLOCK'+str(len(self.blocks)).zfill(5)+'END';self.blocks.append((key,block,content))
  return '\n\n'+key+'\n\n'
 def convert_code(self,el,text,parent_tags):
  if el.find_parent('pre'):return text
  content=el.get_text();fence='`'*max(1,max([len(m[0])+1 for m in re.finditer(r'`+',content)]+[1]))
  return fence+content+fence
 def convert_details(self,el,text,parent_tags):return '\n\n<details markdown="1">\n'+text+'\n</details>\n\n'
 def convert_summary(self,el,text,parent_tags):return '\n<summary>'+text+'</summary>\n\n'
units=json.loads((BASE/'sources/units.json').read_text(encoding='utf-8')) if (BASE/'sources/units.json').exists() else []
by_source={u['source']:u['id'] for u in units};by_id={u['id']:u for u in units};next_id=max(by_id,default=-1)+1
for u in units:u['projects']=[];u['pages']=[]
assets={};summary=[]
for page in pages:
 project=page['project'];root=ROOT/project
 soup=BeautifulSoup((root/page['html']).read_bytes(),'html.parser')
 main=soup.select_one('main .vp-doc') or soup.select_one('main') or soup.select_one('.VPHome')
 main=BeautifulSoup(str(main),'html.parser')
 for n in main.select('.header-anchor,button.copy,.lang,.line-numbers-wrapper,script,style'):
  n.decompose()
 for d in main.select('div.custom-block'):
  d.name='blockquote';d.attrs={}
  title=d.select_one('.custom-block-title')
  if title:title.name='strong'
 for a in main.select('a[href]'):
  href=a['href'];a['href']=urljoin(page['url'],href)
 for media in main.select('img[src],video[src],source[src],iframe[src]'):
  media['src']=urljoin(page['url'],media['src'])
  if media.name in ['img','video','source']:
   url=media['src'];key=project+'|'+url
   assets[key]={'project':project,'url':url}
  if media.has_attr('poster'):
   media['poster']=urljoin(page['url'],media['poster']);assets[project+'|'+media['poster']]={'project':project,'url':media['poster']}
 # Retain playable embeds as original HTML; translate surrounding captions normally.
 kept=[]
 for element in main.find_all(['video','iframe']):
  if element.find_parent(['video','iframe']):continue
  key='PHXMEDIA'+str(len(kept)).zfill(5)+'END';kept.append((key,str(element)));element.replace_with(key)
 converter=Converter(heading_style='ATX',bullets='-',escape_underscores=False,escape_asterisks=False,wrap=False,keep_inline_images_in=['td','th','a','span','strong','em'])
 body=re.sub(r'\n{3,}','\n\n',converter.convert_soup(main)).strip()+'\n'
 for key,block,_ in converter.blocks:
  body=re.sub(r'(?m)^> '+re.escape(key),key,body).replace(key,block)
 for key,block in kept:body=body.replace(key,block)
 # Category landing pages on the source may be intentionally empty.
 if not body.strip():body=''
 output=root/'sources/en'/page['file'];output.parent.mkdir(parents=True,exist_ok=True);output.write_text(body,encoding='utf-8')
 page['english']='sources/en/'+page['file']
 page['code_blocks']=[{'content':content,'sha256':hashlib.sha256(content.encode()).hexdigest()} for _,_,content in converter.blocks]
 page['inline_code']=[c.get_text() for c in main.find_all('code') if not c.find_parent('pre')]
 inside=False;fence='';page_ids=[]
 for line in body.splitlines():
  m=re.match(r'^(`{3,})',line)
  if m:
   if not inside:inside=True;fence=m[1]
   elif line.strip()==fence:inside=False
   continue
  if inside or not line.strip() or re.fullmatch(r'[\s|:*-]+',line) or re.match(r'^\s*<(?:/?(?:video|source|iframe|details)\b|a[ >])',line):continue
  m=re.match(r'^(\s*(?:#{1,6} |[-*] |\d+\. )?)(.*?)(\s*\{#[^}]+\})?$',line)
  leading,text,anchor=m.groups()
  if not text:continue
  if text not in by_source:
   uid=next_id;next_id+=1;by_source[text]=uid;new_unit={'id':uid,'source':text,'projects':[],'pages':[]};units.append(new_unit);by_id[uid]=new_unit
  unit=by_id[by_source[text]]
  if project not in unit['projects']:unit['projects'].append(project)
  unit['pages'].append(page['key']);page_ids.append(unit['id'])
 page['units']=page_ids
 summary.append({'project':project,'file':page['file'],'chars':len(body),'code_blocks':len(converter.blocks),'inline_code':len(page['inline_code'])})
units=[u for u in units if u['pages']]
(BASE/'sources/pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(BASE/'sources/units.json').write_text(json.dumps(units,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(BASE/'sources/asset-urls.json').write_text(json.dumps(list(assets.values()),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for project in sorted({p['project'] for p in pages}):
 if project!='Phoenix':(ROOT/project/'sources/pages.json').write_text(json.dumps([p for p in pages if p['project']==project],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pages':len(pages),'units':len(units),'source_chars':sum(len(u['source']) for u in units),'code_blocks':sum(s['code_blocks'] for s in summary),'inline_code':sum(s['inline_code'] for s in summary),'assets':len(assets),'largest':sorted(summary,key=lambda s:s['chars'],reverse=True)[:10]},ensure_ascii=False,indent=2))
