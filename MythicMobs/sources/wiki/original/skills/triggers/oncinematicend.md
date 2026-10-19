# On Cinematic End

## Description {#description}

Executes the skill when a [cinematicCamera](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCamera) path stops playing on a player.

> The caster of this trigger is the player the cinematic was playing for. There is no separate associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger).

This fires no matter how the cinematic ended: when the path finishes naturally, when it is interrupted by [cinematicCancel](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCancel), when the player quits, or when the player dies. It is the reliable place to restore state (UI, effects, control) since it always runs once per cinematic. To run a skill only for one specific cinematic, prefer the mechanic's `onEnd` attribute instead.

Because the caster is the player, this trigger only runs skills that belong to that player, such as [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers) item skills or [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/) skills. It never runs a mob's `Skills`; for those, use the mechanic's `onEnd` attribute.

## Examples {#examples}

On a MythicCrucible item, the skill runs for the player holding or wearing it.

```yml
CinematicWatcher:
  Id: LEATHER_HELMET
  Skills:
  # Restore the player's HUD whenever their cinematic ends, however it ends
  - setVariable{var=caster.hud;value=shown} @self ~onCinematicEnd
```
