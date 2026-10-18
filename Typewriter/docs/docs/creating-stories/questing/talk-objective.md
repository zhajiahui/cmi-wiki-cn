---
title: 与 NPC 对话目标（Talk To NPC Objective）
source: https://docs.typewritermc.com/docs/creating-stories/questing/talk-objective
source_version: 0.8.0
---

# 与 NPC 对话目标（Talk To NPC Objective）

**开始前**

在开始本教程之前，最好先阅读[任务系统](../questing.md)。

**NPC**

本教程要求你已经使用[实体与 NPC](../entity-extension.md)指南创建了 NPC。

在本教程中，你将学习如何创建任务：

- 玩家与 NPC 互动
- NPC给玩家一个任务
- 玩家通过与不同的 NPC 交谈来完成任务。

## 任务流程 {#quest-flow}

| 状态 | 事实 | 说明 | 状态转换 |
| --- | --- | --- | --- |
| 未开始 | `Talk Quest Fact = 0` | 玩家尚未开始任务 | 与第一个 NPC 对话 → 已接受任务 |
| 已接受任务 | `Talk Quest Fact = 1` | 玩家已从第一个 NPC 处接受任务 | 与第二个 NPC 对话 → 已完成 |
| 已完成 | `Talk Quest Fact = 2` | 玩家与第二个 NPC 对话后完成任务 | 重置任务 → 未开始 |

## 任务设置 {#quest-setup}

本指南分为 2 部分。

- [与 NPC 对话目标](talk-objective.md#manifest-section)：介绍如何设置任务和添加目标。
- [与 NPC 对话目标](talk-objective.md#sequence-section)：解释如何让npc给出任务并且其他npc对任务做出反应。

## 呈现部分 {#manifest-section}

**开始前**

你必须已经使用[实体与 NPC](../entity-extension.md)指南创建了 2 个 NPC。

> 在本指南中，我们将使用年轻的 npc`James`和老人 npc`Old Man`。

![](../../../assets/2e8f18bf01d3-npc-example.0bc9ff5.821.avif)

> 在本节中，我们将创建任务并向其添加目标。

### 创建任务 {#creating-the-quest}

现在在呈现页面中，单击右上角的**+**按钮并搜索`Quest`。单击**+**按钮将其添加到你的页面。

添加任务

任务定义

+

#### 配置任务条目 {#configuring-the-quest-entry}

现在在任务条目内设置以下字段：

- **显示名称**:`TalkQuest`
- **有效条件**:`Talk Quest Fact >= 1`
- **已完成条件**:`Talk Quest Fact = 2`
  *在本指南中，我使用了永久事实*

### 添加目标 {#adding-the-objective}

你现在已成功创建任务条目。现在我们需要将目标添加到任务中。
点击右上角的**+**按钮，搜索`Add Interact Entity Objective`。单击**+**按钮将其添加到你的页面。

添加交互实体目标

与实体交互

+

### 配置目标条目 {#configuring-the-objective-entry}

在目标条目内设置以下字段：

- **探索**:`TalkQuest`
- **条件**:`Talk Quest Fact = 1`
- **实体**:`Old Man`（或者你为第二个 npc 命名的名称）
- **覆盖显示**:`Talk to the Old Man`

### 呈现结果 {#manifest-result}

[manifest.json](../../../assets/2df87e26c603-manifest.json)

[static.json](../../../assets/eba0f36e2739-static.json)

## 序列部分 {#sequence-section}

**开始前**

建议在开始本节之前充分了解[第一个交互](../interactions.md)和[事实](../facts.md)。

> 在本节中，我们将创建向玩家提供任务以及其他 npc 对任务做出反应的序列。

### 与第一个 NPC 交互 {#interaction-with-the-first-npc}

现在我们需要创建与第一个 npc 的交互。这是玩家将收到任务的地方。
点击右上角的**+**按钮，搜索`Add Entity Interact Event`。单击**+**按钮将其添加到你的页面。

添加实体交互事件

当玩家点击一个实体时

+

在条目内将“定义”字段设置为你创建的第一个 npc。在本例中，我们将使用`James`。

### 为第一个 NPC 添加对话 {#adding-dialogue-to-the-first-npc}

现在，当你点击第一个NPC时，什么也没有发生。让我们为 npc 添加一些对话。

> 以下步骤是可选的，但建议执行，以使任务更加身临其境。

1. 将`New Option`添加到序列中并设置以下字段：
   - **文本**:`Could you help me with something?`
   - **选项 1**:`Yeah sure, whats up?`
   - **选项 2**:`No sorry.`
2. 现在，在选项 1 中添加一个带有字段的逐字对话触发器：
   - **文本**:`Go talk to that old man on the other side.`
   - **持续时间**:`2s 500ms`
3. 在该逐字对话中添加修改器：`Talk Quest Fact = 1`

### 与第二个 NPC 交互 {#interaction-with-the-second-npc}

现在你已经创建了第一个 NPC 交互。现在我们需要创建第二个 npc 交互。这是玩家完成任务的地方。
添加新的`Add Entity Interact Event`条目并将定义字段设置为你创建的第二个 npc。在本例中，我们将使用`Old Man`。

添加实体交互事件

当玩家点击一个实体时

+

### 配置第二个 NPC 的交互 {#configuring-the-second-npc-interaction}

现在我们将使交互触发逐字对话。为此，右键单击`Entity Interact Event`并选择`Link with ...`选择`Triggers | 1`并搜索`Add Spoken`。

添加逐字对话

向玩家显示动画消息

+

#### 配置逐字对话 {#configuring-the-spoken}

在逐字对话条目内设置以下字段：

- **条件**:`Talk Quest Fact = 1`
- **修改器**:`Talk Quest Fact = 2`
- **文本**:`Thanks for going to me!`

### 序列结果 {#sequence-result}

[sequence.json](../../../assets/e702de34915e-sequence.json)

[manifest.json](../../../assets/2df87e26c603-manifest.json)

[static.json](../../../assets/eba0f36e2739-static.json)

## 结果 {#result}

现在你已经成功创建了一个任务，玩家可以与一个 npc 交互并通过与另一个 npc 交谈来完成任务。

<video controls preload="metadata" src="../../../assets/ded8e1935082-talk-objective-result.webm"></video>

**任务状态变更**

在此视频中，你可以看到当任务开始和结束时，它会显示标题和一些额外的效果。要添加此内容，请阅读：**很快**

**可视化路径**

你还可以使用`Interact Entity Objectives Path Stream`条目来可视化任务的路径。

添加交互实体目标路径流

交互实体目标的路径流

+

在条目内将`Road`字段设置为你创建的道路网络，它将为你可视化通往 npc 的路径！

在[道路网络](../road-network.md)中了解有关道路网络的更多信息。

---

原文：[Talk To NPC Objective](https://docs.typewritermc.com/docs/creating-stories/questing/talk-objective) · 文档版本：0.8.0
