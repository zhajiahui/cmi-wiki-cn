# On Cinematic Start

## Description {#description}

Executes the skill when a [cinematicCamera](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCamera) path begins playing on a player.

> The caster of this trigger is the player the cinematic is playing for. There is no separate associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger).

This trigger fires for every cinematic start, regardless of whether the path was started from a named file or from inline keyframes. To run a skill only for one specific cinematic, prefer the mechanic's `onStart` attribute instead.

Because the caster is the player, this trigger only runs skills that belong to that player, such as [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers) item skills or [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/) skills. It never runs a mob's `Skills`; for those, use the mechanic's `onStart` attribute.

## Examples {#examples}

On a MythicCrucible item, the skill runs for the player holding or wearing it.

```yml
CinematicWatcher:
  Id: LEATHER_HELMET
  Skills:
  # Hide the player's bossbar UI the moment any cinematic starts
  - setVariable{var=caster.hud;value=hidden} @self ~onCinematicStart
```
