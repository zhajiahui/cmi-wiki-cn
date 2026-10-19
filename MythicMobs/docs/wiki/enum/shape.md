---
title: 形状
source_url: https://wiki.mythiccraft.io/mythicmobs/Enum/Shape
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 形状

如果某个机制、目标选择器等说明某项属性可以使用形状，***并且链接到本页***，就表示该属性的值可以是以下任意一种：

1. [SPHERE](shape.md#sphere)
2. [CUBE](shape.md#cube)
3. [CYLINDER](shape.md#cylinder)

这也表示，相应机制、目标选择器等在使用该形状时，可以使用该形状指定的额外属性。

# SPHERE {#sphere}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 球形范围的半径 | 5.0 |
| livingonly | living, l | 是否只选中活体实体 | true |

# CUBE {#cube}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 立方体一条边长度的一半 | 5.0 |
| livingonly | living, l | 是否只选中活体实体 | true |

# CYLINDER {#cylinder}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 圆柱体的半径 | 5.0 |
| height | h | 圆柱体的高度 | 5.0 |
| yOffset | offsety, yo | y 偏移量 | 0 |
