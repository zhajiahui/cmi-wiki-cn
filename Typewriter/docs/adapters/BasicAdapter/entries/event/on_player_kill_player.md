---
title: 玩家击杀玩家事件（Player Kill Player Event）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_kill_player
source_version: 0.8.0
---

# 玩家击杀玩家事件（Player Kill Player Event）

当一名玩家杀死另一名玩家时，会触发`Player Kill Player Event`。如果你想检测玩家何时杀死其他东西，请改用[`Player Kill Entity Event`](on_player_kill_entity.md)。

## 用途示例 {#how-could-this-be-used}

这可以用来创建一个赏金系统，有人向另一个玩家发放赏金，当该玩家被杀时，赏金就会支付给杀死他们的玩家。

## 字段 {#fields}

## 后续触发（Triggers）

必填 · 列表

## 被击杀者触发项（Killed Triggers）

必填 · 列表

被杀死的玩家将会触发与此字段相关的条目。

---

原文：[Player Kill Player Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_kill_player) · 文档版本：0.8.0
