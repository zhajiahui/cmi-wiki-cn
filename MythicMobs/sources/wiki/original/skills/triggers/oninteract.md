# Oninteract

## Description {#description}

Executes the skill when a player interacts with, or *right-clicks*, the mob.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the player that interacted with the caster

## Implementations {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onInteract)
- [MythicRPG](https://wiki.mythiccraft.io/mythicrpg/Skills/Triggers/onInteract)

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when a player right-clicks the mob
    - message{m=INTERACTED} @World ~onInteract
```
