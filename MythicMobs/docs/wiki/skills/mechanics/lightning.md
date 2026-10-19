---
title: Lightning
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/lightning
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Lightning {#lightning}

## 说明 {#description}

在目标实体或位置召唤闪电并造成伤害。如果当前没有下雨，且已开启火焰蔓延，还可能点燃目标实体或方块。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| damage | d | 雷击造成的伤害量。 | 0.01337 |

> 此机制继承 [Damage](damage.md) 机制的所有*可继承*属性。

## 示例 {#examples}

此示例将向指定的目标召唤一道闪电。

```yaml
StaticSheep:
  Type: SHEEP
  Skills:
  - lightning @EntitiesInRadius{r=10} ~onTimer:100
```

##  {#section}

此示例将向指定目标召唤一道闪电并造成 6 伤害。

```yaml
StaticSheep:
  Type: SHEEP
  Skills:
  - lightning{d=6} @EntitiesInRadius{r=10} ~onTimer:100
```
