---
title: 执行玩家命令（Player Command Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/player_run_command
source_version: 0.8.0
---

# 执行玩家命令（Player Command Action）

`Player Command Action`是一个运行命令的动作，就像玩家输入的一样。
此操作使你能够代表玩家执行命令以响应特定事件。

## 用途示例 {#how-could-this-be-used}

此操作在多种情况下都很有用。
你可以使用它为玩家提供触发特定操作的自定义命令，
例如将玩家传送到特定位置或给他们一个物品。
你还可以使用它来自动执行重复性任务，
例如当玩家完成任务或成就时向他们发送消息。
也可以用于其他类似场景。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 命令（Command）

必填 · 多行 · 支持占位符

每一行都是一个不同的命令。命令不应以`/`为前缀。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

---

原文：[Player Command Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/player_run_command) · 文档版本：0.8.0
