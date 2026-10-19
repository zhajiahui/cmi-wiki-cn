---
title: Holding
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/holding
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Holding {#holding}

## 说明 {#description}

检查目标是否持有给定材料。   使用[物品匹配器](../../items/item-matcher.md)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m, type, t, item, i, mat, types | 要检查的材质或 MythicItem。 |  |
| strict | exact, e | 匹配器是否应更严格地匹配目标物品。 | false |
| vanillaonly | vanilla | 匹配的物品是否只能为原版物品。 | false |

## 示例 {#examples}

```yaml
# Make sure you use all caps for materials, otherwise the console will say it is not a valid material!
Conditions:
- holding{m=DIAMOND_SWORD} true
```
