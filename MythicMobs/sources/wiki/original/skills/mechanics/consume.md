# Consume

## Description {#description}

Damages each entity targeted for the given amount, and heals the casting
mob for each entity that takes damage this way.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| damage | d,dmg | The amount of damage to deal | 1 |
| heal | h | The amount of healing per mob damaged | 1 |

> This mechanic inherits every *inheritable* attribute of the [Damage](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Damage) mechanic

## Examples {#examples}

Would consume all nearby zombies, healing the boss for 20 hp for each
zombie killed.

```yaml
  Skills:
  - consume{d=1000;h=20} @MobsInRadius{type=ZOMBIE;r=20}
```
