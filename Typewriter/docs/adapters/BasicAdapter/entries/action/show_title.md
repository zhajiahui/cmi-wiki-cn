---
title: 显示标题（Show Title Action）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/show_title
source_version: 0.8.0
---

# 显示标题（Show Title Action）

`Show Title Action`是向玩家显示头衔的动作。如果需要，你可以指定字幕和持续时间。

## 用途示例 {#how-could-this-be-used}

可以用它来创建文本效果以响应特定事件，例如完成问题或其他任何内容。也可以用于其他场景。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 修改器（Modifiers）

继承 · 列表

此条目触发时，要为玩家修改的事实列表。

## 后续触发（Triggers）

必填 · 列表

## 标题（Title）

必填 · 支持颜色 · 支持占位符

要显示的标题文本。

可以使用[`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html)中的颜色和格式。例如，你可以使用`<red>Some Text</red>`表示红色文本。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

## 副标题（Subtitle）

必填 · 支持颜色 · 支持占位符

要显示的副标题文本。

可以使用[`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html)中的颜色和格式。例如，你可以使用`<red>Some Text</red>`表示红色文本。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

## 各阶段时长（Durations）

可选

标题的持续时间：淡入、停留多长时间、淡出。

---

原文：[Show Title Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/show_title) · 文档版本：0.8.0
