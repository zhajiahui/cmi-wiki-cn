# On Bow Hit

## Description {#description}

Executes a skill when the mob's projectile hits an entity.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the entity that has been hit

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

## Implementations {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onBowHit)

## Examples {#examples}

```yaml
NotYourAverageSkeleton:
  Type: SKELETON
  Equipment:
    - BOW HAND
  Skills:
  - modifyDamage{a=3;modifier=MULTIPLY;sync=true} ~onBowHit
```

## Aliases {#aliases}

- onBow_Hit
- onArrowHit
