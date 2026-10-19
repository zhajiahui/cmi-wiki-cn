---
title: Pitch
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/pitch
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Pitch {#pitch}

## 说明 {#description}

检查目标实体的俯仰角是否在范围内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| pitch | p | 要匹配的数值范围。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - pitch{p=-45to45} true
```

```yaml
  Conditions:
  - pitch{p=>45} true
```
