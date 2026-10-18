---
title: 组内触发（Group Trigger Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/group_trigger_action
source_version: 0.8.0
---

# 组内触发（Group Trigger Action）

`Group Trigger Action` 为触发玩家所在组的每位成员触发后续条目。

**注意**

修改器仅应用于触发动作的玩家。
要修改其他玩家的事实，需要在后续条目中处理。

## 用途示例 {#how-could-this-be-used}

这可用于触发与玩家同一组中的每个人的下一个条目，
当玩家加入阵营时，同一阵营中的所有其他玩家都会收到通知。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 组（Group）

必填

## 强制分组（Force Group）

可选

要触发后续条目的组。未设置时，使用触发该动作的玩家所在的组。

---

原文：[Group Trigger Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/group_trigger_action) · 文档版本：0.8.0
