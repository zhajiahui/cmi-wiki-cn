---
title: 执行控制台命令（Console Command Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/console_run_command
source_version: 0.8.0
---

# 执行控制台命令（Console Command Action）

控制台命令动作向服务器控制台发送命令，用来在指定事件发生时执行控制台命令。

## 用途示例 {#how-could-this-be-used}

可以用于管理操作，例如向所有玩家发送消息，或自动设置服务器时间、天气等。

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

原文：[Console Command Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/console_run_command) · 文档版本：0.8.0
