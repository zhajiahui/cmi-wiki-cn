---
title: 计时器受众（Timer Audience）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/timer_audience
source_version: 0.8.0
---

# 计时器受众（Timer Audience）

`Timer Audience`条目是受众过滤器，当玩家位于受众中时，它会在每个指定的持续时间内触发操作。

**注意**

非常短的持续时间可能会导致性能问题，并且可能不准确。

## 用途示例 {#how-could-this-be-used}

这可用于每隔几秒触发一个序列。

## 字段 {#fields}

## 持续时间（Duration）

必填

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

## 计时结束时（On Timer）

必填

---

原文：[Timer Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/timer_audience) · 文档版本：0.8.0
