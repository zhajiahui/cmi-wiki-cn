"""Archive the current default-version documentation from public HTML."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin,urlsplit,urldefrag
import requests,json,re,time,hashlib,argparse
from datetime import datetime
from bs4 import BeautifulSoup
BASE=Path(__file__).resolve().parents[1]
HOST='https://docs.typewritermc.com'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--refresh',action='store_true',help='Write a new candidate snapshot under sources/incoming, preserving the reviewed baseline.')
args=parser.parse_args()
DEST=(BASE/'sources/incoming'/datetime.now().strftime('%Y%m%d-%H%M%S')/'live') if args.refresh else BASE/'sources/live'
INVENTORY=DEST.parent/'pages.json'
previous={p['path']:p for p in json.loads(INVENTORY.read_text(encoding='utf-8'))} if INVENTORY.exists() else {}
DEST.mkdir(parents=True,exist_ok=True)
def allowed(url):
    part=urlsplit(url)
    return part.netloc=='docs.typewritermc.com' and re.match(r'^/(docs|adapters|develop)(/|$)',part.path)
def fetch(url):
    path=urlsplit(url).path.rstrip('/') or '/'
    output=DEST/(hashlib.sha256(path.encode()).hexdigest()[:16]+'.html')
    if output.exists():body=output.read_text(encoding='utf-8')
    else:
        for attempt in range(3):
            try:
                response=requests.get(url,timeout=(15,60));response.raise_for_status();body=response.text;break
            except Exception:
                if attempt==2:raise
                time.sleep(1)
        output.write_text(body,encoding='utf-8')
    soup=BeautifulSoup(body,'html5lib')
    article=soup.select_one('.theme-doc-markdown')
    if not article:raise ValueError('No document body at '+url)
    source=next((a['href'] for a in soup.find_all('a',href=True) if '/tree/' in a['href'] and 'documentation' in a['href']),None)
    links={urldefrag(urljoin(url,a['href']))[0].split('?')[0].rstrip('/') for a in soup.find_all('a',href=True) if allowed(urljoin(url,a['href']))}
    title=article.find('h1').get_text(' ',strip=True) if article.find('h1') else soup.title.get_text().split(' | ')[0]
    row={**previous.get(path,{}),'url':url,'path':path,'title':title,'html':output.relative_to(BASE).as_posix(),'source':source,'text_characters':len(article.get_text(' ',strip=True))}
    return row,links
seen=set();frontier={HOST+'/docs/home',HOST+'/adapters',HOST+'/develop'};pages=[]
with ThreadPoolExecutor(max_workers=8) as pool:
    while frontier:
        current=sorted(frontier-seen);seen.update(current);frontier=set()
        if not current:break
        for page,links in pool.map(fetch,current):pages.append(page);frontier.update(links-seen)
        INVENTORY.write_text(json.dumps(sorted(pages,key=lambda x:x['path']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print('Archived',len(pages),'pages; discovered',len(frontier),'more',flush=True)
print(json.dumps({'pages':len(pages),'text_characters':sum(p['text_characters'] for p in pages)},ensure_ascii=False))
