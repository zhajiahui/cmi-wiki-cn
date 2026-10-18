---
title: 玩家在附近活动（Player Close By Activity）
source: https://docs.typewritermc.com/adapters/EntityAdapter/entries/activity/player_close_by_activity
source_version: 0.8.0
---

# 玩家在附近活动（Player Close By Activity）

`PlayerCloseByActivityEntry`是一种当观看者靠近时激活子活动的活动。

仅当观看者位于定义的范围内时，该活动才会激活。

当达到最大空闲持续时间时，活动将停用。
如果最大空闲时间设置为0，则不会使用计时器。

## 用途示例 {#how-could-this-be-used}

例如，玩家需要跟随 NPC，却走远了，可以让 NPC 在玩家离开的位置附近徘徊或停下。玩家回来后，NPC 继续沿路径行走。

也可以让正在行走的 NPC 在玩家进入范围时停下。

## 字段 {#fields}

## 范围（Range）

必填

玩家必须靠近才能激活活动的范围。

## 最长待机时长（Max Idle Duration）

必填

在活动停用之前，玩家可以在相同范围内闲置的最长持续时间。

可以按以下格式指定持续时间：`1d 2h 3m 4s`。支持以下单位：`d`（天）、`h`（小时）、`m`（分钟）和`s`（秒）。

## 附近活动（Close By Activity）

必填

当附近有玩家时将使用的活动。

## 待机活动（Idle Activity）

必填

当附近没有玩家时将使用的活动。

---

原文：[Player Close By Activity](https://docs.typewritermc.com/adapters/EntityAdapter/entries/activity/player_close_by_activity) · 文档版本：0.8.0
