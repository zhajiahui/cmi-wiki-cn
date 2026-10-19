# On Player Exit

## Description {#description}

This Trigger has a special syntax: `~onPlayerExit{corner1=<location>;corner2=<location>}` for a cuboid, or `~onPlayerExit{shape=<sphere|cylinder>;location=<location>;radius=<number>}` for a sphere or cylinder

Executes the skill when a player moves out of a region: a cuboid between two corners (the default), a sphere, or an upright cylinder. Every player in the mob's world is checked on the mob's timer clock (the same clock that drives [onTimer](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer)), in any game mode, and the skill fires once for each player who crosses out of the region.

Each location accepts a location targeter, a pin name, `world,x,y,z`, or `x,y,z`. Targeters are resolved again on every check, with the mob as the caster, so a region built from `@selfLocation` moves with the mob. Coordinate values support placeholders and math expressions (math and placeholders in numbers require MythicMobs Premium).

Leaving the region by logging out, dying, or changing worlds does not fire this trigger. When the player comes back inside, [onPlayerEnter](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onPlayerEnter) fires again.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the player who left the region

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

Sends a message to each player who moves more than 20 blocks away from the mob:

```yml
ARENA_GUARD:
  Type: WITHER_SKELETON
  Skills:
  - message{m=Come back and fight} @trigger ~onPlayerExit{shape=sphere;location=@selfLocation;radius=20}
```

## Aliases {#aliases}

- onPlayer_Exit
- onPlayerLeave
- onPlayer_Leave
- onPlayerExitBounds
- onPlayer_Exit_Bounds
- onPlayerLeaveBounds
- onPlayer_Leave_Bounds
