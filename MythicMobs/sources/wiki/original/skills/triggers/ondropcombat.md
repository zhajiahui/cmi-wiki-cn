# Ondropcombat

## Description {#description}

Executes the skill when the mob drops combat.

> **REQUIRES [ThreatTables](https://wiki.mythiccraft.io/mythicmobs/Mobs/ThreatTables) to be enabled**

> There is no associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger)

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # sends a message to all the players in the world
    # when the mob enters combat
    - message{m=DROPPED COMBAT} @World ~onDropCombat
```

## Aliases {#aliases}

- onLeaveCombat
- onCombatDrop
- onExitCombat
