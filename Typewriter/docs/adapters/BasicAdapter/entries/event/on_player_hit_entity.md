---
title: 玩家攻击实体事件（Player Hit Entity Event）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_hit_entity
source_version: 0.8.0
---

# 玩家攻击实体事件（Player Hit Entity Event）

当玩家击中实体时，会触发`Player Hit Entity Event`事件。如果你想检测玩家何时杀死实体，请使用[`Player Kill Entity Event`](on_player_kill_entity.md)事件。

## 用途示例 {#how-could-this-be-used}

此事件可用于创建自定义游戏模式，其中玩家必须击中一定数量的实体才能获胜。它还可以用来检测你何时击中某个实体，并使其对你产生攻击性。

## 字段 {#fields}

## 后续触发（Triggers）

必填 · 列表

## 实体类型（Entity Type）

可选

如果指定，实体类型必须与命中的实体类型匹配才能触发事件。

---

原文：[Player Hit Entity Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_hit_entity) · 文档版本：0.8.0
