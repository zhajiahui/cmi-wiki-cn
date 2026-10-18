---
title: 聊天包含文本事件（Chat Contains Text Event）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_message_contains_text
source_version: 0.8.0
---

# 聊天包含文本事件（Chat Contains Text Event）

当玩家发送包含特定文本的聊天消息时，会调用`Chat Contains Text Event`。

## 用途示例 {#how-could-this-be-used}

当玩家提到某事时，你可以向他们显示对话。

## 字段 {#fields}

## 后续触发（Triggers）

必填 · 列表

## 文本（Text）

必填 · 正则表达式

要在消息中查找的文本。

[`Regular expressions`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)可用于匹配模式。例如，`^.*$`将匹配任何字符串。

## 完全一致（Exact Same）

必填

文本是否应该完全匹配。

---

原文：[Chat Contains Text Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_message_contains_text) · 文档版本：0.8.0
