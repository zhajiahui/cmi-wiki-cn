---
title: 触发序列过场动画（Trigger Sequence Cinematic）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/trigger_sequence_cinematic
source_version: 0.8.0
---

# 触发序列过场动画（Trigger Sequence Cinematic）

运行一系列触发器的`Trigger Sequence Cinematic`条目。它非常强大，但也非常危险。

**注意**

请注意哪些触发器正在运行。如果你运行每个人都可以查看的触发器，那么每个人都将看到它。
此外，**不要在这里触发对话**；对话不应从过场动画中触发。
如果你想在过场动画结束后触发对话，请将其连接到[启动过场动画](../action/cinematic.md)

## 用途示例 {#how-could-this-be-used}

当你想使用任何可触发条目时。就像在特定帧向玩家提供物品一样。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 片段（Segments）

必填 · 列表 · 片段

触发器运行的顺序

片段是过场动画中的一个时间区间，可在此期间执行动作或显示信息。

**说明**

同一条目中的片段无法重叠。需要重叠片段时，请新建条目。

---

原文：[Trigger Sequence Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/trigger_sequence_cinematic) · 文档版本：0.8.0
