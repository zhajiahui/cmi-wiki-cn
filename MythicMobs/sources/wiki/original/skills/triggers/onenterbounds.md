# On Enter Bounds

## Description {#description}

This Trigger has a special syntax: `~onEnterBounds{corner1=<location>;corner2=<location>}` for a cuboid, or `~onEnterBounds{shape=<sphere|cylinder>;location=<location>;radius=<number>}` for a sphere or cylinder

Executes the skill when the mob moves into a region: a cuboid between two corners (the default), a sphere, or an upright cylinder. The mob's position is checked on its timer clock (the same clock that drives [onTimer](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer)), and the skill fires once when the mob crosses into the region, not repeatedly while it stays inside. A mob that spawns already inside the region fires this trigger on its first check.

Each location accepts a location targeter such as `@CasterSpawnLocation`, a pin name, `world,x,y,z`, or `x,y,z` (the world of the mob's location is used for the three-value form). Targeters are resolved again on every check, with the mob as the caster. Coordinate values support placeholders and math expressions (math and placeholders in numbers require MythicMobs Premium). Both corners must be in the same world.

To run a skill when a player enters a region, use [onPlayerEnter](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onPlayerEnter).

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the mob itself

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

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob walks into the region between the two corners
    - message{m=Entered the arena} @World ~onEnterBounds{corner1=world,100,64,100;corner2=world,120,80,120}
```

The same for a cylinder with a radius of 5 and a height of 6, standing on `0,64,0`:

```yml
  Skills:
  - message{m=The chicken reached the altar} @World ~onEnterBounds{shape=cylinder;location=world,0,64,0;radius=5;height=6}
```

## Aliases {#aliases}

- onEnter_Bounds
- onBoundsEnter
- onBounds_Enter
