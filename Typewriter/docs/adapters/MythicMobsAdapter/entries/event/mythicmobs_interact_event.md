---
title: Mythic 生物交互事件（Mythic Mob Interact Event）
source: https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/event/mythicmobs_interact_event
source_version: 0.8.0
---

# Mythic 生物交互事件（Mythic Mob Interact Event）

当玩家与 MythicMob 交互时，`MythicMob Interact Event`就会被触发。

## 用途示例 {#how-could-this-be-used}

这可用于创建 MythicMob 和玩家之间发生的各种交互。例如，你可以创建一个 MythicMob，当玩家与之交互时为玩家提供一个物品。

## 字段 {#fields}

## 后续触发（Triggers）

必填 · 列表

## 生物名称（Mob Name）

必填 · 正则表达式

要侦听的特定 MythicMob 类型

[`Regular expressions`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)可用于匹配模式。例如，`^.*$`将匹配任何字符串。

---

原文：[Mythic Mob Interact Event](https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/event/mythicmobs_interact_event) · 文档版本：0.8.0
