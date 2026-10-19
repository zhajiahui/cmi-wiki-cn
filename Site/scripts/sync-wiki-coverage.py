"""Build the reader-facing coverage inventory from each plugin's frozen source ledger."""
from pathlib import Path
import json,sys,yaml,re
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'Site'))
from hooks import PROJECTS
lines=['---','title: Wiki 收录范围','source_kind: translation-inventory','translation_review: reviewed','---','','# Wiki 收录范围','','本页列出插件包所含主插件的官方 Wiki 正文。API、SDK 接口参考单独排除；安装、配置、命令、权限、内容制作和排错资料按官方目录收录。','','文档以归档时的官方页面为准，随包插件版本见[插件与配置](index.md)。官网持续更新的文档不等同于随包版本的专用手册。原文中的历史版本说明和限制保留。','','| 插件 | 已收录正文 | API 排除项 | 缺源或失效项 | 收录情况 |','| --- | ---: | ---: | ---: | --- |']
details=[];totals=0;catalogue={}
def landing(rows):
    priorities=['wiki/index.md','wiki/home.md','wiki/Home.md','wiki/main-page.md','wiki/core.md','wiki/master.md','wiki/readme.md']
    return next((row for file in priorities for row in rows if row['file']==file),rows[0] if rows else None)
for project,prefix in PROJECTS:
 base=ROOT/project;p=base/'sources/wiki-coverage.json';m=base/'sources/wiki-manifest.json'
 if not p.exists() or not m.exists():continue
 c=json.loads(p.read_text('utf-8'));rows=json.loads(m.read_text('utf-8'));n=len(rows);totals+=n
 api=c.get('excluded_api',[]);missing=c.get('unavailable',[])
 pending=c.get('pending_pages',c.get('translation_pending',[]))
 pending=len(pending) if isinstance(pending,list) else pending
 if isinstance(c.get('pages'),dict):pending=c['pages'].get('pending',pending)
 state='已收录当前可取得的非 API 正文'
 if pending:state=f'还有 {pending} 页待译'
 if project=='NeigeItems':state='公开资料；完整 Wiki 为付费内容，尚缺正文'
 elif project=='CrackShotX':state='随包 1.1.0 对应的官方文档尚未确认'
 elif project=='pStats':state='未发现独立官方 Wiki'
 elif missing:state='可取得的正文已收录；失效项见下方'
 first=landing(rows)
 target=f'../{prefix}'+(first['file'] if first else 'index.md')
 count=f'{n} 页' if project!='NeigeItems' else f'{n} 份公开资料'
 catalogue[project]=(f'[{count}]({target})' if rows else '资料待确认') if project!='pStats' else '无独立 Wiki'
 lines.append(f'| [{project}]({target}) | {count} | {len(api)} | {len(missing)} | {state} |')
 if api or missing:
  details+=['',f'## {project}','']
  for title,items in [('API 排除项',api),('缺源或失效项',missing)]:
   if not items:continue
   details += [f'### {title}','']
   for item in items:
    url=item.get('url') or item.get('source_url') or item.get('prefix') or '';label=item.get('title') or url or '接口参考片段'
    reason=item.get('reason','')
    if not reason and item.get('http'):reason=f'官方地址返回 HTTP {item["http"]}'
    if item.get('scope')=='sections_only':reason='仅排除页内接口片段。'+reason
    reason=reason.replace('\n',' ').replace('|','&#124;')
    details.append((f'- [{label}]({url})' if url else '- '+label)+('：'+reason if reason else ''))
lines+=['','API 排除项既包括整页接口参考，也包括混合页面中的接口片段，因此不能用此列与正文页数直接相加。缺源项包括空白页、失效引用及无法确认的文档入口。原站的同页别名不重复计数。','','NeigeItems 的公开仓库资料未替代其付费 Wiki。CrackShotX 和 pStats 尚无可确认的独立完整文档，保留已提供的配置入口。']+details
out=ROOT/'Plugins/docs/wiki-coverage.md';out.write_text('\n'.join(lines)+'\n','utf-8',newline='\n')
p=ROOT/'Plugins/mkdocs.yml';config=yaml.safe_load(p.read_text('utf-8'));config['nav']=[{'插件总览':'index.md'},{'Wiki 收录范围':'wiki-coverage.md'}];p.write_text(yaml.safe_dump(config,allow_unicode=True,sort_keys=False),'utf-8',newline='\n')
print(json.dumps({'projects':sum(1 for line in lines if line.startswith('| [')),'archived_articles':totals},ensure_ascii=False))

p=ROOT/'Plugins/docs/index.md';updated=[]
for line in p.read_text('utf-8').splitlines():
    match=re.match(r'\| \[([^]]+)\]',line)
    if match and match[1] in catalogue:
        cells=line.split('|');cells[3]=' '+catalogue[match[1]]+' ';line='|'.join(cells)
    updated.append(line)
p.write_text('\n'.join(updated)+'\n','utf-8',newline='\n')
