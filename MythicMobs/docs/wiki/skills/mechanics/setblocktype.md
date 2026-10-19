---
title: Setblocktype
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setblocktype
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setblocktype {#setblocktype}

## 说明 {#description}

更改目标位置的块类型。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m, mat, t, type, types, block, b | 要设置的方块材质 | [DIRT](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html "CLICK ME to view valid block materials") |
| physics | p | 是否对受影响的区域应用物理更新 | true |

## 示例 {#examples}

在施法者的位置设置一个方块

```yaml
SetBlockExample:
  Skills:
  - setblock{m=STONE} @selflocation
```

##  {#section}

在目标位置设置一个 mmoitems 块

```yaml
SetMMOItemsBlock:
  Skills:
  - setblock{m=mmoitems:50} @targetlocation
```

##  {#section-2}

在目标位置设置具有指定方块状态的方块

```yaml
SetButton:
 Skills:
 - setblock{m=JUNGLE_BUTTON[facing=east,face=floor]} @targetlocation
```

## 别名 {#aliases}

- setblock
