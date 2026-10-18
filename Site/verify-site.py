"""Check built document coverage, local links, anchors and search labels."""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import json
import sys
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent.parent
SITE=ROOT/'.cache/site'
errors=[]
# Keep compact facts about each document, rather than hundreds of full DOMs.
html_paths=sorted(SITE.rglob('*.html'))
html_files={path.resolve():None for path in html_paths}
anchors={};references={};page_tabs={}
for path in html_paths:
    resolved=path.resolve()
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    anchors[resolved]={str(n.get('id') or n.get('name')) for n in soup.find_all(lambda n:n.has_attr('id') or (n.name=='a' and n.has_attr('name')))}
    references[resolved]=[n.get('src') if n.name in {'img','script','video','source'} else n.get('href') for n in soup.find_all(['a','img','script','link','video','source'])]
    if path.relative_to(SITE).as_posix() in {'index.html','residence/index.html','typewriter/index.html'}:
        active=soup.select_one('.md-tabs__item--active')
        page_tabs[resolved]=([n.get_text(strip=True) for n in soup.select('.md-tabs__link')],active.get_text(strip=True) if active else None)
    soup.decompose()
checked=0
prefix='/cmi-wiki-cn/'
for path,urls in references.items():
    for url in urls:
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
for project,base in [('CMI',''),('Residence','residence/'),('Typewriter','typewriter/')]:
    manifest=json.loads((ROOT/project/'sources/manifest.json').read_text(encoding='utf-8'))
    for row in manifest:
        file=Path(base+row['file'])
        output=(SITE/file.parent/'index.html') if file.name=='index.md' else (SITE/file.with_suffix('')/'index.html')
        if not output.is_file():errors.append('Translated page not built: '+str(file))
        else:
            edit_url=f'https://github.com/zhajiahui/cmi-wiki-cn/edit/main/{project}/docs/{row["file"]}'
            if edit_url not in references[output.resolve()]:errors.append('Wrong source edit link: '+str(file))
search=json.loads((SITE/'search/search_index.json').read_text(encoding='utf-8'))
project_pages={}
for name,base in [('CMI',''),('Residence','residence/'),('Typewriter','typewriter/')]:
    items=[row for row in search['docs'] if '#' not in row['location'] and (row['location'].startswith(base) if base else not row['location'].startswith(('residence/','typewriter/')))]
    expected=json.loads((ROOT/name/'sources/manifest.json').read_text(encoding='utf-8'))
    if len(items)!=len(expected):errors.append('Search page coverage mismatch: '+name)
    if any(not item['title'].startswith(name+' · ') or name not in item.get('tags',[]) for item in items):errors.append('Search project labels missing: '+name)
    project_pages[name]=len(items)
table_entries=[row for row in search['docs'] if row['location'].startswith(('residence/permissions/#permission-','residence/flags/#flag-'))]
if len(table_entries)!=172:errors.append('Permission or flag search rows missing')
for item in table_entries:
    parts=urlsplit(item['location'])
    target=(SITE/parts.path/'index.html').resolve()
    if unquote(parts.fragment) not in anchors[target]:errors.append('Search table-row anchor missing: '+item['location'])
for address,project in [('index.html','CMI'),('residence/index.html','Residence'),('typewriter/index.html','Typewriter')]:
    tabs,active=page_tabs[(SITE/address).resolve()]
    if tabs!=['CMI','Residence','Typewriter']:errors.append('Expected exactly three top-level tabs: '+address)
    if active!=project:errors.append('Wrong active project tab: '+address)
print(json.dumps({'html_pages':len(html_files),'local_references':checked,'search_entries':len(search['docs']),'table_row_entries':len(table_entries),'project_pages':project_pages,'errors':errors},ensure_ascii=False,indent=2))
if errors:sys.exit(1)
