---
title: 添加实体（Adding entities）
source: https://docs.typewritermc.com/docs/creating-stories/cinematics/entities
source_version: 0.8.0
---

# 添加实体（Adding entities）

**开始前**

在开始本教程之前，最好先阅读[过场动画](../cinematics.md)。

**实体扩展**

在开始本教程之前，你必须已安装实体扩展。

在本教程中，你将学习如何将实体添加到交互中。

## 添加实体 {#adding-an-entity}

首先点击面板右上角的+图标，搜索`Add Entity Cinematic`。单击 + 图标将其添加到你的页面。

添加实体动画

在过场动画中使用动画实体

+

### 选择定义 {#selecting-the-definition}

现在在属性面板中，单击`Select a entity_definition`并选择你想要作为 NPC 的实体类型，但在本教程中，我们将使用`Add Npc Definition`。现在，你需要选择一个呈现页面或通过单击`Add manifest`创建一个呈现页面。

<video controls preload="metadata" src="../../../assets/8e1884d5f813-select-entity-definition.webm"></video>

然后在该 NPC 定义中，你可以按照[实体与 NPC](../entity-extension.md)教程来创建一个美丽的 NPC。

### 添加片段 {#adding-segments}

在属性面板的操作菜单中点击 `Add Segment`，向轨道添加片段。

### 配置片段 {#configuring-the-segment}

在该段中，我们现在需要添加一个文件产物。你可以通过单击`Select a entity_cinematic_artifact`并选择你的文件产物来完成此操作，或者通过单击`Add Entity Cinematic Artifact`创建一个文件产物。然后选择或创建你的静态页面。

### 请求内容模式 {#requesting-the-content-mode}

回到过场动画页面，点击属性面板中 artifact 上方的采集图标，在 Minecraft 中打开内容模式。将鼠标移到背包中的物品上，可以查看各物品的作用；这里暂时只使用书。
点击书后，Typewriter 开始录制你的动作，并采用进入内容模式前手持的物品。

#### 录制 NPC {#recording-the-npc}

**背包物品**

在请求内容模式之前你持有的物品将是 NPC 将持有的物品。

<video controls preload="metadata" src="../../../assets/7e4ede08a51e-recording.webm"></video>

#### 使用回放物品 {#using-the-playback-items}

<video controls preload="metadata" src="../../../assets/5ec128fbe50b-playback.webm"></video>

## 结果 {#result}

现在你已成功添加实体，你可以在动画中查看它。

<video controls preload="metadata" src="../../../assets/ab8e06d46355-cinematic-npc-result.webm"></video>

---

原文：[Adding entities](https://docs.typewritermc.com/docs/creating-stories/cinematics/entities) · 文档版本：0.8.0
