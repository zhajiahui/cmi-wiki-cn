---
title: Lastsignal
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lastsignal
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Lastsignal {#lastsignal}

## 说明 {#description}

匹配目标生物最后收到的信号

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| signal | s | 要匹配的信号。 | DEFAULT |

## 示例 {#examples}

```yaml
  Conditions:
  - lastsignal{s=fireCannonShot} true
```
