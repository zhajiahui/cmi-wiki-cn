---
title: 选项边界（Option Bound）
source: https://docs.typewritermc.com/docs/creating-stories/advanced-interactions/interaction-bounds/option-bound
source_version: 0.8.0
---

# 选项边界（Option Bound）

**开始前**

本指南是为高级用户编写的。建议充分了解[第一个交互](../../interactions.md)和[交互边界](../interaction-bounds.md)的工作原理。

**故事**

本指南的故事将是一名服务员询问玩家想坐在哪张桌子上。

本教程给选项添加交互边界。玩家切换选项时，边界锁定的位置也会随之改变。

## 创建选项 {#creating-the-option}

**实体扩展**

在本指南中，我们将从[实体与 NPC](../../entity-extension.md)将该选项连接到`On Entity Interact Event`。

### 创建选项对话 {#creating-the-option-dialogue}

首先，我们将创建一个选项对话框，当玩家与我们的服务员 NPC 交互时将显示该对话框：

1. 右键单击你的`On Entity Interact Event`条目并选择`+ Link with ...`
2. 搜索`Option`并将其添加到你的序列中

添加选项

向玩家显示选项列表

+

## 配置选项 {#configuring-the-option}

现在我们已经添加了该选项，我们需要对其进行配置。选择`Option`条目并打开属性面板。

配置对话文本为：`Welcome, at which table would you like to sit?`，选项：

- **云杉桌**
- **桦木桌**
- **深色橡木桌**
- **返回**

了解如何配置[添加选项](../../interactions/options.md)中的选项。

## 添加交互边界 {#adding-the-interaction-bound}

要添加交互边界，请右键单击`On Entity Interact Event`条目并选择`Link with ...`，搜索`Lock Interaction Bound`并将其添加到序列中。

添加锁交互边界

锁定玩家镜头的交互边界

+

## 配置交互边界 {#configuring-the-interaction-bound}

选择`Lock Interaction Bound`条目并打开属性面板。

### 添加条件分支变量 {#adding-a-case-variable}

在属性面板中启用 Target Position，点击动态变量图标，搜索 `Add Case Variable`，将其添加到事实页面。

添加分支变量

根据选择返回值的变量

+

### 配置条件分支变量 {#configuring-the-case-variable}

选择`Case Variable`条目并打开属性面板。

**外壳变量**

Case 变量根据给定的数值，返回相应位置：

- 这个系统**从 1 开始计数**，而非从 0 开始。
- Case 0 = 默认位置（未找到匹配的 case 时使用）
- 如果没有分支匹配，则使用默认位置

对于我们的餐厅场景：

1. 用采集图标设置**默认位置**（没有分支匹配时显示）
2. 点击 cases 字段中的 `+` 图标，添加四个观景位置：
   - **分支 1**：云杉 桌子位置
   - **分支 2**：桦木桌子位置
   - **分支 3**：深色橡木桌子位置
   - **分支 4**：返回位置（原始位置）
3. 用采集图标记录每个位置
4. 你的`Case Variable`应该如下所示：

![](../../../../assets/eeb8e8d1b935-option-bound-case-variables.4ee1eef.522.avif)

### 添加交互上下文变量 {#adding-a-interaction-context-variable}

现在，当玩家滚动选项时，什么也没有发生。为此，我们需要将`Interaction Context Variable`添加到`Lock Interaction Bound`条目内的`Case Variable`。

点击 `Case Variable` 条目中 `Selection` 字段旁的动态变量图标，搜索 `Interaction Context Variable`。

添加交互上下文变量

使用另一个条目中的一些数据填充字段

+

### 配置上下文变量 {#configuring-the-context-variable}

该变量自动提供当前选择的选项索引：

1. 选择`Interaction Context Variable`条目
2. 在属性面板中，单击`Select a Entry`
3. 选择我们之前创建的`Option`条目
4. 你的`Interaction Context Variable`应该如下所示：

![](../../../../assets/a4e55a41cc17-option-bound-target-position.daa5430.521.avif)

**关于箱数**

图片中显示 `Cases (0)`，是因为这些分支已在事实页面中统一配置，而没有单独配置在这个条目里。
变量有 2 种配置方式：

- 全局（在事实页面中以便跨多个条目重用）
- 本地（在特定条目内）。

两种配置方式的效果相同，系统都会根据所选选项的索引使用相应位置。

## 结果 {#result}

现在你的页面应该如下所示：

**序列页面**

![](../../../../assets/ae3b31bc9673-option-bound-sequence.3d15527.1294.avif)

**静态页面**

![](../../../../assets/568154ee58f9-option-bound-static.6a7809d.892.avif)

玩家与服务员 NPC 交互后，会看到选项菜单。切换不同的餐桌选项时，视角会自动转向相应餐桌，让玩家直接查看自己要选择的位置。

<video controls preload="metadata" src="../../../../assets/0af4855ec8ca-option-bound-result.webm"></video>

**确认键**

编写原文时，确认键存在一个问题：设为 `SWAP_HANDS`（F）时，交互边界中的对话不会继续，需要按空格键继续。

## 工作方式 {#how-it-works}

Option Bound 系统通过以下关键组件发挥作用：

1. **锁定交互边界**：控制玩家的位置和视角。
2. **条件分支变量**：保存每个选项对应的位置。
3. **交互上下文变量**：提供当前选项索引。
4. **选项条目**：提供对话接口。

玩家切换选项时，交互上下文变量会更新为新的选项索引。Case 变量据此选择位置，再由锁定交互边界将这个位置应用给玩家。

这样，玩家的视角会随当前选中的选项变化，直接看到该选项对应的游戏场景。

---

原文：[Option Bound](https://docs.typewritermc.com/docs/creating-stories/advanced-interactions/interaction-bounds/option-bound) · 文档版本：0.8.0
