---
title: On Projectile Hit
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onProjectileHit
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Projectile Hit {#on-projectile-hit}

## 说明 {#description}

生物的特殊弹射物（三叉戟、雪球、凋灵之首、羊驼的唾沫等）击中实体时执行技能。

> 关联的[@trigger](../targeters/trigger.md)是被击中的实体

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

### 兼容的投射物 {#compatible-projectiles}

| 施法实体类型 | 投射物 |
| --- | --- |
| BLAZE | SMALL_FIREBALL |
| ENDER_DRAGON | DRAGON_FIREBALL |
| GHAST | FIREBALL |
| LLAMA | LLAMA_SPIT |
| WITHER | WITHER_SKULL |
| DROWNED | TRIDENT |
| SNOW_GOLEM | SNOWBALL |

## 示例 {#examples}

```yaml
NotYourAverageDrowned:
  Type: DROWNED
  Equipment:
    - TRIDENT HAND
  Skills:
  - modifyDamage{a=3;modifier=MULTIPLY;sync=true} ~onProjectileHit
```

## 别名 {#aliases}

- onProjectile_Hit
- onTrident_Hit
- onTridentHit
