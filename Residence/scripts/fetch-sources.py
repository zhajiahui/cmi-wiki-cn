from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlsplit
import requests, json, re, html, argparse
from bs4 import BeautifulSoup
from markdownify import markdownify
BASE = Path(__file__).resolve().parents[1]
API = 'https://www.zrips.net/wp-json/wp/v2/pages'
FIELDS = 'id,parent,slug,link,title,content,modified'
def get_page(page_id):
    r=requests.get(f'{API}/{page_id}', params={'_fields':FIELDS}, timeout=(20,90)); r.raise_for_status(); return r.json()
def children(parent):
    result=[]; n=1
    while True:
        r=requests.get(API, params={'parent':parent,'per_page':100,'page':n,'_fields':FIELDS},timeout=(20,90));r.raise_for_status();result+=r.json()
        if n>=int(r.headers.get('X-WP-TotalPages','1')): return result
        n+=1
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--initial',action='store_true',help='Create a new baseline archive only when no archive exists')
    args=parser.parse_args()
    if args.initial and (BASE/'sources/pages.json').exists():raise SystemExit('Source archive already exists; omit --initial to compare incoming sources.')
    target=BASE/'sources' if args.initial else BASE/'sources/incoming'
    target.mkdir(parents=True,exist_ok=True)
    root=get_page(122);pages=[root];frontier=[122];seen={122}
    with ThreadPoolExecutor(max_workers=4) as pool:
        while frontier:
            upcoming=[]
            for batch in pool.map(children,frontier):
                for page in batch:
                    if page['id'] not in seen:
                        seen.add(page['id']); pages.append(page); upcoming.append(page['id'])
            frontier=upcoming
    (target/'html').mkdir(exist_ok=True);(target/'en').mkdir(exist_ok=True)
    rows=[];known={urlsplit(p['link']).path.rstrip('/') for p in pages};extra=set()
    for p in sorted(pages,key=lambda x:x['id']):
        body=p['content']['rendered'];(target/'html'/f"{p['id']}.html").write_text(body,encoding='utf-8')
        soup=BeautifulSoup(body,'html.parser')
        for a in soup.find_all('a',href=True):
            u=urlsplit(urljoin(p['link'],a['href']))
            if u.netloc in {'zrips.net','www.zrips.net'} and u.path.startswith('/residence/') and u.path.rstrip('/') not in known:extra.add(u._replace(fragment='').geturl())
        for node in soup.select('script,style,svg,button,nav,form'):node.decompose()
        for pre in soup.find_all('pre'):
            for br in pre.find_all('br'):br.replace_with('\n')
            content=pre.get_text();pre.clear();pre.string=content
        for frame in soup.find_all('iframe'):
            a=soup.new_tag('a',href=frame.get('src',''));a.string='Video';frame.replace_with(a)
        content=markdownify(str(soup),heading_style='ATX',bullets='-',strip=['span','div','i'],escape_underscores=False,escape_asterisks=False)
        content=re.sub(r'\n{3,}','\n\n',content).strip()+'\n'
        (target/'en'/f"{p['id']}.md").write_text(content,encoding='utf-8')
        rows.append({'id':p['id'],'parent':p['parent'],'slug':p['slug'],'link':p['link'],'title':html.unescape(BeautifulSoup(p['title']['rendered'],'html.parser').get_text()),'modified':p['modified'],'characters':len(content),'pre_blocks':len(soup.find_all('pre')),'images':len(soup.find_all('img'))})
    (target/'pages.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    changes=[]
    for row in rows:
        baseline=BASE/'sources/html'/f"{row['id']}.html"
        incoming=target/'html'/f"{row['id']}.html"
        if not baseline.exists() or baseline.read_text(encoding='utf-8')!=incoming.read_text(encoding='utf-8'):
            changes.append({'id':row['id'],'source':row['link'],'change':'new' if not baseline.exists() else 'changed'})
    report={'pages':len(rows),'changes':changes,'extra_urls':sorted(extra)}
    (target/'refresh-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
