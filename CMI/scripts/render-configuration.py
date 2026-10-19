"""Render reviewed YAML examples with comments beside their configuration fields."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import yaml
from markdown.extensions.toc import slugify_unicode, unique
from yaml.nodes import MappingNode, SequenceNode

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / 'sources/configuration-comments.json'
EXAMPLES = BASE / 'sources/configuration-examples.json'
NOTES = [
    '`ChatFilter.yml` 的 `:DDD` 示例同时写了“2 个字母”和“3 个大写字母”，数量存在矛盾；译文保留原说明。',
    '`Scavenge.yml` 对提取失败后附魔降级的两条说明都提到 `100`，却分别表示避免降级和总是降级；译文保留原说明。',
    '`Ranks.yml` 中 `Branch2Rank1` 的原广播指向 `Branch1Rank1`，汉化保留这个指向。',
    '`config.yml` 的重生优先级注释提到“随机重生条件”，原文没有进一步解释；译文按原文保留。',
]


def source_hash(path):
    return hashlib.sha256(path.read_text(encoding='utf-8').encode('utf-8')).hexdigest()


def page_path(entry):
    return entry['page'] or 'configuration/' + Path(entry['name']).stem.lower() + '.md'


def page(title, content, source_file=None):
    metadata = {'title': title, 'source_kind': 'configuration-examples', 'translation_review': 'reviewed'}
    if source_file:
        metadata['source_file'] = source_file
    return '---\n' + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False) + '---\n\n# ' + title + '\n\n' + content.rstrip() + '\n'


def mapping_fields(node, path=()):
    if isinstance(node, MappingNode):
        for key, value in node.value:
            nested = path + (key.value,)
            yield nested, key.start_mark.line
            yield from mapping_fields(value, nested)
    elif isinstance(node, SequenceNode):
        for index, value in enumerate(node.value):
            yield from mapping_fields(value, path + (str(index),))


def preceding_comments(lines, line, lower_bound=0):
    while line > lower_bound and (not lines[line - 1].strip() or lines[line - 1].lstrip().startswith('#')):
        line -= 1
    return line


def yaml_sections(text, max_lines=100):
    """Keep complete top-level sections; split very long mappings between children."""
    lines = text.splitlines()
    root = yaml.compose(text)
    if not isinstance(root, MappingNode) or not root.value:
        return [{'path': (), 'text': text.rstrip(), 'start': 0, 'end': len(lines), 'prefix': 0}] if text.strip() else []
    starts = [preceding_comments(lines, key.start_mark.line) for key, _ in root.value]
    sections = []
    for index, (key, value) in enumerate(root.value):
        start = starts[index]
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        if end - start <= max_lines + 25 or not isinstance(value, MappingNode) or len(value.value) < 2:
            sections.append({'path': (key.value,), 'text': '\n'.join(lines[start:end]).rstrip(), 'start': start, 'end': end, 'prefix': 0})
            continue
        child_starts = [preceding_comments(lines, child.start_mark.line, key.start_mark.line + 1) for child, _ in value.value]
        # The first chunk retains the parent comments. Later chunks repeat only its YAML key.
        chunk_start = start
        for child_index in range(1, len(child_starts)):
            next_end = child_starts[child_index + 1] if child_index + 1 < len(child_starts) else end
            if next_end - chunk_start > max_lines and child_starts[child_index] > chunk_start:
                prefix = [] if chunk_start == start else [lines[key.start_mark.line]]
                sections.append({'path': (key.value,), 'text': '\n'.join(prefix + lines[chunk_start:child_starts[child_index]]).rstrip(), 'start': chunk_start, 'end': child_starts[child_index], 'prefix': len(prefix)})
                chunk_start = child_starts[child_index]
        prefix = [] if chunk_start == start else [lines[key.start_mark.line]]
        sections.append({'path': (key.value,), 'text': '\n'.join(prefix + lines[chunk_start:end]).rstrip(), 'start': chunk_start, 'end': end, 'prefix': len(prefix)})
    return sections


def render_documents(data=None, examples=None):
    data = data or json.loads(SOURCE.read_text(encoding='utf-8'))
    examples = examples or json.loads(EXAMPLES.read_text(encoding='utf-8'))
    templates = {entry['name']: entry for entry in examples['files']}
    units = {row['id']: row for row in data['units']}
    pages = {}
    manifest = []
    digest = source_hash(SOURCE)
    examples_digest = source_hash(EXAMPLES)
    index = [
        '配置文件按原有 YAML 层级展示，中文注释与对应配置项放在一起。代码块右上角可复制当前片段。',
        '示例整理自 2026-10-19 提供的配置，原包未标明 CMI 版本。连接信息、玩家标识和世界示例使用占位符；具体设置以服务器本地文件为准。',
        '| 文件 | 配置内容 |\n| --- | --- |',
    ]
    for entry in data['files']:
        name = entry['name']
        filename = page_path(entry)
        example = templates[name]
        text = example['yaml']
        title = entry['title'] + '（' + Path(name).name + '）'
        index[-1] += f'\n| `{name}` | [{entry["title"]}]({Path(filename).name}) |'
        content = [f'文件：`plugins/CMI/{name}`']
        if example['redacted_paths']:
            content.append('连接信息、玩家标识和世界示例已使用占位符，使用时按本地配置填写。')
        sections = yaml_sections(text)
        fields = list(mapping_fields(yaml.compose(text)))
        descriptions = {}
        for block in entry['blocks']:
            descriptions.setdefault(tuple(block['path']), []).extend(units[identity]['translation'] for identity in block['units'])
        used_ids = set()
        anchors = []
        paths = {}
        for path, line in fields:
            identity = unique(slugify_unicode('.'.join(path), '-'), used_ids)
            paths[path] = identity
            anchors.append({'path': list(path), 'id': identity, 'source_line': line, 'text': '\n'.join(descriptions.get(path, []))})
        last_root = None
        part_counts = Counter(section['path'] for section in sections)
        part_numbers = Counter()
        for block_index, section in enumerate(sections):
            path = section['path']
            if path and path != last_root:
                content.append('## `' + '.'.join(path) + '` { #' + paths[path] + ' }')
                last_root = path
            part_numbers[path] += 1
            label = Path(name).name
            if path:
                label += ' · ' + '.'.join(path)
            if part_counts[path] > 1:
                label += f'（{part_numbers[path]}/{part_counts[path]}）'
            content.append('```yaml title="' + label + '"\n' + section['text'] + '\n```')
            for anchor in anchors:
                if section['start'] <= anchor['source_line'] < section['end']:
                    anchor['block'] = block_index
                    comment_line = preceding_comments(text.splitlines(), anchor['source_line'], section['start'])
                    anchor['line'] = comment_line - section['start'] + 1 + section['prefix']
                    anchor['heading'] = len(anchor['path']) == 1
        if not text.strip():
            content.append('原文件为空，没有可展示的配置项。')
        pages[filename] = page(title, '\n\n'.join(content), name)
        manifest.append({'file': filename, 'title': title, 'source_kind': 'configuration-examples', 'source_sha256': digest, 'examples_sha256': examples_digest, 'translation_review': 'reviewed', 'anchors': anchors})
    pages['configuration/index.md'] = page('配置文件', '\n\n'.join(index + ['## 翻译备注', '\n'.join('- ' + note for note in NOTES)]))
    manifest.append({'file': 'configuration/index.md', 'title': '配置文件', 'source_kind': 'configuration-examples', 'source_sha256': digest, 'examples_sha256': examples_digest, 'translation_review': 'reviewed', 'anchors': []})
    return pages, manifest


def render_pages(data=None):
    return render_documents(data)[0]


def render():
    pages, manifest = render_documents()
    for name, content in pages.items():
        target = BASE / 'docs' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8', newline='\n')
    (BASE / 'sources/configuration-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(f'Rendered {len(pages)} annotated YAML configuration pages.')


if __name__ == '__main__':
    render()
