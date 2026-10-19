---
title: Lastdamagecause
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lastdamagecause
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Lastdamagecause {#lastdamagecause}

## 说明 {#description}

检查目标最后一次受到伤害的原因。有效原因列表见 [Spigot Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| damagecause | cause, c | 要匹配的伤害来源。 | ENTITY_ATTACK |

## 示例 {#examples}

```yaml
  Conditions:
  - lastdamagecause{c=ENTITY_ATTACK} true
```
