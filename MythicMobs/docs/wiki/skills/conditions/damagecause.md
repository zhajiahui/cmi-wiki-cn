---
title: Damage Cause
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/DamageCause
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Damage Cause {#damage-cause}

## 说明 {#description}

若技能树源自 [onDamaged 触发器](../triggers/ondamaged.md)或 [onDamaged 光环](../mechanics/ondamaged.md)，检查实体受到的伤害原因。有效原因见 [Spigot DamageCause Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| damagecause | cause, c | 要匹配的伤害来源。 | ENTITY_ATTACK |

## 示例 {#examples}

```yaml
  Conditions:
  - damagecause{cause=ENTITY_ATTACK} true
```
