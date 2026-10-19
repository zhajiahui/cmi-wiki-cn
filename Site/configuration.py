"""Render imported, public configuration examples without changing their values."""
from pathlib import Path
from collections import Counter
import hashlib
import importlib.util
import json
import re
import yaml
from markdown.extensions.toc import slugify_unicode, unique
from yaml.nodes import MappingNode

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location('cmi_configuration_layout', ROOT / 'CMI/scripts/render-configuration.py')
LAYOUT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LAYOUT)
EXAMPLES_NAME = 'imported-configuration-examples.json'
MANIFEST_NAME = 'imported-configuration-manifest.json'


def page(title, body, **metadata):
    meta = dict(title=title, source_kind='imported-configuration', translation_review='reviewed', **metadata)
    return '---\n' + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + '---\n\n# ' + title + '\n\n' + body.rstrip() + '\n'


def render_documents(project, data=None):
    source = ROOT / project / 'sources' / EXAMPLES_NAME
    data = data if data is not None else json.loads(source.read_text('utf-8'))
    digest = hashlib.sha256(source.read_text('utf-8').encode('utf-8')).hexdigest()
    pages, manifest = {}, []
    index = [
        '中文注释与配置放在同一个代码块中，保留原文件的层级。可用页面目录查找章节，也可在站内搜索配置键。',
        '本页按随包的 **' + data['version'] + '** 整理。这里展示公开示例，连接信息和服务器标识已替换为占位符；完整汉化配置另提供本地覆盖包。',
    ]
    if project == 'Typewriter':
        index.append('站内其余 Typewriter 文档的来源版本是 0.8.0；本批配置来自 0.9.0-beta-177，选项以本页配置为准。')
    index.append('| 文件 | 内容 |\n| --- | --- |')
    index_rows = []
    for entry in data['files']:
        text, filename = entry['code'], entry['page']
        language = entry['language']
        root = yaml.compose(text) if language in ('yaml', 'json') else None
        sections = LAYOUT.yaml_sections(text) if language == 'yaml' else [{'path': (), 'text': text.rstrip(), 'start': 0, 'end': len(text.splitlines()), 'prefix': 0}]
        # Superfences drops leading empty code lines; account for that before anchoring fields.
        for section in sections:
            parts = section['text'].splitlines()
            leading = 0
            while leading < len(parts) and not parts[leading].strip():
                leading += 1
            section['text'] = '\n'.join(parts[leading:])
            section['start'] += leading
        fields = list(LAYOUT.mapping_fields(root)) if root else []
        lines = text.splitlines()
        anchors, ids, paths = [], set(), {}
        for path, line in fields:
            identity = unique(slugify_unicode('.'.join(path), '-'), ids)
            paths[path] = identity
            start = LAYOUT.preceding_comments(lines, line)
            description = '\n'.join(re.sub(r'^\s*#+\s?', '', part) for part in lines[start:line] if part.lstrip().startswith('#'))
            anchors.append(dict(path=list(path), id=identity, source_line=line, text=description))
        body = ['文件：`' + entry['name'] + '`。版本：`' + data['version'] + '`。', entry['description']]
        if entry.get('redacted_paths'):
            body.append('连接信息或服务器标识已替换为示例值，使用时填写自己的信息。')
        last_root = None
        counts = Counter(section['path'] for section in sections)
        numbers = Counter()
        for block, section in enumerate(sections):
            path = section['path']
            if path and path != last_root:
                body.append('## `' + '.'.join(path) + '` { #' + paths[path] + ' }')
                last_root = path
            numbers[path] += 1
            title = entry['name'] + (' · ' + '.'.join(path) if path else '')
            if counts[path] > 1:
                title += f'（{numbers[path]}/{counts[path]}）'
            body.append('```' + language + ' title="' + title + '"\n' + section['text'] + '\n```')
            for anchor in anchors:
                if section['start'] <= anchor['source_line'] < section['end']:
                    anchor.update(block=block, line=LAYOUT.preceding_comments(lines, anchor['source_line'], section['start']) - section['start'] + 1 + section['prefix'], heading=language == 'yaml' and len(anchor['path']) == 1)
        if not text.strip():
            body.append('原文件为空。')
        pages[filename] = page(entry['name'], '\n\n'.join(body), source_file=entry['name'], source_version=data['version'])
        manifest.append(dict(file=filename, title=entry['name'], source_kind='imported-configuration', source_sha256=digest, translation_review='reviewed', anchors=anchors))
        target = Path(filename).relative_to('configuration').as_posix()
        index_rows.append('| [`' + entry['name'] + '`](' + target + ') | ' + entry['description'].replace('|', '\\|') + ' |')
    if data.get('index', True):
        pages['configuration/index.md'] = page('配置文件', '\n\n'.join(index[:-1]) + '\n\n' + index[-1] + '\n' + '\n'.join(index_rows), source_version=data['version'])
        manifest.append(dict(file='configuration/index.md', title='配置文件', source_kind='imported-configuration', source_sha256=digest, translation_review='reviewed', anchors=[]))
    return pages, manifest


def render(project):
    pages, manifest = render_documents(project)
    base = ROOT / project
    for name, content in pages.items():
        target = base / 'docs' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, 'utf-8', newline='\n')
    (base / 'sources' / MANIFEST_NAME).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', 'utf-8', newline='\n')
    return len(pages)


if __name__ == '__main__':
    for source in sorted(ROOT.glob('*/sources/' + EXAMPLES_NAME)):
        project = source.parent.parent.name
        print(project, render(project))
