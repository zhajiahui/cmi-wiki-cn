# Onplayerkill

## Description {#description}

Executes the skill when the mob kills a player.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the player that has been killed

## Implementations {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onKillPlayer)

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob kills a player
    - message{m=PLAYER KILLED} @World ~onPlayerKill
```

## Aliases {#aliases}

- onKillPlayer
