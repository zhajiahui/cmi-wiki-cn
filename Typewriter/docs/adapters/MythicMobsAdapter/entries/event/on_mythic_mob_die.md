---
title: Mythic 生物死亡事件（Mythic Mob Death Event）
source: https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/event/on_mythic_mob_die
source_version: 0.8.0
---

# Mythic 生物死亡事件（Mythic Mob Death Event）

当玩家杀死小怪时，会触发`Mob Death Event`事件。

## 用途示例 {#how-could-this-be-used}

杀死最终首领后，对话或过场动画部分就可以开始。玩家第一次杀死特定怪物时还可以获得特殊奖励。

## 字段 {#fields}

## 后续触发（Triggers）

必填 · 列表

## 生物名称（Mob Name）

必填 · 正则表达式

仅当特定生物死亡时触发。

[`Regular expressions`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)可用于匹配模式。例如，`^.*$`将匹配任何字符串。

---

原文：[Mythic Mob Death Event](https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/event/on_mythic_mob_die) · 文档版本：0.8.0
