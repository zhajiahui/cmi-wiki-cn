---
title: Has Enchantment
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HasEnchantment
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Has Enchantment {#has-enchantment}

## 说明 {#description}

检查目标实体的装备是否带有附魔。有效附魔见 [Spigot Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/enchantments/Enchantment.html)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| enchantment | type, ench, e, t | 要检测的附魔。 | ANY |
| level | lvl, l | 要检测的等级。 | >0 |

## 示例： {#examples}

```yaml
  TargetConditions:
  - hasenchantment{e=DAMAGE_ALL;l=>3} true
```

## 别名 {#aliases}

- hasEnchant
