# On Damaged

## Description {#description}

Executes the skill when the mob takes damage.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the entity that dealt the damage

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

## Implementations {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onDamaged)

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob takes damage
    - message{m=DAMAGED} @World ~onDamaged
```

## Aliases {#aliases}

- onHurt
