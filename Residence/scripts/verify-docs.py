"""Check Residence page coverage, commands, flags, source examples and assets."""
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys
import markdown
import yaml
from bs4 import BeautifulSoup

BASE=Path(__file__).resolve().parents[1]
DOCS=BASE/'docs'
errors=[]
rows=json.loads((BASE/'sources/pages.json').read_text(encoding='utf-8'))
manifest=json.loads((BASE/'sources/manifest.json').read_text(encoding='utf-8'))
assets=json.loads((BASE/'sources/assets.json').read_text(encoding='utf-8'))
if {r['id'] for r in rows}!={p['source_id'] for p in manifest}:errors.append('Page coverage mismatch')
def navfiles(items):
    for item in items:
        for value in item.values():
            if isinstance(value,list):yield from navfiles(value)
            else:yield value
nav=list(navfiles(yaml.safe_load((BASE/'mkdocs.yml').read_text(encoding='utf-8'))['nav']))
if len(nav)!=len(set(nav)) or set(nav)!={p['file'] for p in manifest}:errors.append('Navigation coverage mismatch')
code_count=0
counts={}
norm=lambda text:re.sub(r'\s+','',text)
for page in manifest:
    path=DOCS/page['file']
    if not path.is_file():errors.append('Missing page: '+page['file']);continue
    text=path.read_text(encoding='utf-8')
    source_path=BASE/'sources/html'/f"{page['source_id']}.html"
    source_text=source_path.read_text(encoding='utf-8')
    if hashlib.sha256(source_text.encode()).hexdigest()!=page['source_sha256']:errors.append('Source hash changed: '+page['file'])
    soup=BeautifulSoup(source_text,'html.parser')
    blocks=[]
    for pre in soup.find_all('pre'):
        for br in pre.find_all('br'):br.replace_with('\n')
        if pre.get_text().strip():blocks.append(norm(pre.get_text()))
    output_blocks=Counter(norm(m) for m in re.findall(r'^```[^\n]*\n([\s\S]*?)^```',text,re.M))
    code_count+=len(blocks)
    for block,count in Counter(blocks).items():
        if output_blocks[block]<count:errors.append('Source code block changed: '+page['file']+': '+block[:70])
    for image in soup.find_all('img',src=True):
        info=assets.get(image['src'])
        if not info or info['file'].rsplit('/',1)[-1] not in text:errors.append('Source image missing: '+image['src'])
    body=re.sub(r'^---\n.*?\n---\n','',text,count=1,flags=re.S)
    rendered=BeautifulSoup(markdown.markdown(body,extensions=['fenced_code','tables','attr_list']),'html.parser')
    for node in rendered.find_all(['a','img']):
        url=node.get('href') if node.name=='a' else node.get('src')
        if not url:continue
        parts=urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:continue
        target=(path.parent/unquote(parts.path)).resolve()
        if not target.is_relative_to(DOCS.resolve()) or not target.exists():errors.append('Broken local reference: '+page['file']+': '+url)
    if '{{SOURCE_CODE_' in text:errors.append('Unresolved source block: '+page['file'])
    original=(BASE/'sources/en'/f"{page['source_id']}.md").read_text(encoding='utf-8')
    if page['file']=='commands.md':
        signatures=re.findall(r'^- \*\*(.+?)\*\*\s*–',original,re.M)
        headings=re.findall(r'^### `([^`]+)`$',text,re.M)
        counts['commands']=len(signatures)
        normalize=lambda value:re.sub(r'\s+',' ',value).strip()
        if [normalize(s) for s in signatures]!=[normalize(s) for s in headings]:errors.append('Command signatures omitted or changed')
    if page['file']=='permissions.md':
        keys=re.findall(r'\*\*(residence\.[^*]+)\*\*\s*–',original)
        output_keys=re.findall(r'^\| `(residence\.[^`]+)` \|',text,re.M)
        counts['permission_nodes']=len(keys)
        if keys!=output_keys:errors.append('Permission nodes omitted or changed')
    if page['file']=='flags.md':
        keys=re.findall(r'^\*\*([a-z0-9]+)\*\*\s*–',original,re.M)
        output_keys=re.findall(r'^\| `([a-z0-9]+)` \|',text,re.M)
        counts['flags']=len(keys)
        if keys!=output_keys:errors.append('Flag identifiers omitted or changed')
    if page['file']=='placeholders.md':counts['placeholders']=len(set(re.findall(r'%residence_[^%\s]+%',original)))
    for token in set(re.findall(r'%residence_[^%\s]+%|Residence\w+Event',original)):
        if token not in text:errors.append('Technical identifier omitted: '+page['file']+': '+token)
for info in assets.values():
    path=DOCS/info['file']
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=info['sha256']:errors.append('Asset hash mismatch: '+info['file'])
report={'project':'Residence','source_pages':len(rows),'translated_pages':len(manifest),**counts,'verbatim_source_code_blocks':code_count,'assets':len(assets),'errors':errors}
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:sys.exit(1)
