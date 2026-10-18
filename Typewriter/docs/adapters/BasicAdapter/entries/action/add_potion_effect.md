---
title: 添加药水效果（Add Potion Effect Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/add_potion_effect
source_version: 0.8.0
---

# 添加药水效果（Add Potion Effect Action）

`Add Potion Effect Action`是一个为玩家添加药水效果的动作。

## 用途示例 {#how-could-this-be-used}

可以用它为玩家提供增益或减益，例如速度或缓慢，或创建自定义效果。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 药水效果（Potion Effect）

必填

要添加的药水效果。

## 持续时间（Duration）

必填

药水效果的持续时间。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

## 效果等级（Amplifier）

必填

药水效果的等级。

## 环境效果（Ambient）

必填

是否作为环境效果。

## 粒子（Particles）

必填

是否显示药水效果粒子。

## 图标（Icon）

必填

是否在玩家的物品栏中显示药水效果图标。

---

原文：[Add Potion Effect Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/add_potion_effect) · 文档版本：0.8.0
