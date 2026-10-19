"""Verify full-Wiki translations against their archived originals and declared coverage."""
from pathlib import Path
from collections import Counter
import json,re,sys,hashlib,yaml
from bs4 import BeautifulSoup
import markdown
from hooks import ROOT,PROJECTS
errors=[];projects={};code_count=inline_count=asset_count=0

def fenced_parts(text):
    lines=text.splitlines(keepends=True);parts=[];plain=[];i=0
    while i<len(lines):
        match=re.match(r'^(\s*(?:>\s*)?)(`{3,}|~{3,})[^\n]*$',lines[i].rstrip('\r\n'))
        if not match:
            plain.append(lines[i]);i+=1;continue
        if plain:parts.append((False,''.join(plain)));plain=[]
        prefix,fence=match.groups();i+=1;code=[]
        while i<len(lines):
            if re.match(r'^'+re.escape(prefix)+re.escape(fence[0])+'{'+str(len(fence))+r',}\s*$',lines[i]):i+=1;break
            code.append(lines[i][len(prefix):] if '>' in prefix and lines[i].startswith(prefix) else lines[i]);i+=1
        parts.append((True,''.join(code).rstrip('\r\n')))
    if plain:parts.append((False,''.join(plain)))
    return parts

def blocks(text):return [value for code,value in fenced_parts(text) if code]
def outside(text):return ''.join(value for code,value in fenced_parts(text) if not code)

def article_source(project,row,text):
    if row.get('source_exclusions'):
        coverage=json.loads((ROOT/project/'sources/wiki-coverage.json').read_text('utf-8'))
        allowed=any(item.get('scope')=='sections_only' and item.get('url')==row['source_url'] for item in coverage.get('excluded_api',[]))
        if not allowed:raise ValueError(project+'/'+row['file']+': source section exclusions lack a coverage declaration')
        lines=text.splitlines(keepends=True);excluded=set()
        for span in row['source_exclusions']:
            first,last=span['start_line'],span['end_line']
            if not 1<=first<=last<=len(lines) or not span.get('reason'):raise ValueError('Invalid API source section range')
            excluded.update(range(first-1,last))
        text=''.join(line for i,line in enumerate(lines) if i not in excluded)
    # GitBook's export preamble describes its machine transport, not the Wiki article.
    if text.startswith('> For the complete documentation index, see [llms.txt]('):
        text=text.split('\n\n',1)[1]
    if project=='NeigeItems' and row['file']=='wiki/public-readme.md':
        # The coverage inventory explicitly excludes these two API/SDK sections.
        text=re.sub(r'^## Development\n[\s\S]*?(?=^## |\Z)','',text,flags=re.M)
        text=re.sub(r'^## API\n[\s\S]*','',text,flags=re.M)
    if project=='CrackShot' and row['file'] in ('wiki/List-of-Accepted-Mobs.md','wiki/List-of-Accepted-Sounds.md'):
        # Upstream put the first enum value on the opening fence and omitted its close.
        text=text.replace('```AMBIENT_CAVE','```text\nAMBIENT_CAVE').replace('```Bat','```text\nBat')+'\n```\n'
    if (project=='NeigeItems' and row['file'].startswith('wiki/public-examples/')) or Path(row['source_file']).suffix.lower() not in ('.md','.mdx','.markdown'):
        # Complete repository examples are displayed as one verbatim code block.
        text='```text\n'+text.rstrip('\r\n')+'\n```\n'
    return text

def navfiles(items):
    for item in items:
        for v in item.values():
            if isinstance(v,list):yield from navfiles(v)
            else:yield v

for project,prefix in PROJECTS:
    if sys.argv[1:] and project not in sys.argv[1:]:continue
    base=ROOT/project;source=base/'sources/wiki-manifest.json'
    if not source.is_file():continue
    rows=json.loads(source.read_text('utf-8'))
    coverage_path=base/'sources/wiki-coverage.json'
    if not coverage_path.is_file():errors.append(project+': official scope inventory missing')
    else:
        coverage=json.loads(coverage_path.read_text('utf-8'))
        pending=coverage.get('pending_pages',coverage.get('translation_pending',0))
        pending=len(pending) if isinstance(pending,list) else pending
        if isinstance(coverage.get('pages'),dict):pending=coverage['pages'].get('pending',pending)
        if pending:errors.append(project+': available non-API pages still pending: '+str(pending))
        expected=coverage.get('canonical_pages') or coverage.get('translated_page_count') or coverage.get('actual_page_count') or coverage.get('actual_pages')
        if expected is None and isinstance(coverage.get('counts'),dict):expected=coverage['counts'].get('translated_pages',coverage['counts'].get('translated'))
        if expected is None and isinstance(coverage.get('pages'),dict):expected=coverage['pages'].get('in_scope')
        if expected is not None and expected!=len(rows):errors.append(project+': Wiki manifest count differs from official coverage')
    checked_assets=set()
    for ledger_name in ('assets.json','asset-manifest.json','assets-manifest.json'):
        ledger=base/'sources/wiki'/ledger_name
        if not ledger.is_file():continue
        for item in json.loads(ledger.read_text('utf-8')):
            if not item.get('file'):continue
            resource=base/item['file'] if item['file'].startswith('docs/') else base/'docs'/item['file']
            if resource in checked_assets:continue
            checked_assets.add(resource);digest=item.get('sha256') or item.get('native_sha256')
            if not resource.is_file() or not digest or hashlib.sha256(resource.read_bytes()).hexdigest()!=digest:errors.append(project+': native asset differs: '+item['file'])
            asset_count+=1
    paths=[r['file'] for r in rows]
    if len(paths)!=len(set(paths)):errors.append(project+': duplicate Wiki files')
    nav_path=base/'sources/wiki-nav.yml'
    if not nav_path.is_file():errors.append(project+': Wiki navigation missing')
    else:
        nav=list(navfiles(yaml.safe_load(nav_path.read_text('utf-8')) or []))
        if len(nav)!=len(set(nav)) or set(nav)!=set(paths):errors.append(project+': full-Wiki navigation differs from manifest')
    for row in rows:
        label=project+'/'+row['file'];original=base/row['source_file'];target=base/'docs'/row['file']
        if not original.is_file() or not target.is_file():errors.append(label+': source or translation missing');continue
        en=original.read_text('utf-8');zh=target.read_text('utf-8')
        if hashlib.sha256(en.encode('utf-8')).hexdigest()!=row['source_sha256']:errors.append(label+': source hash differs')
        if not zh.startswith('---\n'):errors.append(label+': frontmatter missing');continue
        try:
            header,body=zh[4:].split('\n---\n',1);meta=yaml.safe_load(header)
        except (ValueError,yaml.YAMLError):errors.append(label+': invalid frontmatter');continue
        if any(not meta.get(key) for key in ('title','source_url','source_kind','source_version')):errors.append(label+': source metadata incomplete')
        if meta.get('translation_review')!='reviewed' or row.get('translation_review')!='reviewed':errors.append(label+': review not finished')
        scoped=article_source(project,row,en)
        dom=lambda t:BeautifulSoup(markdown.markdown(t,extensions=['admonition','pymdownx.details','tables','pymdownx.superfences','md_in_html']),'html.parser')
        a,b=dom(scoped),dom(body)
        codeblocks=lambda soup:[node.get_text().rstrip('\r\n') for node in soup.find_all('pre')]
        code_source=a;code_target=b
        if row.get('source_html_file'):
            raw_path=base/row['source_html_file'];raw=raw_path.read_text('utf-8')
            if hashlib.sha256(raw.encode('utf-8')).hexdigest()!=row['source_html_sha256']:errors.append(label+': native source hash differs')
            if raw_path.suffix=='.json':raw=json.loads(raw)['parse']['text']['*']
            code_source=BeautifulSoup(raw,'html.parser')
            code_target=BeautifulSoup(body,'html.parser')
        source_blocks,target_blocks=codeblocks(code_source),codeblocks(code_target)
        display_reviews={item['index']:item for item in row.get('translated_display_blocks',[])}
        if len(source_blocks)!=len(target_blocks):errors.append(label+': source code block count differs')
        else:
            for block_index,(original_block,translated_block) in enumerate(zip(source_blocks,target_blocks)):
                if original_block==translated_block:continue
                review=display_reviews.get(block_index)
                if not review or hashlib.sha256(original_block.encode('utf-8')).hexdigest()!=review['source_sha256'] or hashlib.sha256(translated_block.encode('utf-8')).hexdigest()!=review['translation_sha256']:
                    errors.append(label+': source code block differs: '+str(block_index));continue
                if not review.get('reason'):errors.append(label+': display block review reason missing')
                for token in review.get('protected_tokens',[]):
                    if original_block.count(token)!=translated_block.count(token):errors.append(label+': display block identifier differs: '+token)
        code_count+=len(source_blocks)
        tokens=lambda soup:Counter(node.get_text() for node in soup.find_all('code') if node.find_parent('pre') is None and '\n' not in node.get_text())
        lost=tokens(a)-tokens(b)
        if lost:errors.append(label+': inline identifiers lost: '+str(list(lost.elements())[:4]))
        inline_count+=sum(tokens(a).values())
        anchors=re.findall(r'\{\s*#([^}\s]+)\s*\}',outside(scoped))
        if any(not re.search(r'\{\s*#'+re.escape(a)+r'\s*\}',body) for a in anchors):errors.append(label+': source heading anchor lost')
        if re.search(r'ZXQ\s*\d+\s*QXZ|__TRANSLATION_PENDING__|TODO_TRANSLATE',body):errors.append(label+': unfinished translation marker')
        # Tables keep every row; columns may use HTML for the source's spanning cells.
        at,bt=a.find_all('table'),b.find_all('table')
        if len(at)!=len(bt):errors.append(label+': table count changed')
        elif any(len(x.find_all('tr'))!=len(y.find_all('tr')) for x,y in zip(at,bt)):errors.append(label+': table rows changed')
    projects[project]=len(rows)
print(json.dumps({'full_wiki_projects':projects,'translated_pages':sum(projects.values()),'verbatim_code_blocks':code_count,'protected_inline_tokens':inline_count,'native_assets':asset_count,'errors':errors},ensure_ascii=False,indent=2))
if errors:sys.exit(1)
