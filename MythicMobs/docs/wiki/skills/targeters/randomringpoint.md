---
title: Random Ring Point
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RandomRingPoint
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Random Ring Point {#random-ring-point}

## 说明 {#description}

瞄准施法者周围环内的随机点

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 圆环半径。 | 5 |
| points | p | 要生成的点数。 | 10 |
| amount | a | 生成的点中要选择多少个作为目标。 | 1 |
| rotationx | rotx, rx | 绕 x 轴的旋转角度。 | 0 |
| rotationy | roty, ry | 绕 y 轴的旋转角度。 | 0 |
| rotationz | rotz, rz | 绕 z 轴的旋转角度。 | 0 |
| offsetx | offx, ox | x 轴偏移。 | 0 |
| offsety | offy, oy | y 轴偏移。 | 0 |
| offsetz | offz, oz | z 轴偏移。 | 0 |

## 示例 {#examples}

```yaml
  Skills:
  - particle @randomRingPoint{r=4;p=20;a=10}
```
