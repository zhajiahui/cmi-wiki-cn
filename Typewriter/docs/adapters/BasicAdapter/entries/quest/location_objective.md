---
title: 位置目标（Location Objective）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/location_objective
source_version: 0.8.0
---

# 位置目标（Location Objective）

`LocationObjective`条目是玩家到达特定位置即可完成的任务。
主要用于向玩家显示进度。

设置目标**并不一定要**使用这个条目。
这只是视觉上的新奇。

该条目根据目标是否活跃来过滤受众。
如果满足条件，它将向玩家显示目标。

它允许将路径流显示到目标位置。

## 用途示例 {#how-could-this-be-used}

这可以用来引导玩家到特定位置。
通过路径流向玩家展示他们需要去的地方。

## 字段 {#fields}

## 任务（Quest）

必填

## 子条目（Children）

必填 · 列表

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 显示（Display）

必填

## 目标位置（Target Location）

必填

## 优先级覆盖（Priority Override）

可选

---

原文：[Location Objective](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/location_objective) · 文档版本：0.8.0
