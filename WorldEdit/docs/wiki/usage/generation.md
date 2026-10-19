---
title: 生成
source_url: https://worldedit.enginehub.org/en/latest/usage/generation/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 生成 { #generation }

有时你可能想自动生成森林或创建球体，因为手动制作太繁琐。WorldEdit 提供了多种工具来完成这些工作。这些命令不需要选区，而是使用你所处的方块位置。

与大多数 WorldEdit 命令一样，这些命令都接受[方块模式](general/patterns.md)作为参数。

!!! tip "提示"

    这些命令实际使用的是“放置位置”，默认为你当前所在的位置。可以使用 `//toggleplace` 命令，改为使用选区的第一个点（通过工具左键单击或 `//pos1` 选定的点）。

<a id="contents"></a>

- [圆柱体](#cylinders)

- [球体](#sphere)

- [金字塔](#pyramids)

- [森林](#forests)

- [南瓜地](#pumpkin-patches)

- [生成任意形状](#generating-arbitrary-shapes)



  - [选项](#flags)

  - [变量](#variables)

  - [形状示例](#shape-examples)

- [生成生物群系形状](#generating-biome-shapes)

## 圆柱体 { #cylinders }

```text
//cyl <pattern> <radius> [height]
//hcyl <pattern> <radius> [height]
```

WorldEdit 可以生成空心或实心的圆柱体，也可以生成空心或实心的圆。它使用快速算法生成这些形状，边缘整齐且对称。圆柱体从脚下向上延伸。如果要创建圆，只需创建高度为 1 的圆柱体。

!!! tip "提示"

    半径可以使用小数，以便更精细地控制形状边缘。

要生成椭圆柱，可以指定两个半径：一个用于东西轴，另一个用于南北轴。

```text
//cyl <pattern> <radiusEW>,<radiusNS> [height]
//hcyl <pattern> <radiusEW>,<radiusNS> [height]
```

示例：创建圆柱体和圆

创建半径为 5、高度为 10 的实心玻璃圆柱体：

```text
//cyl glass 5 10
```

创建半径分别为 5.5 和 15、高度为 1 的石头空心椭圆柱：

```text
//hcyl stone 5.5,15 1
```

## 球体 { #sphere }

```text
//sphere [-r] <pattern> <radius>
//hsphere [-r] <pattern> <radius>
```

可以创建空心或实心球体。默认情况下，球心位于脚下所站方块的上一个方块。提供 -r（抬高）选项时，球体会向上移动一个半径的距离，让球体底部位于脚下。

与圆柱体一样，可以指定多个半径来创建椭球（半径同样可以是小数）。半径顺序为南北轴、上下轴，然后是东西轴。

```text
//sphere [-r] <pattern> <radius>,<radius>,<radius>
//hsphere [-r] <pattern> <radius>,<radius>,<radius>
```

## 金字塔 { #pyramids }

```text
//pyramid <pattern> <size>
//hpyramid <pattern> <size>
```

此命令会用给定方块模式创建指定*高度*的金字塔。例如，指定高度为 5，就会有 5 层，从下到上每层在各个方向都比前一层短一个方块。最底层的边长是高度的两倍。

## 森林 { #forests }

```text
/forestgen [size] [type] [density]
```

此命令可以生成森林。大小参数表示生成森林的正方形区域的宽和长。密度可以在 0 到 100 之间，也可以使用 0.1 之类的小数。默认密度 5 已经相当茂密。大小是以放置位置为中心的长方体的边心距（半径）。

!!! tip "提示"

    此命令与[选区操作](regions/regionops.md)中的森林生成器作用相同，只是它根据放置位置和大小参数确定范围，而不是使用选区。

!!! warning "警告"

    根据所用平台不同，WorldEdit 可能无法使用 //undo 撤销这些树木的生成。

## 南瓜地 { #pumpkin-patches }

```text
/pumpkins [size]
```

WorldEdit 可以生成南瓜地。大小参数表示从脚下向外延伸、用于生成南瓜地的正方形区域的宽和长。目前无法调整南瓜地的密度。

## 生成任意形状 { #generating-arbitrary-shapes }

```text
//generate <pattern> <expression>
```

别名：`//g`、`//gen`

生成任何能用数学公式描述的形状：

> - 圆环体
>
> - 旋转后的圆柱体
>
> - 锯齿状峡谷
>
> - 任何你能想象并归纳为公式的形状

此功能使用[表达式解析器](other/expressions.md)。

### 选项 { #flags }

- `-r`——使用原始坐标，一个方块对应一个单位。

- `-c`——将原点移到选区中心，一个方块对应一个单位。

- `-o`——将原点移到放置位置（你的位置或 pos1，通过 `/togglepos` 切换），一个方块对应一个单位。

- 不使用这些选项时，坐标会根据选区的最小点和最大点归一化到 -1..1（即整个选区为 2x2x2 个单位）。根据选区各轴长度的差异，每个轴上一个单位对应的方块数可能不同。

- `-h`——生成空心形状。只有与形状以外的方块相邻的位置才会设置方块。

### 变量 { #variables }

- `x`、`y`、`z`（输入）——坐标。

- `type`、`data`（输入／输出）——要使用的材料，默认为输入的方块或方块模式。

!!! note "注意"

    由于表达式解析器只接受数值变量，type/data 变量和查询函数只能用于具有旧版 type/data 值的方块。如果需要使用较新的方块（> MC 1.13），先用占位方块生成形状，再通过 `//replace` 替换占位方块。此限制只针对表达式，不限制命令的 `<pattern>` 参数。

对于属于形状的方块，表达式应返回真（`> 0`）；不属于形状的方块则返回假（`<= 0`）。选区中的每个方块都会测试此表达式。

### 形状示例 { #shape-examples }

示例：生成各种形状

主半径为 0.75、管半径为 0.25 的圆环体：

```text
//g stone (0.75-sqrt(x^2+y^2))^2+z^2 < 0.25^2
```

扭曲的空心树：

```text
//g -h oak_log (0.5+sin(atan2(x,z)*8)*0.2)*(sqrt(x*x+z*z)/0.5)^(-2)-1.2 < y
```

彩虹圆环体：

```text
//g white_wool data=(32+15/2/pi*atan2(x,y))%16; (0.75-sqrt(x^2+y^2))^2+z^2 < 0.25^2
```

彩虹蛋：

```text
//g white_wool data=(32+y*16+1)%16; y^2/9+x^2/6*(1/(1-0.4*y))+z^2/6*(1/(1-0.4*y))<0.08
```

心形：

```text
//g red_wool (z/2)^2+x^2+(5*y/4-sqrt(abs(x)))^2<0.6
```

正弦波：

```text
//g -h glass sin(x*5)/2<y
```

径向余弦波：

```text
//g -h glass cos(sqrt(x^2+z^2)*5)/2<y
```

圆双曲面：

```text
//g stone -(z^2/12)+(y^2/4)-(x^2/12)>-0.03
```

!!! tip "提示"

    想要更多有趣的形状？可以试试 [MathMod](https://github.com/parisolab/mathmod/releases) 之类的程序，它们自带大量形状，也能帮助你创建更多形状。注意，WorldEdit 使用等距坐标公式 (x,y,z)，而不是参数方程 (u,v,t)。此外，根据选区大小和函数定义域，你可能需要缩放 x、y、z 变量。

## 生成生物群系形状 { #generating-biome-shapes }

与生成命令一样，可以使用表达式将生物群系设置为特定形状。语法与上文相同，但接受的是生物群系 ID，而不是方块模式。

!!! note "注意"

    从 Minecraft 1.15 开始，生物群系以三维方式存储。WorldEdit 自 1.16 起使用完整的三维生物群系，但 Mojang 也引入了一些新的限制。详情见[设置生物群系](regions/regionops.md#setting-biomes)。
