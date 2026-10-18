---
title: 延迟动作（Delayed Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/delayed_action
source_version: 0.8.0
---

# 延迟动作（Delayed Action）

`Delayed Action Entry`是一个在指定持续时间后触发其触发器的条目。此条目使你能够创建基于时间的操作和事件。

## 用途示例 {#how-could-this-be-used}

此条目在你需要延迟操作或事件的各种情况下都很有用。
你可以使用它来创建倒计时器，在经过一定时间后执行操作，或者安排将来的事件。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 持续时间（Duration）

必填

触发后续条目前的等待时间。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

---

原文：[Delayed Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/delayed_action) · 文档版本：0.8.0
