# On Shoot

## Description {#description}

Executes the skill when the mob shoots a projectile.  
For example, skeletons with bows will shoot arrows; ghasts, blazes, or ender dragon will shoot some type of fireball.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the caster

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.bow-tension>` |

## Implementations {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onShoot)
- [MythicRPG](https://wiki.mythiccraft.io/mythicrpg/Skills/Triggers/onShoot)

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: SKELETON
  Skills:
    # sends a message to all the players in the world
    # when the skeleton shoots from a bow
    - message{m=I SHOT AN ARROW} @World ~onShoot
```

## Aliases {#aliases}

- onBowShoot
- onShootBow
