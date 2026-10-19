---
title: Giveitemfromslot
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/giveitemfromslot
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Giveitemfromslot {#giveitemfromslot}

## 说明 {#description}

将施法者指定槽位中物品的副本给予目标。

不会消耗给定施法者槽中的物品。

当目标的物品栏中没有空间时，该机制不会执行任何操作。

fakeLooting 被添加到 4.12 中，它使给予的物品显示在屏幕上并飞向玩家的物品栏，就像玩家从地上捡起物品一样。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| slot | s | 施法者的[槽位](../equipslot.md)。 |  |
| fakeLooting | fl, dofakelooting | 从原点播放拾取物品动画。 | false |

## 示例 {#examples}

将施法者的主手物品交给服务器上的所有玩家，并播放拾取动画。

```yaml
  Skills:
  - giveitemfromslot{slot=HAND;fakelooting=true} @server ~onTimer:10
```

## 别名 {#aliases}

- givefromslot
