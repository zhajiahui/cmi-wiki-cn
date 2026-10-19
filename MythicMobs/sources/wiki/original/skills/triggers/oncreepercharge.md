# Oncreepercharge

## Description {#description}

Executes the skill when the casting creeper is charged.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the caster itself

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # sends a message to all the players in the world
    # when the mob gets charge
    - message{m=CHARGED} @World ~onCreeperCharge
```

## Aliases {#aliases}

- onCreeper_Charge
- onCharged
- onCharge
