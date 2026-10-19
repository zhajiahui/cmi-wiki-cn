"""Check page coverage, source examples, local assets and navigation."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
import hashlib, json, re, sys
from bs4 import BeautifulSoup
import markdown, yaml

BASE = Path(__file__).resolve().parents[1]
DOCS = BASE / 'docs'
errors = []
rows = json.loads((BASE / 'sources/pages.json').read_text(encoding='utf-8'))
manifest = json.loads((BASE / 'sources/manifest.json').read_text(encoding='utf-8'))
configuration_manifest = json.loads((BASE / 'sources/configuration-manifest.json').read_text(encoding='utf-8'))
assets = json.loads((BASE / 'sources/assets.json').read_text(encoding='utf-8'))
expected = {r['id'] for r in rows if (BASE / 'sources/en' / f"{r['id']}.md").read_text(encoding='utf-8').strip()}
actual = {r['source_id'] for r in manifest}
if expected != actual:
    errors.append(f'Coverage mismatch: missing={expected-actual}, unexpected={actual-expected}')
config = yaml.safe_load((BASE / 'mkdocs.yml').read_text(encoding='utf-8'))
def navfiles(items):
    for item in items:
        for value in item.values():
            if isinstance(value, list):
                yield from navfiles(value)
            else:
                yield value
nav = list(navfiles(config['nav']))
imported_path = BASE / 'sources/imported-configuration-manifest.json'
imported_manifest = json.loads(imported_path.read_text('utf-8')) if imported_path.is_file() else []
if set(nav) != {r['file'] for r in manifest + configuration_manifest + imported_manifest}:
    errors.append('Navigation does not cover exactly the translated pages')
if len(nav) != len(set(nav)):
    errors.append('Duplicate navigation entries')
norm = lambda s: re.sub(r'\s+', '', s)
blocks = 0
translated_help_blocks = 0
# These four source blocks are textual help lists, not executable examples.
# Their visible explanations are translated; tags, commands and nodes stay exact.
translatable_help = {1437: {7, 8}, 91: {1, 6}}
for page in manifest:
    path = DOCS / page['file']
    if not path.exists():
        errors.append('Missing translated page: ' + page['file'])
        continue
    text = path.read_text(encoding='utf-8')
    if page.get('translation_review') != 'reviewed':
        errors.append('Unreviewed translation: ' + page['file'])
    source_path = BASE / 'sources/html' / f"{page['source_id']}.html"
    if hashlib.sha256(source_path.read_text(encoding='utf-8').encode('utf-8')).hexdigest() != page['source_sha256']:
        errors.append('Source hash changed: ' + page['file'])
    source = BeautifulSoup(source_path.read_text(encoding='utf-8'), 'html.parser')
    source_blocks = []
    for pre_index, pre in enumerate(source.find_all('pre')):
        for br in pre.find_all('br'):
            br.replace_with('\n')
        if norm(pre.get_text()):
            if pre_index in translatable_help.get(page['source_id'], set()):
                translated_help_blocks += 1
                technical = re.findall(r'<[^>\n]+>|cmi\.[A-Za-z0-9_.\[\]*/-]+|/cmi [a-z]+', pre.get_text())
                for token in technical:
                    if token not in text:
                        errors.append('Translated help identifier missing: ' + page['file'] + ': ' + token)
            else:
                source_blocks.append(norm(pre.get_text()))
    output_blocks = re.findall(r'^[ \t]*```[^\n]*\n([\s\S]*?)^[ \t]*```', text, re.M)
    output_counts = Counter(norm(c) for c in output_blocks)
    blocks += len(source_blocks)
    for block, count in Counter(source_blocks).items():
        if output_counts[block] < count:
            errors.append(f'Source code block missing or changed: {page["file"]}: {block[:85]}')
    for image in source.find_all('img', src=True):
        url = image['src']
        if url.startswith('//'):
            url = 'https:' + url
        if 'clear.png' in url:
            continue
        info = assets.get(url)
        if not info or 'file' not in info:
            errors.append('Source image missing from asset archive: ' + url)
        elif info['file'].split('/')[-1] not in text:
            errors.append('Source image omitted: ' + page['file'] + ': ' + url)
    # Parse links as Markdown rather than splitting on a parenthesis in a title.
    body = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.S)
    rendered = BeautifulSoup(markdown.markdown(body, extensions=['fenced_code', 'tables', 'attr_list']), 'html.parser')
    for node in rendered.find_all(['a', 'img']):
        url = node.get('href') if node.name == 'a' else node.get('src')
        if not url:
            continue
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        if parts.path.startswith('/'):
            errors.append('Absolute local link: ' + page['file'] + ': ' + url)
            continue
        target = (path.parent / unquote(parts.path)).resolve()
        if not target.is_relative_to(DOCS.resolve()) or not target.exists():
            errors.append('Broken local link: ' + page['file'] + ': ' + url)
    if re.search(r'ZXQ\d+X', text):
        errors.append('Editor token left in page: ' + page['file'])
for url, info in assets.items():
    if 'file' not in info:
        errors.append('Asset download failed: ' + url)
        continue
    path = DOCS / info['file']
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != info['sha256']:
        errors.append('Asset hash mismatch: ' + info['file'])
report = {'source_pages': len(rows), 'translated_pages': len(manifest), 'configuration_pages': len(configuration_manifest), 'empty_source_pages': len(rows)-len(expected), 'assets': len(assets), 'verbatim_source_code_blocks': blocks, 'translated_help_blocks': translated_help_blocks, 'errors': errors}
print(json.dumps(report, ensure_ascii=False, indent=2))
if errors:
    sys.exit(1)
