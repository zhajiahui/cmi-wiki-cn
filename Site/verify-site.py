"""Check built document coverage, local links, anchors and search labels."""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import json
import sys
from html.parser import HTMLParser
import os
from hooks import PROJECTS, PHOENIX_PROJECTS, PLUGIN_PROJECTS, PROJECT_TAB, DISPLAY_NAMES, TABLE_PAGES, configuration_pages
ROOT=Path(__file__).resolve().parent.parent
SITE=ROOT/'.cache/site'
SITE_ROOT=SITE.resolve()
errors=[]

def page_manifest(project):
    source=ROOT/project/'sources'
    rows=json.loads((source/'manifest.json').read_text(encoding='utf-8'))
    for name in ('configuration-manifest.json','imported-configuration-manifest.json','wiki-manifest.json'):
        path=source/name
        if path.is_file():rows+=json.loads(path.read_text(encoding='utf-8'))
    return rows

tab_addresses={base+'index.html':PROJECT_TAB.get(project,project) for project,base in PROJECTS}
class DocumentFacts(HTMLParser):
    """Read links, anchors and tab labels without constructing a full page DOM."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors=set();self.references=[];self.tabs=[];self.active=None
        self.active_item=False;self.tab_text=None;self.tab_active=False
    def handle_starttag(self,tag,attributes):
        attrs=dict(attributes);classes=attrs.get('class','').split()
        if attrs.get('id') or (tag=='a' and attrs.get('name')):self.anchors.add(attrs.get('id') or attrs['name'])
        if tag in {'a','img','script','link','video','source'}:self.references.append(attrs.get('src') if tag in {'img','script','video','source'} else attrs.get('href'))
        if tag=='li' and 'md-tabs__item--active' in classes:self.active_item=True
        if tag=='a' and 'md-tabs__link' in classes:self.tab_text=[];self.tab_active=self.active_item
    def handle_data(self,data):
        if self.tab_text is not None:self.tab_text.append(data)
    def handle_endtag(self,tag):
        if tag=='a' and self.tab_text is not None:
            text=''.join(self.tab_text).strip();self.tabs.append(text)
            if self.tab_active:self.active=text
            self.tab_text=None
        if tag=='li':self.active_item=False

html_paths=sorted(SITE.rglob('*.html'))
html_files={path.absolute():None for path in html_paths}
existing_files={path.absolute() for path in SITE.rglob('*') if path.is_file()}
anchors={};references={};page_tabs={}
for path in html_paths:
    resolved=path.absolute();facts=DocumentFacts();facts.feed(path.read_text(encoding='utf-8'));facts.close()
    anchors[resolved]=facts.anchors;references[resolved]=facts.references
    if path.relative_to(SITE).as_posix() in tab_addresses:page_tabs[resolved]=(facts.tabs,facts.active)
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
        target=Path(os.path.abspath(target))
        if target not in existing_files and target/'index.html' in existing_files:target=target/'index.html'
        checked+=1
        if not target.is_relative_to(SITE_ROOT) or target not in existing_files:errors.append(f'Broken file: {path.relative_to(SITE)}: {url}');continue
        if parts.fragment and target in html_files:
            fragment=unquote(parts.fragment)
            if fragment not in anchors[target]:errors.append(f'Broken anchor: {path.relative_to(SITE)}: {url}')
for project,base in PROJECTS:
    manifest=page_manifest(project)
    for row in manifest:
        file=Path(base+row['file'])
        output=(SITE/file.parent/'index.html') if file.name=='index.md' else (SITE/file.with_suffix('')/'index.html')
        if not output.is_file():errors.append('Translated page not built: '+str(file))
        else:
            edit_url=f'https://github.com/zhajiahui/cmi-wiki-cn/edit/main/{project}/docs/{row["file"]}'
            if edit_url not in references[output.resolve()]:errors.append('Wrong source edit link: '+str(file))
search=json.loads((SITE/'search/search_index.json').read_text(encoding='utf-8'))
project_pages={}
for name,base in PROJECTS:
    items=[row for row in search['docs'] if '#' not in row['location'] and (row['location'].startswith(base) if base else not row['location'].startswith(tuple(prefix for _,prefix in PROJECTS if prefix)))]
    expected=page_manifest(name)
    if len(items)!=len(expected):errors.append('Search page coverage mismatch: '+name)
    if any(not item['title'].startswith(DISPLAY_NAMES.get(name,name)+' · ') or DISPLAY_NAMES.get(name,name) not in item.get('tags',[]) for item in items):errors.append('Search project labels missing: '+name)
    project_pages[name]=len(items)
table_entries=[row for row in search['docs'] if row['location'].startswith(tuple(source.removesuffix('.md')+'/#'+anchor for source,anchor in TABLE_PAGES.items()))]
residence_entries=[row for row in table_entries if row['location'].startswith('residence/')]
if len(residence_entries)!=172:errors.append('Residence permission or flag search rows missing')
for item in table_entries:
    parts=urlsplit(item['location'])
    target=(SITE/parts.path/'index.html').resolve()
    if unquote(parts.fragment) not in anchors[target]:errors.append('Search table-row anchor missing: '+item['location'])
configuration_entries={item['location']:item for item in search['docs']}
configuration_fields=0
for source,page in configuration_pages().items():
    relative=source.removesuffix('.md')+'/'
    if source.endswith('/index.md'):relative=source.removesuffix('index.md')
    target=(SITE/relative/'index.html').resolve()
    for item in page.get('anchors',[]):
        if item['id'] not in anchors[target]:errors.append('Configuration field anchor missing: '+relative+'#'+item['id'])
        if not item['heading']:
            configuration_fields+=1
            if relative+'#'+item['id'] not in configuration_entries:errors.append('Configuration field not searchable: '+relative+'#'+item['id'])
for address,project in tab_addresses.items():
    tabs,active=page_tabs[(SITE/address).resolve()]
    if tabs!=['CMI','Residence','Typewriter','Phoenix','插件与配置']:errors.append('Top-level tabs differ: '+address)
    if active!=project:errors.append('Wrong active project tab: '+address)
print(json.dumps({'html_pages':len(html_files),'local_references':checked,'search_entries':len(search['docs']),'table_row_entries':len(table_entries),'configuration_fields':configuration_fields,'project_pages':project_pages,'errors':errors},ensure_ascii=False,indent=2))
if errors:sys.exit(1)
