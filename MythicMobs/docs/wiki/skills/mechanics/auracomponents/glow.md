---
title: Glow
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/Glow
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Glow {#glow}

## 说明 {#description}

使目标实体发光（就像发光药水效果一样）。

> 请注意，这个机制实际上并没有以任何形式提供“发光”效果：它只是“看起来”像这样。如果你想检查此机制是否存在，则必须检查所应用的光环是否存在（例如，[hasaura](../../conditions/hasaura.md) 条件就可以做到这一点）

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c | 实体发光时使用的[颜色](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Color.html)。 | white |
| audience |  | 发光效果的[可见对象](../../audience.md)。 | nearby |

## 别名 {#aliases}

- e:glow
- effect:glow
