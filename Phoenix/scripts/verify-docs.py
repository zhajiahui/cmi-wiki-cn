"""Check the complete Phoenix source snapshot and all translated projects."""
from pathlib import Path
from collections import Counter
import json,re,hashlib,yaml,sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import markdown
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'Phoenix'
pages=json.loads((BASE/'sources/pages.json').read_text(encoding='utf-8'))
assets=json.loads((BASE/'sources/all-assets.json').read_text(encoding='utf-8'))
errors=[];code_count=inline_count=anchor_count=0
if len(pages)!=243:errors.append('Official page coverage changed; review the source snapshot.')
def blocks(text):return [m[2] for m in re.finditer(r'^(`{3,})[^\n]*\n([\s\S]*?)^\1\s*$',text,re.M)]
def inline(text):
 text=re.sub(r'^(`{3,})[^\n]*\n[\s\S]*?^\1\s*$','',text,flags=re.M)
 return Counter(m[2].replace('\\|','|') for m in re.finditer(r'(?<!`)(`{1,2})([^`\n]+)\1(?!`)',text))
def navfiles(items):
 for item in items:
  for value in item.values():
   if isinstance(value,list):yield from navfiles(value)
   else:yield value
counts={}
for project in sorted({p['project'] for p in pages}):
 source=[p for p in pages if p['project']==project]
 manifest=json.loads((ROOT/project/'sources/manifest.json').read_text(encoding='utf-8'))
 if {p['key'] for p in source}!={p['source_key'] for p in manifest}:errors.append('Missing source pages: '+project)
 nav=list(navfiles(yaml.safe_load((ROOT/project/'mkdocs.yml').read_text(encoding='utf-8'))['nav']))
 extra_path=ROOT/project/'sources/imported-configuration-manifest.json'
 extra=json.loads(extra_path.read_text('utf-8')) if extra_path.is_file() else []
 if len(nav)!=len(set(nav)) or set(nav)!={p['file'] for p in manifest+extra}:errors.append('Navigation coverage mismatch: '+project)
 counts[project]=len(manifest)
for p in pages:
 root=ROOT/p['project'];name=p['project']+'/'+p['file'];original=(root/p['html']).read_bytes()
 if hashlib.sha256(original).hexdigest()!=p['sha256']:errors.append('Source snapshot modified: '+name)
 en=(root/p['english']).read_text(encoding='utf-8');zh=(root/'docs'/p['file']).read_text(encoding='utf-8')
 a,b=blocks(en),blocks(zh);code_count+=len(a)
 if a!=b:errors.append('Code changed: '+name)
 tokens=inline(en);inline_count+=sum(tokens.values());missing=tokens-inline(zh)
 if missing:errors.append('Inline code changed: '+name+': '+repr(list(missing.elements())))
 ids=re.findall(r'\{#([^}]+)\}',en);anchor_count+=len(ids)
 if any('{#'+key+'}' not in zh for key in ids):errors.append('Original anchor lost: '+name)
 if re.search(r'ZXQ\s*\d+\s*QXZ|PHXCODEBLOCK|PHXMEDIA|PHXTABLETOKEN',zh):errors.append('Unresolved marker: '+name)
 original_dom=BeautifulSoup(original,'html.parser');main=original_dom.select_one('main') or original_dom.select_one('.VPHome')
 for media in main.select('img[src],video[src],source[src]'):
  url=urljoin(p['url'],media['src']);info=next((a for a in assets if a['project']==p['project'] and a['url']==url),None)
  if not info or info['file'].rsplit('/',1)[-1] not in zh:errors.append('Source media missing: '+name)
 expected_code=[a['content']+('' if a['content'].endswith('\n') else '\n') for a in p['code_blocks']]
 if blocks(en)!=expected_code:errors.append('Original HTML code block missing: '+name)
 rendered=BeautifulSoup(markdown.markdown(zh,extensions=['fenced_code','tables','attr_list','md_in_html','pymdownx.superfences']),'html.parser')
 source_tables=main.find_all('table');output_tables=rendered.find_all('table')
 if len(source_tables)!=len(output_tables):errors.append('Source table missing: '+name)
 else:
  for original_table,output_table in zip(source_tables,output_tables):
   original_rows=original_table.find_all('tr');output_rows=output_table.find_all('tr')
   if len(original_rows)!=len(output_rows):errors.append('Table rows changed: '+name)
   elif any(sum(int(c.get('colspan',1)) for c in a.find_all(['th','td']))!=len(b.find_all(['th','td'])) for a,b in zip(original_rows,output_rows)):errors.append('Table columns changed: '+name)
seen=set()
for project in counts:
 for unit in json.loads((ROOT/project/'sources/translations.json').read_text(encoding='utf-8')):
  if unit['id'] in seen:continue
  seen.add(unit['id'])
  clean=lambda text:re.sub(r'`+[^`]*`+|\]\([^\n]*?\)|<[^>]+>|\{#[^}]+\}','',text)
  nums=lambda text:Counter(re.findall(r'\d+(?:\.\d+)*',clean(text)))
  if nums(unit['source'])-nums(unit['zh']):errors.append('Prose number changed: '+str(unit['id']))
for info in assets:
 path=ROOT/info['project']/'docs'/info['file']
 if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=info['sha256']:errors.append('Media changed: '+str(path.relative_to(ROOT)))
report={'source_snapshot':'2026-10-19','source_pages':len(pages),'translated_pages':sum(counts.values()),'project_pages':counts,'verbatim_code_blocks':code_count,'protected_inline_tokens':inline_count,'source_heading_anchors':anchor_count,'native_assets':len(assets),'errors':errors}
(BASE/'notes/verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:sys.exit(1)
