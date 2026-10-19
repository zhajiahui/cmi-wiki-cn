---
title: 笔刷
source_url: https://worldedit.enginehub.org/en/latest/usage/tools/brushes/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 笔刷 { #brushes }

与通用实用[工具](tools.md)相比，笔刷工具通常更适合建造、塑形和绘制。与其他工具一样，执行命令可将笔刷绑定到物品，右键单击即可使用（具有两种操作的笔刷也会使用左键）。使用 `/brush none` 命令解除绑定。

笔刷有一些独有设置，可以选择蒙版、大小、方块模式和范围，以便细调建造和绘制方式。

<a id="contents"></a>

- [笔刷列表](#brush-listing)



  - [球体笔刷](#sphere-brush)

  - [圆柱体笔刷](#cylinder-brush)

  - [设置笔刷](#set-brush)

  - [剪贴板笔刷](#clipboard-brush)

  - [平滑笔刷](#smooth-brush)

  - [重力笔刷](#gravity-brush)

  - [森林笔刷](#forest-brush)

  - [灭火笔刷](#extinguish-brush)

  - [清除生物笔刷](#butcher-brush)

  - [变形笔刷](#deform-brush)

  - [生物群系笔刷](#biome-brush)

- [笔刷设置](#brush-settings)



  - [蒙版](#mask)

  - [大小](#size)

  - [材料](#material)

  - [范围](#range)

  - [射线蒙版](#trace-mask)

## 笔刷列表 { #brush-listing }

### 球体笔刷 { #sphere-brush }

```text
/brush sphere [-h] <pattern> [radius]
/br s [-h] <pattern> [radius]
```

顾名思义，球体笔刷会在目标点创建球体。`-h` 选项会创建空心球体。

### 圆柱体笔刷 { #cylinder-brush }

```text
/brush cylinder [-h] <pattern> [radius] [height]
/br cyl [-h] <pattern> [radius] [height]
```

圆柱体笔刷会创建指定半径和高度的圆柱体。与其他命令一样，`-h` 表示空心。

### 设置笔刷 { #set-brush }

```text
/brush set <shape> [size] <pattern>
```

设置笔刷可以按给定大小和方块模式创建球体、圆柱体或长方体。除非需要立方体，否则其功能与前两种笔刷大多重复。

### 剪贴板笔刷 { #clipboard-brush }

```text
/brush clipboard [-aoeb] [-m <mask>]
```

剪贴板笔刷以剪贴板内容作为形状，每次使用都会将它放到目标位置。`aebm` 选项与[粘贴命令](../clipboard.md)完全相同。`-o` 略有不同：它将笔刷位置作为原点来粘贴剪贴板，否则会将剪贴板居中放在该位置。复制内容供此笔刷使用时，要仔细选择自己的相对位置。

### 平滑笔刷 { #smooth-brush }

```text
/brush smooth [radius] [iterations] [mask]
```

平滑区域，与[选区操作](../regions/regionops.md)中介绍的 `//smooth` 命令相同。可以指定构建高度图时要考虑的方块蒙版（这与决定哪些方块受影响的蒙版彼此独立）。

### 重力笔刷 { #gravity-brush }

```text
/brush gravity [radius] [-h]
```

重力笔刷会让笔刷作用区域内的方块向下移动。使用 `-h` 选项时，会从最大 y 高度开始，而不是从笔刷区域顶部开始。

### 森林笔刷 { #forest-brush }

```text
/brush forest <shape> [radius] [density] <tree type>
```

与 `//forest` 和 `//forestgen` 命令一样，此笔刷会根据提供的形状、半径、密度和树木类型种树。

### 灭火笔刷 { #extinguish-brush }

```text
/brush extinguish [radius]
/br ex [radius]
```

这是一个方便的快捷方式，相当于使用空气球体笔刷并将蒙版设为火焰方块。着火时如果来不及输入 3 条命令灭火，就可以用它。

### 清除生物笔刷 { #butcher-brush }

```text
/brush butcher [radius] [-pngabtfr]
/br kill [radius] [-pngabtfr]
```

与 `//butcher` [实用命令](../utilities.md)一样，清除生物笔刷会杀死作用区域内的实体。它的作用范围严格来说是圆柱体，竖直方向从世界最低高度一直延伸到最高高度，并不是球体。默认只杀死敌对生物，可以通过选项指定还要清除哪些生物。

清除生物选项

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**选项**</td>
<td markdown="span">**说明**</td>
</tr>
<tr>
<td markdown="span">`-p`</td>
<td markdown="span">杀死已驯服的宠物</td>
</tr>
<tr>
<td markdown="span">`-n`</td>
<td markdown="span">杀死 NPC</td>
</tr>
<tr>
<td markdown="span">`-g`</td>
<td markdown="span">杀死傀儡</td>
</tr>
<tr>
<td markdown="span">`-a`</td>
<td markdown="span">杀死动物</td>
</tr>
<tr>
<td markdown="span">`-b`</td>
<td markdown="span">杀死环境生物</td>
</tr>
<tr>
<td markdown="span">`-t`</td>
<td markdown="span">杀死有命名牌名称的生物</td>
</tr>
<tr>
<td markdown="span">`-f`</td>
<td markdown="span">组合以上所有选项</td>
</tr>
<tr>
<td markdown="span">`-r`</td>
<td markdown="span">杀死盔甲架</td>
</tr>
</tbody>
</table>

### 变形笔刷 { #deform-brush }

```text
/brush deform <shape> [size] [expression] [-ro]
```

与[选区操作](../regions/regionops.md)中介绍的 `//deform` 命令一样，此笔刷会对指定形状和半径内的方块应用表达式。也同样可以用 `-r` 使用原始坐标，用 `-o` 以放置位置为偏移原点。默认原点为笔刷目标点。

#### 抬高笔刷 { #raise-brush }

```text
/brush raise <shape> [size]
```

变形笔刷的一种特例，使用表达式 `y-=1`。

#### 降低笔刷 { #lower-brush }

```text
/brush lower <shape> [size]
```

变形笔刷的一种特例，使用表达式 `y+=1`。

### 生物群系笔刷 { #biome-brush }

```text
/brush biome <shape> [radius] <biomeType>
```

设置指定形状和半径内的生物群系。注意，从 1.15 开始，生物群系是三维的，能更改的最小区域为 4x4x4 的长方体。重新进入世界后才能看到效果。

## 笔刷设置 { #brush-settings }

这些命令只修改*当前选中*笔刷的设置。绑定的每个笔刷都有独立设置。

并非所有笔刷都使用全部设置：剪贴板笔刷没有大小设置（使用剪贴板自身大小），清除生物笔刷没有蒙版或材料设置（它作用于实体，而不是方块），等等。

### 蒙版 { #mask }

```text
/mask [mask]
/mask
```

为当前笔刷设置[蒙版](../general/masks.md)，限制它可以影响哪些方块。不指定蒙版时，会停用此笔刷的蒙版，让它重新能够影响所有方块。如果已经通过 `//gmask` 设置了全局蒙版，两者会组合使用。

### 大小 { #size }

```text
/size [size]
```

设置笔刷大小，通常表示半径或作用区域。最大大小可以在[配置](../../config.md)中调整。

### 材料 { #material }

```text
/material <pattern>
```

设置笔刷使用的方块模式。

### 范围 { #range }

```text
/range <range>
```

设置笔刷尝试建造的最大距离。如果范围足够短，笔刷在射线检测中找不到方块时，*会在半空中建造*。

### 射线蒙版 { #trace-mask }

```text
/tracemask [mask]
/tracemask
```

设置射线检测使用的蒙版。默认情况下，笔刷会对射线遇到的第一个非空气方块执行操作，或在射线达到最大范围时执行，以先发生者为准。设置射线蒙版后，可以让笔刷射线穿过指定方块。例如，`/tracemask #solid` 会穿过水等非实心方块。这适用于水下建造、隔墙操作等场景。
