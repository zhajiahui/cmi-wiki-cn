---
title: 动作栏对话过场动画（Action Bar Dialogue Cinematic）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/actionbar_dialogue_cinematic
source_version: 0.8.0
---

# 动作栏对话过场动画（Action Bar Dialogue Cinematic）

`Action Bar Dialogue Cinematic` 在动作栏中显示对话。
你可以指定说话者和对话。

## 用途示例 {#how-could-this-be-used}

该动画对于结合镜头路径显示对话非常有用。
对话显示在动作栏时，玩家仍可移动并观看镜头路径。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 说话者（Speaker）

必填

对话的说话者。

## 片段（Segments）

必填 · 列表 · 片段

片段是过场动画中的一个时间区间，可在此期间执行动作或显示信息。

**说明**

同一条目中的片段无法重叠。需要重叠片段时，请新建条目。

---

原文：[Action Bar Dialogue Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/actionbar_dialogue_cinematic) · 文档版本：0.8.0
