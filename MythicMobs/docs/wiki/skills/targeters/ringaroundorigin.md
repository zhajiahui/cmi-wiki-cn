---
title: Ring Around Origin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RingAroundOrigin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ring Around Origin {#ring-around-origin}

## 说明 {#description}

定位原点周围指定环中的位置。

旋转以弧度为单位，例如绕轴旋转 90 度对应 `1.57`。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |
| points | p | 组成圆环的点。 | 10 |
| rotationx | rotx, rx | 圆环绕 x 轴的旋转角度。 | 0 |
| rotationy | roty, ry | 圆环绕 y 轴的旋转角度。 | 0 |
| rotationz | rotz, rz | 圆环绕 z 轴的旋转角度。 | 0 |
| offsetx | offx, ox | 圆环在 x 轴上的偏移。 | 0 |
| offsety | offy, oy | 圆环在 y 轴上的偏移。 | 0 |
| offsetz | offz, oz | 圆环在 z 轴上的偏移。 | 0 |
| relative |  | 圆环朝向是否相对于施法者的朝向。 | false |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - effect:particles @RingAroundOrigin{r=5;p=15}
    ]}

# This will draw a vertical circle instead of a flat one:
VerticalRingSkill:
  Skills:
  - particles{p=enchanted_hit;a=1;} @RAO{r=2;rz=1.57;p=9;relative=true}
```

## 别名 {#aliases}

- ringOrigin
- RAO
