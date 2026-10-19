---
title: Heightbelow
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/heightbelow
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Heightbelow {#heightbelow}

## 说明 {#description}

检查目标的 Y 位置是否低于给定值

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| height | h | 目标必须低于的高度。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - heightbelow{h=50} true
```
