"""Check imported examples, repeatable pages, file coverage, anchors and project navigation."""
from pathlib import Path
import json
import hashlib
import re
import sys
import yaml
from configuration import ROOT, EXAMPLES_NAME, MANIFEST_NAME, render_documents, LAYOUT
from hooks import PROJECTS, PLUGIN_PROJECTS

errors=[];file_count=page_count=field_count=block_count=redaction_count=0

def nav_files(items):
    for item in items:
        for value in item.values():
            if isinstance(value,list):yield from nav_files(value)
            else:yield value

for project,prefix in PROJECTS:
    base=ROOT/project
    extras=[]
    example=base/'sources'/EXAMPLES_NAME
    if example.is_file():
        data=json.loads(example.read_text('utf-8'))
        expected,expected_manifest=render_documents(project,data)
        actual=json.loads((base/'sources'/MANIFEST_NAME).read_text('utf-8'))
        if expected_manifest!=actual:errors.append(project+': imported manifest changed')
        extras=actual
        file_count+=len(data['files']);page_count+=len(actual)
        for name,text in expected.items():
            target=base/'docs'/name
            if not target.is_file() or target.read_text('utf-8')!=text:errors.append(project+': generated page differs: '+name)
        for row in actual:
            ids=[a['id'] for a in row.get('anchors',[])]
            field_count+=len(ids)
            if len(ids)!=len(set(ids)):errors.append(project+': duplicate field anchors: '+row['file'])
        for row in data['files']:
            code=row['code'];language=row['language']
            if language in ('yaml','json'):
                parsed=yaml.safe_load(code)
                if language=='json':json.loads(code)
                for redaction in row.get('redacted_paths',[]):
                    v=parsed
                    for key in redaction['path']:
                        v=v[int(key)] if isinstance(v,list) else v[key]
                    if v!=redaction['placeholder']:errors.append(project+': public placeholder differs: '+row['name'])
                    redaction_count+=1
            if language=='yaml':
                recovered=[]
                for part in LAYOUT.yaml_sections(code):
                    recovered.extend(part['text'].splitlines()[part['prefix']:]);block_count+=1
                    try:yaml.safe_load(part['text'])
                    except yaml.YAMLError:errors.append(project+': invalid display YAML: '+row['name'])
                if [s for s in recovered if s.strip()]!=[s for s in code.splitlines() if s.strip()]:errors.append(project+': display split lost/reordered lines: '+row['name'])
            else:block_count+=1
    if (project,prefix) in PLUGIN_PROJECTS:
        source=base/'sources/manifest.json'
        if not source.is_file():errors.append(project+': main plugin manifest is missing');continue
        manifest=json.loads(source.read_text('utf-8'))
        for row in manifest:
            page=base/'docs'/row['file']
            if not page.is_file():errors.append(project+': main plugin page missing')
            elif not page.read_text('utf-8').startswith('---\n'):errors.append(project+': frontmatter missing')
            primary=base/'sources/overview-sources.md'
            if primary.is_file() and row.get('source_sha256')!=hashlib.sha256(primary.read_text('utf-8').encode('utf-8')).hexdigest():errors.append(project+': overview source hash differs')
        if project!='Plugins' and not (base/'sources/overview-sources.md').is_file():errors.append(project+': primary sources missing')
        nav=list(nav_files(yaml.safe_load((base/'mkdocs.yml').read_text('utf-8'))['nav']))
        if len(nav)!=len(set(nav)) or set(nav)!={row['file'] for row in manifest+extras}:errors.append(project+': plugin navigation coverage differs')
report=dict(imported_projects=sum((ROOT/project/'sources'/EXAMPLES_NAME).is_file() for project,_ in PROJECTS),configuration_files=file_count,configuration_pages=page_count,configuration_fields=field_count,code_blocks=block_count,public_placeholders=redaction_count,errors=errors)
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:sys.exit(1)
