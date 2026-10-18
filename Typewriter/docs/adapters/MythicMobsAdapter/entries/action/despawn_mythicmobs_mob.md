---
title: 移除生物（Despawn Mob Action）
source: https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/action/despawn_mythicmobs_mob
source_version: 0.8.0
---

# 移除生物（Despawn Mob Action）

`Despawn Mob Action`行动将MythicMobs生物从世界上移除。

## 用途示例 {#how-could-this-be-used}

这个动作可以以多种方式用在故事或任务中。例如，如果玩家杀死 10 个僵尸的任务失败，那么僵尸可能会消失，以表明该任务不再有效。人们甚至可以使用这个动作来完成在限定时间内杀死一定数量的小怪的任务！

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 生物名称（Mob Name）

必填 · 支持占位符

生物的名字

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

---

原文：[Despawn Mob Action](https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/action/despawn_mythicmobs_mob) · 文档版本：0.8.0
