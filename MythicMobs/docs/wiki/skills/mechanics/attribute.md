---
title: Attribute
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Attribute
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Attribute {#attribute}

## 说明 {#description}

设置目标实体的[属性](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html)的基础值。不应该用于玩家。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| attribute | attr | 要设置的[属性](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html)。 | GENERIC_LUCK |
| amount | amt, a | 属性的数值。 | 0 |
| duration | dur | 属性的持续时间。 | 0 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - attribute{attribute=GENERIC_LUCK;a=2;duration=1200} @trigger ~onDeath
```

## 别名 {#aliases}

- setattribute
