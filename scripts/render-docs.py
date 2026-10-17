"""Render reviewed translation entries and keep code, references and assets intact."""
from pathlib import Path
from urllib.parse import urljoin,urlsplit,unquote,urldefrag
from concurrent.futures import ThreadPoolExecutor,as_completed
import json,re,hashlib,requests,os,posixpath
from bs4 import BeautifulSoup
import yaml
BASE=Path(__file__).resolve().parents[1]
DOCS=BASE/'docs';DOCS.mkdir(exist_ok=True)
ROWS=json.loads((BASE/'sources/pages.json').read_text(encoding='utf-8'))
TITLES={'cmi':'前言','first-run':'首次运行','commands':'指令列表','permissions':'权限节点','placeholders':'占位符','hex-colors':'十六进制颜色','hologram-api':'全息图 API','bungeecord':'BungeeCord 跨服','api':'自定义事件 API','faq':'常见问题','jail':'监狱','dynamic-signs':'动态告示牌','playtime-rewards':'在线时长奖励','holograms':'全息图','kits':'礼包','rankup-system':'自动晋级','armor-stand-editor':'盔甲架编辑器','portals':'传送门','custom-text':'自定义文本','chat-rooms':'聊天室','chat-filter':'聊天过滤','scavenge':'物品分解','custom-mob-heads':'自定义生物头颅','particles':'粒子效果','custom-recipes':'自定义合成配方','elevator':'电梯','tablist':'Tab 列表','search':'查找玩家物品','scan':'扫描容器物品','totems':'不死图腾','flight-charge':'飞行能量','dialogs':'对话框','icwol':'一行创建物品','spawnmob':'生成生物','rtp':'随机传送','warmups':'指令预热','user-meta':'玩家元数据','warps':'传送点','spawn':'出生点','bossbarmsg-handling':'Boss 栏消息','kill-all':'清理实体','attached-commands':'物品附加指令','custom-alias':'自定义别名','interactive-commands':'交互指令','specialized':'特殊指令','extra':'其他功能','import-from-essentials':'从 Essentials 导入'}

def target(row):
 p=urlsplit(row['link']).path.removeprefix('/cmi/').strip('/')
 if not p:return 'index.md'
 return p+'.md'
NONEMPTY=[r for r in ROWS if (BASE/'sources/en'/f"{r['id']}.md").stat().st_size>5]
URLMAP={urlsplit(r['link']).path.rstrip('/'):target(r) for r in NONEMPTY}
SLUGMAP={r['slug']:target(r) for r in NONEMPTY}
ASSETS_PATH=BASE/'sources/assets.json'
ASSETS=json.loads(ASSETS_PATH.read_text(encoding='utf-8')) if ASSETS_PATH.exists() else {}

def copy_assets():
 urls=set()
 for row in NONEMPTY:
  soup=BeautifulSoup((BASE/'sources/html'/f"{row['id']}.html").read_text(encoding='utf-8'),'html.parser')
  for im in soup.find_all('img',src=True):urls.add(urljoin(row['link'],im['src']))
  for a in soup.find_all('a',href=True):
   u=urljoin(row['link'],a['href'])
   if re.search(r'\.(png|jpe?g|gif|webp|svg)$',urlsplit(u).path,re.I):urls.add(u)
 def fetch(u):
  if u in ASSETS and (DOCS/ASSETS[u]['file']).exists():return u,ASSETS[u]
  name=unquote(urlsplit(u).path.split('/')[-1]) or 'image'
  name=re.sub(r'[^A-Za-z0-9._-]','_',name)
  dst='assets/images/'+hashlib.sha256(u.encode()).hexdigest()[:10]+'-'+name
  try:
   response=requests.get(u,timeout=(12,90));response.raise_for_status()
   if not response.content:raise RuntimeError('empty file')
   if 'text/html' in response.headers.get('Content-Type',''):raise RuntimeError('received HTML instead of image')
   p=DOCS/dst;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(response.content)
   return u,{'file':dst,'bytes':len(response.content),'sha256':hashlib.sha256(response.content).hexdigest()}
  except Exception as e:return u,{'error':str(e)}
 with ThreadPoolExecutor(max_workers=6) as ex:
  for f in as_completed([ex.submit(fetch,u) for u in urls]):
   u,info=f.result();ASSETS[u]=info
 ASSETS_PATH.write_text(json.dumps(ASSETS,ensure_ascii=False,indent=2),encoding='utf-8')
 print('ASSETS',len(ASSETS),'FAILED',sum('error' in v for v in ASSETS.values()),flush=True)

def link_label(label,url):
 if label in ['HERE','here','THIS','this']:return '此处'
 if label in ['Video','video']:return '视频'
 path=urlsplit(url).path.rstrip('/')
 if path in URLMAP:
  r=next((r for r in NONEMPTY if target(r)==URLMAP[path]),None)
  if r and re.fullmatch(r'[A-Za-z /-]+',label):return TITLES[r['slug']]
 return label

def rewrite_links(text,row,dest):
 def link(m):
  mark,label,url,extra=m.groups()
  url=html_unescape(url);full=urljoin(row['link'],url);parts=urlsplit(full)
  new=url
  if full in ASSETS and 'file' in ASSETS[full]:new=posixpath.relpath(ASSETS[full]['file'],posixpath.dirname(dest) or '.')
  elif parts.netloc in ['www.zrips.net','zrips.net']:
   p=parts.path.rstrip('/')
   tgt=URLMAP.get(p)
   if not tgt and p.strip('/') in SLUGMAP:tgt=SLUGMAP[p.strip('/')]
   if not tgt and p=='/cmi/faq/import-from-essentials':tgt=SLUGMAP['first-run']
   if tgt:
    new=posixpath.relpath(tgt,posixpath.dirname(dest) or '.')
    # Existing explicit source anchors are retained below.
    if parts.fragment:new+='#'+parts.fragment
  elif url.startswith(('/','//')):new=full
  return f'{mark}[{link_label(label,full)}]({new}{extra})'
 rendered=re.sub(r'(!?)\[([^\]\n]*)\]\(([^\s)]+)((?:\s+"[^"]*")?)\)',link,text)
 for asset_url,info in ASSETS.items():
  if 'file' in info:
   local=posixpath.relpath(info['file'],posixpath.dirname(dest) or '.')
   rendered=rendered.replace(']('+asset_url,']('+local)
 return rendered

def html_unescape(s):
 import html
 return html.unescape(s)

def render():
 manifest=[]
 for row in NONEMPTY:
  slug=row['slug'];dest=target(row)
  custom=BASE/'sources/reviewed'/f'{slug}.md'
  if not custom.exists():raise RuntimeError('Reviewed translation missing: '+slug)
  out=custom.read_text(encoding='utf-8')
  # Preserve the original code content and restore WordPress <br> line breaks.
  soup=BeautifulSoup((BASE/'sources/html'/f"{row['id']}.html").read_text(encoding='utf-8'),'html.parser')
  originals=[]
  for pre in soup.find_all('pre'):
   for br in pre.find_all('br'):br.replace_with('\n')
   originals.append(pre.get_text())
  normalize=lambda s:re.sub(r'\s+','',s)
  def codeblock(m):
   code=m.group(2)
   for original in originals:
    if normalize(original)==normalize(code):
     indent=re.match(r'^[ \t]*',m.group(1))[0]
     body='\n'.join(indent+line for line in original.rstrip('\n').split('\n'))
     return m.group(1)+body+'\n'+m.group(3)
   return m.group(0)
  out=re.sub(r'(^[ \t]*```[^\n]*\n)([\s\S]*?)(^[ \t]*```)',codeblock,out,flags=re.M)
  anchors=[str(t.get('id')) for t in soup.find_all(id=True) if t.name not in ['div','section'] and t.get('id')]
  if anchors:out='\n'.join(f'<span id="{a}"></span>' for a in dict.fromkeys(anchors))+'\n\n'+out
  out=rewrite_links(out,row,dest)
  content=f'---\ntitle: {TITLES[slug]}\n---\n\n# {TITLES[slug]}\n\n'+out+'\n---\n\n[查看原文]('+row['link']+')\n'
  path=DOCS/dest;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
  manifest.append({'title':TITLES[slug],'source':row['link'],'source_id':row['id'],'source_modified':row['modified'],'file':dest,'source_sha256':hashlib.sha256((BASE/'sources/html'/f"{row['id']}.html").read_text(encoding='utf-8').encode('utf-8')).hexdigest(),'translation_review':'reviewed'})
 (BASE/'sources/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
 print('RENDERED',len(manifest),'PAGES',flush=True)

if __name__=='__main__':
 if '--assets' in __import__('sys').argv:copy_assets()
 render()