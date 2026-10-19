---
title: Entity Item Type
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EntityItemType
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Entity Item Type {#entity-item-type}

## 说明 {#description}

检查目标物品实体的类型。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | mat, m, type, types, t | 要匹配的物品列表。 |  |

## 示例 {#examples}

```yaml
  TargetConditions:
  - entityItemType{m=STONE} true
```
