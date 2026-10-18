---
title: 掉落物品（Drop Item Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/drop_item
source_version: 0.8.0
---

# 掉落物品（Drop Item Action）

`Drop Item Action`是一个在世界中掉落物品的动作。
可以指定掉落物品的 Minecraft 材质、数量、显示名称、物品描述和位置。

## 用途示例 {#how-could-this-be-used}

此操作在多种情况下都很有用。
你可以使用它来创建带有随机物品的宝箱，从被击败的敌人那里掉落战利品，或者在世界中生成自定义物品。
也可以用于其他类似场景。

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

要掉落的物品。

## 位置（Location）

可选

掉落物品的位置。留空时，物品会掉落在触发动作的玩家所在位置。

---

原文：[Drop Item Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/drop_item) · 文档版本：0.8.0
