---
title: 实体交互目标（Interact Entity Objective）
source: https://docs.typewritermc.com/adapters/EntityAdapter/entries/quest/interact_entity_objective
source_version: 0.8.0
---

# 实体交互目标（Interact Entity Objective）

`InteractEntityObjective`类是表示与实体交互的目标的条目。
当此类目标处于活动状态时，它将在任何 NPC 上方显示一个图标。

## 字段 {#fields}

## 子条目（Children）

必填 · 列表

## 任务（Quest）

必填

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 实体（Entity）

必填

玩家需要与之交互的实体。

## 覆盖显示（Override Display）

可选

向玩家显示的目标文本。用 `<entity>` 插入实体名称。

## 优先级覆盖（Priority Override）

可选

---

原文：[Interact Entity Objective](https://docs.typewritermc.com/adapters/EntityAdapter/entries/quest/interact_entity_objective) · 文档版本：0.8.0
