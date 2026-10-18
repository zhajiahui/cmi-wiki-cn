---
title: 道路网络（Road Network）
source: https://docs.typewritermc.com/docs/creating-stories/road-network
source_version: 0.8.0
---

# 道路网络（Road Network）

**开始前**

本指南假设你已经安装了 Road Network Extension。
另外，请确保你已阅读[界面布局](../getting-started/layout.md)文档并创建了**静态**页面。

如果你想让 NPC 在地图上移动或让玩家沿着路径行走，道路网络就至关重要。在本指南中，我们将向你展示如何创建道路网络以及如何在你的故事中使用它。

## 什么是道路网络？ {#what-is-the-road-network}

道路网络是Typewriter用于有效计算两个遥远点之间的路径的内部图形结构。

## 创建道路网络 {#creating-a-road-network}

首先，我们需要在页面中添加`Base Road Network`条目。要将其添加到我们的页面，请单击面板右上角的 + 图标并搜索`base road network`，然后单击 + 图标将其添加到你的页面。

添加基础道路网

道路网络一词的定义

+

### 打开内容模式 {#opening-the-content-mode}

在属性面板中找到 `Base Road Network` 条目，点击 ArtifactId 字段旁的采集图标，打开内容模式。

### 添加节点 {#adding-a-node}

打开内容模式后，先添加节点。节点是世界中的点，通过边互相连接。在快捷栏选择钻石并右键，打开节点编辑器；点击末地水晶，退出节点菜单。

<video controls preload="metadata" src="../../assets/bda8202b350a-add-node.webm"></video>

### 创建路径 {#creating-the-path}

要创建路径，你始终需要 2 个节点。因此，创建 2 个节点，然后从快捷栏中选择红石并右键单击它。现在它应该看起来有点像这样：

<video controls preload="metadata" src="../../assets/c22d36104097-path.webm"></video>

现在你已经创建了一条路径。你可以扩展具有无限节点的道路网络并在它们之间创建路径。

**节点放置**

建议你在世界中道路或路径的起点和终点创建节点。这是为了节省加载和重新计算边缘的资源。

### 编辑节点 {#editing-a-node}

在节点编辑器中，你有 4 个选项：

**更改半径**

#### 半径有什么作用？ {#why-is-their-radius}

从节点 A 开始寻路时，会检查**30 块**半径范围内的所有节点，例如节点 B、C、D、E、F、G。如果发现到节点 C 的路径需要经过节点 B 半径，则停止计算到 C 的路径。这是因为寻路避开了需要跳过 B 等节点的路径。

![路网半径说明](../../assets/d1ab50b104c7-radius.04ce433.1920.avif)

#### 如何使用？ {#how-to-use}

在快捷栏选择幽匿感测体并右键，即可修改节点半径。

**节点单击**

右键单击某个物品时，不得将光标指向正在编辑的节点。这将打开内容模式并且不会触发事件。

然后，使用滚轮，你可以更改节点的半径。

<video controls preload="metadata" src="../../assets/2657a128a6eb-radius.webm"></video>

**移除边**

#### 为什么要移除边？ {#why-remove-an-edge}

当你希望路径跳过节点或仅使路径成为单向时，删除边可能很有用。

#### 如何使用？ {#how-to-use-1}

要删除边缘，请从快捷栏中选择红石，然后在要从中删除边缘的节点上右键单击它。

<video controls preload="metadata" src="../../assets/35a05959d7e8-remove-edges.webm"></video>

**重新计算**

添加或删除负节点后，你必须使用热栏中的红石重新计算边

#### 单向路径 {#one-way-path}

为了仅以一种方式实现，你不仅应该单击右键，还应该按住 Shift 键。这将使边缘仅是单向的。

<video controls preload="metadata" src="../../assets/92fc32825d2e-remove-edge.webm"></video>

**添加快速旅行连接**

#### 为什么添加快速旅行连接？ {#why-add-a-fast-travel-connection}

快速旅行连接用于将 NPC 传送到另一个节点，而无需步行前往该节点。

#### 如何使用？ {#how-to-use-2}

要添加快速旅行连接，请从快捷栏中选择绿宝石，然后右键单击你希望其传送到的节点。

<video controls preload="metadata" src="../../assets/7aa3ba23d048-fast-travel.webm"></video>

#### 单向快速旅行 {#one-way-fast-travel}

为了仅以一种方式实现，你不仅应该单击右键，还应该按住 Shift 键。这将使快速旅行仅是单向的。

**移除节点**

要删除节点，请从快捷栏中选择红石块并右键单击它。

**节点单击**

右键单击某个物品时，不得将光标指向正在编辑的节点。这将打开内容模式并且不会触发事件。

### 负节点 {#negative-nodes}

有时你希望寻路不经过某条路径。例如，当你有一个地方寻路认为它可以向下或向上跳 1 个方块但不应该时，你可以添加一个负节点来防止这种情况。
这是一个例子：

**使用负节点**

<video controls preload="metadata" src="../../assets/a0f6bfc232f3-negative-nodes-preview.webm"></video>

**不使用负节点**

<video controls preload="metadata" src="../../assets/8fb362ab10d2-non-negative-nodes-example.webm"></video>

#### 如何添加负节点？ {#how-to-add-a-negative-node}

你可以通过在内容模式的快捷栏中选择下界合金锭并右键单击它来添加负节点。

**重新计算**

添加或删除负节点后，你必须使用热栏中的红石重新计算边

### 高亮节点 {#highlighting-nodes}

当你有很多节点时，很难看出哪些节点相互连接。为了使这更容易，你可以突出显示彼此连接的节点。为此，请从快捷栏中选择萤石并右键单击它。

## 结束 {#ending}

现在你已经了解了如何成功设置道路网络。

---

原文：[Road Network](https://docs.typewritermc.com/docs/creating-stories/road-network) · 文档版本：0.8.0
