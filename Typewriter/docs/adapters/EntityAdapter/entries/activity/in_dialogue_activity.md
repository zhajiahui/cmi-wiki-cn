---
title: 对话中活动（In Dialogue Activity）
source: https://docs.typewritermc.com/adapters/EntityAdapter/entries/activity/in_dialogue_activity
source_version: 0.8.0
---

# 对话中活动（In Dialogue Activity）

`InDialogueActivityEntry`是一个当玩家与 NPC 对话时激活子活动的活动。

该活动仅在玩家与 NPC 对话时才会激活。

## 用途示例 {#how-could-this-be-used}

当玩家与NPC对话时，这可以用来阻止NPC移动。

## 字段 {#fields}

## 对话后待机时长（Dialogue Idle Duration）

必填

玩家在同一段对话中可保持无操作状态的时长；超时后，活动停用。

设置为0时，不使用定时器。

**说明**

当对话的优先级高于此活动时，会忽略这个计时器，
仅在对话结束后退出活动。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

## 对话活动（Talking Activity）

必填

NPC 对话时使用的活动。

## 待机活动（Idle Activity）

必填

NPC 没有对话时使用的活动。

---

原文：[In Dialogue Activity](https://docs.typewritermc.com/adapters/EntityAdapter/entries/activity/in_dialogue_activity) · 文档版本：0.8.0
