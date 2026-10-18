---
title: 受众条目（Audience Entries）
source: https://docs.typewritermc.com/docs/concepts/Audience
source_version: 0.8.0
---

# 受众条目（Audience Entries）

受众条目是一种特定类型的[呈现条目](Manifest.md)，用于有条件地向一组玩家显示内容。
玩家可以是条目的受众。
换句话说，受众条目的内容将显示给其受众中的玩家。

受众条目有两种类型：

### 受众显示条目 {#audience-display-entry}

受众显示条目用于向一组玩家显示内容，
例如施加药水效果，或显示 Boss 栏。

### 受众过滤条目 {#audience-filter-entry}

受众过滤条目有一个子条目列表，可包含受众条目和受众过滤条目。
它们用于筛选受众显示条目的受众。

受众过滤器可以：

#### 筛选玩家 {#filter-players}

筛选自身及其子条目的受众。例如，`CriteriaAudience` 仅允许满足条件的玩家加入受众。

#### 显示内容 {#display-content}

像普通受众显示条目一样显示内容，但内容由子条目提供。例如，`Sidebar` 使用 `Lines` 条目作为显示内容。

# 筛选如何工作？

玩家加入服务器时，会被加入所有根受众条目的受众中。
根受众条目是没有父条目的条目。

## 根条目 {#root-entries}

[查看原文交互图](https://docs.typewritermc.com/docs/concepts/Audience#root-entries)

[audience_entries.riv](../../assets/03f5a8cfa036-audience_entries.riv)

上图中，所有没有父条目的条目都是根条目。
过滤器仍可决定玩家是否属于自己的受众，
但没有连接其他条目时，不会影响其他条目的受众。

## 链式连接 {#chaining}

将过滤器串联，可以组成更复杂的筛选条件。
这里，玩家必须同时满足两个条件，才会属于 `Display` 的受众。

[查看原文交互图](https://docs.typewritermc.com/docs/concepts/Audience#chaining)

[audience_entries.riv](../../assets/03f5a8cfa036-audience_entries.riv)

试着切换条件的开关，观察结果。

## 多个父条目 {#multiple-parents}

条目有多个父条目时，只要任意父条目允许玩家加入受众，玩家就属于该条目的受众。

[查看原文交互图](https://docs.typewritermc.com/docs/concepts/Audience#multiple-parents)

[audience_entries.riv](../../assets/03f5a8cfa036-audience_entries.riv)

试着切换条件的开关，观察结果。

---

原文：[Audience Entries](https://docs.typewritermc.com/docs/concepts/Audience) · 文档版本：0.8.0
