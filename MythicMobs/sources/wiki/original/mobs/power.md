# Power

**Power Level**

Skill Power is an attribute available to all skills that increases the potency of skills. Base attributes set in the mob configuration will not be affected by power levels. It is primarily used as a way to increase skill power with a mob's level, and can only be applied using [Level Modifiers](https://wiki.mythiccraft.io/mythicmobs/Mobs/Levels). Some mechanics have certain attributes that can be multiplied by power levels.

Future builds will allow you to define a scaling factor on it. In current builds it's not possible to turn off the affection of power levels when using mechanics except for the [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) and [Missile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/missile) mechanics. If you don't wish to utilize power levels simply do not use them in the level modifiers.

Mechanics that are affected by power levels + formulas:

| Mechanic | Attribute | Power Levels Effect |
| --- | --- | --- |
| [basedamage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/basedamage) | {multiplier=M} | damage = M * power |
| [consume](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/consume) | {damage=D} | damage = D * power |
| [consume](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/consume) | {heal=H} | heal = H * power |
| [damage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/damage) | {amount=A} | damage = A * power |
| [leap](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/leap) | {velocity=V} | velocity = V * ( 1 + power * 0.1 ) |
| [projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) | {velocity=V} | velocity = V * power |
| [projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) | {maxrange=MR} | maxrange = MR * power |
| [missile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/missile) | {velocity=V} | velocity = V * power |
| [missile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/missile) | {maxrange=MR} | maxrange = MR * power |

**Examples**

```
ThornySkeleton:
  Type: SKELETON
  Health: 20
  LevelModifiers:
    Health: 10
    Power: 1
  Skills:
  - damage{amount=5} @trigger ~onDamaged
```

In this example, a Level 2 ThornySkeleton has a power of 2 (base of 1, +1 from its LevelModifiers), so its skill would do 10 damage since the damage amount attribute is multiplied by its power.  
A level 3 ThornySkeleton would do 15 damage due to 3 power, and so on.
