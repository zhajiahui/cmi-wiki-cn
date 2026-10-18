---
title: 实体过场动画（Entity Cinematic）
source: https://docs.typewritermc.com/adapters/EntityAdapter/entries/cinematic/entity_cinematic
source_version: 0.8.0
---

# 实体过场动画（Entity Cinematic）

`Entity Cinematic` 在实体上回放录制的动画，展示给玩家。

## 用途示例 {#how-could-this-be-used}

这可用于创建动画的过场动画实体。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 定义（Definition）

必填

将在过场动画中使用的实体

## 片段（Segments）

必填 · 列表 · 片段

片段是过场动画中的一个时间区间，可在此期间执行动作或显示信息。

**说明**

同一条目中的片段无法重叠。需要重叠片段时，请新建条目。

---

原文：[Entity Cinematic](https://docs.typewritermc.com/adapters/EntityAdapter/entries/cinematic/entity_cinematic) · 文档版本：0.8.0
