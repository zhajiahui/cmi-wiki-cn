"""Render the reviewed configuration comments without reading server values."""
from pathlib import Path
from html import escape
import hashlib
import json
import re
import yaml

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / 'sources/configuration-comments.json'
NOTES = [
    '`ChatFilter.yml` 的 `:DDD` 示例同时写了“2 个字母”和“3 个大写字母”，数量存在矛盾；译文保留原说明。',
    '`Scavenge.yml` 对提取失败后附魔降级的两条说明都提到 `100`，却分别表示避免降级和总是降级；译文保留原说明。',
    '`Ranks.yml` 中 `Branch2Rank1` 的原广播指向 `Branch1Rank1`，汉化保留这个指向。',
    '`config.yml` 的重生优先级注释提到“随机重生条件”，原文没有进一步解释；译文按原文保留。',
]


def plain(text):
    """Keep comment punctuation literal in Markdown paragraphs."""
    text = escape(text.strip(), quote=False)
    return re.sub(r'([\\`*_\[\]])', r'\\\1', text)


def comment_block(ids, units):
    parts = []
    pending = []
    mode = None

    def flush():
        if not pending:
            return
        if mode == 'code':
            # These lines are source examples or indented example fragments.
            parts.append('```text\n' + '\n'.join(pending).rstrip() + '\n```')
        else:
            parts.append('<br>\n'.join(pending))
        pending.clear()

    for identity in ids:
        row = units[identity]
        text = row['translation']
        kind = 'code' if row['source'] == text or text[:1].isspace() else 'prose'
        if kind != mode:
            flush()
            mode = kind
        pending.append(text if kind == 'code' else plain(text))
    flush()
    return '\n\n'.join(parts)


def page(title, content, source_file=None):
    metadata = {'title': title, 'source_kind': 'configuration-comments', 'translation_review': 'reviewed'}
    if source_file:
        metadata['source_file'] = source_file
    return '---\n' + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False) + '---\n\n# ' + title + '\n\n' + content.rstrip() + '\n'


def render_pages(data=None):
    data = data or json.loads(SOURCE.read_text(encoding='utf-8'))
    units = {row['id']: row for row in data['units']}
    pages = {}
    index = [
        '本节翻译 2026-10-19 提供的 CMI 配置注释，保留配置项名称和注释中的示例。原包未标明 CMI 版本。',
        '页面按文件和配置项排列，不展示服务器的实际设置值。',
        '| 文件 | 注释说明 |\n| --- | --- |',
    ]
    for entry in data['files']:
        name = entry['name']
        if entry['page']:
            filename = Path(entry['page']).name
            index[-1] += f'\n| `{name}` | [{entry["title"]}]({filename}) |'
            title = entry['title'] + '（' + Path(name).name + '）'
            content = [f'文件：`plugins/CMI/{name}`', '来源：用户提供的配置文件；本文仅收录原注释的中文翻译。']
            last_root = None
            last_path = None
            for block in entry['blocks']:
                path = block['path']
                root = path[0] if path else None
                if root != last_root:
                    content.append('## `' + root + '`' if root else '## 文件末尾说明')
                    last_root = root
                    last_path = None
                if len(path) > 1 and path != last_path:
                    content.append('### `' + '.'.join(path) + '`')
                content.append(comment_block(block['units'], units))
                last_path = path
            pages[entry['page']] = page(title, '\n\n'.join(content), name)
        else:
            reason = '原文件为空' if entry['empty'] else '原文件没有注释，示例中的显示文字已在本地覆盖包中汉化'
            index[-1] += f'\n| `{name}` | {reason} |'
    index.extend(['## 翻译备注', '\n'.join('- ' + note for note in NOTES)])
    pages['configuration/index.md'] = page('配置文件', '\n\n'.join(index))
    return pages


def render():
    pages = render_pages()
    digest = hashlib.sha256(SOURCE.read_text(encoding='utf-8').encode('utf-8')).hexdigest()
    manifest = []
    for name, content in pages.items():
        target = BASE / 'docs' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
        metadata = yaml.safe_load(content[4:].split('\n---\n', 1)[0])
        manifest.append({'file': name, 'title': metadata['title'], 'source_kind': 'configuration-comments', 'source_sha256': digest, 'translation_review': 'reviewed'})
    (BASE / 'sources/configuration-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Rendered {len(pages)} configuration comment pages.')


if __name__ == '__main__':
    render()
