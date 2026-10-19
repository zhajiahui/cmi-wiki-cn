"""Check configuration-comment coverage, rendering and technical identifiers."""
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import importlib.util
import json
import re
import sys
import markdown
from bs4 import BeautifulSoup

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / 'sources/configuration-comments.json'
spec = importlib.util.spec_from_file_location('render_configuration', BASE / 'scripts/render-configuration.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
data = json.loads(SOURCE.read_text(encoding='utf-8'))
manifest = json.loads((BASE / 'sources/configuration-manifest.json').read_text(encoding='utf-8'))
errors = []
units = {row['id']: row for row in data['units']}
references = {identity for entry in data['files'] for block in entry['blocks'] for identity in block['units']}
if len(units) != len(data['units']) or references != set(units):
    errors.append('Configuration comment coverage or identity mismatch')
# Explicit review exceptions: third party/person and two types are written in Chinese;
# "100% capitalized" becomes "全部大写" and repeated 100 becomes "两项都设为 100".
number_equivalents = {25, 252, 293, 303, 386, 1191, 1204, 1327, 1793, 1809}
protected = re.compile(r'https?://[^\s<>]+|cmi\.[A-Za-z0-9_.\[\]*/-]+|%[^%\s]+%|\[[^\]\n]*\]|\{[^{}\n]*\}|\b[\w-]+\.(?:yml|yaml|json|txt|jar)\b')
for identity, row in units.items():
    if not row['translation'].strip():
        errors.append(f'Empty configuration translation: {identity}')
    missing = Counter(protected.findall(row['source'])) - Counter(protected.findall(row['translation']))
    if missing:
        errors.append(f'Configuration identifier lost: {identity}: {dict(missing)}')
    if identity not in number_equivalents and Counter(re.findall(r'\d+(?:\.\d+)?', row['source'])) != Counter(re.findall(r'\d+(?:\.\d+)?', row['translation'])):
        errors.append(f'Configuration number changed: {identity}')
expected = renderer.render_pages(data)
if {row['file'] for row in manifest} != set(expected):
    errors.append('Configuration manifest coverage mismatch')
digest = hashlib.sha256(SOURCE.read_text(encoding='utf-8').encode('utf-8')).hexdigest()
for row in manifest:
    path = BASE / 'docs' / row['file']
    if row.get('source_sha256') != digest or row.get('translation_review') != 'reviewed':
        errors.append('Configuration review/hash mismatch: ' + row['file'])
    if not path.is_file() or path.read_text(encoding='utf-8') != expected[row['file']]:
        errors.append('Configuration page differs from reviewed comments: ' + row['file'])
        continue
    text = path.read_text(encoding='utf-8').split('\n---\n', 1)[1]
    rendered = BeautifulSoup(markdown.markdown(text, extensions=['fenced_code', 'tables']), 'html.parser')
    for link in rendered.find_all('a', href=True):
        url = link['href']
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        target = (path.parent / unquote(parts.path)).resolve()
        if not target.is_relative_to((BASE / 'docs').resolve()) or not target.is_file():
            errors.append('Broken configuration link: ' + row['file'] + ': ' + url)
report = {'configuration_files': len(data['files']), 'unique_source_comments': len(units), 'configuration_pages': len(manifest), 'errors': errors}
print(json.dumps(report, ensure_ascii=False, indent=2))
if errors:
    sys.exit(1)
