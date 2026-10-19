---
title: 过场动画
source_url: https://wiki.mythiccraft.io/mythicmobs/Cinematics
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 过场动画 {#cinematics}

镜头动画系统可以为指定玩家播放由脚本控制的平滑镜头路径，适用于过场动画、Boss 登场和剧情揭示。路径由一系列关键帧组成，每个关键帧包含位置、偏航角和俯仰角，玩家视角会沿这些关键帧进行插值移动。

使用 [cinematicCamera](skills/mechanics/cinematiccamera.md) 技能机制播放路径，路径既可以来自 `cutscenes/` 文件夹中的文件，也可以使用行内关键帧。动画播放期间，可通过[镜头动画占位符](cinematics.md#placeholders)和 [isInCinematic](skills/conditions/isincinematic.md) 条件查询其状态，并通过 [onCinematicStart](skills/triggers/oncinematicstart.md) / [onCinematicEnd](skills/triggers/oncinematicend.md) 触发器响应播放事件。

1. [路径文件](cinematics.md#path-files)
2. [关键帧](cinematics.md#keyframes)
3. [缓动曲线](cinematics.md#easing-curves)
4. [模式](cinematics.md#modes)
5. [机制](cinematics.md#mechanics)
   1. [cinematicCamera](cinematics.md#cinematiccamera)
   2. [cinematicCancel](cinematics.md#cinematiccancel)
6. [条件](cinematics.md#condition)
   1. [isInCinematic](cinematics.md#isincinematic)
7. [触发器](cinematics.md#triggers)
8. [占位符](cinematics.md#placeholders)
9. [命令](cinematics.md#commands)
10. [示例](cinematics.md#examples)

## 路径文件 {#path-files}

镜头路径使用 YAML 文件，放在 `plugins/MythicMobs/cutscenes/` 中。插件也会查找内容包中的 `plugins/MythicMobs/packs/<PackName>/cutscenes/`。文件名可以任意设置，引用路径时使用其顶层 id。

```yaml
my_path_id:
  duration: 100              # total ticks
  loop: false               # repeat until cancelled
  easing: EASE_IN_OUT_CUBIC # default leg easing
  points:
    - "world,x,y,z,yaw,pitch[,hold[,easing]]"
    - "~,dx,dy,dz,yaw,pitch[,hold[,easing]]"   # ~ = relative to the anchor
```

随后可以通过 `cinematicCamera{path=my_path_id} @target` 播放路径。

| 配置键 | 说明 | 默认值 |
| --- | --- | --- |
| duration | 路径的总时长，以刻为单位。设置了 `hold` 的路径段保留其时长，剩余刻数平均分配给其他路径段。所有路径段都设置了 `hold` 时忽略此项。 | 100 |
| loop | 路径是否循环播放，直到取消或达到此机制的 `maxDuration`（默认为 6000 刻）。 | false |
| easing | 未覆盖此设置的路径段使用的默认[缓动曲线](cinematics.md#easing-curves)。 | EASE_IN_OUT_CUBIC |
| points | [关键帧](cinematics.md#keyframes)列表。 |  |

## 关键帧 {#keyframes}

每个关键帧采用 `world,x,y,z,yaw,pitch` 格式，末尾还可以附加两个可选字段：`hold` 和 `easing`。

- **绝对位置**以任意已加载世界的名称开头，例如 `world,100,70,100,90,10`。
- **相对位置**以 `~` 开头，将 `x/y/z` 视为相对于镜头动画**锚点**的偏移，例如 `~,0,5,-10,0,30`。锚点是技能原点（[@origin](skills/targeters/origin.md)），通常位于施法者的位置。相对路径让同一段过场动画可以在任意地点重复使用。
- 关键帧上的 **`hold`** 表示*从该点到下一点*这一段的持续时间，单位为游戏刻（`0` 表示不指定持续时间）。设置了 `hold` 的路径段使用该值，其余 `duration` 会平均分配给其他路径段。如果每一段都设置了 `hold`，则忽略 `duration`。最后一个关键帧后面没有路径段，因此在该点设置 `hold` 无效。
- 关键帧上的 **`easing`** 会覆盖从该点出发的路径段所使用的路径级缓动设置。例如，整条路径使用 `CATMULL_ROM` 时，可以让其中一段使用 `STEP` 实现直接切换。

在技能机制上使用行内 `points` 属性时，用 `;` 分隔关键帧，并用双引号括起整个值。不加引号时，第一个 `;` 会结束 `points` 属性，后面的关键帧会被忽略，镜头也会停在第一个关键帧。

```yaml
points="world,100,70,100,90,10,40;~,0,3,-8,90,10,40,LINEAR"
```

## 缓动曲线 {#easing-curves}

`easing` 的值，无论设置在路径级别、单个关键帧还是技能机制的 `easing` 属性中，都可以使用以下任一值：

`LINEAR`, `EASE_IN_QUAD`, `EASE_OUT_QUAD`, `EASE_IN_OUT_QUAD`, `EASE_IN_CUBIC`, `EASE_OUT_CUBIC`, `EASE_IN_OUT_CUBIC`, `EASE_IN_SINE`, `EASE_OUT_SINE`, `EASE_IN_OUT_SINE`, `SMOOTHSTEP`, `SMOOTHERSTEP`, `CATMULL_ROM`, `STEP`

`STEP` 会让镜头停在路径段的起点，直到该段结束后直接切到下一点。`CATMULL_ROM` 会沿相邻关键帧形成曲线，仅可作为路径的默认缓动方式，也就是路径文件的 `easing` 或技能机制的 `easing`；若只为某个关键帧设置，则按 `LINEAR` 处理。无法识别的值会回退为 `EASE_IN_OUT_CUBIC`；若该值设置在关键帧上，则回退为路径的缓动方式。

## 模式 {#modes}

- **DISPLAY**（默认）会生成一个仅通过数据包呈现的镜头实体，并让玩家旁观该实体，从而实现平滑的插值移动。
- **TELEPORT** 则每个游戏刻传送玩家一次。游戏刻之间没有插值，但可以作为可靠的备用模式。

DISPLAY 需要 Paper。如果服务器无法使用此模式，例如运行 Spigot 或 Paper 1.20.1，控制台会记录错误，并改用 TELEPORT 模式播放路径。

## 技能机制 {#mechanics}

### cinematicCamera {#cinematiccamera}

为目标玩家播放镜头动画路径。完整属性列表见 [cinematicCamera](skills/mechanics/cinematiccamera.md) 页面。此技能机制必须以玩家为目标。

```yaml
  Skills:
  - cinematicCamera{path=intro_pan} @trigger
```

### cinematicCancel {#cinematiccancel}

中断目标玩家正在播放的镜头动画，立即归还视角和控制权。参见 [cinematicCancel](skills/mechanics/cinematiccancel.md) 页面。

```yaml
  Skills:
  - cinematicCancel @trigger
```

## 条件 {#condition}

### isInCinematic {#isincinematic}

检查目标玩家当前是否正在播放镜头动画。参见 [isInCinematic](skills/conditions/isincinematic.md) 页面。

## 触发器 {#triggers}

这两个触发器都会将正在观看动画的玩家作为施法者，因此只会运行属于该玩家的技能，例如 [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers) 物品技能或 [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/) 技能，不会运行生物的 `Skills`。要在动画开始或结束时运行生物技能，应使用技能机制的 `onStart` 和 `onEnd` 属性。

- [onCinematicStart](skills/triggers/oncinematicstart.md)：开始为玩家播放路径时触发。
- [onCinematicEnd](skills/triggers/oncinematicend.md)：路径结束时触发，无论是自然播放完毕、通过 [cinematicCancel](skills/mechanics/cinematiccancel.md) 中断，还是玩家退出或死亡。

## 占位符 {#placeholders}

这些[实体作用域占位符](skills/placeholders.md)可以查询任意玩家的镜头动画状态。使用时添加 `caster.` 或 `target.` 等作用域前缀：

| 占位符 | 说明 |
| --- | --- |
| `<caster.cinematic.active>` | `true` / `false`——玩家是否处于过场动画中 |
| `<caster.cinematic.frame>` | 过场动画开始后已播放的刻数；玩家不在过场动画中时为 `-1` |
| `<caster.cinematic.progress>` | 从 `0.0` 到 `1.0` 的进度（循环路径在首次播放完成后保持为 `1.0`）；玩家不在过场动画中时为 `0.0` |

## 命令 {#commands}

可以在游戏中通过 `/mm camera` 命令编辑镜头路径，将当前位置、偏航角和俯仰角保存为关键帧。路径必须已存在于某个路径文件中，且至少包含一个关键帧；该命令只编辑已有文件，不会创建新路径。需要 `mythicmobs.command.camera` 权限。完整语法见[命令与权限](commands-and-permissions.md#camera-commands)。

- **/mm camera <pathId> add [index] [hold=N] [easing=NAME] [relative=true]**：在当前位置添加关键帧。
- **/mm camera <pathId> remove [index]**：移除指定索引的关键帧，省略索引时移除最后一个。

## 示例 {#examples}

Boss 登场示例：冻结触发动画的玩家，围绕 Boss 移动镜头 80 个游戏刻，然后在动画结束时运行技能。

```yaml
BossIntro:
  Skills:
  - cinematicCamera{path=boss_orbit;freezePlayer=true;onEnd=BossRoar} @trigger
```
