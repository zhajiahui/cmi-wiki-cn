# Onchangetarget

## Description {#description}

Executes the skill when the mob changes target.

> **REQUIRES [ThreatTables](https://wiki.mythiccraft.io/mythicmobs/Mobs/ThreatTables) to be enabled**

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # sends a message to all the players in the world
    # when the mob's target changes
    - message{m=Target Changed} @World ~onChangeTarget
```

## Aliases {#aliases}

- onTargetChange
