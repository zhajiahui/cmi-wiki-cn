---
title: Item Type
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ItemType
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Item Type {#item-type}

## 说明 {#description}

检查触发技能的物品的材料。   使用[物品匹配器](../../items/item-matcher.md)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| types | type, t, material, mat, m, i, item | 用于检查的[材质](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)列表。 | DIRT |
| strict | exact, e | 匹配器是否应更严格地匹配目标物品。 | false |
| vanillaonly | vanilla | 匹配的物品是否只能为原版物品。 | false |

## 示例 {#examples}

```yaml
  Conditions:
  - itemType{types=STONE,STONE_SWORD} true
```
