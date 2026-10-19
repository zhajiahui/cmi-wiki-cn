---
title: Structure
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/structure
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Structure {#structure}

## 说明 {#description}

如果目标位置位于结构内部，则匹配。支持数据包中的通配符和结构。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| structure | structures, s | 要检查的结构，可以是列表。 | village |

## 示例 {#examples}

```yml
  Conditions:
  - structure{s=minecraft:desert_pyramid} true
```
