---
title: 生成生物（Spawn Mob Action）
source: https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/action/spawn_mythicmobs_mob
source_version: 0.8.0
---

# 生成生物（Spawn Mob Action）

`Spawn Mob Action`行动向世界生成MythicMobs生物。

## 用途示例 {#how-could-this-be-used}

此操作可用于多种场景。从要求你杀死一些生成的小怪的简单任务，到模拟整个战斗的复杂故事情节，这个动作没有界限！

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

## 等级（Level）

必填

生物等级

## 仅对该玩家可见（Only Visible For Player）

必填

生物是否只能被玩家看到

## 生成位置（Spawn Location）

必填

生物的生成位置

---

原文：[Spawn Mob Action](https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/action/spawn_mythicmobs_mob) · 文档版本：0.8.0
