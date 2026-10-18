---
title: Boss 栏（Boss Bar）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/boss_bar
source_version: 0.8.0
---

# Boss 栏（Boss Bar）

`BossBarEntry`是一个在屏幕顶部显示一个栏的显示器。

## 用途示例 {#how-could-this-be-used}

这可用于显示任务中的目标，或显示任务的进度。

## 字段 {#fields}

## 标题（Title）

必填 · 支持颜色 · 支持占位符

Boss 栏的标题。

可以使用[`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html)中的颜色和格式。例如，你可以使用`<red>Some Text</red>`表示红色文本。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

## 进度（Progress）

必填

Boss 栏的填充比例。0.0 为空，1.0 为满。

## 颜色（Color）

必填

Boss 栏的颜色。

## 样式（Style）

必填

Boss 栏是否分段。

## 标志（Flags）

必填 · 列表

应用于 Boss 栏的标志。

---

原文：[Boss Bar](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/boss_bar) · 文档版本：0.8.0
