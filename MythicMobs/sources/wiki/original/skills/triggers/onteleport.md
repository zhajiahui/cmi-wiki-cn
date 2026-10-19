# Onteleport

## Description {#description}

Executes the skill when the mob teleports.

> There is no associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger)

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: ENDERMAN
  Skills:
    # sends a message to all the players in the world
    # when the mob teleports
    - message{m=TELEPORT} @World ~onTeleport
```
