---
title: Wearing
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/wearing
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Wearing {#wearing}

## 说明 {#description}

检查目标实体是否穿戴指定物品，使用[物品匹配器](../../items/item-matcher.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| armorslot | slot, s | 要检查的[物品槽位](../equipslot.md)。 | HEAD |
| material | mat, m, item, i, t, type, types | 要检查的材质或 MythicItem 名称。也支持 MMOItems，格式为 mmoitems.TYPE.ID。 | DIRT |
| strict | exact, e | 匹配器是否应更严格地匹配目标物品。 | false |
| vanillaonly | vanilla | 匹配的物品是否只能为原版物品。 | false |

## 示例 {#examples}

```yaml
Conditions:
  - wearing{slot=HAND;m=IRON_SWORD} true
  - wearing{slot=CHEST;m=mmoitems.TYPE.ID} true
```

## 别名 {#aliases}

- iswearing
- wielding
- iswielding
