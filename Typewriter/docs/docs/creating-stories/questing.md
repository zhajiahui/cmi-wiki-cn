---
title: 任务系统（Questing）
source: https://docs.typewritermc.com/docs/creating-stories/questing
source_version: 0.8.0
---

# 任务系统（Questing）

**任务扩展**

在继续使用任何与任务相关的功能之前，你必须安装任务扩展。

**作家笔记**

原文的任务部分正在重写。完整的旧版文档见：[**旧任务文档**](https://docs.typewritermc.com/0.7.0/docs/creating-stories/questing)。

## Typewriter 的任务实现方式 {#typewriters-unique-approach-to-quests}

**大创意**

在 Typewriter 中，任务是游戏状态的**直观呈现**。真正的进度由永久事实记录，任务负责向玩家显示这些进度。

### 🔑 关键概念 {#-key-concept}

传统任务插件通常在完成任务时直接推进进度，Typewriter 则将两部分分开：

- **游戏状态**：实际推动进度的事实。
- **任务显示**- 玩家在 UI 中看到的内容

### ⚙️ 任务如何工作 {#️-how-quests-work}

非活动活动已完成

**任务状态由以下因素决定：**

1. 如果满足**已完成条件**→ 已完成
2. 如果满足**有效条件**→ 有效
3. 否则 → 无效

### 💪 这种方式的作用 {#-why-this-is-powerful}

**🤔 开放式目标**

以目标引导玩家，而不仅仅是点击。使用**`Find a way into the locked study`**等沉浸式目标，而不是刚性的**`Use the Silver Key on the Study Door`**。

**🕵️‍♀️ 多个入口点**

提供不同的方式来开始同一个任务。调查可以从**`Being briefed by the chief detective`**或独立查找**`Discarded Ransom Note`**开始。

**⏳ 进化目标**

目标可以根据时间或进展情况进行更新。如果**`Search the market district for clues`**一段时间后没有产生结果，它可能会细化为**`Focus your search near the merchant stalls`**。

**🗺️ 上下文目标**

根据上下文显示最相关的任务。在广场上，显示**`Ask locals about the suspect`**，但进入附近的小巷，它会更新为**`Check the alley for escape routes`**。

**🌿 分支叙事**

根据玩家的行动调整任务。根据发现的证据，目标可以更改为**`Investigate the garden shed`**或**`Confront the butler`**。

**⚖️ 持久后果**

先前的决定会影响当前的任务。腐败的侦探可能会得到**`Plant misleading evidence`**而不是**`Collect all available evidence`**。

## 图示：事实如何驱动任务 {#visual-guide-how-facts-drive-quests}

任务推进流程

事实如何驱动Typewriter中的任务状态

| 状态 | 事实 | 说明 | 状态转换 |
| --- | --- | --- | --- |
| 未开始 | `Quest Fact = 0` | 玩家尚未开始任务 | 与 NPC 对话 → 搜索中 |
| 搜索中 | `Quest Fact = 1` `Item Fact = 0` | 玩家正在寻找所需物品 | 找到物品 → 已找到物品；放弃任务 → 未开始 |
| 已找到物品 | `Quest Fact = 1` `Item Fact >= 1` | 玩家已找到所需物品 | 返回 NPC 处 → 已完成；丢失物品 → 搜索中 |
| 已完成 | `Quest Fact = 2` | 任务已完成 | 重置任务 → 未开始 |

## 创建任务 {#creating-a-quest}

在Typewriter中，任务是使用**任务**条目创建的。

**任务条目**

任务条目只是任务状态的视觉表示。它不会影响任务状态本身。

**开始前**

在开始创建任务之前，你必须对Typewriter的[事实](facts.md)和[第一个交互](interactions.md)有充分的了解。

### 添加任务条目 {#adding-the-quest-entry}

在Typewriter编辑器的右上角，单击**+**按钮并搜索`Quest`。单击**+**按钮将其添加到你的页面。

添加任务

任务定义

+

### 配置任务条目 {#configuring-the-quest-entry}

显示名称（Display Name）

玩家任务日志中显示的名称（例如，**`QuestGuide`**）

激活条件（Active Criteria）

任务可见性条件（例如，**`Permanent Fact >= 1`**）

完成条件（Completed Criteria）

任务完成条件（例如，**`Permanent Fact == 5`**）

### 任务条目预览 {#visualizing-the-quest-entry}

在此编辑器中，你可以增加和减少右侧图像中使用的永久事实。

尝试将其设置为 0 到 5！

<div class="tw-status-editor" data-value="0">
  <h4 data-status-title>未激活的任务</h4>
  <p data-status-description>任务尚未开始，或当前不可用。</p>
  <p><code data-status-fact>Permanent Fact = 0 (Inactive)</code></p>
  <p><strong>状态详情</strong></p>
  <ul data-status-details><li>等待激活触发</li></ul>
  <div class="tw-status-controls">
    <button type="button" data-change="-1" aria-label="减少事实值">−</button>
    <span>值：<output aria-live="polite">0</output></span>
    <button type="button" data-change="1" aria-label="增加事实值">+</button>
  </div>
</div>

![任务配置](../../assets/04083c9e7751-quest-configuration.c3d537d.521.avif)

## 添加目标 {#adding-objectives}

你现在已经创建了一个任务条目，但它还没有任何目标。对于本文档，我们创建了多个关于如何实现不同目标的指南。

- **与 NPC**对话：[与 NPC 对话目标](questing/talk-objective.md)
- **杀死 10 个僵尸**:[击杀僵尸目标](questing/kill-zombie-objective.md)
- **收集 10 颗绿宝石**：很快
- **交给NPC（邮件递送）**：很快

## 显示任务 {#displaying-the-quest}

还可以通过占位符向玩家显示任务。请阅读：**正在编写**以了解更多信息。

---

原文：[Questing](https://docs.typewritermc.com/docs/creating-stories/questing) · 文档版本：0.8.0
