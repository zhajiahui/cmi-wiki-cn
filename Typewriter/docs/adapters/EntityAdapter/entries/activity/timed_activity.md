---
title: 定时活动（Timed Activity）
source: https://docs.typewritermc.com/adapters/EntityAdapter/entries/activity/timed_activity
source_version: 0.8.0
---

# 定时活动（Timed Activity）

`TimedActivityEntry` 在限定时长内运行子活动。

当持续时间结束时，活动将停用。
然后该活动将处于冷却状态一段时间，然后才能再次激活。

## 用途示例 {#how-could-this-be-used}

这可以用来让实体在有限的时间内做某事。

## 字段 {#fields}

## 持续时间（Duration）

必填

子活动的活动持续时间。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

## 冷却时间（Cooldown）

必填

活动再次激活前的冷却时间。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

## 生效时活动（Active Activity）

必填

当持续时间处于活动状态时将使用的活动。

## 冷却时活动（Cooldown Activity）

必填

处于冷却状态时将使用的活动。

---

原文：[Timed Activity](https://docs.typewritermc.com/adapters/EntityAdapter/entries/activity/timed_activity) · 文档版本：0.8.0
