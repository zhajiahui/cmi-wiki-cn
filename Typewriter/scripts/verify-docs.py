"""Verify source coverage, examples, protected tokens, resources and navigation."""
from pathlib import Path
from collections import Counter
import json,re,hashlib,sys,yaml
from bs4 import BeautifulSoup
BASE=Path(__file__).resolve().parents[1]
errors=[];code_count=0;inline_count=0;media_count=0
pages=json.loads((BASE/'sources/pages.json').read_text(encoding='utf-8'))
manifest=json.loads((BASE/'sources/manifest.json').read_text(encoding='utf-8'))
assets=json.loads((BASE/'sources/assets.json').read_text(encoding='utf-8'))
translations=json.loads((BASE/'sources/translations.json').read_text(encoding='utf-8'))
if len(pages)!=316 or {p['path'] for p in pages}!={p['source_path'] for p in manifest}:errors.append('Page coverage mismatch')
def navfiles(items):
    for item in items:
        for value in item.values():
            if isinstance(value,list):yield from navfiles(value)
            else:yield value
nav=list(navfiles(yaml.safe_load((BASE/'mkdocs.yml').read_text(encoding='utf-8'))['nav']))
if len(nav)!=len(set(nav)) or set(nav)!={p['file'] for p in manifest}:errors.append('Navigation coverage mismatch')
for item in translations:
    source=item['source'];zh=item['zh'];original=Counter(re.findall(r'`([^`]+)`',source));output=Counter(re.findall(r'`([^`]+)`',zh))
    if original-output:errors.append('Inline token changed: '+str(item['id'])+': '+str(list((original-output).elements())))
    inline_count+=sum(original.values())
    for token in re.findall(r'(?:typewriter\.[A-Za-z0-9_./*]+|%typewriter_[^%]+%)',source):
        if token not in zh:errors.append('Technical identifier changed: '+str(item['id'])+': '+token)
    if re.search(r'ZXQ\d+QXZ|SOURCE_CODE_',zh):errors.append('Unresolved marker: '+str(item['id']))
    clean=lambda s:re.sub(r'`[^`]+`|https?://[^)\s]+','',s)
    numbers=lambda s:Counter(re.findall(r'(?<![A-Za-z0-9_.])\d+(?:\.\d+)*(?![A-Za-z0-9_.])',clean(s)))
    if numbers(source)-numbers(zh):errors.append('Number missing: '+str(item['id'])+': '+str(numbers(source)-numbers(zh)))
for row in manifest:
    page=next(p for p in pages if p['path']==row['source_path'])
    source=(BASE/page['html']).read_bytes()
    if hashlib.sha256(source).hexdigest()!=row['source_sha256']:errors.append('Source hash changed: '+row['file'])
    en=(BASE/page['english']).read_text(encoding='utf-8')
    zh=(BASE/'docs'/row['file']).read_text(encoding='utf-8')
    blocks=lambda s:re.findall(r'^(`{3,})[^\n]*\n([\s\S]*?)^\1\s*$',s,re.M)
    original=[c for _,c in blocks(en)];output=[c for _,c in blocks(zh)]
    if original!=output:errors.append('Code block changed: '+row['file'])
    code_count+=len(original)
    original_ids=re.findall(r'\{#([^}]+)\}',en)
    if any('{#'+a+'}' not in zh for a in original_ids):errors.append('Original heading anchor missing: '+row['file'])
    for url,info in assets.items():
        if url in en and info['file'].rsplit('/',1)[-1] not in zh:errors.append('Resource omitted: '+row['file']+': '+url)
    media_count+=en.count('<video ')
for url,info in assets.items():
    path=BASE/'docs'/info['file']
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=info['sha256']:errors.append('Resource hash mismatch: '+info['file'])
report={'project':'Typewriter','source_version':'0.8.0','source_pages':len(pages),'translated_pages':len(manifest),'translation_units':len(translations),'verbatim_code_blocks':code_count,'protected_inline_tokens':inline_count,'videos':media_count,'assets':len(assets),'errors':errors}
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:sys.exit(1)
