---
title: 游戏时间受众（Game Time Audience）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/game_time_audience
source_version: 0.8.0
---

# 游戏时间受众（Game Time Audience）

`GameTimeAudienceEntry`根据游戏时间过滤受众。

## Minecraft日的总时间为`24000`tick。
时间的一些例子是： {#the-total-time-of-a-minecraft-day-is-24000-tickssome-examples-of-times-are}

|一天中的时间 |蜱虫 |
| --- | --- |
|黎明| 0 |
|中午| 6000 |
|黄昏| 12000 |
|午夜| 18000 |

---

## 用途示例 {#how-could-this-be-used}

这可用于仅允许在夜间通行到特定区域。
例如，一座只在晚上开门的吸血鬼城堡。
或者只在白天开放的市场。

## 字段 {#fields}

## 子条目（Children）

必填 · 列表

## 世界（World）

必填

## 生效时段（Active Times）

必填 · 列表

## 反转（Inverted）

必填

---

原文：[Game Time Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/game_time_audience) · 文档版本：0.8.0
