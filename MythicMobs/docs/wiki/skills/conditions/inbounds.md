---
title: In Bounds
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/inBounds
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# In Bounds {#in-bounds}

## 说明 {#description}

测试目标是否位于某个区域内：两个对角之间的长方体（默认）、球体或直立圆柱体。坐标值支持占位符和数学表达式（数字中的数学和占位符需要 MythicMobs Premium）。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| shape |  | `cuboid`、`sphere` 或 `cylinder`。 | cuboid |
| corner1 | c1 | 长方体的第一个角点。可使用位置目标选择器、定位点名称、`world,x,y,z` 或 `x,y,z`。 |  |
| corner2 | c2 | 长方体的第二个角点，格式与 `corner1` 相同。 |  |
| x1, y1, z1 |  | 在 `corner1` 解析完成后，替换其对应坐标。 |  |
| x2, y2, z2 |  | 在 `corner2` 解析完成后，替换其对应坐标。 |  |
| location | loc, l, center, centre, origin | 球心或圆柱体底面的中心。可使用位置目标选择器、定位点名称、`world,x,y,z` 或 `x,y,z`。 |  |
| radius | r | 球体或圆柱体的半径。 |  |
| height | h | 圆柱体的高度，从 `location` 向上计算。 |  |

长方体需要`corner1`和`corner2`。球体需要`location`和`radius`，圆柱体也需要`height`。

当角点指定为`x,y,z`（无世界）时，将使用检查位置的世界。

`@selfLocation` 等位置目标选择器根据正在执行的技能解析。刷怪点、随机生成和掉落表条件不在技能内执行，因此这些位置应使用 pin 或坐标。

## 示例 {#examples}

```yaml
  Conditions:
  - inBounds{c1=-10,60,-10;c2=10,80,10} true
```

```yaml
  TargetConditions:
  - inBounds{corner1=world,0,64,0;corner2=world,32,96,32}
```

```yaml
  Conditions:
  - inBounds{c1=mypin;c2=anotherpin} true
```

```yaml
  TargetConditions:
  - inBounds{shape=sphere;l=@selfLocation;r=10}
```

```yaml
  Conditions:
  - inBounds{shape=cylinder;l=world,0,64,0;r=5;h=10} true
```

## 别名 {#aliases}

- withinBounds
- insideBounds
