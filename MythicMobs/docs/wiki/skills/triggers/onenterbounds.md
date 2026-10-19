---
title: On Enter Bounds
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onEnterBounds
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Enter Bounds {#on-enter-bounds}

## 说明 {#description}

该触发器具有特殊语法：`~onEnterBounds{corner1=<location>;corner2=<location>}`表示长方体，或`~onEnterBounds{shape=<sphere|cylinder>;location=<location>;radius=<number>}`表示球体或圆柱体

生物进入指定区域时执行技能。区域可以是由两个角点界定的长方体（默认）、球体或竖直的圆柱体。生物的位置会按其计时器时钟检查，与 [onTimer](ontimer.md) 使用同一时钟。只在生物跨入区域时触发一次，停留在区域内不会反复触发。如果生物生成时就已在区域内，会在首次检查时触发。

每个位置都可以填写位置目标选择器（例如 `@CasterSpawnLocation`）、Pin 名称、`world,x,y,z` 或 `x,y,z`。使用三坐标形式时，采用生物所在的世界。每次检查都会以生物为施法者重新解析目标选择器。坐标值支持占位符和数学表达式，其中数字中的占位符和数学运算需要 MythicMobs Premium。两个角点必须位于同一世界。

要在玩家进入某个区域时运行技能，请使用 [onPlayerEnter](onplayerenter.md)。

> 关联的 [@trigger](../targeters/trigger.md) 是生物本身

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

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob walks into the region between the two corners
    - message{m=Entered the arena} @World ~onEnterBounds{corner1=world,100,64,100;corner2=world,120,80,120}
```

以下同样适用于半径为 5、高度为 6、底部位于 `0,64,0` 的圆柱体：

```yml
  Skills:
  - message{m=The chicken reached the altar} @World ~onEnterBounds{shape=cylinder;location=world,0,64,0;radius=5;height=6}
```

## 别名 {#aliases}

- onEnter_Bounds
- onBoundsEnter
- onBounds_Enter
