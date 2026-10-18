---
title: 限时事实（Timed Fact）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/timed_fact
source_version: 0.8.0
---

# 限时事实（Timed Fact）

该事实被存储一段时间。
过了该时间，它就会被重置。

## 用途示例 {#how-could-this-be-used}

这个事实可以充当计时器，当事实用完时，它可以用来触发一个动作。

## 字段 {#fields}

## 备注（Comment）

继承 · 可选

用于跟踪该事实用途的注释。

## 组（Group）

必填

## 持续时间（Duration）

必填

事实到期后的持续时间。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

---

原文：[Timed Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/timed_fact) · 文档版本：0.8.0
