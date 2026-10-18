---
title: 手持物品事实（Item Holding Fact）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/item_holding_fact
source_version: 0.8.0
---

# 手持物品事实（Item Holding Fact）

`Item Holding Fact`是返回玩家当前持有的特定物品数量的事实。
当没有设置该物品的属性时，事实将返回玩家持有的物品的数量。

此事实仅供**读取**，无法写入，因此只适合用于条件判断。

## 用途示例 {#how-could-this-be-used}

当玩家持有特定物品时显示 PathStreams。
就像当玩家拿着地图时显示通往某个位置的路径一样。

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

原文：[Item Holding Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/item_holding_fact) · 文档版本：0.8.0
