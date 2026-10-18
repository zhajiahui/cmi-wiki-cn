"""Fetch the official WordPress page tree without replacing reviewed translations."""
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import argparse, hashlib, html, json, re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

BASE = Path(__file__).resolve().parents[1]
API = 'https://www.zrips.net/wp-json/wp/v2/pages'

def fetch(params):
    response = requests.get(API, params=params, timeout=(20, 180))
    response.raise_for_status()
    return response.json()

def children(parent):
    found = []
    page = 1
    while True:
        batch = fetch({'parent': parent, 'per_page': 100, 'page': page,
                       '_fields': 'id,parent,slug,link,title,content,modified'})
        found.extend(batch)
        if len(batch) < 100:
            return found
        page += 1

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--initial', action='store_true', help='Create a first source archive in an empty project.')
    args = parser.parse_args()
    dest = BASE / 'sources' if args.initial else BASE / 'sources/incoming'
    if args.initial and (dest / 'pages.json').exists():
        raise SystemExit('Source archive already exists. Omit --initial to compare incoming sources.')
    root = requests.get(API + '/65', timeout=(20, 180))
    root.raise_for_status()
    pages = [root.json()]
    frontier = [65]
    seen = {65}
    with ThreadPoolExecutor(max_workers=4) as pool:
        while frontier:
            next_frontier = []
            for batch in pool.map(children, frontier):
                for page in batch:
                    if page['id'] not in seen:
                        seen.add(page['id'])
                        pages.append(page)
                        next_frontier.append(page['id'])
            frontier = next_frontier
    # Discover pages linked from article bodies but absent from the parent tree.
    paths = {urlsplit(p['link']).path.rstrip('/') for p in pages}
    extra_urls = set()
    for page in pages:
        soup = BeautifulSoup(page['content']['rendered'], 'html.parser')
        for a in soup.find_all('a', href=True):
            url = urljoin(page['link'], a['href'])
            part = urlsplit(url)
            if part.netloc in {'www.zrips.net', 'zrips.net'} and part.path.startswith('/cmi/') and part.path.rstrip('/') not in paths:
                extra_urls.add(url.split('#')[0])
    if extra_urls:
        raise SystemExit('Review extra CMI article links before completing the inventory: ' + ', '.join(sorted(extra_urls)))
    (dest / 'html').mkdir(parents=True, exist_ok=True)
    (dest / 'en').mkdir(exist_ok=True)
    inventory = []
    for page in sorted(pages, key=lambda p: p['id']):
        body = page['content']['rendered']
        (dest / 'html' / f"{page['id']}.html").write_text(body, encoding='utf-8')
        soup = BeautifulSoup(body, 'html.parser')
        for node in soup.select('script,style,svg,button,nav,form'):
            node.decompose()
        for pre in soup.find_all('pre'):
            for br in pre.find_all('br'):
                br.replace_with('\n')
            text = pre.get_text()
            pre.clear()
            pre.string = text
        for video in soup.find_all('iframe'):
            link = soup.new_tag('a', href=video.get('src', ''))
            link.string = 'Video'
            video.replace_with(link)
        markdown = markdownify(str(soup), heading_style='ATX', bullets='-', strip=['span', 'div'],
                               code_language='text', escape_underscores=False, escape_asterisks=False)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown).strip() + '\n'
        (dest / 'en' / f"{page['id']}.md").write_text(markdown, encoding='utf-8')
        inventory.append({'id': page['id'], 'parent': page['parent'], 'slug': page['slug'],
                          'link': page['link'], 'title': html.unescape(BeautifulSoup(page['title']['rendered'], 'html.parser').get_text()),
                          'modified': page['modified']})
    (dest / 'pages.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding='utf-8')
    baseline = BASE / 'sources/pages.json'
    changes = []
    for p in inventory:
        original = BASE / 'sources/html' / f"{p['id']}.html"
        incoming = dest / 'html' / f"{p['id']}.html"
        if not original.exists() or original.read_text(encoding='utf-8') != incoming.read_text(encoding='utf-8'):
            changes.append({'id': p['id'], 'source': p['link'], 'change': 'new' if not original.exists() else 'changed'})
    report = {'pages': len(inventory), 'changes': changes, 'empty_pages': [p['link'] for p in inventory if not (dest / 'en' / f"{p['id']}.md").read_text(encoding='utf-8').strip()]}
    (dest / 'refresh-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
