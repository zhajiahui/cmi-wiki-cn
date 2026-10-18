---
title: 实体活动（Entity Activities）
source: https://docs.typewritermc.com/docs/creating-stories/entity-extension/activities
source_version: 0.8.0
---

# 实体活动（Entity Activities）

**开始之前**

在开始本教程之前，请务必阅读[实体与 NPC](../entity-extension.md)。

在本教程中，你将学习如何将活动分配给实体。

## 什么是活动？ {#what-are-activities}

默认情况下，实体是静态的。幸运的是，活动可以让他们充满活力。例如，你可以设置一个活动，当玩家接近实体时或在特定时刻（例如玩家与实体交谈时）触发。你甚至可以使用道路网络使实体在不同节点之间旅行！

## 为实体指定活动 {#assigning-an-activity-to-an-entity}

在本教程中，我们将配置**Oliver**自动沿着道路网移动。当玩家与他互动时，他会停下来并转身面对他们。

这里使用 **In Dialogue Activity**，分别设置玩家正在与实体对话和未与实体对话时的两种行为。

让我们通过添加`In Dialogue Activity`来更新 Oliver 的实例。

添加对话活动

对话活动

+

## 配置活动 {#configuring-the-activity}

`In Dialogue Activity`控制两个子活动，具体取决于玩家当前是否正在与实体交谈。

![对话活动面板图像](../../../assets/2c8889550822-in_dialogue_activity.fea2a9f.648.avif)

- 对于**谈话活动**，我们将使用`Look Close Activity`，因此 Oliver 在对话过程中会直视玩家。
- 对于**空闲活动**，我们将使用`Patrol Activity`，允许 Oliver 在道路网络的节点之间行走。

如果还没有创建道路网络，先阅读[道路网络](../road-network.md)教程，再点击采集按钮添加所需节点。

![巡逻活动面板图片](../../../assets/0239ed4a2916-patrol_activity.412a105.532.avif)

## 最终结果 {#final-result}

当玩家与奥利弗互动时，他会停止巡逻并转向面对他们。一旦交互结束，他将恢复在路网节点之间的巡逻。

### 页面预览 {#page-preview}

[manifest.json](../../../assets/57d659a2984d-manifest.json)

[static.json](../../../assets/1f470fc885f9-static.json)

[sequence.json](../../../assets/8f6751545705-sequence.json)

### 游戏内预览 {#in-game-preview}

<video controls preload="metadata" src="../../../assets/dd6284ab7abf-result.webm"></video>

---

原文：[Entity Activities](https://docs.typewritermc.com/docs/creating-stories/entity-extension/activities) · 文档版本：0.8.0
