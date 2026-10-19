---
title: Attribute Modifier
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/AttributeModifier
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Attribute Modifier {#attribute-modifier}

## 说明 {#description}

为可拥有属性的目标添加属性修饰符，不应对玩家使用。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| attribute | attr | [属性](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html) | GENERIC_LUCK |
| operation | op | 要执行的[运算](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/AttributeModifier.Operation.html)。 | ADD_NUMBER |
| name | modifierName | 修饰符名称。 | <caster.uuid> |
| amount | amt, a | 属性的修饰值。 | 0 |
| duration | dur | 属性的持续时间。 | 0 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - attributeModifier{attribute=GENERIC_LUCK;a=2;dur=1200;op=ADD_NUMBER} @trigger ~onDeath
```
