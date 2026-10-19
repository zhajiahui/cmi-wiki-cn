---
title: Itemissimilar
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/itemissimilar
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Itemissimilar {#itemissimilar}

## 说明 {#description}

检查目标玩家的物品栏中是否有与指定物品相似的物品。   更具体地说，将比较它们的ItemStacks，如果匹配，则条件将返回  true  。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| item | i, material, m, mm, mythicitem | 要检查的物品。 | DIRT |
| slot | s | 要检查的物品栏槽位。接受 0 到 35，或装备槽位。 | HAND |

## 示例 {#examples}

检查目标玩家物品栏第 0 个槽位，也就是第一个槽位中的物品。

```yml
  Conditions:
  - itemissimilar{i=MyCustomItem;slot=0} true
```

## 别名 {#aliases}

- issimilar
- similarto
