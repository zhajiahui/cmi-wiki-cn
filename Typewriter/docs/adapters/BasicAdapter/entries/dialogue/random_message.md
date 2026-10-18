---
title: 随机消息对话（Random Message Dialogue）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/random_message
source_version: 0.8.0
---

# 随机消息对话（Random Message Dialogue）

`Random Message Dialogue`操作向玩家显示列表中的随机消息。此操作使你能够创建具有随机响应的交互式对话。

## 用途示例 {#how-could-this-be-used}

可以用它来创建随机 NPC 对话、具有多个随机结果的任务，或者为你的游戏添加一定程度的不可预测性。也可以用于其他场景。

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

## 消息（Messages）

必填 · 列表 · 支持颜色 · 多行 · 支持占位符

要向玩家显示的文本，随机选择其中一条。

可以使用[`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html)中的颜色和格式。例如，你可以使用`<red>Some Text</red>`表示红色文本。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

---

原文：[Random Message Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/random_message) · 文档版本：0.8.0
