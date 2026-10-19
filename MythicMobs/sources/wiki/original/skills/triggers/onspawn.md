# On Spawn

## Description {#description}

Executes the skill when the mob spawns.

> There is no associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger)

## Implementations {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onSpawn)
- [MythicRPG](https://wiki.mythiccraft.io/mythicrpg/Skills/Triggers/onSpawn)

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob spawns
    - message{m=SPAWN} @World ~onSpawn
```
