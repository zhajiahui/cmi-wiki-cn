---
title: On Player Enter
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onPlayerEnter
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Player Enter {#on-player-enter}

## 说明 {#description}

该触发器具有特殊语法：`~onPlayerEnter{corner1=<location>;corner2=<location>}`表示长方体，或`~onPlayerEnter{shape=<sphere|cylinder>;location=<location>;radius=<number>}`表示球体或圆柱体

玩家进入指定区域时执行技能。区域可以是由两个角点界定的长方体（默认）、球体或竖直的圆柱体。每次生物计时器运行时，会检查生物所在世界中所有游戏模式的玩家，与 [onTimer](ontimer.md) 使用同一时钟。每名玩家跨入区域时触发一次。如果生物生成时玩家就已在区域内，会在首次检查时触发。

每个位置都可以填写位置目标选择器、Pin 名称、`world,x,y,z` 或 `x,y,z`。每次检查都会以生物为施法者重新解析目标选择器，因此用 `@selfLocation` 定义的区域会随生物移动。坐标值支持占位符和数学表达式，其中数字中的占位符和数学运算需要 MythicMobs Premium。

玩家因退出服务器、死亡或切换世界而离开区域时，不会触发 [onPlayerExit](onplayerexit.md)；重新回到区域内时，会再次触发此触发器。

> 关联的[@trigger](../targeters/trigger.md)是进入该区域的玩家

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

向进入生物周围 20 格范围内的每位玩家发送消息：

```yml
ARENA_GUARD:
  Type: WITHER_SKELETON
  Skills:
  - message{m=Turn back while you can} @trigger ~onPlayerEnter{shape=sphere;location=@selfLocation;radius=20}
```

一个宽 20 格、从世界底部延伸到顶部，并随生物移动的长方体区域：

```yml
  Skills:
  - message{m=You entered the patrol area} @trigger ~onPlayerEnter{c1=@selfLocation{xoffset=-10;zoffset=-10};c2=@selfLocation{xoffset=10;zoffset=10};y1=-64;y2=320}
```

Pin `arena_a` 与 `arena_b` 之间的区域，高度不限：

```yml
  Skills:
  - message{m=Welcome to the arena} @trigger ~onPlayerEnter{c1=arena_a;c2=arena_b;y1=-64;y2=320}
```

## 别名 {#aliases}

- onPlayer_Enter
- onPlayerEnterBounds
- onPlayer_Enter_Bounds
