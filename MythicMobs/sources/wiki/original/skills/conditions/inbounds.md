# In Bounds

## Description {#description}

Tests whether the target is inside a region: a cuboid between two opposite corners (the default), a sphere, or an upright cylinder. Coordinate values support placeholders and math expressions (math and placeholders in numbers require MythicMobs Premium).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| shape |  | `cuboid`, `sphere`, or `cylinder` | cuboid |
| corner1 | c1 | First corner of a cuboid. A location targeter, pin name, `world,x,y,z`, or `x,y,z`. |  |
| corner2 | c2 | Second corner of a cuboid, in the same formats as `corner1`. |  |
| x1, y1, z1 |  | Replaces that coordinate of `corner1` after it is resolved. |  |
| x2, y2, z2 |  | Replaces that coordinate of `corner2` after it is resolved. |  |
| location | loc, l, center, centre, origin | Center of a sphere, or the center of a cylinder's base. A location targeter, pin name, `world,x,y,z`, or `x,y,z`. |  |
| radius | r | Radius of a sphere or cylinder. |  |
| height | h | Height of a cylinder, measured up from `location`. |  |

A cuboid needs `corner1` and `corner2`. A sphere needs `location` and `radius`, and a cylinder also needs `height`.

When a corner is given as `x,y,z` (no world), the world of the checked location is used.

Location targeters such as `@selfLocation` are resolved against the running skill. Spawner, random spawn, and drop table conditions do not run inside a skill, so use pins or coordinates there.

## Examples {#examples}

```yaml
  Conditions:
  - inBounds{c1=-10,60,-10;c2=10,80,10} true
```

```yaml
  TargetConditions:
  - inBounds{corner1=world,0,64,0;corner2=world,32,96,32}
```

```yaml
  Conditions:
  - inBounds{c1=mypin;c2=anotherpin} true
```

```yaml
  TargetConditions:
  - inBounds{shape=sphere;l=@selfLocation;r=10}
```

```yaml
  Conditions:
  - inBounds{shape=cylinder;l=world,0,64,0;r=5;h=10} true
```

## Aliases {#aliases}

- withinBounds
- insideBounds
