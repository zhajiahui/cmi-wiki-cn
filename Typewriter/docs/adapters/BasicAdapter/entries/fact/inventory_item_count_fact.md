---
title: 背包物品数量事实（Inventory Item Count Fact）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/inventory_item_count_fact
source_version: 0.8.0
---

# 背包物品数量事实（Inventory Item Count Fact）

`Inventory Item Count Fact`是返回玩家背包中特定物品数量的事实。

此事实仅供**读取**，无法写入，因此只适合用于条件判断。

## 用途示例 {#how-could-this-be-used}

这可以用来检查玩家的背包中是否有特定的物品，或者检查他们是否有特定数量的物品。
比如给玩家一个收集 10 个苹果的任务，然后检查他们的背包中是否有 10 个苹果。

## 字段 {#fields}

## 备注（Comment）

继承 · 可选

用于跟踪该事实用途的注释。

## 组（Group）

必填

## 物品（Item）

必填

要检查的物品。

---

原文：[Inventory Item Count Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/inventory_item_count_fact) · 文档版本：0.8.0
