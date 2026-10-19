# Cinematic Camera

## Description {#description}

Plays a smooth cinematic camera path for the target player, moving their view along a series of keyframes. Useful for cutscenes, boss intros, and scripted reveals. The mechanic must target a player.

The path can be loaded from a file in the `cutscenes/` folder via the `path` attribute, or defined directly on the mechanic line with the `points` attribute. See the [Cinematics](https://wiki.mythiccraft.io/mythicmobs/Cinematics) page for the path-file format, [keyframes](https://wiki.mythiccraft.io/mythicmobs/Cinematics#keyframes), [easing curves](https://wiki.mythiccraft.io/mythicmobs/Cinematics#easing-curves), [modes](https://wiki.mythiccraft.io/mythicmobs/Cinematics#modes), placeholders, and the in-game authoring command.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| path | p, name | Name of a camera path defined under `cutscenes/`. Required if `points` is not set. |  |
| points | keyframes | Inline [keyframes](https://wiki.mythiccraft.io/mythicmobs/Cinematics#keyframes), separated by `;`. Wrap the value in double quotes when it has more than one keyframe, or every keyframe after the first is ignored. Alternative to `path`. |  |
| duration | d | Total duration in ticks, split across the legs that have no `hold`. Only used with `points`; a path file sets its own. | 100 |
| easing | e, curve | Default [easing curve](https://wiki.mythiccraft.io/mythicmobs/Cinematics#easing-curves) for legs that do not override it. Only used with `points`; a path file sets its own. | EASE_IN_OUT_CUBIC |
| loop |  | Whether the path repeats until cancelled. Only used with `points`; a path file sets its own. | false |
| maxDuration | max, maxd | Safety cap in ticks for looping paths, so a loop can never run forever. | 6000 |
| freezePlayer | freeze | Makes the player invulnerable and locks their movement (walk/fly speed 0) for the duration. | true |
| mode | m | [`DISPLAY`](https://wiki.mythiccraft.io/mythicmobs/Cinematics#modes) (smooth) or `TELEPORT` (per-tick teleport, no interpolation). | DISPLAY |
| onStart | onStartSkill, os | Skill executed when the cinematic begins. It runs with this mechanic's caster and targets, not with the player as caster. |  |
| onEnd | onEndSkill, oe | Skill executed when the cinematic ends. It runs with this mechanic's caster and targets, not with the player as caster. |  |

## Examples {#examples}

Plays a named path from `cutscenes/` for the triggering player.

```yaml
  Skills:
  - cinematicCamera{path=intro_pan} @trigger
```

##  {#section}

Defines the whole path inline with two keyframes and a custom easing, lasting 80 ticks. The double quotes keep both keyframes inside `points`.

```yaml
  Skills:
  - cinematicCamera{points="world,100,70,100,90,10;world,120,72,100,90,10";easing=CATMULL_ROM;duration=80} @trigger
```

##  {#section-2}

Plays a looping orbit around the boss, capped at 60 seconds, and restores the player's HUD when it ends. The `boss_orbit` file sets `loop: true`; the mechanic's own `loop` only applies to `points`.

```yaml
  Skills:
  - cinematicCamera{path=boss_orbit;maxDuration=1200;onEnd=RestoreHud} @target
```

## Aliases {#aliases}

- cinecam
- camerapath
