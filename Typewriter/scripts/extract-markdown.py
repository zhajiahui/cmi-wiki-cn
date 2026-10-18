"""Extract the rendered 0.8.0 docs, including generated fields and original anchors."""
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
from urllib.parse import urljoin
import json,re,ast
BASE=Path(__file__).resolve().parents[1]
rows=json.loads((BASE/'sources/pages.json').read_text(encoding='utf-8'))
OUT=BASE/'sources/en';OUT.mkdir(exist_ok=True)
class Converter(MarkdownConverter):
    def convert_a(self,el,text,parent_tags):
        heading=el.find(re.compile('^h[1-6]$'))
        if heading:
            label=heading.get_text(' ',strip=True).removeprefix('📄️ ')
            # Docusaurus document cards are block links, which Markdown links cannot contain.
            body=re.sub(r'^\s*#{1,6} [^\n]+\n*','',text).strip()
            return '\n\n## ['+label+']('+el.get('href','')+')\n\n'+body+'\n\n'
        return super().convert_a(el,text,parent_tags)
    def convert_pre(self,el,text,parent_tags):
        language=next((x.removeprefix('language-') for x in el.get('class',[]) if x.startswith('language-')),'text')
        lines=el.select('.token-line')
        raw='\n'.join(line.get_text() for line in lines) if lines else el.get_text()
        fence='`'*max(3,max((len(m.group())+1 for m in re.finditer(r'`+',raw)),default=3))
        return '\n\n'+fence+language+'\n'+raw.rstrip('\n')+'\n'+fence+'\n\n'
    def convert_video(self,el,text,parent_tags):
        src=el.get('src') or next((s.get('src') for s in el.find_all('source') if s.get('src')),'')
        if not src:return text
        poster=' poster="'+el['poster']+'"' if el.get('poster') else ''
        return '\n\n<video controls preload="metadata"'+poster+' src="'+src+'"></video>\n\n'
    def convert_iframe(self,el,text,parent_tags):
        return '\n\n[Video]('+el.get('src','')+')\n\n'
    def convert_button(self,el,text,parent_tags):
        return '\n\n**'+text.strip()+'**\n\n' if el.get('role')=='tab' else ''
    def convert_heading(self,n,el,text,parent_tags):
        # Explicit IDs keep all official fragment links stable after translation.
        anchor=' {#'+el['id']+'}' if el.get('id') else ''
        return '\n\n'+'#'*n+' '+text.strip()+anchor+'\n\n'
    def convert_h1(self,e,t,parent_tags):return self.convert_heading(1,e,t,parent_tags)
    def convert_h2(self,e,t,parent_tags):return self.convert_heading(2,e,t,parent_tags)
    def convert_h3(self,e,t,parent_tags):return self.convert_heading(3,e,t,parent_tags)
    def convert_h4(self,e,t,parent_tags):return self.convert_heading(4,e,t,parent_tags)
    def convert_h5(self,e,t,parent_tags):return self.convert_heading(5,e,t,parent_tags)
    def convert_h6(self,e,t,parent_tags):return self.convert_heading(6,e,t,parent_tags)
    def convert_div(self,el,text,parent_tags):
        if any('admonitionHeading' in c for c in el.get('class',[])):
            return '\n\n**'+text.strip()+'**\n\n'
        return '\n\n'+text.strip()+'\n\n'

def split_unit(line):
    if not line.strip() or re.fullmatch(r'[\s|:*-]+',line) or re.match(r'^\s*<(?:video|/video|source|a[ >])',line):return None
    m=re.match(r'^(\s*(?:#{1,6} |[-*] |\d+\. )?)(.*?)(\s*\{#[^}]+\})?$',line)
    return m.groups() if m else ('',line,'')
old=json.loads((BASE/'sources/units.json').read_text(encoding='utf-8')) if (BASE/'sources/units.json').exists() else []
old_ids={u['source']:u['id'] for u in old}
next_id=max(old_ids.values(),default=-1)+1
units={};sequence=[]
media_report=[]
COMMIT=json.loads((BASE/'sources/source-info.json').read_text(encoding='utf-8-sig')).get('commit','9b0a087150c594120d6b89b158f3402bb9d85142')
def source_url(path):
    return 'https://raw.githubusercontent.com/gabber235/Typewriter/'+COMMIT+'/documentation/'+path.relative_to(BASE/'sources/repository').as_posix()

for page in rows:
    soup=BeautifulSoup((BASE/page['html']).read_text(encoding='utf-8'),'html5lib')
    article=soup.select_one('.theme-doc-markdown')
    original=BASE/'sources/repository'/page['source'].split('/documentation/',1)[1]
    mdx=original.read_text(encoding='utf-8')
    players=re.findall(r'<Player[\s\S]*?/>',mdx)
    placeholders=[d for d in article.find_all('div') if 'outline-none' in d.get('class',[]) and d.find('input',type='range') and not d.get('tabindex')]
    if len(players)!=len(placeholders):raise ValueError('Video count mismatch: '+page['path'])
    for element,tag in zip(placeholders,players):
        src=re.search(r"require\([\"']([^\"']+)[\"']\)",tag)[1]
        video=soup.new_tag('video',src=source_url((original.parent/src).resolve()));element.replace_with(video)
    displays=re.findall(r'<EntryDisplay[\s\S]*?/>',mdx)
    graphs=[d for d in article.select('.tabs-container') if d.select_one('.react-flow')]
    if len(displays)!=len(graphs):raise ValueError('Example count mismatch: '+page['path'])
    for element,tag in zip(graphs,displays):
        block=soup.new_tag('div')
        for src in re.findall(r"require\([\"']([^\"']+)[\"']\)",tag):
            a=soup.new_tag('a',href=source_url((original.parent/src).resolve()));a.string=Path(src).name
            para=soup.new_tag('p');para.append(a);block.append(para)
        element.replace_with(block)
    for group in article.select('.tabs-container'):
        labels=group.select('[role=tab]');panels=group.select('[role=tabpanel]')
        if len(labels)==len(panels):
            for label,panel in zip(labels,panels):
                title=soup.new_tag('p');strong=soup.new_tag('strong');strong.string=label.get_text(' ',strip=True);title.append(strong);panel.insert_before(title)
            if labels:
                ul=labels[0].find_parent('ul')
                if ul:ul.decompose()
    boards=re.findall(r'<RiveBoard[\s\S]*?/>',mdx)
    canvases=article.find_all('canvas')
    if len(boards)!=len(canvases):raise ValueError('Interactive figure count mismatch: '+page['path'])
    for tag,canvas in zip(boards,canvases):
        src=re.search(r"require\([\"']([^\"']+)[\"']\)",tag)[1]
        heading=canvas.find_previous(re.compile('^h[1-6]$'))
        fragment=('#'+heading['id']) if heading and heading.get('id') else ''
        block=soup.new_tag('div')
        para=soup.new_tag('p');a=soup.new_tag('a',href=page['url']+fragment);a.string='Interactive Visualization';para.append(a);block.append(para)
        para=soup.new_tag('p');a=soup.new_tag('a',href=source_url((original.parent/src).resolve()));a.string=Path(src).name;para.append(a);block.append(para)
        canvas.parent.replace_with(block)
    media_report.append({'path':page['path'],'videos':len(players),'example_displays':len(displays)})
    flows=re.findall(r'<StateFlow[\s\S]*?/>',mdx)
    flow_elements=[d for d in article.find_all('div') if 'my-6' in d.get('class',[]) and 'relative' in d.get('class',[]) and d.find('button',attrs={'title':'Pause animation'})]
    if len(flows)!=len(flow_elements):raise ValueError('Flow count mismatch: '+page['path'])
    for element,tag in zip(flow_elements,flows):
        literal=re.search(r'nodes=\{(\[[\s\S]*\])\}',tag)[1]
        literal=re.sub(r'([{,]\s*)([A-Za-z_][\w]*)\s*:',r'\1"\2":',literal)
        nodes=ast.literal_eval(literal);by_id={n['id']:n for n in nodes}
        block=soup.new_tag('div')
        for attr in ['title','description']:
            m=re.search(attr+r'="([^"]+)"',tag)
            if m:
                para=soup.new_tag('p');para.string=m[1];block.append(para)
        table=soup.new_tag('table');head=soup.new_tag('thead');tr=soup.new_tag('tr')
        for label in ['State','Facts','Description','Transitions']:
            th=soup.new_tag('th');th.string=label;tr.append(th)
        head.append(tr);table.append(head);tbody=soup.new_tag('tbody')
        for node in nodes:
            tr=soup.new_tag('tr')
            values=[node['title'],node.get('facts',[]),node.get('description',''),'; '.join(t['label']+' → '+by_id[t['targetId']]['title'] for t in node.get('transitions',[]))]
            for value in values:
                td=soup.new_tag('td')
                if isinstance(value,list):
                    for i,fact in enumerate(value):
                        if i:td.append(soup.new_tag('br'))
                        code=soup.new_tag('code');code.string=fact;td.append(code)
                else:td.string=value
                tr.append(td)
            tbody.append(tr)
        table.append(tbody);block.append(table);element.replace_with(block)
    if '<StatusEditor' in mdx:
        header=next(h for h in article.find_all('h4') if h.get_text(' ',strip=True)=='Inactive Quest')
        wrapper=header
        while wrapper and 'my-4' not in wrapper.get('class',[]):wrapper=wrapper.parent
        if not wrapper:raise ValueError('Status editor missing')
        marker=soup.new_tag('p');marker.string='TW_STATUS_EDITOR_PLACEHOLDER';wrapper.replace_with(marker)
    for tag in article.select('svg,script,style,button,[class*="hash-link"]'):
        if tag.name=='button' and tag.get('role')=='tab':continue
        tag.decompose()
    for image in article.find_all(['img','source','video','iframe']):
        for attr in ['src','poster']:
            if image.get(attr):image[attr]=urljoin(page['url'],image[attr])
    for tag in article.find_all('a',href=True):tag['href']=urljoin(page['url'],tag['href'])
    for span in article.select('span[class*="badge_"]'):span.insert_after(' ')
    text=Converter(heading_style='ATX',bullets='-',strip=['span','header','section'],escape_underscores=False,escape_asterisks=False).convert(str(article))
    text=re.sub(r'\n{3,}','\n\n',text).strip()+'\n'
    relative=page['path'].strip('/')+'.md'
    path=OUT/relative;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')
    page['english']=path.relative_to(BASE).as_posix()
    in_code=False;fence=''
    for line in text.splitlines():
        if re.match(r'^`{3,}',line):
            if not in_code:fence=re.match(r'^`+',line).group();in_code=True
            elif line.strip()==fence:in_code=False
            continue
        if in_code:continue
        split=split_unit(line)
        if not split:continue
        part=split[1]
        if part not in units:
            uid=old_ids.get(part)
            if uid is None:uid=next_id;next_id+=1
            unit={'id':uid,'source':part,'pages':[]};units[part]=unit;sequence.append(unit)
        units[part]['pages'].append(page['path'])
(BASE/'sources/pages.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sequence.sort(key=lambda u:u['id'])
(BASE/'sources/media-report.json').write_text(json.dumps(media_report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(BASE/'sources/units.json').write_text(json.dumps(sequence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pages':len(rows),'unique_lines':len(sequence),'translation_characters':sum(len(x['source']) for x in sequence),'longest':max(len(x['source']) for x in sequence)},ensure_ascii=False))
