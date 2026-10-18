"""Build the Chinese pages from archived English, terminology and reviewed corrections."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json,re,hashlib,os,yaml
BASE=Path(__file__).resolve().parents[1]
units=json.loads((BASE/'sources/units.json').read_text(encoding='utf-8'))
draft=json.loads((BASE/'sources/draft.json').read_text(encoding='utf-8'))
pages=json.loads((BASE/'sources/pages.json').read_text(encoding='utf-8'))
titles=json.loads((BASE/'titles.json').read_text(encoding='utf-8'))
terms=dict(line.split('\t',1) for line in (BASE/'terminology.tsv').read_text(encoding='utf-8').splitlines() if line.strip())
for path in sorted((BASE/'sources/review').glob('*.tsv')):
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.strip():key,value=line.split('\t',1);draft[key]=value
assets=json.loads((BASE/'sources/assets.json').read_text(encoding='utf-8'))
lookup={u['source']:u for u in units}
INTERACTIVE_URLS={re.search(r'\]\(([^)]+)\)',u['source'])[1] for u in units if u['source'].startswith('[Interactive Visualization]')}
en_titles={}
for data in titles.values():en_titles.setdefault(data['en'],data['zh'])
# Literal labels are kept in the page titles as well as in command/config examples.
LABELS={'Typewriter':'Typewriter','Bossbar':'Boss 栏','Boss Bar':'Boss 栏'}
BADGES={'Required':'必填','Inherited':'继承','Optional':'可选','List':'列表','Deprecated':'已弃用','Colored':'支持颜色','Multi-Line':'多行','Regex':'正则表达式','Placeholders':'支持占位符','Reference':'引用','Segment':'片段'}
REPLACEMENTS=[('打字机','Typewriter'),('播放器','玩家'),('电影','过场动画'),('观众','受众'),('听众','受众'),('扬声器','说话者'),('老板酒吧','Boss 栏'),('老板栏','Boss 栏'),('Boss酒吧','Boss 栏'),('老板条','Boss 栏'),('区块','方块'),('街区','方块'),('清单条目','呈现条目'),('清单页面','呈现页面'),('清单页','呈现页面'),('清单部分','呈现部分'),('修饰符','修改器'),('调节器','修改器'),('物料','材质'),('生成器模式','内容模式'),('检查器','属性面板'),('检视器','属性面板'),('检查员','属性面板'),('您','你'),('Web 面板','网页面板'),('网络面板','网页面板'),('Web 套接字','WebSocket'),('库存','背包'),('运营商','运算符'),('操作员','运算符'),('物镜','目标'),('工件','文件产物'),('制品','文件产物'),('全球','全局'),('祖母绿','绿宝石'),('暴民','生物'),('暴徒','生物'),('序列页','序列页'),('顺序页面','序列页面'),('交互绑定','交互边界'),('绑定条件','边界条件'),('任务跟踪','任务追踪'),('跟踪任务','追踪任务'),('跟踪的任务','追踪的任务'),('跟踪的目标','追踪的目标'),('信使','Messenger'),('使用站点','使用处'),('健康值','生命值'),('磁道','轨道'),('物品捕获器','物品采集器'),('轨迹持续时间','轨道持续时间'),('商品','物品'),('儿童','子活动'),('孩子','子条目'),('插槽','槽位'),('操作栏','动作栏'),('选项卡列表','玩家列表'),('生物群落','生物群系'),('演讲者','说话者'),('讲话者','说话者'),('发言者','说话者'),('受众席','受众'),('群组','组'),('小组成员','组员'),('专业提示','提示')]
PROTECTED=re.compile(r'`+[^`\n]*`+|\]\([^\n]*?\)|<[^>]+>')
def polish(value,source):
    parts=PROTECTED.split(value);tokens=PROTECTED.findall(value)
    for i,part in enumerate(parts):
        for a,b in REPLACEMENTS:part=part.replace(a,b)
        if re.search(r'\bevents?\b',source,re.I) and not re.search(r'\bactivit(?:y|ies)\b',source,re.I):part=part.replace('活动','事件')
        part=part.replace('此操作在多种情况下都很有用。你可以使用它','可以用它').replace('此操作在多种情况下都很有用。你可以用它','可以用它').replace('可能性是无限的！','也可以用于其他场景。')
        if re.search(r'\binterfaces?\b',source,re.I) and not re.search(r'user interface|\bUI\b',source,re.I):part=part.replace('界面','接口')
        if re.search(r'\bannotations?\b',source,re.I):part=part.replace('注释','注解')
        if re.search(r'\bbalance\b',source,re.I):part=part.replace('平衡性','余额').replace('平衡','余额')
        if re.search(r'\bassets?\b',source,re.I):part=part.replace('资产','资源')
        if re.search(r'\bevent\b',source,re.I):part=part.replace('被发射','被触发').replace('触发器开火','触发后续条目')
        if re.search(r'\bcase\b',source,re.I) and not re.search(r'\bsensitive\b',source,re.I):part=part.replace('大小写','分支').replace('案例','分支')
        if re.search(r'\bentry\b',source,re.I) and not re.search(r'entry.?point',source,re.I):part=part.replace('入口','条目')
        if re.search(r'\bticks?\b',source,re.I):part=part.replace('刻度','tick').replace('滴答声','tick').replace('滴答','tick')
        if re.search(r'\bcamera\b',source,re.I) and re.search(r'\bpitch\b',source,re.I):part=part.replace('间距','俯仰角')
        if re.search(r'\bcinematic\b',source,re.I) and re.search(r'\bcamera\b',source,re.I):part=part.replace('相机','镜头').replace('摄像机','镜头')
        if re.search(r'\bspoken\b',source,re.I):
            for word in ('口语','口头','口述','语音'):part=part.replace(word,'逐字对话')
        if re.search(r'\bitems?\b',source,re.I) and not re.search(r'\bprojects?\b',source,re.I):part=part.replace('项目','物品')
        if re.search(r'\bcriteria\b',source,re.I):part=part.replace('标准','条件')
        if re.search(r'\blore\b',source,re.I):part=part.replace('传说','物品描述').replace('知识','物品描述')
        if re.search(r'\bquests?\b',source,re.I):part=part.replace('追求','任务')
        if re.search(r'\bmanifest\b',source,re.I):part=part.replace('清单','呈现')
        parts[i]=part
    result=''.join(p+(tokens[i] if i<len(tokens) else '') for i,p in enumerate(parts))
    if source.startswith('[Interactive Visualization]'):return result
    result=re.sub(r'\[([^]\n]+)\]\((https://docs\.typewritermc\.com[^)]+)\)',lambda m:'['+(m[1] if '`' in m[1] else titles.get(urlsplit(m[2]).path.rstrip('/'),{}).get('zh',m[1]))+']('+m[2]+')',result)
    field=re.match(r'^\*\*([a-z_][A-Za-z0-9_]*)\*\*\s*:',source)
    if field:
        result=re.sub(r'^\*\*([^*]+)\*\*\s*[:：]?',lambda m:'**'+field[1]+'**'+('（'+m[1]+'）' if m[1]!=field[1] else '')+'：',result)
    return result
translated={}
for u in units:
    source=u['source'];uid=str(u['id'])
    if re.fullmatch(r'[A-Za-z0-9_./-]+\.(?:yml|yaml|kt|kts|json|jar|zip)',source):value=source
    elif source in terms:value=terms[source]
    elif source in en_titles:value=en_titles[source]
    elif all(w in BADGES for w in source.split()):value=' · '.join(BADGES[w] for w in source.split())
    else:
        if uid not in draft:raise ValueError('Untranslated unit: '+uid)
        value=draft[uid]
    translated[source]=polish(value,source)

def file_for(route):return 'index.md' if route=='/docs/home' else route.strip('/')+'.md'
files={p['path']:file_for(p['path']) for p in pages}
def local_url(url,current):
    if url in INTERACTIVE_URLS:return url
    if url in assets:target=assets[url]['file'];fragment=''
    else:
        parts=urlsplit(url)
        if parts.netloc!='docs.typewritermc.com':return url
        route=parts.path.rstrip('/') or '/docs/home'
        if route not in files:return url
        target=files[route];fragment=('#'+parts.fragment) if parts.fragment else ''
        if url.startswith('https://docs.typewritermc.com/docs/concepts/') and parts.fragment=='interactive-visualization' and target==current:return url
    return Path(os.path.relpath(BASE/'docs'/target,(BASE/'docs'/current).parent)).as_posix()+fragment
manifest=[]
for page in pages:
    original=(BASE/page['english']).read_text(encoding='utf-8');out=[];fence='';inside=False
    for line in original.splitlines():
        if re.match(r'^`{3,}',line):
            if not inside:fence=re.match(r'^`+',line).group();inside=True
            elif line.strip()==fence:inside=False
            out.append(line);continue
        if inside or not line.strip() or re.fullmatch(r'[\s|:*-]+',line) or re.match(r'^\s*<(?:video|/video|source|a[ >])',line):out.append(line);continue
        m=re.match(r'^(\s*(?:#{1,6} |[-*] |\d+\. )?)(.*?)(\s*\{#[^}]+\})?$',line)
        leading,part,trailing=m.groups()
        if part not in translated:raise ValueError('Missing source unit: '+part)
        out.append(leading+translated[part]+(trailing or ''))
    body='\n'.join(out)+'\n'
    body=body.replace('TW_STATUS_EDITOR_PLACEHOLDER',(BASE/'scripts/status-editor.html').read_text(encoding='utf-8'))
    title=titles[page['path']]['zh'];en=page['title']
    if title!=en and en not in title:title+='（'+en+'）'
    body=re.sub(r'^# .*$',lambda m:'# '+title,body,count=1,flags=re.M)
    current=files[page['path']]
    # Rewrite only Markdown destinations and media src attributes; code stays verbatim.
    blocks=re.split(r'(^`{3,}[^\n]*\n[\s\S]*?^`{3,}\s*$)',body,flags=re.M)
    for i in range(0,len(blocks),2):
        blocks[i]=re.sub(r'(?<=\]\()https?://[^)\n]+',lambda m:local_url(m.group(),current),blocks[i])
        blocks[i]=re.sub(r'(?<=src=")https?://[^"]+',lambda m:local_url(m.group(),current),blocks[i])
    body=''.join(blocks)
    body+='\n---\n\n原文：['+page['title']+']('+page['url']+') · 文档版本：0.8.0\n'
    meta={'title':title,'source':page['url'],'source_version':'0.8.0'}
    content='---\n'+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False)+'---\n\n'+body
    target=BASE/'docs'/current;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(content,encoding='utf-8')
    manifest.append({'title':title,'source':page['url'],'source_path':page['path'],'file':current,'source_sha256':hashlib.sha256((BASE/page['html']).read_bytes()).hexdigest(),'english_sha256':hashlib.sha256(original.encode()).hexdigest(),'translation_review':'terminology-and-technical-content-checked'})
(BASE/'sources/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(BASE/'sources/translations.json').write_text(json.dumps([{'id':u['id'],'source':u['source'],'zh':translated[u['source']]} for u in units],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Use source order for tutorials; preserve the official extension names in the directory.
def make_nav(selected,prefix):
    tree={}
    for p in sorted(selected,key=lambda p:p['source']):
        key=p['path'].removeprefix(prefix).strip('/');node=tree
        for part in key.split('/') if key else []:node=node.setdefault(part,{})
        node['_page']=p
    group_names={'creating-stories':'编写故事','helpful-features':'辅助功能','entries':'条目','action':'动作','audience':'受众','cinematic':'过场动画','dialogue':'对话','event':'事件','fact':'事实','group':'组','quest':'任务','sound':'声音','static':'静态条目','activity':'活动','data':'实体数据','entity':'实体','instance':'实例','manifest':'呈现条目','trigger':'触发条目'}
    def walk(node):
        result=[]
        if '_page' in node:result.append({'概览':files[node['_page']['path']]})
        for key,child in node.items():
            if key=='_page':continue
            p=child.get('_page');label=titles[p['path']]['zh'] if p else group_names.get(key,key)
            if key.endswith('Adapter'):label=key
            if set(child)=={'_page'}:result.append({label:files[p['path']]})
            else:result.append({label:walk(child)})
        return result
    return walk(tree)
nav=[{'前言':'index.md'},{'使用文档':make_nav([p for p in pages if p['path'].startswith('/docs/') and p['path']!='/docs/home'],'/docs')},{'扩展条目':make_nav([p for p in pages if p['path'].startswith('/adapters')],'/adapters')},{'开发文档':make_nav([p for p in pages if p['path'].startswith('/develop')],'/develop')}]
config={'site_name':'Typewriter 中文 Wiki','site_url':'https://zhajiahui.github.io/cmi-wiki-cn/typewriter/','theme':{'name':'material','language':'zh','font':False},'plugins':[{'search':{'lang':['zh','en']}}],'markdown_extensions':['admonition','attr_list','md_in_html','tables',{'toc':{'permalink':True}},'pymdownx.details','pymdownx.superfences'],'nav':nav,'hooks':['scripts/media-hook.py'],'extra_javascript':['assets/typewriter.js'],'docs_dir':'docs','site_dir':'.cache/site'}
(BASE/'mkdocs.yml').write_text(yaml.safe_dump(config,allow_unicode=True,sort_keys=False),encoding='utf-8')
print(json.dumps({'pages':len(manifest),'units':len(units),'assets':len(assets)},ensure_ascii=False))
