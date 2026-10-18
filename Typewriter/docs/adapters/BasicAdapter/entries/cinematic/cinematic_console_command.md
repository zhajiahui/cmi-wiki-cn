---
title: 过场动画控制台命令（Cinematic Console Command）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/cinematic_console_command
source_version: 0.8.0
---

# 过场动画控制台命令（Cinematic Console Command）

`Cinematic Console Command`条目作为控制台在特定帧运行命令。

## 用途示例 {#how-could-this-be-used}

可以配合其他插件让方块产生动画、隐藏记分板，或触发其他插件的功能。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 片段（Segments）

必填 · 列表 · 片段

在不同的段上运行命令

片段是过场动画中的一个时间区间，可在此期间执行动作或显示信息。

**说明**

同一条目中的片段无法重叠。需要重叠片段时，请新建条目。

---

原文：[Cinematic Console Command](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/cinematic_console_command) · 文档版本：0.8.0
