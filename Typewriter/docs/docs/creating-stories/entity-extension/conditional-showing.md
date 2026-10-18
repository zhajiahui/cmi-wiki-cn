---
title: 按条件显示 NPC（Conditional NPC showing）
source: https://docs.typewritermc.com/docs/creating-stories/entity-extension/conditional-showing
source_version: 0.8.0
---

# 按条件显示 NPC（Conditional NPC showing）

**NPC 创建了**

在本教程中，我们假设你已经创建了一个实体。
如果你还没有这样做，请先按照[实体与 NPC](../entity-extension.md)进行操作。

在本教程中，你将学习如何使用受众有条件地显示实体。

## 添加受众条目 {#adding-an-audience-entry}

有许多不同的受众条目可用。在本教程中，我们将使用“游戏时间”受众，但所有其他受众都具有类似的功能。

首先，点击面板右上角的+图标，搜索`New Game Time Audience`。单击 + 图标将其添加到你的页面。

添加游戏时间受众

根据游戏时间过滤受众

+

## 添加到实体实例 {#adding-it-onto-your-entity-instance}

现在按住你的实体实例并将其拖到`New Game Time Audience`条目上。这会将受众与实体联系起来。

现在它应该看起来像这样：

[manifest.json](../../../assets/aa208561c585-manifest.json)

## 配置受众 {#configuring-the-audience}

在受众条目中，有 2 个字段：

- **子条目**：添加玩家满足受众条件时应显示的实体。
- **生效时段（Active Times）**：只有满足此条件时，才显示受众下的子条目。
- **反转**：这将反转受众，这意味着该实体仅在未满足受众时才会显示。

## 结果 {#result}

<video controls preload="metadata" src="../../../assets/1ccbdcf635ce-conditional-npc-result.webm"></video>

---

原文：[Conditional NPC showing](https://docs.typewritermc.com/docs/creating-stories/entity-extension/conditional-showing) · 文档版本：0.8.0
