---
title: 选项对话（Option Dialogue）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/option
source_version: 0.8.0
---

# 选项对话（Option Dialogue）

`Option Dialogue`操作会显示一个选项列表供玩家选择。此操作使你能够为玩家提供影响游戏结果的选择。

## 用途示例 {#how-could-this-be-used}

此操作在多种情况下都很有用，例如向玩家提供决定故事进程的对话选择，或为玩家提供完成任务的奖励选择。

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

必填 · 支持颜色 · 支持占位符

要向玩家显示的文本。

可以使用[`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html)中的颜色和格式。例如，你可以使用`<red>Some Text</red>`表示红色文本。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

## 选项（Options）

必填 · 列表

供玩家选择的选项。

## 持续时间（Duration）

必填

输入消息所需的时间。如果持续时间为零，则消息将立即显示。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

---

原文：[Option Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/option) · 文档版本：0.8.0
