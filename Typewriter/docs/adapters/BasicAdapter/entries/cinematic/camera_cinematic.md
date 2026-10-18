---
title: 镜头过场动画（Camera Cinematic）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/camera_cinematic
source_version: 0.8.0
---

# 镜头过场动画（Camera Cinematic）

`Camera Cinematic`条目用于创建过场动画镜头路径。

各路径点的持续时间，根据片段总时长和已指定的路径点时长计算。
假设你有一个持续时间为 300 个tick的线段，并且它有 3 个路径点。
然后我们将第二个路径点的持续时间指定为 200 个tick。
路径点之间的最终持续时间如下：

|来自 |至 |持续时间 |
| --- | --- | --- |
| 1 | 2 | 100 | 100
| 2 | 3 | 200 | 200

**警告**

由于路径点的持续时间是从该点到下一个点的持续时间，
最后一个路径点的持续时间始终为`0`。
无论最后一个路径点指定的持续时间如何。

## 用途示例 {#how-could-this-be-used}

当你想要将玩家的注意力引导到特定对象/位置时。
或者当你想炫耀构建时。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 片段（Segments）

必填 · 列表 · 片段

片段是过场动画中的一个时间区间，可在此期间执行动作或显示信息。

**说明**

同一条目中的片段无法重叠。需要重叠片段时，请新建条目。

---

原文：[Camera Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/camera_cinematic) · 文档版本：0.8.0
