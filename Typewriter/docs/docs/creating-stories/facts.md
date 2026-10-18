---
title: 事实（Facts）
source: https://docs.typewritermc.com/docs/creating-stories/facts
source_version: 0.8.0
---

# 事实（Facts）

事实本质上是变量，用来保存可由其他条目修改的信息。所有事实都是数值，也都按数值处理。

[`Basic Extension`](../../adapters/BasicAdapter.md) 提供了多种事实，[`extensions`](../../adapters.md) 还可以增加更多可用的事实。

## 为什么使用事实？ {#why-use-facts}

事实可用于创建动态内容和自定义系统行为，例如：

- **动态任务：**用事实保存和修改完成状态，记录玩家的任务进度。
- **自定义体验：**通过事实调整难度、角色属性等游戏参数，定制玩家体验。
- **互动叙事：**用事实记住玩家的选择和行为，让故事随之发展。
- **成就系统：**用事实记录指定的里程碑和成就，追踪完成情况。

### 事实的类型 {#types-of-facts}

事实分为可读和可写两种。

- **可读事实：**用于条目的条件判断，例如检查玩家背包中是否有某种物品。
- **可写事实：**用于修改器，以修改事实的值，例如更新玩家的任务进度。

**说明**

有些事实既可读又可写。例如，[永久事实](../../adapters/BasicAdapter/entries/fact/permanent_fact.md)可以同时用于条件和修改器。
有些事实只读。例如，[背包物品数量事实](../../adapters/BasicAdapter/entries/fact/inventory_item_count_fact.md)只能用于条件判断。

## 组 {#groups}

事实可以指定所属的组，共有 3 种：

- **全局（Global）**：所有玩家共用一个事实。
- **世界（World）**：同一世界中的所有玩家共用一个事实。
- **玩家（Player）**：每位玩家分别保存事实。

## 字段 {#fields}

部分条目的字段会影响事实的处理方式。

![条件和修改器字段](../../assets/2f85a9ee6ff8-criteria_and_modifier.7444206.432.avif)

### 条件（Criteria） {#criteria}

Criteria 是条目的触发条件，例如 `if fact = 10 then...`，用于决定条目是否执行。

![条件字段](../../assets/cc2d6e7acb81-criteria.aedf976.428.avif)

配置条件的步骤如下：

1. 选择要检查的事实。
2. 选择运算符。
3. 输入用于比较的值。

### 修改器（Modifiers） {#modifiers}

修改器用于修改事实的值。

![修改器字段](../../assets/264d1702e913-modifier.914e01c.431.avif)

配置修改器的步骤如下：

1. 选择要修改的事实。
2. 选择运算符。可以直接赋值 (=)，也可以在原值上相加 (+)。
3. 输入要参与运算的值。

**警告**

修改器只在条目执行时运行。
如果条目设有条件，只要**其中一个条件**为 `false`，条目就不会执行，事实也不会被修改。

## 教程 {#tutorial}

下面用永久事实记录任务进度，说明事实的用法。

1. 新建页面，类型选择 `static`，命名为 `Playerprogress`。
2. 点击 + 图标，选择 `Add Permanent Fact`，将其重命名为 `Playerprogress`，并填写便于理解的备注。

   ![静态页面按钮](../../assets/da49f96ebb45-static-page.2b9bf54.1789.avif)
3. 选择玩家组。
4. 在序列页面中，点击一个动作。
   - 设置**条件：**检查 `Playerprogress` == 0。
   - 设置**修改器：**满足条件时，将 `Playerprogress` 更新为 1。
5. 为任务的其他阶段创建动作，并相应修改 `Playerprogress`。

## 示例 {#examples}

事实系统有多种用法，以下是一些示例。

**收集物品任务**

**目标：**玩家与 NPC 对话，然后收集物品。

**使用的事实：**

- **可读事实：**[背包物品数量事实](../../adapters/BasicAdapter/entries/fact/inventory_item_count_fact.md)

**流程：**

1. 玩家与 NPC 对话。
2. 通过背包物品数量事实检查条件，判断玩家是否持有所需物品。

**进度记录**

**目标：**记录玩家在任务各阶段的进度。

**使用的事实：**

- **可写事实：**[永久事实](../../adapters/BasicAdapter/entries/fact/permanent_fact.md)

**流程：**

1. 玩家与 NPC 对话（进度设为 1）。
2. 完成指定动作（进度设为 2）。
3. 完成任务（进度设为 3）。

**余额检查**

**目标：**判断玩家是否有足够的钱购买物品。

**使用的事实：**

- **可读事实：**[余额事实](../../adapters/VaultAdapter/entries/fact/balance_fact.md)

**流程：**

1. 玩家与 NPC 对话。
2. 通过余额事实检查条件，判断玩家的余额是否足够。
3. 余额足够时，允许玩家购买物品。
4. 余额不足时，向玩家显示消息。

**提示**

所有可用的事实见[扩展](../../adapters.md)。

---

原文：[Facts](https://docs.typewritermc.com/docs/creating-stories/facts) · 文档版本：0.8.0
