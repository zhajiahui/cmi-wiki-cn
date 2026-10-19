---
title: 物品匹配器
source_url: https://wiki.mythiccraft.io/mythicmobs/Items/Item-Matcher
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 物品匹配器 {#item-matcher}

MythicMobs 的部分功能支持通过特定语法匹配物品或方块：

##  {#section}

填写 Mythic 物品或 [Mythic（Crucible）自定义方块](https://wiki.mythiccraft.io/mythiccrucible/Custom-Blocks)的内部名称，将会匹配：

- 对应的 Mythic 物品。
- 对应的 Mythic 自定义方块。

##  {#section-2}

填写 [Spigot 材质类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html)，将会匹配：

- 具有该材质类型的物品。
- 具有该材质类型的方块。

##  {#section-3}

在条目开头使用 `#`，将会匹配：

- 具有该[物品标签](https://minecraft.wiki/w/Item_tag_(Java_Edition)的物品。）
  - `#arrows`、`#axes` 等。
- 具有该[方块标签](https://minecraft.wiki/w/Block_tag_(Java_Edition)的方块。）
  - `#air`、`#animals_spawnable_on` 等。

##  {#section-4}

在条目的任意位置使用 `*`，就会让每个 * 匹配任意数量的字符。对于熟悉正则表达式的人来说，这里的 `*` 相当于 `.*`。

- `netherite_*` 会匹配类型以 "netherite_" 开头的任何物品或方块。
- `*_log` 会匹配类型以 "_log" 结尾的任何物品或方块。
- `*a*` 会匹配类型中任意位置包含字母 "a" 的任何物品或方块。
- `*` 会匹配所有内容。

##  {#section-5}

仅对于方块，可以在条目后的方括号 `[]` 中指定要匹配的特定[方块状态](https://minecraft.wiki/w/Block_states)。

- redstone_torch[lit=true;facing=north]
