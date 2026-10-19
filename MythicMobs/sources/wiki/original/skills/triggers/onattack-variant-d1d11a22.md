# On Attack

## Description {#description}

Executes the skill when the mob attacks an entity.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the entity that was attacked

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

## Implementations {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onAttack)

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Damage: 1
  Skills:
    # sends a message to all the players in the world
    # when the mob attacks an entity
    - message{m=ATTACK} @World ~onAttack
```

## Aliases {#aliases}

- onHit
