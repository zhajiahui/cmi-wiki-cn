---
title: Entity Item Is Similar
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EntityItemIsSimilar
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Entity Item Is Similar {#entity-item-is-similar}

## 说明 {#description}

检查物品实体是否与指定物品堆栈相似。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| item | i, material, m, mm, mythicitem | 用于检查的物品。 | DIRT |

## 示例 {#examples}

```yaml
  TargetConditions:
  - entityitemissimilar{i=MyCustomItem} true
```
