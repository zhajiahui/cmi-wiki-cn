---
title: 交互边界（Interaction Bounds）
source: https://docs.typewritermc.com/docs/creating-stories/advanced-interactions/interaction-bounds
source_version: 0.8.0
---

# 交互边界（Interaction Bounds）

**开始前**

本教程假定你已按[安装指南](../../getting-started/installation.md#basic-extension)安装 Basic Extension。

**开始前**

本教程面向进阶用户，建议先了解[第一个交互](../interactions.md)的工作方式。

在故事中使用交互边界前，先了解以下概念。

## 什么是交互边界？ {#what-are-interaction-bounds}

交互边界通过条件，将交互限制在特定操作或空间内，控制交互何时发生、何时被打断。例如，玩家远离 NPC 时取消对话。

### 边界的两种模式 {#two-modes-of-bounds}

交互边界有两种模式：

#### 中断模式 {#interruption-mode}

在中断模式下，玩家一旦违反边界条件（例如走出指定区域），交互就会立即取消。适合允许玩家随时走开的日常对话。

#### 阻止模式 {#blocking-mode}

在阻止模式下，玩家会被阻止违反边界条件。例如，重要对话进行时，玩家无法走开，需完整经历这段剧情后再继续。

|模式|行为 |使用分支|
| --- | --- | --- |
|中断|打破绑定时交互取消 |可选对话、环境互动 |
|封锁|玩家无法突破界限|关键故事时刻，重要指示 |

### 如何决定模式 {#how-modes-are-determined}

模式由交互与边界的**优先级**比较决定：

- 交互的优先级**高于**边界 → **阻止模式**
- 交互的优先级**等于或低于**边界 → **中断模式**

**提示**

条目继承所属页面的优先级。可以在页面属性面板中设置页面优先级。

## 使用交互边界 {#how-to-use-interaction-bounds}

下面介绍如何在故事中使用交互边界。
本教程用 3 个示例说明不同情境下的用法：

**中断模式**

**教程**

这个示例在玩家远离花朵时中断交互。

**初始设置**

本教程接续[第一个交互](../interactions.md)，编辑器中至少需要有一个
`On Interact With Block` 条目。

#### 添加交互边界 {#adding-the-interaction-bound}

右键点击 `On Interact With Block` 条目，选择 `Link with ...`，搜索 `Player Radius Interaction Bound`，并将其添加到序列中。

添加 Player Radius Interaction Bound

以玩家为中心的交互边界

+

#### 配置交互边界 {#configuring-the-interaction-bound}

添加交互边界后，继续配置。
选中 `Player Radius Interaction Bound` 条目，打开属性面板。

这里有 2 个设置项：

- **Radius**：交互边界的半径。玩家超出这个距离时，交互会被取消。
- **zoom**：玩家靠近时镜头是否拉近、走远时是否拉远。

此时序列应与下图类似：

![](../../../assets/7f36bc956fcb-interaction-bound-player-radius-interupting.9abd31a.1585.avif)

#### 结果 {#result}

交互效果如下：

<video controls preload="metadata" src="../../../assets/9f4467866530-interaction-bound-interupting-result.webm"></video>

**阻止模式**

**教程**

这个示例在玩家试图远离花朵时，阻止玩家离开交互范围。

**初始设置**

本教程接续[第一个交互](../interactions.md)，编辑器中至少需要有一个
`On Interact With Block` 条目。

#### 添加交互边界 {#adding-the-interaction-bound-1}

右键点击 `On Interact With Block` 条目，选择 `Link with ...`，搜索 `Player Radius Interaction Bound`，并将其添加到序列中。

添加 Player Radius Interaction Bound

以玩家为中心的交互边界

+

#### 设置为阻止模式 {#making-it-a-blocking-interaction}

前面的设置创建了中断模式的边界。要改为阻止模式，需要让 `Spoken` 条目的优先级高于 `Player Radius Interaction Bound` 条目。
操作如下：

1. 新建一个序列页面，例如命名为 `Blocking Bounds`。
2. 选中并长按 `Player Radius Interaction Bound` 条目几秒钟。
3. 将它拖到新页面中。
4. 右键点击包含 `Spoken` 条目的页面。
5. **选择 `Change Priority`，将优先级设为高于 `Player Radius Interaction Bound` 条目的数值。**
   例如，`Blocking Bounds` 页面优先级为 0，就将包含 `Spoken` 条目的页面设为 1。
6. 此时序列应如下图所示：

![](../../../assets/784f0b17d166-interaction-bound-player-radius-blocking.8643896.1027.avif)

#### 结果 {#result-1}

交互效果如下：

<video controls preload="metadata" src="../../../assets/72de15819de1-interaction-bound-blocking-result.webm"></video>

**中断模式（Entity Extension）**

**教程**

这个示例在玩家远离 NPC 时中断交互。

**实体扩展**

本教程需要先通过 [实体与 NPC](../entity-extension.md) 创建一个 NPC。

**待补充**

原文尚未提供这部分教程，请稍后查看。

---

原文：[Interaction Bounds](https://docs.typewritermc.com/docs/creating-stories/advanced-interactions/interaction-bounds) · 文档版本：0.8.0
