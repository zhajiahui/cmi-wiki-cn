---
title: 给予物品（Giving items）
source: https://docs.typewritermc.com/docs/creating-stories/interactions/items
source_version: 0.8.0
---

# 给予物品（Giving items）

**开始前**

在开始本教程之前，最好先阅读[第一个交互](../interactions.md)。

在本教程中，你将学习如何在交互中提供物品。

## 添加给予物品的动作 {#adding-the-give-item}

要添加给定物品条目，请按照下列步骤操作：

1. 右键单击你的条目并选择`+ Link with ...`。
2. 搜索`Add give item`并单击 + 图标将其添加到你的序列中。

添加赠送物品

给玩家一个物品

+

## 配置给予物品的动作 {#configuring-the-give-item}

给予物品条目有两种给予物品的类型：自定义物品和序列化物品。

### 区别 {#differences}

**定制物品**

自定义物品允许你自定义该物品的几乎所有方面。

**NBT**

自定义物品不能包含 NBT 数据。

**序列化物品**

序列化的物品使你能够使用物品采集器并从游戏中捕获该物品。

**不可编辑**

你无法编辑序列化物品。只能更改名称。

### 使用物品采集器（Serialized Item） {#using-the-item-capturerserialized-item}

更简单的方式是使用物品采集器，把游戏中当前手持的物品复制到面板中。点击 `item` 字段旁的采集图标即可。

<video controls preload="metadata" src="../../../assets/a61136307f2d-item-capturer.webm"></video>

### 手动配置（Custom Item） {#configuring-it-yourselfcustom-item}

也可以手动配置物品。在 item 字段中选择 `Custom Item`，点击 `Components(0)` 文字旁的 + 图标，添加以下组件之一：

1. **数量（Amount）**：要给予玩家的物品数量。
2. **标志**：该物品的特定选项。
3. **物品描述**：该物品的物品描述。
4. **材质**：这是玩家将获得的物品。
5. **物品名称**：这是物品的名称。

## 结果 {#result}

配置物品后，你可以通过单击发布按钮来测试交互，然后它应该如下所示：

<video controls preload="metadata" src="../../../assets/bb1ee550198f-final-result-give-item.webm"></video>

---

原文：[Giving items](https://docs.typewritermc.com/docs/creating-stories/interactions/items) · 文档版本：0.8.0
