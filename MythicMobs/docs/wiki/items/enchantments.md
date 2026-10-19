---
title: 附魔
source_url: https://wiki.mythiccraft.io/mythicmobs/Items/Enchantments
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 附魔 {#enchantments}

Enchantments 属性用于为 MythicMobs 创建的物品添加附魔。任何附魔都可以添加到任何物品上，也可以超过 Minecraft 原版的附魔等级上限。不过，将某些附魔添加到不适用的物品上时，可能没有效果。

## 语法 {#syntax}

```yml
internal_itemname:
  Id: <material>
  Enchantments:
  - <enchantment> <level>
  - <enchantment> <level>
  - ...
```

**<enchantment>**  
要应用到指定物品上的附魔类型。

**<level>**  
指定附魔的等级。

## 可用附魔 {#available-enchantments}

可用[附魔](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/enchantments/Enchantment.html)的列表见 Spigot Javadocs。

如果存在其他附魔提供方，也可以通过 `namespace:enchant_name` 语法添加附魔。

## 示例 {#example}

```yml
lethal_pickaxe:
  Id: diamond_pickaxe
  Enchantments:
  - SHARPNESS 3
  - KNOCKBACK 1
  - mythic:example_enchant 2
```
