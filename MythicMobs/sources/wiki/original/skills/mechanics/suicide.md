# Suicide

## Description {#description}

Instantly kills the mob. This is a no-target mechanic and will only
affect the casting mob.  
This won't work on a few non-mob entities like boats or armor stands! For them, the use of [Remove](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/remove) is advised!

## Attributes {#attributes}

> *This mechanic has no attributes*

## Examples {#examples}

10% Chance to kill the casting mob when damaged.

```yaml
  Skills:
  - suicide ~onDamaged 0.1
```
