---
title: 消息对话（Message Dialogue）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/message
source_version: 0.8.0
---

# 消息对话（Message Dialogue）

`Message Dialogue Action`是一个向玩家显示一条消息的操作。此操作使你能够向玩家显示消息以响应特定事件。

## 用途示例 {#how-could-this-be-used}

可以用它向玩家提供有关周围环境的信息、为他们提供提示或为你的冒险增添趣味。也可以用于其他场景。

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

## 文本（Text）

必填 · 支持颜色 · 多行 · 支持占位符

要向玩家显示的文本。

可以使用[`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html)中的颜色和格式。例如，你可以使用`<red>Some Text</red>`表示红色文本。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

---

原文：[Message Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/message) · 文档版本：0.8.0
