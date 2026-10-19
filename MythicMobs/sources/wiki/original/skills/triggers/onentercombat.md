# Onentercombat

## Description {#description}

Executes the skill when the mob enters combat.

> **REQUIRES [ThreatTables](https://wiki.mythiccraft.io/mythicmobs/Mobs/ThreatTables) to be enabled**

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the entity that made the caster enter combat

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # sends a message to all the players in the world
    # when the mob enters combat
    - message{m=ENTERED COMBAT} @World ~onEnterCombat
```
