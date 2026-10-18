---
title: 玩家击杀实体事件（Player Kill Entity Event）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_kill_entity
source_version: 0.8.0
---

# 玩家击杀实体事件（Player Kill Entity Event）

当玩家杀死实体时，`Player Kill Entity Event`就会被触发。如果你想检测一个玩家何时杀死另一个玩家，请改用[`Player Kill Player Event`](on_player_kill_player.md)。

## 用途示例 {#how-could-this-be-used}

此事件可用于检测玩家何时杀死 Boss，并给予他们一些奖励。它还可以用来创建一个自定义生物，当被玩家杀死时会掉落物品。

## 字段 {#fields}

## 后续触发（Triggers）

必填 · 列表

## 实体类型（Entity Type）

可选

如果指定，实体类型必须与被杀死的实体类型匹配才能触发事件。

---

原文：[Player Kill Entity Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_kill_entity) · 文档版本：0.8.0
