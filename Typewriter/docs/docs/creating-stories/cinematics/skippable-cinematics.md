---
title: 可跳过的过场动画（Skippable Cinematics）
source: https://docs.typewritermc.com/docs/creating-stories/cinematics/skippable-cinematics
source_version: 0.8.0
---

# 可跳过的过场动画（Skippable Cinematics）

**开始前**

在开始本教程之前，最好先阅读[过场动画](../cinematics.md)。

在本教程中，你将学习如何允许玩家跳过过场动画的某些部分。

## 添加可跳过的过场动画 {#adding-a-skippable-cinematic}

首先点击面板右上角的+图标，搜索`Add Skippable Cinematic`。单击 + 图标将其添加到你的页面。

添加跳过动画

允许玩家手动跳过过场动画

+

### 配置可跳过的过场动画 {#configuring-the-skippable-cinematic}

在跳过动画的属性面板中，你可以在确认键字段中选择`SNEAK`或`SWAP_HANDS`。该键将是玩家必须按下才能跳过过场动画的键。本指南将使用 SNEAK 键跳过动画。

## 添加可跳过片段 {#adding-a-skippable-part}

现在，在可跳过动画的属性面板中，你可以通过单击操作部分的`Add segment`文本来添加新片段。这将创建一个新段
在“开始帧”和“结束帧”字段中，你可以设置希望玩家能够跳过过场动画的时间。对于本指南，该值为 0 和 100。

## 结果 {#result}

现在你有了一个可跳过的动画，可以通过按确认键字段中设置的键来跳过。

<video controls preload="metadata" src="../../../assets/b51236f3fad4-skip_cinematic_result.webm"></video>

---

原文：[Skippable Cinematics](https://docs.typewritermc.com/docs/creating-stories/cinematics/skippable-cinematics) · 文档版本：0.8.0
