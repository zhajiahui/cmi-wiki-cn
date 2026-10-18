---
title: 任务状态更新事件（Quest Status Update Event）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/quest_status_update_event
source_version: 0.8.0
---

# 任务状态更新事件（Quest Status Update Event）

当玩家的任务状态更新时，会触发`Quest Status Update Event`条目。

未指定任务时，所有任务都可触发此事件。

## 用途示例 {#how-could-this-be-used}

这可用于在更新任务状态时向玩家显示标题或通知。

## 字段 {#fields}

## 后续触发（Triggers）

必填 · 列表

## 任务（Quest）

必填

未设置时，它将触发所有任务。

## 起始值（From）

可选

未设置时，它将触发所有状态。

## 结束值（To）

必填

任务更新后的状态。

---

原文：[Quest Status Update Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/quest_status_update_event) · 文档版本：0.8.0
