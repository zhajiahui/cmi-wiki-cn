---
title: 生成粒子（Spawn Particle Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/spawn_particles
source_version: 0.8.0
---

# 生成粒子（Spawn Particle Action）

`Spawn Particle Action`是在给定位置生成特定粒子的动作。此操作使你能够生成具有指定类型、数量和位置的粒子。

## 用途示例 {#how-could-this-be-used}

可以用它来创建视觉效果以响应特定事件，例如爆炸或魔法咒语。也可以用于其他场景。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 位置（Location）

可选

产生粒子的位置。 （默认为玩家位置

## 粒子（Particle）

必填

要生成的粒子。

## 数量（Count）

必填

要生成的粒子数量。

## X 轴偏移（Offset X）

必填

相对于指定位置在 X 轴上的偏移。

## Y 轴偏移（Offset Y）

必填

相对于指定位置在 Y 轴上的偏移。

## Z 轴偏移（Offset Z）

必填

相对于指定位置在 Z 轴上的偏移。

## 速度（Speed）

必填

粒子的速度。对于某些粒子，这是控制粒子行为的“额外”数据值。

---

原文：[Spawn Particle Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/spawn_particles) · 文档版本：0.8.0
