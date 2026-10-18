---
title: 任务状态事实（Quest Status Fact）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/quest_status_fact
source_version: 0.8.0
---

# 任务状态事实（Quest Status Fact）

`QuestStatusFact`是返回特定任务状态的事实。

此事实仅供**读取**，无法写入，因此只适合用于条件判断。

|状态 |价值|
| --- | --- |
|不活跃 | 0 |
|活跃| 1 |
|主动式和跟踪式 | 2 |
|已完成 | -1 |

**警告**

**已完成的**状态值为**-1**，这是为了方便查询`>= 1`的任务是否处于活动状态。

## 用途示例 {#how-could-this-be-used}

这可用于抽象任务的状态。
如果任务有多个条件，你可以检查此事实，而不是检查每个条件。

## 字段 {#fields}

## 备注（Comment）

继承 · 可选

用于跟踪该事实用途的注释。

## 组（Group）

必填

## 任务（Quest）

必填

---

原文：[Quest Status Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/quest_status_fact) · 文档版本：0.8.0
