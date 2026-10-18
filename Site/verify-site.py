"""Check built document coverage, local links, anchors and search labels."""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import json
import sys
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent.parent
SITE=ROOT/'.cache/site'
errors=[]
html_files={file.resolve():BeautifulSoup(file.read_text(encoding='utf-8'),'html.parser') for file in SITE.rglob('*.html')}
anchors={path:{str(node.get('id') or node.get('name')) for node in soup.find_all(lambda node:node.has_attr('id') or (node.name=='a' and node.has_attr('name')))} for path,soup in html_files.items()}
checked=0
prefix='/cmi-wiki-cn/'
for path,soup in html_files.items():
    for node in soup.find_all(['a','img','script','link']):
        url=node.get('src') if node.name in {'img','script'} else node.get('href')
        if not url:continue
        parts=urlsplit(url)
        if parts.scheme or parts.netloc:continue
        ref=unquote(parts.path)
        if ref.startswith('/'):
            if not ref.startswith(prefix):errors.append('Unexpected site path: '+url);continue
            target=SITE/ref.removeprefix(prefix)
        elif ref:target=path.parent/ref
        else:target=path
        if target.is_dir():target=target/'index.html'
        target=target.resolve()
        checked+=1
        if not target.is_relative_to(SITE.resolve()) or not target.is_file():errors.append(f'Broken file: {path.relative_to(SITE)}: {url}');continue
        if parts.fragment and target in html_files:
            fragment=unquote(parts.fragment)
            if fragment not in anchors[target]:errors.append(f'Broken anchor: {path.relative_to(SITE)}: {url}')
for project,base in [('CMI',''),('Residence','residence/')]:
    manifest=json.loads((ROOT/project/'sources/manifest.json').read_text(encoding='utf-8'))
    for row in manifest:
        file=Path(base+row['file'])
        output=(SITE/file.parent/'index.html') if file.name=='index.md' else (SITE/file.with_suffix('')/'index.html')
        if not output.is_file():errors.append('Translated page not built: '+str(file))
        else:
            edit_url=f'https://github.com/zhajiahui/cmi-wiki-cn/edit/main/{project}/docs/{row["file"]}'
            if not html_files[output.resolve()].find('a',href=edit_url):errors.append('Wrong source edit link: '+str(file))
search=json.loads((SITE/'search/search_index.json').read_text(encoding='utf-8'))
cmipages=[row for row in search['docs'] if '#' not in row['location'] and not row['location'].startswith('residence/')]
respages=[row for row in search['docs'] if '#' not in row['location'] and row['location'].startswith('residence/')]
if len(cmipages)!=45 or len(respages)!=10:errors.append('Search page coverage mismatch')
for name,items in [('CMI',cmipages),('Residence',respages)]:
    if any(not item['title'].startswith(name+' · ') or name not in item.get('tags',[]) for item in items):errors.append('Search project labels missing: '+name)
for address,project in [('index.html','CMI'),('residence/index.html','Residence')]:
    soup=html_files[(SITE/address).resolve()]
    if [node.get_text(strip=True) for node in soup.select('.md-tabs__link')]!=['CMI','Residence']:errors.append('Expected exactly two top-level tabs: '+address)
    active=soup.select_one('.md-tabs__item--active')
    if not active or active.get_text(strip=True)!=project:errors.append('Wrong active project tab: '+address)
print(json.dumps({'html_pages':len(html_files),'local_references':checked,'search_entries':len(search['docs']),'cmi_pages':len(cmipages),'residence_pages':len(respages),'errors':errors},ensure_ascii=False,indent=2))
if errors:sys.exit(1)
