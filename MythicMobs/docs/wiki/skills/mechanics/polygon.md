---
title: Polygon
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Polygon
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Polygon {#polygon}

## 说明 {#description}

polygon 元机制可以沿多边形图案执行其他技能。顶点数量、缩放、持续时间等由下列属性控制。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onPointSkill | onPoint, oP | 在每个顶点执行的元技能。 |  |
| onStarSkill | onStar, oS | 在多边形“星形”图案起点执行的元技能；此图案是通过调整“skip”参数在多边形内部形成的图形。 |  |
| onEdgeSkill | onEdge, oE | 在连接顶点的线段上执行的元技能。 |  |
| onHitEntitySkill | onHitEntity, ohe, oh | 多边形命中实体时执行的元技能。每次执行多边形机制时，其区域内每个实体仅触发一次。 |  |
| Points | p | 多边形的顶点数量。 | 32 |
| Duration | d | 多边形完全形成所需的刻数。为 0 时会立即创建多边形。 | 0 |
| DistanceBetween | distance, density, db | 多边形上各点之间的距离。 | 0.1 |
| Scale | size, s | 多边形的缩放比例。 | 1 |
| Skip | star, sv | 为形成星形图案而跳过的点数。 | 2 |
| xOffset | xo, x | X 轴偏移。 | 0 |
| yOffset | yo, y | Y 轴偏移。 | 0 |
| zOffset | zo, z | Z 轴偏移。 | 0 |
| targetxoffset | tx, txo | 目标的 X 轴偏移。 | 0 |
| targetyoffset | ty, tyo | 目标的 Y 轴偏移。 | 0 |
| targetzoffset | tz, tzo | 目标的 Z 轴偏移。 | 0 |
| ForwardOffset | foffset, fo | 向前偏移。 | 0 |
| Pitch |  | 俯仰旋转角。 | 0 |
| Yaw |  | 偏航旋转角。 | 0 |
| Roll |  | 滚转角。 | 0 |
| Radius | r | 命中半径。 | 1 |
| Rotation | rot | 多边形的旋转角度，格式为 x,y,z，与使用 pitch/yaw/roll 相同。 | 0,0,0 |
| MatchCasterDirection | matchPlayerDirection, matchDirection, mcd, mpd, md, direction | 使多边形方向与施法者的朝向一致。 | true |
| directiontowardstarget | dtt | 是否计算 yaw/pitch，使绘制的形状朝向目标。 | false |
| FromOrigin |  | 多边形是否从元技能的原点开始。 | false |
| HitConditions | conditions, cond, c, oC, hC | 实体必须满足这些[内联条件](../inline-conditions.md)，才能被多边形机制命中。 |  |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - polygon{db=0.25;y=0.1;mpd=false;scale=6;
    oE=[ - effect:particles{p=FLAME} ];
    oP=[ - effect:particles{p=CRIT;a=1;repeat=20;repeati=1} ];
    oS=[ - effect:particles{p=SOUL_FIRE_FLAME} ]
    ;p=10;skip=6;duration=20} @Origin
```

```yaml
ExampleSkill:
  Skills:
  - setVar{var=global.a;v=0}
  - skill{s=[
    - addVar{var=global.a;a=1}
    - polygon{db=0.25;y=0.1;mpd=false;radius=1;scale=6;yaw=<global.var.a>;
      oE=[ - effect:particles{p=FLAME} ];
      oP=[ - effect:particles{p=CRIT;a=1} ];
      oS=[ - effect:particles{p=SOUL_FIRE_FLAME} ]
      ;p=10;skip=2} @Origin
    ];repeat=180;repeati=1}
```
