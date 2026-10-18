---
title: 设置方块（Set Block Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/set_block
source_version: 0.8.0
---

# 设置方块（Set Block Action）

`SetBlockActionEntry`是在特定位置设置块的操作。

**注意**

这将为服务器上的所有玩家设置阻止，而不仅仅是触发该操作的玩家。
它会改变世界，所以使用这个动作时要小心。

## 用途示例 {#how-could-this-be-used}

可以用它来创建结构、设置陷阱或任何其他你想要放置的自定义块。也可以用于其他场景。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 材质（Material）

必填

要设置的方块材质。

## 位置（Location）

必填

要设置方块的位置。

---

原文：[Set Block Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/set_block) · 文档版本：0.8.0
