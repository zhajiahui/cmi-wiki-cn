---
title: 显示选项
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/DisplayOptions
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 显示选项

以下是所有可用的展示实体选项。这些选项都放在 `DisplayOptions` 部分下，如下所示：

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
```

目录：

1. [基本选项](displayoptions.md#base-options)
2. [方块展示实体](displayoptions.md#block-display)
3. [物品展示实体](displayoptions.md#item-display)
4. [文本展示实体](displayoptions.md#text-display)

# 基本选项 {#base-options}

这些选项适用于所有展示实体类型。

#### ViewRange {#viewrange}

最大可见范围或距离。[当距离超过 `viewRange x entityDistanceScaling x 64` 时，实体不会被渲染](https://minecraft.wiki/w/Display#Entity_data)。默认值为 `1`。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ViewRange: 1
```

#### 宽度 {#width}

展示实体的宽度。默认值为 `0`。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Width: 0
```

#### Height {#height}

展示实体的高度。默认值为 `0`。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Height: 0
```

#### ShadowRadius {#shadowradius}

展示实体的阴影半径。默认值为 `0`。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ShadowRadius: 0
```

#### ShadowStrength {#shadowstrength}

展示实体阴影的不透明度。默认值为 `1`。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ShadowStrength: 1
```

#### 面向模式（Billboard） {#billboard}

控制展示实体向玩家渲染时的旋转轴约束。默认值为 `FIXED`。可用约束：

| 面向模式（Billboard） | 说明 |
| --- | --- |
| FIXED | 不旋转。 |
| CENTER | 绕中心点旋转。 |
| HORIZONTAL | 绕水平轴旋转。 |
| VERTICAL | 绕竖直轴旋转。 |

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Billboard: FIXED
```

#### TeleportDuration {#teleportduration}

设置传送持续时间，单位为刻。默认值为 `0`。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    TeleportDuration: 0
```

#### InterpolationDelay {#interpolationdelay}

设置开始插值前的延迟。默认值为 `0`。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    InterpolationDelay: 0
```

#### InterpolationDuration {#interpolationduration}

设置插值持续时间，单位为刻。默认值为 `0`。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    InterpolationDuration: 0
```

#### ColorOverride {#coloroverride}

设置发光边框的颜色。为 `0` 时，使用展示实体所在队伍的颜色。默认值为 `0`。
**格式**：`a,r,g,b` 或其等效整数。
可以使用以下网站：[color-hex](https://www.color-hex.com/)、[arg-int-calculator](https://argb-int-calculator.netlify.app/)。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ColorOverride: 0
```

### Brightness {#brightness}

必须同时设置 blocklight 和 skylight，才能覆盖亮度。数值范围必须为 `0` 到 `15`。

使用 `-1`，让展示实体采用环境的方块光照或天空光照，不覆盖它们。

#### BlockLight 与 SkyLight {#blocklight-skylight}

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    BlockLight: 0
    SkyLight: 0
```

### 变换 {#transformations}

#### Translation {#translation}

设置展示实体的平移。默认值为 `0,0,0`。
**格式**：x,y,z

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Translation: 0,0,0
```

#### Scale {#scale}

设置展示实体的缩放，以原点为中心缩放模型。默认值为 `1,1,1`。
**格式**：x,y,z

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Scale: 1,1,1
```

#### LeftRotation {#leftrotation}

提供 4 个值 (x,y,z,w) 时，使用[四元数](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)设置左旋转。提供 3 个值 (x,y,z) 时，使用欧拉角。默认值为 `0,0,0,1`（无旋转）。
**格式**：x,y,z,w

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    LeftRotation: 0,0,0,1
```

#### RightRotation {#rightrotation}

提供 4 个值 (x,y,z,w) 时，使用[四元数](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)设置左旋转。提供 3 个值 (x,y,z) 时，使用欧拉角。默认值为 `0,0,0,1`（无旋转）。
**格式**：x,y,z,w

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    RightRotation: 0,0,0,1
```

# 方块展示实体 {#block-display}

此展示实体类型只有一个专用选项。

#### Block {#block}

使用的方块状态。

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: bell[facing=north]
```

# 物品展示实体 {#item-display}

#### Item {#item}

使用的物品。支持 Mythic 物品。

```yml
cool_display:
  Type: item_display
  DisplayOptions:
    Item: stick
```

#### Transform {#transform}

应用到物品上的模型变换。默认值为 `NONE`。

| 类型 |
| --- |
| FIRSTPERSON_LEFTHAND |
| FIRSTPERSON_RIGHTHAND |
| FIXED |
| GROUND |
| GUI |
| HEAD |
| NONE |
| THIRDPERSON_LEFTHAND |
| THIRDPERSON_RIGHTHAND |

```yml
cool_display:
  Type: item_display
  DisplayOptions:
    Item: stick
    Transform: NONE
```

# 文本展示实体 {#text-display}

#### Text {#text}

设置显示的文本。默认值为 `Give This Poor Dude A Text To Display`。

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
```

#### Opacity {#opacity}

设置文本不透明度，范围为 `0` 到 `255`。默认值为 `255`。

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    Opacity: 255
```

#### DefaultBackground {#defaultbackground}

设置是否使用默认文本背景色（与聊天相同）渲染，并覆盖 [BackgroundColor](https://wiki.mythiccraft.io/mythicmobs/Mobs/DisplayOptions#BackgroundColor) 选项。默认值为 `false`。

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    DefaultBackground: false
```

#### BackgroundColor {#backgroundcolor}

设置文本背景色。默认值为 `1073741824`。
**格式**：`a,r,g,b` 或其等效整数。

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    BackgroundColor: 1073741824
```

#### Alignment {#alignment}

设置文本对齐方式。默认值为 `CENTER`。

| 类型 | 说明 |
| --- | --- |
| CENTER | 文字居中对齐。 |
| LEFT | 文字左对齐。 |
| RIGHT | 文字右对齐。 |

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    Alignment: CENTER
```

#### LineWidth {#linewidth}

用于分行的最大行宽。也可以使用 `\n` 字符换行。默认值为 `200`。

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    LineWidth: 200
```

#### Shadowed {#shadowed}

设置文本是否显示阴影。默认值为 `false`。

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    Shadowed: false
```

#### SeeThrough {#seethrough}

设置是否可以透过方块看见文本。默认值为 `false`。

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    SeeThrough: false
```
