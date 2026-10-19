---
title: Rectangle
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Rectangle
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Rectangle {#rectangle}

## 说明 {#description}

返回指定数量的目标位置，这些点组成一个矩形。可通过参数调整矩形的各项设置，例如是否填充、是否只选取边框，以及矩形的位置等

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| x |  | 矩形在 **x** 轴上的大小。 | 1 |
| y |  | 矩形在 **y** 轴上的大小。 | 1 |
| z |  | 矩形在 **z** 轴上的大小。 | 1 |
| xOffset |  | 矩形在 **x** 轴上的偏移。 | 0 |
| yOffset |  | 矩形在 **y** 轴上的偏移。 | 0 |
| zOffset |  | 矩形在 **z** 轴上的偏移。 | 0 |
| points | p, density, d | 立方体每条“线”上的点数。 | 10 |
| filled | fill, f | 是否填充矩形。 | false |
| outline | edge, onlyEdge, e, onlyOutline, o | 是否仅绘制轮廓。 | false |
| rotation | r | 矩形的 3D 旋转。 | 0,0,0 |
| fromOrigin | origin | 是否从元技能原点开始绘制矩形。 | false |

## 示例 {#examples}

```yaml
ExampleMob1:
  Type: ZOMBIE
  Skills:
  - particle{p=FLAME;a=1} @Rectangle{d=12;f=false;r=45,45,0;yOffset=1.5;outline=true} ~onDamaged

ExampleMob2:
  Type: ZOMBIE
  Skills:
  - particle{p=SOUL_FIRE_FLAME;a=1} @Rectangle{d=12;r=45,45,45;yOffset=3;fill=true} ~onDamaged
```

## 别名 {#aliases}

- cube
- cuboid
