# Projectile Velocity

## Description {#description}

Modifies the velocity of the calling [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) or [Missile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/missile). In this context, it works the same as the [Velocity](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/velocity) mechanic.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| mode | m | The operation to perform. Can be SET, ADD, REMOVE, DIVIDE, or MULTIPLY. | SET |
| velocityx | vx, x | Velocity on the x-axis. Can be negative. | 1 |
| velocityy | vy, y | Velocity on the y-axis. Can be negative. | 1 |
| velocityz | vz, z | Velocity on the z-axis. Can be negative. | 1 |
| relative | r | If the change in velocity should be relative to the projectile's facing direction. In this instance, the `z` axis becomes `forward/backward`, `y` becomes `up/down` and `x` becomes `left/right` | true |

## Examples {#examples}

```yaml
Projectile-onTick:
  Conditions:
  - chance{chance=0.1} true
  Skills:
  - projectilevelocity{mode=ADD;vz=0.3}
```

## Aliases {#aliases}

- pvelocity
