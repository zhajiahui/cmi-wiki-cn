"""Merge each project's full-Wiki navigation without touching its configuration navigation."""
from pathlib import Path
import sys,yaml
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'Site'))
from hooks import PROJECTS
for project,_ in PROJECTS:
    source=ROOT/project/'sources/wiki-nav.yml'
    if not source.is_file():continue
    extra=yaml.safe_load(source.read_text('utf-8')) or []
    path=ROOT/project/'mkdocs.yml';config=yaml.safe_load(path.read_text('utf-8'))
    nav=[row for row in config['nav'] if '插件 Wiki' not in row]
    if extra:nav.insert(1,{'插件 Wiki':extra})
    config['nav']=nav
    path.write_text(yaml.safe_dump(config,allow_unicode=True,sort_keys=False),'utf-8',newline='\n')
    print(project,len(extra))
