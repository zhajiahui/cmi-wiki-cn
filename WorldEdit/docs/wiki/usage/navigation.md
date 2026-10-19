---
title: 移动
source_url: https://worldedit.enginehub.org/en/latest/usage/navigation/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 移动 { #navigation }

为了更方便地完成工作，你可能经常需要移动到不同位置。以下命令用于解决这一问题。

<a id="contents"></a>

- [移动工具](#the-navigation-wand)

- [脱困](#freeing-yourself)

- [跳转到视线中的方块](#jumping-to-the-block-in-sight)

- [穿墙](#passing-through-walls)

- [上升与下降](#ascending-and-descending)

- [升到天花板](#ascending-to-the-ceiling)

- [上升任意距离](#ascending-up-an-arbitrary-distance)

## 移动工具 { #the-navigation-wand }

WorldEdit 提供了移动[工具](tools/tools.md)，默认绑定到指南针（可以在[配置](../config.md)中更改）。

随时都可以手持指南针左键单击，跳转到所看向的方块（与下文的 jumpto 命令相同）。也可以用指南针右键单击来穿墙（与下文的 thru 命令相同）。

## 脱困 { #freeing-yourself }

> ```text
> /unstuck
> /!
> ```

如果因某种原因卡在方块内部，此命令可以让你脱困。它会将你移到最上方的可用位置；如果本来没有被卡住，则不做任何操作。在非创造模式下，如果往自己所在位置粘贴或生成内容而导致窒息，简短别名（`/!`）往往很有用。

## 跳转到视线中的方块 { #jumping-to-the-block-in-sight }

```text
/jumpto
```

此命令会将你传送到所看方块的顶部。如果该方块位于竖直墙面，就会将你放在峭壁顶部的最边缘。

## 穿墙 { #passing-through-walls }

```text
/thru
```

此命令会沿视线方向将你传送到墙壁另一侧。看向墙壁并使用命令即可。不要向下看着墙壁，否则命令会尝试穿过地面。此命令会将可穿过的墙壁厚度限制在合理范围内。

## 上升与下降 { #ascending-and-descending }

```text
/ascend [levels]
/descend [levels]
```

这两个命令可以让你穿过上方的天花板或下方的地板。例如，身处房屋内时，使用 /ascend 会移动到屋顶。还可以指定上升或下降的层数。例如，位于摩天楼底层时使用 `/ascend 2`，就会到达第 3 层。

## 升到天花板 { #ascending-to-the-ceiling }

```text
/ceil [clearance]
```

此命令会将你升到当前房间的天花板处。不指定净空参数时，会紧贴天花板；指定净空后，头顶会留出更大的空间。脚下会放置一个玻璃方块作为支撑，需要手动移除。

## 上升任意距离 { #ascending-up-an-arbitrary-distance }

```text
/up <distance>
```

此命令会让你上升指定数量的方块。它无法穿墙，脚下会放置一个玻璃方块作为支撑。使用完毕后需要手动移除玻璃。
