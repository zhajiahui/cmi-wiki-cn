---
title: 粒子过场动画（Particle Cinematic）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/particle_cinematic
source_version: 0.8.0
---

# 粒子过场动画（Particle Cinematic）

`Particle Cinematic`条目用于生成过场动画的粒子。

## 用途示例 {#how-could-this-be-used}

这可用于为过场动画添加戏剧效果。
就像炸毁建筑物并产生一堆粒子一样。
或者，通过在某个区域周围生成粒子来将焦点添加到该区域。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 位置（Location）

必填

产生粒子的位置。

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

## 片段（Segments）

必填 · 列表 · 片段

片段是过场动画中的一个时间区间，可在此期间执行动作或显示信息。

**说明**

同一条目中的片段无法重叠。需要重叠片段时，请新建条目。

---

原文：[Particle Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/particle_cinematic) · 文档版本：0.8.0
