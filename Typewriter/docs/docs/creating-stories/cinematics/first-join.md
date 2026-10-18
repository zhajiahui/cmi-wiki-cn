---
title: 首次加入时播放过场动画（First Join Cinematic）
source: https://docs.typewritermc.com/docs/creating-stories/cinematics/first-join
source_version: 0.8.0
---

# 首次加入时播放过场动画（First Join Cinematic）

**开始前**

在开始之前，建议阅读以下部分：[第一个交互](../interactions.md)、[过场动画](../cinematics.md)和[事实](../facts.md)。确保你已创建序列和过场动画页面。

在本教程中，你将学习如何创建在玩家首次加入服务器时播放的动画。

## 添加加入事件条目 {#adding-the-join-entry}

首先，我们需要将`Add On Player Join`条目添加到我们的序列中。这可以通过单击面板右上角的 + 图标并搜索`Add On Player Join`来完成。单击 + 图标将其添加到你的页面。

添加玩家加入

当玩家加入服务器时

+

## 等待交互 {#waiting-for-interaction}

**早期启动过场动画**

在玩家完全加载服务器之前，Typewriter可能会提前开始过场动画。如果玩家的互联网连接速度较慢或计算机性能较低，则可能会发生这种情况。在这种情况下，玩家可以在过场动画的中间而不是开始时加入服务器。为了解决这个问题，建议添加一个选项或延迟，让玩家需要在过场动画开始之前执行操作。

要将选项添加到序列中，最好阅读[添加选项](../interactions/options.md)页面。在本教程中，我们将使用`New Option`和`Start Cinematic`选项。

### 配置条件 {#configuring-the-criteria}

**选项**

如果使用了[首次加入时播放过场动画](first-join.md#waiting-for-interaction)中的选项，应在那个选项中配置以下内容，**而不是**在启动过场动画的条目中配置。

现在我们需要配置过场动画的条件。这可以通过单击属性面板中条件字段旁边的`+`图标来完成。然后，你可以选择你想要使用的事实。在本教程中，我们将使用名为`First Join`的永久事实，并将组设置为玩家组。

![第一个连接事实](../../../assets/f848be250f05-first-join-fact.2803121.524.avif)

在条件内，将运算符设置为`==`并将值设置为`0`。

### 配置修改器 {#configuring-the-modifier}

你已经配置了条件，但现在我们需要修改事实，以便当你再次加入时，不会播放过场动画。这可以通过单击属性面板中修改器字段旁边的`+`图标来完成。然后，你可以选择要修改的事实。对于本教程，我们将使用相同的事实作为条件。在修改器内，将运算符设置为`=`并将值设置为`1`。

现在你的属性面板应该看起来像这样：

![添加过场动画场](../../../assets/94898bbdbc8d-add-cinematic-fields.b15ef7e.535.avif)

## 添加 `Add Cinematic` 条目 {#adding-the-add-cinematic-entry}

现在我们需要将`Add Cinematic`条目添加到我们的序列中。这可以通过右键单击`New On Player Join`条目并选择`+ Link with ...`来完成。然后，搜索`Add Cinematic`并单击 + 图标将其添加到你的序列中。现在你的序列页面应如下所示：

![附加影院](../../../assets/7f11e17cc0c8-add-cinematic.9e15988.735.avif)

在`New Cinematic`内，通过页面字段的属性面板选择要触发的动画。在本教程中，我们将使用`Tutorial_Cin`动画。

## 结果 {#result}

现在，当玩家第一次加入服务器时，就会播放过场动画。当玩家再次加入时，动画将不会播放。

<video controls preload="metadata" src="../../../assets/f07013ba313f-first-join-result.webm"></video>

---

原文：[First Join Cinematic](https://docs.typewritermc.com/docs/creating-stories/cinematics/first-join) · 文档版本：0.8.0
