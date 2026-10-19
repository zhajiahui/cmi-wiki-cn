---
title: Stringequals
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/stringequals
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Stringequals {#stringequals}

## 说明 {#description}

检查 value1 是否等于 value2。这两个值都可以使用[变量](../variables.md)和[占位符](../placeholders.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| value1 | val1, v1, string, s | 第一个值。 |  |
| value2 | val2, v2, value, val, v, equals, eq, e | 第二个值。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - stringequals{val1="yes!";val2="yes!"} true
```

```yaml
  Conditions:
  - stringequals{val1="%denizen_<player[<trigger.uuid>].item_in_hand.has_nbt[special_item]>%";val2="true"} true
```

使用 Denizen、PlaceholderAPI 和 MythicMobs 检查玩家持有的物品是否具有“special_item”的 Denizen NBT 键。 <trigger.uuid> 是一个 MythicMobs 占位符，在 PlaceholderAPI 解析 Denizen 标签之前进行解析。

```yaml
  Conditions:
  - stringequals{val1="%denizen_<player[<trigger.uuid>].item_in_hand.raw_nbt.get[mythic_type].after[string:]>%";val2="SomeMythicItem"} true
```

## 别名 {#aliases}

- stringEq
