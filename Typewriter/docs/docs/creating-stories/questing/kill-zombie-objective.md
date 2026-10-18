---
title: 击杀僵尸目标（Kill Zombie Objective）
source: https://docs.typewritermc.com/docs/creating-stories/questing/kill-zombie-objective
source_version: 0.8.0
---

# 击杀僵尸目标（Kill Zombie Objective）

**开始前**

在开始本教程之前，最好先阅读[任务系统](../questing.md)。

**NPC**

本教程要求你已经使用[实体与 NPC](../entity-extension.md)指南创建了 NPC。

在本教程中，你将学习如何创建任务：

- 玩家与 NPC 互动
- NPC 给玩家一个任务，目标是杀死 2 个僵尸。
- 玩家通过杀死 2 只僵尸来完成目标。
- 玩家返回NPC处完成任务。

## 任务流程 {#quest-flow}

| 状态 | 事实 | 说明 | 状态转换 |
| --- | --- | --- | --- |
| 未开始 | `Zombie Quest Fact = 0` | 玩家尚未开始任务 | 与 NPC 对话 → 已接受任务 |
| 已接受任务 | `Zombie Quest Fact = 1` `Kill Zombie Fact = 0` | 玩家已从 NPC 处接受任务 | 击杀僵尸 → 击杀僵尸中 |
| 击杀僵尸中 | `Zombie Quest Fact = 1` `Kill Zombie Fact >= 2` | 玩家正在击杀僵尸 | 返回 NPC 处 → 已完成 |
| 已完成 | `Zombie Quest Fact = 2` | 玩家已击杀 2 只僵尸，完成任务 | 重置任务 → 未开始 |

## 任务设置 {#quest-setup}

本指南分为 2 部分。

- [击杀僵尸目标](kill-zombie-objective.md#manifest-section)：介绍如何设置任务和添加目标。
- [击杀僵尸目标](kill-zombie-objective.md#sequence-section)：解释如何让NPC给出任务以及如何使目标可完成。

## 呈现部分 {#manifest-section}

**开始前**

在开始本教程之前，请确保你已完成[实体与 NPC](../entity-extension.md)指南。

> 在本指南中，我们将使用 Oliver NPC 作为任务提供者。

另请确保你已创建呈现页面。

> 在本节中，我们将设置任务并将目标添加到呈现中。

### 创建任务 {#creating-the-quest}

现在在呈现页面中，单击右上角的**+**按钮并搜索`Quest`。单击**+**按钮将其添加到你的页面。

添加任务

任务定义

+

#### 配置任务条目 {#configuring-the-quest-entry}

现在在任务条目内设置以下字段：

- **显示名称**:`ZombieQuest`
- **有效条件**:`Zombie Quest Fact >= 1`
- **已完成条件**:`Zombie Quest Fact = 2`
  *在本指南中，我使用了永久事实*

### 添加目标 {#adding-the-objective}

现在在任务条目内，单击右上角的**+**按钮并搜索`Completable Objective`。单击**+**按钮将其添加到你的页面。

添加可完成的目标

可以显示已完成阶段的目标

+

### 配置目标条目 {#configuring-the-objective-entry}

现在在目标条目内设置以下字段：

- **探索**:`ZombieQuest`
- **显示条件**:`Zombie Quest Fact = 1`
- **已完成条件**:`Zombie Quest Fact = 1`+`Killed Zombies Fact >= 2`
- **显示**:`Kill 2 Zombies`

**可选**

在显示内部，你还可以使用[PlaceholderAPI](../../helpful-features/placeholderapi.md)选择显示进度

*示例：*`Kill 2 zombies (%typewriter_nOfQzADcAmcR6ao%/2)`

> 我们将在最终结果中使用它！

**可选 #2**

你还可以添加第二个目标，要求玩家返回 NPC。

- **显示条件**:`Zombie Quest Fact = 1`+`Kill Zombie Fact >= 2`
- **已完成条件**:`Zombie Quest Fact = 2`
- **显示**:`Return to Oliver`

有关如何执行此操作的更多信息，请参阅[与 NPC 对话目标](talk-objective.md)。

### 呈现结果 {#manifest-result}

[manifest.json](../../../assets/c88a89851e02-manifest.json)

[static.json](../../../assets/ff26a7705109-static.json)

## 序列部分 {#sequence-section}

**开始前**

建议在开始本节之前充分了解[第一个交互](../interactions.md)和[事实](../facts.md)。

> 在本节中，我们将创建为玩家提供任务并使目标可完成的序列。

### 与 Oliver 交互 {#interaction-with-oliver}

现在我们需要创建与 Oliver 的交互。这是玩家将收到任务的地方。
点击右上角的**+**按钮，搜索`Add Entity Interact Event`。单击**+**按钮将其添加到你的页面。

添加实体交互事件

当玩家点击一个实体时

+

在条目内将“定义”字段设置为`Oliver`（或你为 npc 命名的内容）。

### 为 Oliver 添加对话 {#adding-dialogue-to-oliver}

现在，当你单击奥利弗时，什么也不会发生。如果能给npc添加一些对话就好了。

> 以下步骤是可选的，但建议执行，以使任务更加身临其境。

1. 将`New Option`添加到序列中并设置以下字段：
   - **文本**:`Could you help me with something?`
   - **选项 1**:`Yeah sure, whats up?`
   - **选项 2**:`No sorry.`
2. 现在，在选项 1 中添加一个带有字段的逐字对话触发器：
   - **文本**:`Go kill 2 zombies.`
   - **持续时间**:`1s`
3. 在该逐字对话中添加修改器：`Zombie Quest Fact = 1`

### 击杀时增加事实值 {#on-kill-increase-fact}

现在我们需要增加玩家杀死僵尸的事实。为此，我们需要将`On Player Kill Entity`事件添加到序列中。

添加玩家杀死实体

当玩家杀死一个实体时

+

在条目内启用实体类型并将实体类型设置为`Zombie`。

### 增加事实值 {#increasing-the-fact}

现在我们需要增加玩家杀死僵尸的事实。为此，右键单击`On Player Kill Entity`并选择`Link with ...`选择`Triggers | 1`并搜索`Add Simple Action`。

添加简单动作

修改事实的简单动作

+

在条目内设置以下字段：

- **条件**:`Zombie Quest Fact = 1`
- **modifier**（修改器）：`Zombies Killed Fact + 1`

每当玩家杀死僵尸时，事实就会增加 1，并且只有在玩家有任务时才会这样做。

### 序列结果 {#sequence-result}

[sequence.json](../../../assets/a2ee9d640b78-sequence.json)

[manifest.json](../../../assets/c88a89851e02-manifest.json)

[static.json](../../../assets/ff26a7705109-static.json)

## 最终结果 {#final-result}

现在，当你单击奥利弗时，你将看到对话，当你单击第一个选项时，你将收到任务。当你杀死 2 个僵尸时，目标就完成了。

<video controls preload="metadata" src="../../../assets/02002ef03e5a-kill-zombie-objective-result.webm"></video>

---

原文：[Kill Zombie Objective](https://docs.typewritermc.com/docs/creating-stories/questing/kill-zombie-objective) · 文档版本：0.8.0
