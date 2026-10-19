---
title: Block Type In Radius
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/BlockTypeInRadius
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Block Type In Radius {#block-type-in-radius}

## 说明 {#description}

检查指定半径内特定方块的数量。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| types | type, t, material, mat, m, b, block | 用于检查的[材质](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)列表。 | DIRT |
| radius | r | 半径。 | 8 |
| amount | a | 要匹配的方块数量。 | >0 |

## 示例 {#examples}

```yaml
  TargetConditions:
  - blockTypeInRadius{type=STONE;amount=>10;radius=3} true
```
