---
title: On Cinematic Start
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCinematicStart
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Cinematic Start {#on-cinematic-start}

## 说明 {#description}

当玩家的 [cinematicCamera](../mechanics/cinematiccamera.md) 镜头路径开始播放时执行技能。

> 此触发器的施法者是观看该过场镜头的玩家，没有单独关联的 [@trigger](../targeters/trigger.md)。

每次过场镜头开始播放时都会触发，无论路径来自命名文件还是内联关键帧。若只需在某个特定过场镜头开始时执行技能，应优先使用技能机制的 `onStart` 属性。

由于施法者是玩家，此触发器只执行属于该玩家的技能，例如 [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers) 物品技能或 [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/) 技能，不会执行生物的 `Skills`。如需执行生物技能，请使用技能机制的 `onStart` 属性。

## 示例 {#examples}

在 MythicCrucible 物品上，该技能会针对持有或佩戴该物品的玩家运行。

```yml
CinematicWatcher:
  Id: LEATHER_HELMET
  Skills:
  # Hide the player's bossbar UI the moment any cinematic starts
  - setVariable{var=caster.hud;value=hidden} @self ~onCinematicStart
```
