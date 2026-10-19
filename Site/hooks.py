"""Assemble the independent plugin documentation projects for one MkDocs site."""
from pathlib import Path
from urllib.parse import urlsplit
import json
import posixpath
import yaml
import jieba
from bs4 import BeautifulSoup
from html import escape
from mkdocs.plugins import event_priority
from mkdocs.utils import get_relative_url
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent
DOCS=BASE/'docs'
TRACKING=BASE/'.cache/assembled-files.json'
PHOENIX_PROJECTS=[('Phoenix','phoenix/'),('MMOItems','mmoitems/'),('MMOCore','mmocore/'),('MMOInventory','mmoinventory/'),('MMOProfiles','mmoprofiles/'),('MythicLib','mythiclib/'),('BountyHunters','bounty-hunters/'),('Contracts','contracts/')]
PROJECTS=[('CMI',''),('Residence','residence/'),('Typewriter','typewriter/')]+PHOENIX_PROJECTS
SHARED={'assets/wiki.css','assets/logo.svg'}

def prefix_nav(items,prefix):
    return [{label:prefix_nav(value,prefix) if isinstance(value,list) else prefix+value for label,value in item.items()} for item in items]

def on_config(config):
    output=Path(config.site_dir).resolve()
    source_dirs=[ROOT/project for project,_ in PROJECTS]+[BASE]
    if output==ROOT or any(output.is_relative_to(source.resolve()) for source in source_dirs):
        raise ValueError('Build output overlaps a source project directory.')
    expected=set();nav=[];phoenix_nav=[];phoenix_notes=[]
    for project,prefix in PROJECTS:
        source_root=ROOT/project/'docs'
        project_config=yaml.safe_load((ROOT/project/'mkdocs.yml').read_text(encoding='utf-8'))
        project_nav=prefix_nav(project_config['nav'],prefix)
        if project=='Phoenix':phoenix_nav.extend(project_nav[:1]);phoenix_notes.extend(project_nav[1:])
        elif (project,prefix) in PHOENIX_PROJECTS:phoenix_nav.append({project:project_nav})
        else:nav.append({project:project_nav})
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
    nav.append({'Phoenix':phoenix_nav+[{'站点说明':phoenix_notes}]})
    config.nav=nav
    return config

TABLE_PAGES={'residence/permissions.md':'permission-','residence/flags.md':'flag-'}
TABLE_PAGES.update({prefix+'general/permissions.md':'permission-' for project,prefix in PHOENIX_PROJECTS if project in {'MMOItems','MMOCore','MMOInventory','MMOProfiles','BountyHunters'}})

CONFIGURATION_MANIFEST=ROOT/'CMI/sources/configuration-manifest.json'

def configuration_pages():
    return {row['file']:row for row in json.loads(CONFIGURATION_MANIFEST.read_text(encoding='utf-8'))}

def on_page_content(html,*,page,config,files):
    prefix=TABLE_PAGES.get(page.file.src_uri)
    configuration=configuration_pages().get(page.file.src_uri) if page.file.src_uri.startswith('configuration/') else None
    if not prefix and not configuration and '<video ' not in html:return html
    soup=BeautifulSoup(html,'html.parser')
    if configuration:
        article=soup.new_tag('div')
        article['class']='cmi-configuration'
        for node in list(soup.contents):article.append(node.extract())
        soup.append(article)
        blocks=article.select('div.highlight pre code')
        for item in configuration.get('anchors',[]):
            if item['heading']:continue
            line=blocks[item['block']].find('a',id=lambda value:value and value.endswith('-'+str(item['line'])))
            if line is None:raise ValueError('Configuration code anchor missing: '+'.'.join(item['path']))
            # Material treats span[id] as line wrappers; use an empty anchor instead.
            anchor=soup.new_tag('a',id=item['id'])
            anchor['class']='config-key-anchor'
            line.insert_before(anchor)
    # MkDocs rewrites Markdown image URLs, but leaves raw video attributes alone.
    for media in soup.find_all(['video','source']):
        for attr in ['src','poster']:
            value=media.get(attr)
            if not value or urlsplit(value).scheme or value.startswith('/'):continue
            target=posixpath.normpath(posixpath.join(posixpath.dirname(page.file.src_uri),value))
            media[attr]=get_relative_url(target,page.url)
    if not prefix:return str(soup)
    for row in soup.select('table tbody tr'):
        first=row.find('td')
        code=first.find('code') if first else None
        if not code and first and '.' in first.get_text():
            name=first.get_text();first.clear();code=soup.new_tag('code');code.string=name;first.append(code)
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
            project=next((project for project,prefix in PROJECTS if prefix and urlsplit(item['location']).path.startswith(prefix)),'CMI')
            label=project+' · '
            if not item['title'].startswith(label):item['title']=label+item['title']
    # Give every permission and flag its own result and a matching table-row anchor.
    for source in TABLE_PAGES:
        project=next(project for project,prefix in PROJECTS if prefix and source.startswith(prefix))
        relative=source.removesuffix('.md')+'/'
        page_html=Path(config.site_dir)/relative/'index.html'
        soup=BeautifulSoup(page_html.read_text(encoding='utf-8'),'html.parser')
        for row in soup.select('table tbody tr[id]'):
            cells=row.find_all('td')
            code=cells[0].find('code')
            name=code.get_text()
            description=cells[1].get_text(' ',strip=True)
            segmented='\u200b'.join(jieba.cut(description))
            index['docs'].append({'location':relative+'#'+row['id'],'title':project+' · '+name,'text':'<p><code>'+escape(name)+'</code> '+escape(segmented)+'</p>','tags':[project]})
    # Keep individual configuration fields searchable after moving prose into YAML comments.
    for source,configuration in configuration_pages().items():
        relative=source.removesuffix('index.md') if source.endswith('/index.md') else source.removesuffix('.md')+'/'
        for item in configuration.get('anchors',[]):
            if item['heading']:continue
            name='.'.join(item['path'])
            description='\u200b'.join(jieba.cut(item['text']))
            index['docs'].append({'location':relative+'#'+item['id'],'title':'CMI · '+name,'text':'<p><code>'+escape(name)+'</code> '+escape(description)+'</p>','tags':['CMI']})
    path.write_text(json.dumps(index,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
    fix_chinese_search(config.site_dir)


def fix_chinese_search(site_dir):
    """Include the final word/character in Material 9.7.7's Han query segmenter."""
    workers=Path(site_dir)/'assets/javascripts/workers'
    worker=next(workers.glob('search.*.min.js'))
    code=worker.read_text(encoding='utf-8')
    changes={
        'for(let o=s+1;o<t.length;o++)t.slice(s,o)in e':'for(let o=s+1;o<=t.length;o++)t.slice(s,o)in e',
        'n[a]&&a<t.length-1&&(i[s++]=a)':'n[a]&&a<t.length&&(i[s++]=a)',
    }
    for old,new in changes.items():
        if code.count(old)!=1:raise ValueError('Search worker changed; review the Han segmenter fix against the pinned Material version.')
        code=code.replace(old,new)
    worker.write_text(code,encoding='utf-8')
    source_map=worker.with_suffix(worker.suffix+'.map')
    data=json.loads(source_map.read_text(encoding='utf-8'))
    for i,name in enumerate(data['sources']):
        if name.endswith('/query/segment/index.ts'):
            data['sourcesContent'][i]=data['sourcesContent'][i].replace('j < query.length','j <= query.length').replace('q < query.length - 1','q < query.length')
    source_map.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
