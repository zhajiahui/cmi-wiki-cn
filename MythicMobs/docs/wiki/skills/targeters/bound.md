---
title: Bound
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Bound
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Bound {#bound}

## 说明 {#description}

选中区域内的所有活体实体。区域可以是由两个角点界定的长方体（默认）、球体或竖直的圆柱体。支持与 [inBounds](../conditions/inbounds.md) 条件相同的选项，其中的位置目标选择器会以技能施法者为基准解析。会检查施法者所在世界中的每个活体实体。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| shape |  | `cuboid`、`sphere` 或 `cylinder`。 | cuboid |
| corner1 | c1 | 长方体的第一个角点，可使用位置目标选择器、定位点名称、`world,x,y,z` 或 `x,y,z`。 | NONE |
| corner2 | c2 | 长方体的第二个角点，格式与 `corner1` 相同。 | NONE |
| x1, y1, z1 |  | 在 `corner1` 解析完成后，替换其对应坐标。 | NONE |
| x2, y2, z2 |  | 在 `corner2` 解析完成后，替换其对应坐标。 | NONE |
| location | loc, l, center, centre, origin | 球心或圆柱体底面的中心，可使用位置目标选择器、定位点名称、`world,x,y,z` 或 `x,y,z`。 | NONE |
| radius | r | 球体或圆柱体的半径。 | NONE |
| height | h | 圆柱体的高度，从 `location` 向上计算。 | NONE |

长方体需要`corner1`和`corner2`。球体需要`location`和`radius`，圆柱体也需要`height`。

## 示例 {#examples}

```yaml
  Skills:
  - ignite @bound{shape=sphere;l=@selfLocation;r=8}
  - damage{a=5} @bound{c1=arena_a;c2=arena_b;y1=-64;y2=320}
```

## 别名 {#aliases}

- bounds
