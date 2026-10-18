---
title: 移除物品（Remove Item Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/remove_item
source_version: 0.8.0
---

# 移除物品（Remove Item Action）

`Remove Item Action`是从玩家的背包中移除物品的操作。
此操作使你能够根据特定事件从玩家的背包中删除物品。

**注意**

此操作将尝试“尽可能多地”移除，但不会验证玩家的背包中是否有足够的物品。
如果你想保证玩家的背包中有足够的物品，请添加
[背包物品数量事实](../fact/inventory_item_count_fact.md)符合条件。

## 用途示例 {#how-could-this-be-used}

当`giving`NPC 是一个物品，并且你想要从玩家的背包中删除该物品时，可以使用此功能。
或者当你想要在玩家使用钥匙解锁门后从其背包中删除钥匙时。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 物品（Item）

必填

要移除的物品。

---

原文：[Remove Item Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/remove_item) · 文档版本：0.8.0
