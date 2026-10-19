# Bound

## Description {#description}

Targets the living entities inside a region: a cuboid between two corners (the default), a sphere, or an upright cylinder. It takes the same options as the [inBounds](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/inBounds) condition, and location targeters inside it are resolved with the caster of the skill. Every living entity in the caster's world is checked.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| shape |  | `cuboid`, `sphere`, or `cylinder` | cuboid |
| corner1 | c1 | First corner of a cuboid: a location targeter, pin name, `world,x,y,z`, or `x,y,z` | NONE |
| corner2 | c2 | Second corner of a cuboid, in the same formats as `corner1` | NONE |
| x1, y1, z1 |  | Replaces that coordinate of `corner1` after it is resolved | NONE |
| x2, y2, z2 |  | Replaces that coordinate of `corner2` after it is resolved | NONE |
| location | loc, l, center, centre, origin | Center of a sphere, or the center of a cylinder's base: a location targeter, pin name, `world,x,y,z`, or `x,y,z` | NONE |
| radius | r | Radius of a sphere or cylinder | NONE |
| height | h | Height of a cylinder, measured up from `location` | NONE |

A cuboid needs `corner1` and `corner2`. A sphere needs `location` and `radius`, and a cylinder also needs `height`.

## Examples {#examples}

```yaml
  Skills:
  - ignite @bound{shape=sphere;l=@selfLocation;r=8}
  - damage{a=5} @bound{c1=arena_a;c2=arena_b;y1=-64;y2=320}
```

## Aliases {#aliases}

- bounds
