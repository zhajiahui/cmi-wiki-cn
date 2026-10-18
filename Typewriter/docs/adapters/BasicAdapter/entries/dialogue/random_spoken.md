---
title: 随机逐字对话（Random Spoken Dialogue）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/random_spoken
source_version: 0.8.0
---

# 随机逐字对话（Random Spoken Dialogue）

`Random Spoken Dialogue`动作向玩家显示随机选择的动画消息。

## 用途示例 {#how-could-this-be-used}

假设你的游戏中有一个 NPC 给玩家讲笑话。
你可以使用随机逐字对话对话动作
从可能的笑话列表中随机选择一个笑话并让 NPC“讲述”
使用动画消息将其发送给玩家。

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

必填 · 列表 · 支持颜色 · 支持占位符

显示给玩家的消息列表。每次触发对话时，都会随机选择其中一条消息。

可以使用[`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html)中的颜色和格式。例如，你可以使用`<red>Some Text</red>`表示红色文本。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

## 持续时间（Duration）

必填

输入消息所需的时间。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

---

原文：[Random Spoken Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/random_spoken) · 文档版本：0.8.0
