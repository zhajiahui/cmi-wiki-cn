---
title: 条件对话（Conditional dialogue）
source: https://docs.typewritermc.com/docs/creating-stories/interactions/conditional-dialogue
source_version: 0.8.0
---

# 条件对话（Conditional dialogue）

**开始前**

开始前，建议先阅读[第一个交互](../interactions.md)和[事实](../facts.md)。
另外，请确保你已创建**序列**页面。

在本教程中，你将学习如何创建条件对话。这意味着如果玩家将某个事实设置为特定值，它将显示正确的对话。

## 添加逐字对话 {#adding-a-spoken}

首先我们需要添加一个逐字对话。这可以通过学习[第一个交互](../interactions.md)教程来学习。

## 配置逐字对话 {#configuring-the-spoken}

在逐字对话中，我们将字段文本设置为`Hey you clicked me for the first time.`

### 设置条件 {#setting-the-criteria}

在逐字对话的属性面板中，点击 criteria 字段旁的 + 图标，选择要使用的事实。这里使用名为 `Flower Clicked` 的永久事实，组设为玩家组。

![花点击事实](../../../assets/974ed87c1b44-flower-clicked-fact.dfda5a1.539.avif)

在条件内，将运算符设置为`==`并将值设置为`0`。

### 配置修改器 {#configuring-the-modifier}

接下来修改事实，使再次点击花朵时显示不同的对话。点击 modifier 字段旁的 + 图标，选择与条件相同的事实，将运算符设为 `=`，值设为 `1`。

![添加逐字对话字段](../../../assets/103f8ff25826-add-spoken-fields.2df9135.528.avif)

## 添加第二段逐字对话 {#adding-the-second-spoken}

右键点击 `On Interact Block Event`，选择 `+ Link with ...`，搜索 `Add Spoken`，点击 + 图标，将第二段逐字对话添加到序列中。
在文本字段中，我们将设置`Wow you clicked me again!`
你的序列页面应如下所示：

![条件对话序列](../../../assets/38a06cec9999-conditional-dialogue-sequence.6fa3c22.863.avif)

### 配置第二段逐字对话的条件 {#configuring-the-second-spoken-criteria}

在第二段逐字对话中，点击 criteria 字段旁的 + 图标，再次选择 `Flower Clicked` 事实，将运算符设为 `==`，值设为 `1`。

### 补充对话 {#additional-dialogue}

要在单击花朵时添加更多对话或交互，请使用运算符将另一个修改器设置为`=`，将值设置为`2`（或任何其他值），然后重复前面的步骤。

## 结果 {#result}

第一次点击花朵时，会显示第一段对话；再次点击时，显示第二段对话。

<video controls preload="metadata" src="../../../assets/cf8fc87b0a91-final-result-conditional-dialogue.webm"></video>

---

原文：[Conditional dialogue](https://docs.typewritermc.com/docs/creating-stories/interactions/conditional-dialogue) · 文档版本：0.8.0
