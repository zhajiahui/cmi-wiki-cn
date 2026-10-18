---
title: 过场动画（Cinematics）
source: https://docs.typewritermc.com/docs/creating-stories/cinematics
source_version: 0.8.0
---

# 过场动画（Cinematics）

**开始前**

本教程假定已按[安装指南](../getting-started/installation.md#basic-extension)安装 Basic Extension。
另外，请确保你已阅读[界面布局](../getting-started/layout.md)文档并创建了**过场动画**页面。

在本教程中，你将学习如何在交互中创建和查看动画！

## 什么是过场动画？ {#what-are-cinematics}

过场动画是可以在交互中播放的定时动作序列。它们用于创建过场动画或其他定时事件。

## 创建过场动画 {#creating-a-cinematic}

让我们开始创建一个简单的镜头动画。

### 添加镜头过场动画 {#adding-a-camera-cinematic}

首先点击面板右上角的+图标，搜索`Add Camera Cinematic`。单击 + 图标将其添加到你的页面。

添加过场动画

开始新的过场动画

+

### 创建片段 {#creating-a-segment}

点击页面中的 `New Camera Cinematic` 条目，再通过操作菜单点击 `Add Segment`（1），向轨道添加片段。

![添加镜头过场动画片段](../../assets/fb11c39cdd30-segments.e1effa5.597.avif)

创建片段后，点击它（2），打开该片段的属性面板。

### 修改镜头片段 {#modifying-the-camera-segment}

镜头过场动画片段包含一条路径，路径由服务器世界中的位置列表组成。指定多个位置时，玩家会在这些位置间移动；只指定一个位置时，玩家保持不动。
要创建路径，请单击属性面板中`path(0)`处的 + 图标。

要在路径中设置位置，你有 2 个选项：使用内容模式或自行配置。

#### 使用内容模式 {#using-the-content-mode}

内容模式允许你获取玩家的当前位置并为你填写字段。

<video controls preload="metadata" src="../../assets/dc2ec22a75b7-content-mode.webm"></video>

#### 手动配置 {#configuring-it-yourself}

也可以打开 `Path #1` 字段，手动配置路径上的位置，包括：

- **世界**：过场动画发生的世界。
- **X**：位置的 x 坐标。
- **Y**：位置的 y 坐标。
- **Z**：位置的 z 坐标。
- **俯仰角**：摄像机的俯仰角。
- **偏航**：摄像机的偏航。

**持续时间**：从当前位置到下一个位置所需的时间，以 tick 为单位。理解这个设置，才能正确安排过场动画的移动时间。

### 理解持续时间 {#understanding-duration}

路径点的持续时间是从该点到**下一个点**所需的**帧（tick）**的数量。

主要原则：

1. **最后一点的持续时间被忽略**
   -> 没有“下一个”点可以移动
2. **各段移动时间之和必须等于片段总时长**
   -> 所有移动时间必须加起来
3. **未指定的持续时间自动计算**
   -> 剩余时间平均分配

#### 示例：4 个点、100 帧片段 {#example-4-points-100-frame-segment}

**设置：**

- **点 1**：持续时间未指定
- **点 2**：持续时间 50 帧
- **第 3 点**：持续时间未指定
- **点 4**：持续时间 10 帧
  *（忽略-这是最后一点）*

**结果：**

- **点 1 → 点 2**：25 帧
  *（自动计算）*
- **点 2 → 点 3**：50 帧
  *（按规定）*
- **点 3 → 点 4**：25 帧
  *（自动计算）*

*自动计算的持续时间：*
`(100 - 50) ÷ 2 = 25 frames each`

**提示**

如果只有 2 个点，就不必指定持续时间，因为这段移动时长必然等于片段总时长。留空即可自动计算。

重复此过程以在路径中创建更多位置。

## 结果 {#result}

这里使用上面持续时间示例中的设置。可以执行命令查看过场动画：
`/tw cinematic start (page name)`或将`Add cinematic`添加到序列页面。

<video controls preload="metadata" src="../../assets/63db6955fc5f-final-camera-cinematic.webm"></video>

---

原文：[Cinematics](https://docs.typewritermc.com/docs/creating-stories/cinematics) · 文档版本：0.8.0
