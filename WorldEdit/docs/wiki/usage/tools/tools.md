---
title: 工具
source_url: https://worldedit.enginehub.org/en/latest/usage/tools/tools/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 工具 { #tools }

有些任务如果反复执行命令，会很繁琐。WorldEdit 提供多种工具，可以绑定到物品，单击方块时使用。大多数工具通过右键操作，有些也提供左键操作。部分工具（包括所有“笔刷”类工具）可以远距离使用，即使距离很远，也会像单击了视线中的方块一样操作。

要使用工具，手持一个物品，再通过 `/tool [name]` 按名称绑定所需工具。随后会收到工具已绑定到该物品的提示。之后每次使用工具（手持该物品单击）时，就会执行对应操作。**要解除工具绑定，手持该物品并使用** `/tool none` **命令。**

!!! tip "提示"

    从技术上说，选区工具（默认木斧，通过 `/tool selwand` 绑定）和移动工具（默认指南针，通过 `/tool navwand` 绑定）也属于工具。它们分别在[选区](../regions/selections.md)和[移动](../navigation.md)页面介绍。与其他工具一样，可以绑定或解除绑定。

<a id="contents"></a>

- [工具列表](#tool-listing)



  - [树木生成工具](#tree-generation-tool)

  - [浮空树清理工具](#floating-tree-remover)

  - [方块替换工具](#block-replacer-tool)

  - [远距离建造工具](#long-range-building-tool)

  - [远距离选区工具](#long-range-wand)

  - [状态循环工具](#cycler-tool)

  - [查询工具](#query-tool)

  - [泛洪填充工具](#flood-fill-tool)

- [超级镐](#super-pickaxes)



  - [单方块超级镐](#single-superpick)

  - [范围超级镐](#area-superpick)

  - [递归超级镐](#recursive-superpick)

- [笔刷](#brushes)

## 工具列表 { #tool-listing }

### 树木生成工具 { #tree-generation-tool }

```text
/tool tree [type]
```

用此工具右键单击方块，会生成所选类型的树。它使用 Minecraft 的树木生成器，因此也受同样限制：不会在无法种植的方块上生成树，也不会穿过上方的实心方块生成（除非该树本来就能在那里生长）。

### 浮空树清理工具 { #floating-tree-remover }

```text
/tool deltree
```

有玩家只砍一半树，留下到处漂浮的树冠？用此工具右键单击浮空的树叶、原木或蘑菇方块，会移除所有相连的浮空树木方块。仍与其他东西（例如地面）相连的树不会受影响。

### 方块替换工具 { #block-replacer-tool }

```text
/tool repl <pattern>
```

此工具会用当前方块模式替换右键单击的方块。也可以左键单击方块，将当前方块模式改为所单击的方块。

### 远距离建造工具 { #long-range-building-tool }

```text
/tool lrbuild <leftclick pattern> <rightclick pattern>
```

此工具可以远距离放置和破坏方块，只需瞄准并单击。放置效果与右键单击目标方块相同。如果将其中一种方块设为空气，则会删除瞄准的方块。

### 远距离选区工具 { #long-range-wand }

```text
/tool farwand
```

此工具与普通选区工具相同，但可以在任意距离使用。它对应 `//hpos1` 和 `//hpos2`，而不是 `//pos1` 和 `//pos2`。

### 状态循环工具 { #cycler-tool }

```text
/tool cycler
```

此工具用于循环切换方块状态。左键单击选择要切换的属性，右键单击则循环切换该属性的可用值。例如，可以用它原地旋转单个方块。

### 查询工具 { #query-tool }

```text
/tool info
```

查询工具会显示右键单击方块的信息，包括坐标、方块类型、状态、亮度（发出／上方）以及内部 ID（若有）。

### 泛洪填充工具 { #flood-fill-tool }

```text
/tool floodfill <pattern> <range>
```

填充工具会从右键单击的方块开始，将它及给定范围内所有相连的同类型方块改为指定方块模式。

## 超级镐 { #super-pickaxes }

超级镐与其他工具略有不同：它不绑定到单个物品，而是通过命令开启或关闭。开启时，手持*任何*镐左键单击都会触发超级镐。与普通工具不同，使用 `//` 将其关闭。

### 单方块超级镐 { #single-superpick }

```text
//
/sp single
```

这种超级镐可以瞬间破坏方块。现在看来可能多余，但它比创造模式更早出现（创造模式在 Alpha 之前被移除，直到 Beta 1.8 才重新加入）。它还可以让被破坏的方块掉落为物品（可在[配置](../../config.md)中设置），而创造模式不会这样。

### 范围超级镐 { #area-superpick }

```text
/sp area <radius>
```

这种超级镐会破坏半径内与最初单击方块类型相同的所有方块。与单方块模式一样，可以配置为掉落物品。

### 递归超级镐 { #recursive-superpick }

```text
/sp recur <radius>
```

这种超级镐也会破坏半径内与最初单击方块类型相同的方块，但只处理通过同类型方块与原方块相连的部分。可以将它理解为“连锁采矿”模式。

## 笔刷 { #brushes }

上面的工具主要用于实用操作，而另一类称为笔刷的工具，主要用于从远处快速绘制和建造。

详情见[笔刷页面](brushes.md)。
