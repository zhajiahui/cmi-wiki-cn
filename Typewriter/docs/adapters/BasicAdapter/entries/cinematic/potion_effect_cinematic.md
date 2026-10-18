---
title: 药水效果过场动画（Potion Effect Cinematic）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/potion_effect_cinematic
source_version: 0.8.0
---

# 药水效果过场动画（Potion Effect Cinematic）

`PotionEffectCinematicEntry`用于在过场动画期间向玩家应用不同的药水效果。

## 用途示例 {#how-could-this-be-used}

这可用于在不同时间动态应用失明、缓慢等效果
在过场动画中，增强故事讲述或游戏体验。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 片段（Segments）

必填 · 列表 · 片段

片段是过场动画中的一个时间区间，可在此期间执行动作或显示信息。

**说明**

同一条目中的片段无法重叠。需要重叠片段时，请新建条目。

---

原文：[Potion Effect Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/potion_effect_cinematic) · 文档版本：0.8.0
