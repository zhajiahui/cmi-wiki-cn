# Setspeed

## Description {#description}

Causes the target to change its speed attribute

> The [MovementSpeed](https://wiki.mythiccraft.io/mythicmobs/Mobs/Options#movementspeed) option must be explicitly set for this to work!

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speed | a, amount, m, multiplier, s, v, value | Speed multiplier to apply to the base speed of the entity | 1 |
| type | t | Type of speed, can be `FLY` or any other string. If not exactly `FLY`, this will change walk speed | WALK |

## Examples {#examples}

This will set the mob's walking speed to 2 when it spawns

```yaml
  Skills:
  - setspeed{speed=2;type=walking} ~onSpawn
```
