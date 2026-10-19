---
title: Giveitem
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/giveitem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Giveitem {#giveitem}

## 说明 {#description}

给目标一个物品。支持 Droptable。

当目标的物品栏中没有空间时，该机制不会执行任何操作。

fakeLooting 被添加到 4.12 MM 中，它使给予的物品显示在屏幕上并飞向玩家的物品栏，就像玩家从地上捡起物品一样。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| item | items, i, type, t, material, mat, m | 物品材质，支持 MythicMobs 的[物品](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Items/Items)和[掉落表](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/drops/Drops#drop-tables)。可在物品名称后添加一个空格和数字来指定数量。 |  |
| fakeLooting | dofakelooting, fl | 从原点播放拾取物品动画。 | false |
| variable | var | 要将其值作为实际物品给予的 Item 变量。 |  |

## 示例 {#examples}

```yaml
  Skills:
  - giveitem{i=diamond_sword} @PIR{r=20} ~onSpawn
  - ...
```

下面的示例为玩家提供 6 块曲奇。

```yaml
  Skills:
  - giveitem{i=cookie 6} @PIR{r=20} ~onSpawn
  - ...
```

## 别名 {#aliases}

- give
- giveitems
- itemgive
