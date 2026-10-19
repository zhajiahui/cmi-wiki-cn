---
title: Slash
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/slash
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Slash {#slash}

## 说明 {#description}

slash 元机制可以沿斩击形状的图案执行其他技能。形状、大小、位置、旋转等由以下属性控制。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onStartSkill | onStart, oS | 斩击开始时执行的元技能 |  |
| onEndSkill | onEnd, oE | 斩击结束时执行的元技能 |  |
| onPointSkill | onPoint, oP | 斩击上每个点执行的元技能 |  |
| onHitEntitySkill | onHitEntity, ohe, oh | 斩击上的点命中实体时执行的元技能。每次执行斩击机制时，对每个实体只触发一次 |  |
| Points | p | 斩击的点数 | 32 |
| specificStep | ss | 给定值大于 0 时，指定生成点中要显示的步数/索引 | 0 |
| Duration | d | 斩击移动的刻数。值为 0 时立即完成斩击 | 0 |
| Width | w | 斩击的宽度。增大此值会使斩击弧线更平缓 | 1 |
| Height | h | 斩击的高度。增大此值会使斩击弧线弯曲得更明显 | 1 |
| Angle | arc, a | 弧形的角度大小，以度为单位 | 180 |
| xOffset | xo, x | X 轴偏移。 | 0 |
| yOffset | yo, y | Y 轴偏移。 | 0 |
| zOffset | zo, z | Z 轴偏移。 | 0 |
| ForwardOffset | foffset, fo | 前向偏移量 | 0 |
| targetxoffset | txo, tx | 目标的 X 轴偏移。 | 0 |
| targetyoffset | tyo, ty | 目标的 Y 轴偏移。 | 0 |
| targetzoffset | tzo, tz | 目标的 Z 轴偏移。 | 0 |
| Pitch |  | 俯仰旋转角。 | 0 |
| Yaw |  | 偏航旋转角。 | 0 |
| Roll |  | 滚转角。 | 0 |
| Radius | r | 命中半径。 | 1 |
| Rotation | rot | 斩击的旋转，使用 x,y,z 格式，等同于 pitch/yaw/roll | 0,0,0 |
| MatchCasterDirection | matchPlayerDirection, matchDirection, mcd, mpd, md, direction | 使斩击方向与施法者的朝向一致 | true |
| directionTowardsTarget | dtt | 是否计算指向目标的 yaw/pitch | false |
| FromOrigin |  | 斩击是否从元技能原点开始 | false |
| HitConditions | conditions, cond, c, oC, hC | 实体必须满足此[行内条件](../inline-conditions.md)列表，才会被斩击机制命中 |  |

## 示例 {#examples}

下面展示 slash 机制实现后的基本效果。

```yaml
ExampleSkill:
  Skills:
  - slash{y=1.8;w=4;h=2;mpd=true;a=180;oP=[ - effect:particles{p=CRIT} ];roll=-45to45}
```

##  {#section}

如果你安装了[Crucible](https://mythiccraft.io/index.php?resources/crucible-create-unbelievable-mythic-items.2)，那么以下是如何将斜线机制放入物品中的示例

```yaml
SlashSword:
  Id: NETHERITE_SWORD
  Skills:
  - slash{y=1.8;w=4;h=4;mpd=true;a=45;radius=2;roll=-30to30;fo=5;duration=5;
      oP=[ - effect:particles{p=SPARK} ];
      oH=[ - damage{a=2} ]
      } @self ~onUse
```
