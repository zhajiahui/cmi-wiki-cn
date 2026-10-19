---
title: Set Display Entity Item
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setDisplayEntityItem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Display Entity Item {#set-display-entity-item}

## 说明 {#description}

设置目标物品展示实体的物品组件。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| item | i, type, t, material, mat, m | 要使用的物品。未设置时，此机制会改为移除实体上的物品 | AIR |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ITEM_DISPLAY
  Skills:
  - setDisplayEntityItem{i=MyMythicItem} @self ~onSpawn
```
