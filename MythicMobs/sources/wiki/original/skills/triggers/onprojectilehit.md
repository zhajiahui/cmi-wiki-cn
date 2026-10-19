# On Projectile Hit

## Description {#description}

Executes a skill when the mob's special projectile type (trident, snowball, wither skull, llama's spit etc) hits an entity.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the entity that has been hit

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

### Compatible Projectiles {#compatible-projectiles}

| Casting Entity Type | Projectile |
| --- | --- |
| BLAZE | SMALL_FIREBALL |
| ENDER_DRAGON | DRAGON_FIREBALL |
| GHAST | FIREBALL |
| LLAMA | LLAMA_SPIT |
| WITHER | WITHER_SKULL |
| DROWNED | TRIDENT |
| SNOW_GOLEM | SNOWBALL |

## Examples {#examples}

```yaml
NotYourAverageDrowned:
  Type: DROWNED
  Equipment:
    - TRIDENT HAND
  Skills:
  - modifyDamage{a=3;modifier=MULTIPLY;sync=true} ~onProjectileHit
```

## Aliases {#aliases}

- onProjectile_Hit
- onTrident_Hit
- onTridentHit
