"""Assemble the independent CMI and Residence projects for one MkDocs site."""
from pathlib import Path
from urllib.parse import urlsplit
import json
import yaml
import jieba
from bs4 import BeautifulSoup
from html import escape
from mkdocs.plugins import event_priority
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent
DOCS=BASE/'docs'
TRACKING=BASE/'.cache/assembled-files.json'
PROJECTS=[('CMI',''),('Residence','residence/')]
SHARED={'assets/wiki.css','assets/logo.svg'}

def prefix_nav(items,prefix):
    return [{label:prefix_nav(value,prefix) if isinstance(value,list) else prefix+value for label,value in item.items()} for item in items]

def on_config(config):
    output=Path(config.site_dir).resolve()
    source_dirs=[ROOT/'CMI',ROOT/'Residence',BASE]
    if output==ROOT or any(output.is_relative_to(source.resolve()) for source in source_dirs):
        raise ValueError('Build output overlaps a source project directory.')
    expected=set();nav=[]
    for project,prefix in PROJECTS:
        source_root=ROOT/project/'docs'
        project_config=yaml.safe_load((ROOT/project/'mkdocs.yml').read_text(encoding='utf-8'))
        nav.append({project:prefix_nav(project_config['nav'],prefix)})
        for source in source_root.rglob('*'):
            if not source.is_file():continue
            relative=source.relative_to(source_root).as_posix()
            destination=prefix+relative
            if destination in SHARED:continue
            target=DOCS/destination
            target.parent.mkdir(parents=True,exist_ok=True)
            if source.suffix=='.md':
                original=source.read_text(encoding='utf-8')
                header,body=original[4:].split('\n---\n',1)
                meta=yaml.safe_load(header)
                meta['tags']=[project]
                meta['edit_url']=f'https://github.com/zhajiahui/cmi-wiki-cn/edit/main/{project}/docs/{relative}'
                content=('---\n'+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False)+'---\n'+body).encode('utf-8')
            else:content=source.read_bytes()
            if not target.exists() or target.read_bytes()!=content:target.write_bytes(content)
            expected.add(destination)
    if TRACKING.exists():
        for obsolete in set(json.loads(TRACKING.read_text(encoding='utf-8')))-expected:
            stale=(DOCS/obsolete).resolve()
            if not stale.is_relative_to(DOCS.resolve()) or obsolete in SHARED:raise ValueError('Invalid stale document path')
            if stale.is_file():stale.unlink()
    TRACKING.parent.mkdir(exist_ok=True)
    TRACKING.write_text(json.dumps(sorted(expected),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    config.nav=nav
    return config

TABLE_PAGES={'residence/permissions.md':'permission-','residence/flags.md':'flag-'}

def on_page_content(html,*,page,config,files):
    prefix=TABLE_PAGES.get(page.file.src_uri)
    if not prefix:return html
    soup=BeautifulSoup(html,'html.parser')
    for row in soup.select('table tbody tr'):
        first=row.find('td')
        code=first.find('code') if first else None
        if code:row['id']=prefix+code.get_text()
    return str(soup)

def on_page_markdown(markdown,*,page,config,files):
    page.edit_url=page.meta['edit_url']
    return markdown

@event_priority(-100)
def on_post_build(config):
    path=Path(config.site_dir)/'search/search_index.json'
    index=json.loads(path.read_text(encoding='utf-8'))
    for item in index['docs']:
        if '#' not in item['location']:
            project='Residence' if urlsplit(item['location']).path.startswith('residence/') else 'CMI'
            label=project+' · '
            if not item['title'].startswith(label):item['title']=label+item['title']
    # Give every permission and flag its own result and a matching table-row anchor.
    for source in TABLE_PAGES:
        relative=source.removesuffix('.md')+'/'
        page_html=Path(config.site_dir)/relative/'index.html'
        soup=BeautifulSoup(page_html.read_text(encoding='utf-8'),'html.parser')
        for row in soup.select('table tbody tr[id]'):
            cells=row.find_all('td')
            code=cells[0].find('code')
            name=code.get_text()
            description=cells[1].get_text(' ',strip=True)
            segmented='\u200b'.join(jieba.cut(description))
            index['docs'].append({'location':relative+'#'+row['id'],'title':'Residence · '+name,'text':'<p><code>'+escape(name)+'</code> '+escape(segmented)+'</p>','tags':['Residence']})
    path.write_text(json.dumps(index,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
