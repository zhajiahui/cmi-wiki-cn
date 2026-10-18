---
title: 检测命令执行事件（Detect Command Ran Event）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_detect_command_ran
source_version: 0.8.0
---

# 检测命令执行事件（Detect Command Ran Event）

当运行**已有的**命令时，会触发`Detect Command Ran Event`事件。

**注意**

仅当命令已存在时此事件才有效。如果你尝试创建尚不存在的新命令，请改用[`Run Command Event`](on_run_command.md)。

## 用途示例 {#how-could-this-be-used}

该事件可用于在运行特定命令时触发响应。
例如，你可以有一个命令，在运行命令时向通道发送消息，
它可以用作管理员的审核日志。

## 字段 {#fields}

## 后续触发（Triggers）

必填 · 列表

## 命令（Command）

必填 · 正则表达式

要监听的命令。
支持部分匹配。例如，要监听所有 warp 命令，
你可以使用`warp`作为命令。
也可以包含参数。例如，
要监听玩家是否传送到 spawn，
`warp spawn`为命令。

  

**注意**

请勿在命令开头包含`/`。
这将自动添加。

[`Regular expressions`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)可用于匹配模式。例如，`^.*$`将匹配任何字符串。

## 取消（Cancel）

必填

触发时取消事件

---

原文：[Detect Command Ran Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_detect_command_ran) · 文档版本：0.8.0
