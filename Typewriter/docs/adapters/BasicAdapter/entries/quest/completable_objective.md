---
title: 可完成目标（Completable Objective）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/completable_objective
source_version: 0.8.0
---

# 可完成目标（Completable Objective）

`Completable Objective`条目是一个可以显示已完成阶段的目标。
当满足显示条件时，它会向玩家显示，无论是否满足已完成的条件。

## 用途示例 {#how-could-this-be-used}

当任务有多个可以以不同顺序完成的目标时，这非常有用。
例如，玩家需要收集小麦、鸡蛋和牛奶来制作蛋糕。
玩家收集物品的顺序并不重要。
但你想向玩家展示他们收集了哪些物品。

## 字段 {#fields}

## 任务（Quest）

必填

## 子条目（Children）

必填 · 列表

## 显示条件（Show Criteria）

必填 · 列表

需要满足条件才能显示目标。

## 完成条件（Completed Criteria）

必填 · 列表

显示目标已完成的条件。

## 显示（Display）

必填

## 优先级覆盖（Priority Override）

可选

---

原文：[Completable Objective](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/completable_objective) · 文档版本：0.8.0
