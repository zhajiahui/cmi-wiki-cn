---
title: 方块交互事件（Interact Block Event）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_interact_with_block
source_version: 0.8.0
---

# 方块交互事件（Interact Block Event）

玩家右键与方块交互时，触发 `Interact Block Event`。

## 用途示例 {#how-could-this-be-used}

可用于创建特殊的方块交互，例如右键某个方块打开暗门，或设置需要钥匙才能打开的方块。

## 字段 {#fields}

## 后续触发（Triggers）

必填 · 列表

## 方块（Block）

必填

与之交互的块。

## 位置（Location）

可选

发生交互的方块位置。

## 手中物品（Item In Hand）

必填

与方块交互时玩家必须持有的物品。

## 取消（Cancel）

必填

触发时取消事件。
仅当满足所有条件时才会取消事件。
如果设置为 false，则不会修改事件。

## 交互类型（Interaction Type）

必填

应触发事件的交互类型。

## 潜行类型（Shift Type）

必填

触发事件所需的潜行状态。

---

原文：[Interact Block Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_interact_with_block) · 文档版本：0.8.0
