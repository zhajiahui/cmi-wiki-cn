---
title: 与实体交互（Interacting with an entity）
source: https://docs.typewritermc.com/docs/creating-stories/entity-extension/interacting
source_version: 0.8.0
---

# 与实体交互（Interacting with an entity）

**开始前**

在开始本教程之前，最好先阅读[实体与 NPC](../entity-extension.md)。

在本教程中，你将学习如何与实体交互。

## 添加实体交互事件 {#adding-the-entity-interact-event}

首先，我们需要将`Add On Entity Interact Event`条目添加到我们的序列中。这可以通过单击面板右上角的 + 图标并搜索`Add On Entity Interact Event`来完成。单击 + 图标将其添加到你的页面。

添加实体交互事件

当玩家点击一个实体时

+

### 选择定义 {#selecting-the-definition}

在 `New Entity Interact Event` 的属性面板中，通过 definition 字段选择要交互的实体定义。这里使用 Oliver。

![实体交互事件字段](../../../assets/3a7f7589f256-entity-interact-event-fields.f2ab662.540.avif)

## 添加事件 {#adding-the-event}

现在我们需要添加一个当玩家与实体交互时触发的事件（在本教程中我们将使用逐字对话）。右键单击`New Entity Interact Event`条目，然后单击`+ link with ...`打开搜索菜单。搜索`Add Spoken`并将其添加到页面。

添加逐字对话

向玩家显示动画消息

+

将说话者设置为 oliver 定义，并将文本字段设置为`Hello I am Oliver.`。

## 结果 {#result}

你现在可以发布你的页面，在游戏中，与 Oliver 交互时，它应该如下所示：

<video controls preload="metadata" src="../../../assets/b90d19c13481-interact-entity-result.webm"></video>

---

原文：[Interacting with an entity](https://docs.typewritermc.com/docs/creating-stories/entity-extension/interacting) · 文档版本：0.8.0
