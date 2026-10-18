---
title: 交互上下文（Interaction Context）
source: https://docs.typewritermc.com/docs/creating-stories/advanced-interactions/interaction-context
source_version: 0.8.0
---

# 交互上下文（Interaction Context）

**开始前**

对于本教程，我们建议阅读[进阶交互](../advanced-interactions.md)指南，因为我们将在此基础上进行构建。

在本教程中，你将了解交互上下文以及如何使用它们。我们将创建一个交互，玩家需要指定给出的鲜花数量。

## 什么是交互上下文？ {#what-is-an-interaction-context}

交互上下文用于将变量传给序列中的后续条目。可以读取玩家输入、暂存数据，供后续交互使用。
无论是在未来的步骤中使用输入还是触发操作（例如在单击的块上生成效果）。这种灵活性使你的故事更具适应性和吸引力。

**多种型号**

在本教程中，我们将使用`integer input dialogue`但还有更多类型，例如`string input dialogue`。

## 创建输入对话 {#creating-an-input-dialogue}

这个示例让玩家输入想要领取的花朵数量，通过整数输入对话读取这个数值。
要添加整数输入对话框，请转到面板的右上角并单击 + 图标。搜索`Add Integer Input Dialogue`并将其添加到你的序列中
（在本指南中，我们将其链接到[进阶交互](../advanced-interactions.md)的逐字对话）。

添加整数输入对话框

一个除整数之外的输入对话框

+

## 配置整数输入对话 {#configuring-the-integer-input-dialogue}

现在在整数输入对话框中设置你想要的文本。对于本指南，我们将使用：`How many flowers would you like?`。

**系列**

如果需要，你还可以配置整数输入对话框的范围

## 添加给予花朵的动作 {#adding-the-give-flowers}

现在我们需要创建一个当玩家指定鲜花数量时触发的事件。右键单击`Integer Input Dialogue`条目，然后单击`+ link with ...`打开搜索菜单。搜索`Give Item`并将其添加到页面。

添加赠送物品

给玩家一个物品

+

**提供物品条目**

如果你不知道“给予物品条目”的工作原理，那么你应该首先阅读[给予物品](../interactions/items.md)

## 配置给予花朵的动作 {#configuring-the-give-flowers}

接下来配置给予物品的条目。示例使用 `Red Tulip`。

**定制物品**

这里要使用自定义物品。原文编写时，序列化物品的数量还不支持使用变量。

### 创建交互上下文变量 {#creating-the-interaction-context-variable}

在 Give Item 条目的 item 字段中添加组件，选择 amount。点击 amount 字段旁的动态变量图标，搜索 `Add Interaction Context Variable`。

添加交互上下文变量

使用另一个条目中的一些数据填充字段

+

完成后，你可以在输入字段中选择`Integer Input Dialogue`条目。

#### 视频教程 {#video-tutorial}

<video controls preload="metadata" src="../../../assets/75777b94ea6e-configure-spoken-interaction-context.webm"></video>

## 结果 {#result}

现在当玩家指定鲜花数量时，玩家将收到指定数量的鲜花。

<video controls preload="metadata" src="../../../assets/09e6cf1228a5-interaction-context-result.webm"></video>

---

原文：[Interaction Context](https://docs.typewritermc.com/docs/creating-stories/advanced-interactions/interaction-context) · 文档版本：0.8.0
