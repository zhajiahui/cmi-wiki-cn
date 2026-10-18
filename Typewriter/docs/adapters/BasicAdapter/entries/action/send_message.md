---
title: 发送消息（Message Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/send_message
source_version: 0.8.0
---

# 发送消息（Message Action）

`Send Message Action`是一个向玩家发送消息的动作。
你可以指定说话者以及要发送的消息。

这不应与（消息对话）[../dialogue/message]混淆。
(消息对话)[../dialogue/message]将用消息替换当前对话，而此操作不会。

## 用途示例 {#how-could-this-be-used}

此操作在多种情况下都很有用。
你可以使用它来创建文本效果以响应特定事件，例如完成操作或其他任何内容。
也可以用于其他类似场景。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 说话者（Speaker）

必填

消息的说话者。

## 消息（Message）

必填 · 多行 · 支持占位符

要发送的消息。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

---

原文：[Message Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/send_message) · 文档版本：0.8.0
