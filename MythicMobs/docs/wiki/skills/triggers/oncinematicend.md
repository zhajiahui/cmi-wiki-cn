---
title: On Cinematic End
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCinematicEnd
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Cinematic End {#on-cinematic-end}

## 说明 {#description}

当玩家的 [cinematicCamera](../mechanics/cinematiccamera.md) 镜头路径停止播放时执行技能。

> 此触发器的施法者是观看该过场镜头的玩家，没有单独关联的 [@trigger](../targeters/trigger.md)。

无论过场镜头以何种方式结束，都会触发此事件：路径正常播放完毕、被 [cinematicCancel](../mechanics/cinematiccancel.md) 中断、玩家退出或玩家死亡。每次过场镜头都会执行一次，因此适合在这里恢复界面、效果和控制等状态。若只需在某个特定过场镜头结束时执行技能，应优先使用技能机制的 `onEnd` 属性。

由于施法者是玩家，此触发器只执行属于该玩家的技能，例如 [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers) 物品技能或 [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/) 技能，不会执行生物的 `Skills`。如需执行生物技能，请使用技能机制的 `onEnd` 属性。

## 示例 {#examples}

在 MythicCrucible 物品上，该技能会针对持有或佩戴该物品的玩家运行。

```yml
CinematicWatcher:
  Id: LEATHER_HELMET
  Skills:
  # Restore the player's HUD whenever their cinematic ends, however it ends
  - setVariable{var=caster.hud;value=shown} @self ~onCinematicEnd
```
