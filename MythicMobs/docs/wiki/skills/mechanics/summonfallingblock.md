---
title: Summon Falling Block
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SummonFallingBlock
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Summon Falling Block {#summon-falling-block}

## 说明 {#description}

在目标位置召唤指定材料掉落的方块

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | types, t, material, mat, m | 下落方块的[材质](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) | DIRT |

## 示例 {#examples}

```yaml
  Skills:
  - summonfallingblock{m=ANVIL} @PlayerLocationsInRadius{r=20;y=10}
```
