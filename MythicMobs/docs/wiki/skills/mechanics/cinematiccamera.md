---
title: Cinematic Camera
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCamera
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Cinematic Camera {#cinematic-camera}

## 说明 {#description}

为目标玩家播放平滑的过场镜头，按一系列关键帧移动视角，适合过场动画、Boss 登场和脚本演出。必须以玩家为目标。

该路径可以通过 `path` 属性从 `cutscenes/` 文件夹中的文件加载，或者使用 `points` 属性直接在机械线上定义。有关路径文件格式、[关键帧](../../cinematics.md#keyframes)、[缓动曲线](../../cinematics.md#easing-curves)、[模式](../../cinematics.md#modes)、占位符和游戏内创作命令，请参阅[动画](../../cinematics.md)页面。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| path | p, name | 在 `cutscenes/` 中定义的镜头路径名称。未设置 `points` 时必填。 |  |
| points | keyframes | 内联[关键帧](../../cinematics.md#keyframes)，以 `;` 分隔。包含多个关键帧时，必须将整个值用双引号括起来，否则第一个之后的所有关键帧都会被忽略。此项可替代 `path`。 |  |
| duration | d | 总持续时间，单位为刻，在未设置 `hold` 的各段路径之间分配。仅在使用 `points` 时生效；路径文件会自行设置时长。 | 100 |
| easing | e, curve | 未单独覆盖此项的路径段所用的默认[缓动曲线](../../cinematics.md#easing-curves)。仅在使用 `points` 时生效；路径文件会自行设置。 | EASE_IN_OUT_CUBIC |
| loop |  | 路径是否循环，直到被取消。仅在使用 `points` 时生效；路径文件会自行设置。 | false |
| maxDuration | max, maxd | 循环路径的最大时长，单位为刻，避免循环无限持续。 | 6000 |
| freezePlayer | freeze | 在持续期间使玩家无敌并锁定其移动，行走和飞行速度均为 0。 | true |
| mode | m | [`DISPLAY`](../../cinematics.md#modes)（平滑）或 `TELEPORT`（每刻传送，不进行插值）。 | DISPLAY |
| onStart | onStartSkill, os | 过场动画开始时执行的技能。使用此机制的施法者和目标执行，不会将玩家作为施法者。 |  |
| onEnd | onEndSkill, oe | 过场动画结束时执行的技能。使用此机制的施法者和目标执行，不会将玩家作为施法者。 |  |

## 示例 {#examples}

为触发玩家播放来自`cutscenes/`的命名路径。

```yaml
  Skills:
  - cinematicCamera{path=intro_pan} @trigger
```

##  {#section}

直接内联定义整条路径，包含两个关键帧和自定义缓动，持续 80 游戏刻。双引号用于将两个关键帧一同保留在 `points` 中。

```yaml
  Skills:
  - cinematicCamera{points="world,100,70,100,90,10;world,120,72,100,90,10";easing=CATMULL_ROM;duration=80} @trigger
```

##  {#section-2}

围绕 Boss 进行循环轨道，上限为60秒，并在结束时恢复玩家的HUD。 `boss_orbit` 文件集`loop: true`；技能机制自己的`loop`仅适用于`points`。

```yaml
  Skills:
  - cinematicCamera{path=boss_orbit;maxDuration=1200;onEnd=RestoreHud} @target
```

## 别名 {#aliases}

- cinecam
- camerapath
