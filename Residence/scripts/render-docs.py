"""Render the Residence translation, local links and original assets."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import hashlib
import json
import posixpath
import re
import sys
import requests
from bs4 import BeautifulSoup

BASE = Path(__file__).resolve().parents[1]
DOCS = BASE / 'docs'
TITLES = {'residence':'前言','creating-residence':'创建与管理领地','commands':'指令列表','flags':'领地标志（Flags）','permissions':'权限节点','market':'领地市场','placeholders':'占位符','antigrief':'防熊保护（AntiGrief）','raid':'领地战争（Raid）','api':'开发者 API'}
ROWS = json.loads((BASE / 'sources/pages.json').read_text(encoding='utf-8'))
URLMAP = {urlsplit(r['link']).path.rstrip('/'): 'index.md' if r['slug']=='residence' else r['slug']+'.md' for r in ROWS}
ASSET_PATH = BASE / 'sources/assets.json'
ASSETS = json.loads(ASSET_PATH.read_text(encoding='utf-8')) if ASSET_PATH.exists() else {}

def fetch_assets():
    urls = set()
    for row in ROWS:
        soup = BeautifulSoup((BASE / 'sources/html' / f"{row['id']}.html").read_text(encoding='utf-8'), 'html.parser')
        for image in soup.find_all('img', src=True):
            urls.add(urljoin(row['link'], image['src']))
        for link in soup.find_all('a', href=True):
            full = urljoin(row['link'], link['href'])
            if re.search(r'\.(png|jpe?g|gif|webp|svg)$', urlsplit(full).path, re.I): urls.add(full)
    def fetch(url):
        if url in ASSETS and 'file' in ASSETS[url] and (DOCS / ASSETS[url]['file']).exists(): return url, ASSETS[url]
        name = re.sub(r'[^A-Za-z0-9._-]', '_', unquote(urlsplit(url).path.rsplit('/',1)[-1]))
        local = 'assets/images/' + hashlib.sha256(url.encode()).hexdigest()[:10] + '-' + name
        response = requests.get(url, timeout=(15,90))
        response.raise_for_status()
        if not response.content or 'text/html' in response.headers.get('Content-Type',''): raise RuntimeError('Invalid image response: '+url)
        target = DOCS / local
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(response.content)
        return url, {'file':local,'bytes':len(response.content),'sha256':hashlib.sha256(response.content).hexdigest()}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for url, info in pool.map(fetch, sorted(urls)): ASSETS[url] = info
    ASSET_PATH.write_text(json.dumps(ASSETS,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def render():
    DOCS.mkdir(exist_ok=True)
    manifest = []
    for row in ROWS:
        dest = URLMAP[urlsplit(row['link']).path.rstrip('/')]
        reviewed = BASE / 'sources/reviewed' / (row['slug']+'.md')
        body = reviewed.read_text(encoding='utf-8')
        if '{{SOURCE_CODE_' in body: raise RuntimeError('Unresolved code reference: '+str(reviewed))
        def link(match):
            image, label, url = match.groups()
            full = urljoin(row['link'],url)
            parts = urlsplit(full)
            if full in ASSETS:
                return image+'['+label+']('+posixpath.relpath(ASSETS[full]['file'],posixpath.dirname(dest) or '.')+')'
            if parts.netloc in {'zrips.net','www.zrips.net'} and parts.path.rstrip('/') in URLMAP:
                local = posixpath.relpath(URLMAP[parts.path.rstrip('/')],posixpath.dirname(dest) or '.')
                if parts.fragment: local += '#'+parts.fragment
                return image+'['+label+']('+local+')'
            return match[0]
        body = re.sub(r'(!?)\[([^\]]*)\]\(([^\s)]+)\)',link,body)
        # Preserve explicit source anchors independently of translated headings.
        soup = BeautifulSoup((BASE/'sources/html'/f"{row['id']}.html").read_text(encoding='utf-8'),'html.parser')
        ids = list(dict.fromkeys(node['id'] for node in soup.find_all(id=True) if node.name not in {'div','section'}))
        if ids: body = '\n'.join(f'<span id="{anchor}"></span>' for anchor in ids)+'\n\n'+body
        title = TITLES[row['slug']]
        text = f'---\ntitle: {title}\n---\n\n# {title}\n\n'+body.rstrip()+'\n\n---\n\n[查看原文]('+row['link']+')\n'
        (DOCS/dest).write_text(text,encoding='utf-8',newline='\n')
        manifest.append({'title':title,'source':row['link'],'source_id':row['id'],'source_modified':row['modified'],'file':dest,'source_sha256':hashlib.sha256((BASE/'sources/html'/f"{row['id']}.html").read_text(encoding='utf-8').encode()).hexdigest(),'translation_review':'reviewed'})
    (BASE/'sources/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'translated_pages':len(manifest),'assets':len(ASSETS)},ensure_ascii=False))

if __name__ == '__main__':
    if '--assets' in sys.argv: fetch_assets()
    render()
