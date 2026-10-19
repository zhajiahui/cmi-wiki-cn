# On Exit Bounds

## Description {#description}

This Trigger has a special syntax: `~onExitBounds{corner1=<location>;corner2=<location>}` for a cuboid, or `~onExitBounds{shape=<sphere|cylinder>;location=<location>;radius=<number>}` for a sphere or cylinder

Executes the skill when the mob moves out of a region: a cuboid between two corners (the default), a sphere, or an upright cylinder. The mob's position is checked on its timer clock (the same clock that drives [onTimer](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer)), and the skill fires once when the mob crosses out of the region, not repeatedly while it stays outside.

Each location accepts a location targeter such as `@CasterSpawnLocation`, a pin name, `world,x,y,z`, or `x,y,z` (the world of the mob's location is used for the three-value form). Targeters are resolved again on every check, with the mob as the caster. Coordinate values support placeholders and math expressions (math and placeholders in numbers require MythicMobs Premium). Both corners must be in the same world.

To run a skill when a player leaves a region, use [onPlayerExit](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onPlayerExit).

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
    # when the mob leaves the region between the two corners
    - message{m=Left the arena} @World ~onExitBounds{corner1=world,100,64,100;corner2=world,120,80,120}
```

Teleports the mob back to where it spawned when it wanders more than 20 blocks away:

```yml
  Skills:
  - teleport @CasterSpawnLocation ~onExitBounds{shape=sphere;location=@CasterSpawnLocation;radius=20}
```

## Aliases {#aliases}

- onExit_Bounds
- onLeaveBounds
- onLeave_Bounds
- onBoundsExit
- onBounds_Exit
