---
title: 蒙版
source_url: https://worldedit.enginehub.org/en/latest/usage/general/masks/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 蒙版 { #masks }

蒙版与[方块模式](patterns.md)一样，常用于 WorldEdit 命令。与方块模式不同，蒙版决定命令、笔刷等会影响*哪些*方块。

除了将蒙版作为参数的命令（例如 `//replace [mask] <pattern>`），你还可以手持[笔刷](../tools/brushes.md)使用 `/mask` 命令，为单个笔刷应用蒙版；也可以通过 `//gmask`，为所有 WorldEdit 操作应用全局蒙版。

!!! note "注意"

    通过不同方式应用的蒙版会叠加。如果使用 `//gmask dirt` 设置全局蒙版，再用 `/mask stone` 设置笔刷蒙版，该笔刷就无法修改任何方块！因为组合后的蒙版只会匹配同时为石头*和*泥土的方块！

!!! tip "提示"

    再次使用 `//gmask` 且不带参数，可以清除全局蒙版。

<a id="contents"></a>

- [组合蒙版](#combining-masks)

- [可用蒙版](#available-masks)



  - [方块蒙版](#block-mask)

  - [蒙版取反](#mask-negation)

  - [现有方块蒙版](#existing-block-mask)

  - [实心方块蒙版](#solid-block-mask)

  - [完整立方体蒙版](#full-cube-mask)

  - [偏移蒙版](#offset-mask)

  - [相邻蒙版](#adjacency-mask)

  - [选区蒙版](#region-masks)

  - [剪贴板蒙版](#clipboard-mask)

  - [方块类别蒙版](#block-category-mask)

  - [随机噪声蒙版](#random-noise-mask)

  - [方块状态蒙版](#block-state-mask)

  - [表达式蒙版](#expression-mask)

  - [生物群系蒙版](#biome-mask)

  - [表面蒙版](#surface-mask)

## 组合蒙版 { #combining-masks }

要让蒙版匹配多个蒙版的*交集*，用空格分隔它们。只有*所有*给定蒙版都匹配时，交集才会匹配。

示例：组合蒙版

使用蒙版交集，将表面的石头替换为泥土：

```text
//replace "stone <air" dirt
```

设置蒙版，让当前笔刷只能修改选区内的空气方块：

```text
/mask "air #sel"
```

## 可用蒙版 { #available-masks }

### 方块蒙版 { #block-mask }

这是最简单的蒙版，用来匹配一种或多种方块或方块状态。与[单一方块模式](patterns.md)一样，可以只指定方块类型，也可以指定方块类型及任意数量的状态。与方块模式不同，蒙版*不会*为未指定的方块状态采用默认值，而是“模糊”匹配这些状态的任意值。

要匹配多种方块，用逗号分隔。

示例：使用方块蒙版

移除选区内的所有橡木栅栏：

```text
//replace oak_fence air
```

移除所有东侧已连接的橡木栅栏，以及橡木栅栏门：

```text
//replace oak_fence[east=true],oak_fence_gate air
```

### 蒙版取反 { #mask-negation }

`!` 符号可以对其后的全部内容取反，也就是匹配另一个蒙版*未*匹配的方块。其后可以接任意其他蒙版。

示例：对蒙版取反

将不是泥土、石头或草方块的所有方块替换为石头：

```text
//replace !dirt,stone,grass_block stone
```

### 现有方块蒙版 { #existing-block-mask }

`#existing` 蒙版会匹配所有非空气方块。注意，这与 !air 不同，因为游戏实际上会在某些情况下使用多种空气。

### 实心方块蒙版 { #solid-block-mask }

`#solid` 蒙版会匹配所有被视为“实心”的方块，即阻止实体（例如玩家）穿过的方块。

### 完整立方体蒙版 { #full-cube-mask }

`#fullcube` 蒙版会匹配所有占满整个方块立方体的方块。

### 偏移蒙版 { #offset-mask }

在另一个蒙版前加 `>`（覆盖层）或 `<`（下垫层），会分别匹配位于该蒙版所匹配方块上方或下方的方块。

示例：偏移蒙版

在选区内的木板上方创建一层台阶：

```text
//replace >##planks smooth_stone_slab
```

### 相邻蒙版 { #adjacency-mask }

在另一个蒙版前加 ~，会匹配与该蒙版所匹配方块相邻的方块。

!!! note "注意"

    此蒙版中的“相邻”指紧挨着的左右前后或上下方块，不包含对角方向的方块。

示例：相邻蒙版

用荧石包围所有刷怪笼：

```text
//replace ~spawner glowstone
```

### 选区蒙版 { #region-masks }

对于替换之类的命令，选区蒙版没有意义，但用笔刷在限定区域内操作时会很有用。例如，想用笔刷在墙脚周围添加泥土，可以先选中墙，再对选区蒙版取反，这样泥土就不会影响墙体（但仍会影响周围地面）。

第一种选区蒙版是 `#region`（别名：`#sel`、`#selection`），它会复制执行命令时的选区，并将其用作蒙版。

第二种选区蒙版是 `#dregion`（d 表示动态，也可以写作 `#dsel`、`#dselection`），它会始终随当前选区更新。

### 剪贴板蒙版 { #clipboard-mask }

`#clipboard` 蒙版会匹配与当前剪贴板一致的方块。它可以配合 //regen -c` 等命令，匹配所有与自然生成结果相同的方块。

### 方块类别蒙版 { #block-category-mask }

方块类别，也就是[标签](https://minecraft.wiki/w/Tag)，也能用作蒙版。类别蒙版会匹配该类别中的任意方块。与方块模式一样，语法为 ##&lt;tag&gt;。

示例：方块类别蒙版

将所有地毯替换为一层雪：

```text
//replace ##carpets snow
```

### 随机噪声蒙版 { #random-noise-mask }

噪声蒙版可以创建随机噪声。指定 `%<percent>` 会匹配给定百分比的方块。与加权方块模式不同，`%50` 确实表示 50% 的方块。

!!! note "注意"

    注意这里的语法区别：与方块模式不同，此蒙版的 % 符号放在所需百分比之前。

示例：使用随机噪声蒙版

随机将选区内 50% 的方块替换为石头：

```text
//replace %50 stone
```

### 方块状态蒙版 { #block-state-mask }

与方块蒙版一样，此蒙版匹配方块状态。但它不需要指定方块类型，因此可以匹配任何具有指定属性值的方块。

状态蒙版分为宽松和严格两种模式。在宽松模式（`^[state=value,...]`）下，它会匹配指定方块状态等于给定值的方块，*也会*匹配完全没有这些属性的方块。在严格模式（`^=[state=value,...]`）下，它*只会*匹配具有这些方块状态且值等于给定值的方块。

示例：使用方块状态蒙版

移除所有关闭的门、栅栏门和活板门：

```text
//replace ^=[open=false] air
```

### 表达式蒙版 { #expression-mask }

此蒙版可以对每个方块计算数学表达式。蒙版以 `=` 开头，其后必须跟一个[表达式](../other/expressions.md)，其中可以使用变量 `x`、`y` 和 `z`。表达式返回正值时，蒙版就会匹配。

示例：表达式蒙版

只编辑特定 y 高度以下的方块：

```text
//gmask =y<64
```

只编辑下方两个方块处为空气的方块：

```text
//gmask =queryRel(0,-2,0,0,0)
```

### 生物群系蒙版 { #biome-mask }

生物群系蒙版会匹配处于给定生物群系中的方块，语法为 `$<biome id>`。生物群系 ID 必须是[带命名空间的 ID](https://minecraft.wiki/w/Java_Edition_data_values#Biomes)；原版生物群系可省略 minecraft:，模组添加的生物群系则必须包含模组 ID。

### 表面蒙版 { #surface-mask }

表面蒙版会匹配至少有一面暴露在空气中的方块。因此，它只匹配物体表面，不匹配被其他方块完全包围的部分。

此蒙版为 `#surface`（别名为 `#exposed`）。
