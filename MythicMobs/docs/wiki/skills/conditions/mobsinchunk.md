---
title: Mobsinchunk
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mobsinchunk
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mobsinchunk {#mobsinchunk}

## 说明 {#description}

将范围与目标位置区块中的生物数量相匹配

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要匹配的数值范围。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - mobsinchunk{a=1to5} true
```

```yaml
  Conditions:
  - mobsinchunk{a=<5} true
```
