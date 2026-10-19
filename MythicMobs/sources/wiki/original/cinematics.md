# Cinematics

The cinematic camera system plays smooth, scripted camera paths for a specific player — useful for cutscenes, boss intros, and scripted reveals. A path is a series of keyframes (position + yaw + pitch) that the player's view is interpolated along.

Paths are played with the [cinematicCamera](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCamera) mechanic, either from a file in the `cutscenes/` folder or from inline keyframes. While a cinematic is playing you can query its state with the [cinematic placeholders](https://wiki.mythiccraft.io/mythicmobs/Cinematics#placeholders) and the [isInCinematic](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/IsInCinematic) condition, and react to it with the [onCinematicStart](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCinematicStart) / [onCinematicEnd](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCinematicEnd) triggers.

1. [Path Files](https://wiki.mythiccraft.io/mythicmobs/Cinematics#path-files)
2. [Keyframes](https://wiki.mythiccraft.io/mythicmobs/Cinematics#keyframes)
3. [Easing Curves](https://wiki.mythiccraft.io/mythicmobs/Cinematics#easing-curves)
4. [Modes](https://wiki.mythiccraft.io/mythicmobs/Cinematics#modes)
5. [Mechanics](https://wiki.mythiccraft.io/mythicmobs/Cinematics#mechanics)
   1. [cinematicCamera](https://wiki.mythiccraft.io/mythicmobs/Cinematics#cinematiccamera)
   2. [cinematicCancel](https://wiki.mythiccraft.io/mythicmobs/Cinematics#cinematiccancel)
6. [Condition](https://wiki.mythiccraft.io/mythicmobs/Cinematics#condition)
   1. [isInCinematic](https://wiki.mythiccraft.io/mythicmobs/Cinematics#isincinematic)
7. [Triggers](https://wiki.mythiccraft.io/mythicmobs/Cinematics#triggers)
8. [Placeholders](https://wiki.mythiccraft.io/mythicmobs/Cinematics#placeholders)
9. [Commands](https://wiki.mythiccraft.io/mythicmobs/Cinematics#commands)
10. [Examples](https://wiki.mythiccraft.io/mythicmobs/Cinematics#examples)

## Path Files {#path-files}

Camera paths are YAML files placed in `plugins/MythicMobs/cutscenes/`. They are also discovered inside packs at `plugins/MythicMobs/packs/<PackName>/cutscenes/`. The file name does not matter; paths are referenced by their top-level id.

```yaml
my_path_id:
  duration: 100              # total ticks
  loop: false               # repeat until cancelled
  easing: EASE_IN_OUT_CUBIC # default leg easing
  points:
    - "world,x,y,z,yaw,pitch[,hold[,easing]]"
    - "~,dx,dy,dz,yaw,pitch[,hold[,easing]]"   # ~ = relative to the anchor
```

A path can then be played with `cinematicCamera{path=my_path_id} @target`.

| Key | Description | Default |
| --- | --- | --- |
| duration | Total length of the path in ticks. Legs with a `hold` keep it and the remaining ticks are split evenly across the other legs. Ignored when every leg has a `hold`. | 100 |
| loop | Whether the path repeats until cancelled, or until the mechanic's `maxDuration` (6000 ticks by default) runs out. | false |
| easing | Default [easing curve](https://wiki.mythiccraft.io/mythicmobs/Cinematics#easing-curves) for legs that do not override it. | EASE_IN_OUT_CUBIC |
| points | The list of [keyframes](https://wiki.mythiccraft.io/mythicmobs/Cinematics#keyframes). |  |

## Keyframes {#keyframes}

Each keyframe is `world,x,y,z,yaw,pitch`, with two optional trailing fields: `hold` and `easing`.

- **Absolute** points start with any loaded world name: `world,100,70,100,90,10`
- **Relative** points start with `~`, and treat `x/y/z` as offsets from the cinematic's **anchor**: `~,0,5,-10,0,30`. The anchor is the skill's origin (the [@origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Origin)), which is normally the caster's location. Relative paths let one cutscene be reused anywhere.
- **`hold`** is the leg duration in ticks *from this point to the next* (`0` means no hold). Legs with a `hold` keep it and the rest of `duration` is split evenly across the other legs. When every leg has a `hold`, `duration` is ignored. A `hold` on the last point does nothing, since no leg leaves it.
- **`easing`** on a point overrides the path-level easing for the leg leaving that point. For example a single `STEP` leg can cut sharply through an otherwise `CATMULL_ROM` path.

When using the inline `points` attribute on the mechanic, separate keyframes with `;` and wrap the whole value in double quotes. Without the quotes the first `;` ends the `points` attribute, the other keyframes are ignored, and the camera stays on the first keyframe.

```yaml
points="world,100,70,100,90,10,40;~,0,3,-8,90,10,40,LINEAR"
```

## Easing Curves {#easing-curves}

The `easing` value (path-level, per-point, or the mechanic's `easing` attribute) accepts any of the following:

`LINEAR`, `EASE_IN_QUAD`, `EASE_OUT_QUAD`, `EASE_IN_OUT_QUAD`, `EASE_IN_CUBIC`, `EASE_OUT_CUBIC`, `EASE_IN_OUT_CUBIC`, `EASE_IN_SINE`, `EASE_OUT_SINE`, `EASE_IN_OUT_SINE`, `SMOOTHSTEP`, `SMOOTHERSTEP`, `CATMULL_ROM`, `STEP`

`STEP` holds the camera on the leg's first point, then cuts to the next point when the leg ends. `CATMULL_ROM` curves through the neighbouring points and only works as a path's default easing (the path file's `easing` or the mechanic's `easing`); set on a single point it acts like `LINEAR`. An unrecognised value falls back to `EASE_IN_OUT_CUBIC`, or, on a point, to the path's easing.

## Modes {#modes}

- **DISPLAY** (default) spawns a packet-only camera entity and spectates it, producing smooth interpolated motion.
- **TELEPORT** teleports the player every tick instead. It has no interpolation between ticks but is a reliable fallback.

DISPLAY needs Paper. When the server cannot use it (for example Spigot, or Paper 1.20.1), the console logs an error and the path plays in TELEPORT mode.

## Mechanics {#mechanics}

### cinematicCamera {#cinematiccamera}

Plays a cinematic camera path for the target player. See the [cinematicCamera](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCamera) page for the full attribute list. The mechanic must target a player.

```yaml
  Skills:
  - cinematicCamera{path=intro_pan} @trigger
```

### cinematicCancel {#cinematiccancel}

Interrupts an active cinematic for the target player, immediately returning their camera and control. See the [cinematicCancel](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCancel) page.

```yaml
  Skills:
  - cinematicCancel @trigger
```

## Condition {#condition}

### isInCinematic {#isincinematic}

Checks if the target player is currently in an active cinematic. See the [isInCinematic](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/IsInCinematic) page.

## Triggers {#triggers}

Both triggers fire with the player the cinematic is playing for as the caster, so they only run skills that belong to that player, such as [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers) item skills or [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/) skills. They never run a mob's `Skills`. To run a mob's skill when a cinematic starts or ends, use the mechanic's `onStart` and `onEnd` attributes.

- [onCinematicStart](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCinematicStart) — fires when a path begins playing on a player.
- [onCinematicEnd](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCinematicEnd) — fires when a path ends, however it ends (natural finish, [cinematicCancel](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCancel), player quit, or player death).

## Placeholders {#placeholders}

These [entity-scoped placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders) report the cinematic state of any player. Prefix them with a scope such as `caster.` or `target.`:

| Placeholder | Description |
| --- | --- |
| `<caster.cinematic.active>` | `true` / `false` — whether the player is in a cinematic |
| `<caster.cinematic.frame>` | Ticks played since the cinematic started, or `-1` if the player is not in a cinematic |
| `<caster.cinematic.progress>` | Progress from `0.0` to `1.0` (a looping path stays at `1.0` after its first pass), or `0.0` if not in a cinematic |

## Commands {#commands}

Camera paths can be authored in-game with the `/mm camera` command, which captures your current position, yaw, and pitch as a keyframe. The path must already exist in a path file with at least one point; the command edits that file and does not create new paths. Requires the `mythicmobs.command.camera` permission. See [Commands and Permissions](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions#camera-commands) for the full syntax.

- **/mm camera <pathId> add [index] [hold=N] [easing=NAME] [relative=true]** — adds a keyframe at your current location.
- **/mm camera <pathId> remove [index]** — removes the keyframe at the given index (the last one if omitted).

## Examples {#examples}

A boss intro: freeze the triggering player, orbit the boss for 80 ticks, then run a skill when it ends.

```yaml
BossIntro:
  Skills:
  - cinematicCamera{path=boss_orbit;freezePlayer=true;onEnd=BossRoar} @trigger
```
