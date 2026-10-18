---
title: 逐字对话（Spoken Dialogue）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/spoken
source_version: 0.8.0
---

# 逐字对话（Spoken Dialogue）

`Spoken Dialogue Action`是一个向玩家显示动画消息的动作。此操作使你能够显示具有指定说话者、文本和持续时间的消息。

## 用途示例 {#how-could-this-be-used}

可以用它来创建故事情节、向玩家提供说明或创建身临其境的角色扮演体验。也可以用于其他场景。

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

## 持续时间（Duration）

必填

输入消息所需的时间。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

---

原文：[Spoken Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/spoken) · 文档版本：0.8.0
