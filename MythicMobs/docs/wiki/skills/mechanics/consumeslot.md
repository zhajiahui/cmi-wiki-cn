---
title: Consumeslot
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/consumeslot
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Consumeslot {#consumeslot}

## 说明 {#description}

从玩家物品栏的特定位置移除物品。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| slot | s | 要移除物品的物品栏槽位。接受 0 到 35，或装备槽位。 | HAND |
| amount | a | 要移除的物品数量。 | 1 |

## 示例 {#examples}

将删除最近玩家物品栏的插槽 0 或第一个插槽中的任何物品

```yaml
  Skills:
  - consumeslot{slot=0;amount=1} @NearestPlayer{r=10}
```

##  {#section}

会移除最近玩家物品栏中 HAND 装备槽中的所有物品

```yaml
  Skills:
  - consumeslot{slot=HAND;amount=1} @NearestPlayer{r=10}
```

## 别名 {#aliases}

- consumeslotitem
