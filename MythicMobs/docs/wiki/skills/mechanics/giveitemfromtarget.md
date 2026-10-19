---
title: Giveitemfromtarget
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/giveitemfromtarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Giveitemfromtarget {#giveitemfromtarget}

## 说明 {#description}

fakelooting 设为   true   时，给予施法者物品，并播放物品从目标实体或位置飞向施法者的拾取动画。

fakelooting 设为   false   时，从目标实体或位置给予施法者物品。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| item | items, i | 物品材质，支持 mythicmobs 物品。 |  |
| fakeLooting | dofakelooting, fl | 从目标处播放拾取物品动画。 | true |

## 示例 {#examples}

```yaml
  Skills:
  - giveitem{i=diamond_sword;a=1} @PIR{r=20} ~onSpawn
```

## 别名 {#aliases}

- givefromtarget
- giveitemsfromtarget
- itemgivefromtarget
