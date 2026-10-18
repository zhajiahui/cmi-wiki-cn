---
title: 第一个交互（First Interaction）
source: https://docs.typewritermc.com/docs/creating-stories/interactions
source_version: 0.8.0
---

# 第一个交互（First Interaction）

**开始前**

本教程假定你已按[安装指南](../getting-started/installation.md#basic-extension)安装 Basic Extension。

另外，请确保你已阅读[界面布局](../getting-started/layout.md)文档并创建了**序列**页面。

让我们创建我们的第一个交互。我们的示例交互将包含以下步骤：

1. 玩家点击一朵花。
2. 将打开聊天对话框。

如果你在此过程中需要任何帮助，请随时在我们的[Discord](https://discord.gg/HtbKyuDDBw)上寻求帮助。

## 什么是交互？ {#what-are-interactions}

当玩家与某物交互并触发事件时，就会发生交互。在本教程中，玩家点击花朵是交互，聊天对话是触发的事件。

## 创建交互 {#creating-an-interaction}

让我们从创建一个条目开始。单击面板右上角的 + 图标并搜索`on interact with block`。单击 + 图标将其添加到你的页面。

添加与块交互

当玩家与方块交互时

+

### 配置交互 {#configuring-the-interaction}

在属性面板中，将方块设为 `Red Tulip`（1），名称设为 `on flower click`（2）。

![配置与流表项交互](../../assets/ff2f92a436d5-on_flower_click.60a7569.269.avif)

## 创建事件 {#creating-an-event}

现在我们需要创建一个当玩家点击花朵时触发的事件。右键单击`On Flower Click`条目，然后单击`+ link with ...`打开搜索菜单。搜索`Add Spoken`并将其添加到页面。

<video controls preload="metadata" src="../../assets/14b6c7acec41-add-spoken.webm"></video>

### 配置事件 {#configuring-the-event}

在属性面板中，将文本设置为`Hello! I am a flower.`并将持续时间设置为`1s`。

### 配置说话者 {#configuring-the-speaker}

请按照以下步骤配置说话者：

1. 单击文本`Select a speaker`，然后在搜索菜单中单击`Add Simple Speaker`。
2. 选择`Add static`并为该静态页面命名。
3. 单击简单说话者。
4. 在属性面板中，将“显示名称”设置为`A beautiful flower`。

<video controls preload="metadata" src="../../assets/529c5ab2ac2c-simple-speaker.webm"></video>

## 结果 {#result}

你现在可以发布你的页面，在游戏中，单击花朵时它应该如下所示：

<video controls preload="metadata" src="../../assets/37fdfc276168-final-result-default.webm"></video>

---

原文：[First Interaction](https://docs.typewritermc.com/docs/creating-stories/interactions) · 文档版本：0.8.0
