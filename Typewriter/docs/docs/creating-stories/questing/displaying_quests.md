---
title: 显示任务（Displaying Quests）
source: https://docs.typewritermc.com/docs/creating-stories/questing/displaying_quests
source_version: 0.8.0
---

# 显示任务（Displaying Quests）

**开始前**

最好先阅读[任务系统](../questing.md)的理论和[与 NPC 对话目标](talk-objective.md)的实践！

在本教程中，你将学习如何使用Typewriter的任务跟踪系统和占位符向玩家显示任务信息。

## 理解任务追踪 {#understanding-quest-tracking}

Typewriter 在后台通过**事实**记录任务进度。这些事实决定任务的状态；要向玩家**显示**任务信息，还需要追踪一个具体任务。

**大图**

将任务跟踪视为聚光灯。虽然许多任务可能处于活动状态，但跟踪会将一个任务置于聚光灯下，供玩家关注。

### 追踪如何工作 {#how-tracking-works}

当任务被跟踪时，它会成为玩家在任务显示中看到的“突出显示”任务。此跟踪任务成为记分板、侧边栏和自定义 UI 等所有显示系统的焦点，让玩家专注于当前目标。

**一次一个任务**

多个任务可以同时**处于激活状态**，但**同一时间只能追踪一个任务**，以便玩家集中注意力，避免界面混乱。

## 设置任务追踪 {#setting-up-quest-tracking}

### 自动追踪 {#automatic-tracking}

Typewriter在以下情况下自动跟踪任务：

- 当任务激活时
- 当目标变得活跃并且优先级高于当前跟踪的目标时

因此，大多数情况下无需手动管理任务追踪，Typewriter 会自动处理。

### 手动追踪 {#manual-tracking}

有时你想要完全控制跟踪哪个任务。

你可以使用以下命令手动跟踪任务：

```text
/tw quest track <quest_id>
```

或者通过在任务流程中使用**跟踪任务操作**条目。

添加追踪任务

开始追踪玩家的任务

+

## 用占位符显示任务信息 {#displaying-quest-information-with-placeholders}

现在你已经了解了跟踪，让我们看看如何实际向玩家显示任务信息。Typewriter提供了几个占位符，可以动态显示有关当前跟踪的任务的信息。

### 可用的占位符 {#available-placeholders}

|占位符 |描述 |示例输出 |
| --- | --- | --- |
|`%typewriter_tracked_quest%`|跟踪任务的显示名称 |`Kill Zombie Quest`|
|`%typewriter_tracked_objectives%`|以逗号分隔的任务活动目标列表 |`Kill 2 Zombies, Return to Oliver`|
|`%typewriter_tracked_objectives_locations%`|跟踪的可定位目标的位置 |`X: 100, Y: 64, Z: -200`|

## 侧边栏显示 {#sidebar-display}

如果Typewriter正在管理你的侧边栏，你可以使用[目标文本行](../../../adapters/BasicAdapter/entries/quest/objective_lines.md)来显示跟踪任务的目标。

侧边栏的可能设置可以是：

**提示**

注意，Objective Lines 本身没有使用占位符。

[quest_display_manifest.json](../../../assets/b0560b746971-quest_display_manifest.json)

## 任务状态变化 {#quest-status-changes}

你还可以在任务激活或完成时显示视觉反馈。这为玩家创造了令人满意的反馈，并帮助他们了解自己的进度。

常见的方法包括：

- **任务开始或完成时标题公告**
- **粒子效果**庆祝任务完成
- **重要任务里程碑的音效**
- **用于任务更新的聊天消息**

一个示例设置可以是：

[quest_display_sequence.json](../../../assets/e256b269638e-quest_display_sequence.json)

**保持平衡**

虽然视觉反馈很棒，但请避免过多的效果让玩家感到不知所措。简单的标题或声音可能比复杂的动画更有影响力。

---

原文：[Displaying Quests](https://docs.typewritermc.com/docs/creating-stories/questing/displaying_quests) · 文档版本：0.8.0
