---
title: 指定世界的过场动画（World Specific Cinematics）
source: https://docs.typewritermc.com/docs/creating-stories/cinematics/world-specific
source_version: 0.8.0
---

# 指定世界的过场动画（World Specific Cinematics）

**开始前**

在开始本教程之前，最好先阅读[过场动画](../cinematics.md)。

在本教程中，你将学习如何创建特定于世界的动画。此功能允许你创建 1 个可在多个世界中使用的动画。

## 创建动态变量 {#creating-the-dynamic-variable}

首先，我们需要创建一个动态变量。该变量将用于确定玩家所在的世界。为此，请按照以下步骤操作：

1. 转到你的镜头动画并单击一个片段
2. 在片段内某 1 条路径旁，点击动态变量图标。
3. 搜索 `Player World Position Variable`，点击后将其添加到片段中。

添加玩家世界位置变量

在玩家世界中的绝对地位

+

### 配置动态变量 {#configuring-the-dynamic-variable}

**重复**

对镜头过场动画片段内的所有路径重复此步骤。

现在，在**镜头过场动画片段**的属性面板中，你可以设置过场动画的坐标。

![配置动态变量](../../../assets/a77607690aaf-world-specific-player-variable.47acd57.517.avif)

#### 世界值在哪里？ {#where-is-the-world-value}

好问题，世界值消失了，因为我们使用`Player World Position Variable`来确定世界。
玩家所在的世界将是所使用的世界。

## 结果 {#result}

**实体**

在本指南中，我们使用了[添加实体](entities.md)教程中的实体动画和[添加对话](dialogue.md)。这是为了演示动态变量的使用。

<video controls preload="metadata" src="../../../assets/ab8a3a9ef594-world-specific.webm"></video>

---

原文：[World Specific Cinematics](https://docs.typewritermc.com/docs/creating-stories/cinematics/world-specific) · 文档版本：0.8.0
