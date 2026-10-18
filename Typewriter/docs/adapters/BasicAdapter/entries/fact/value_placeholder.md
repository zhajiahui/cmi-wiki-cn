---
title: 值占位符事实（Value Placeholder Fact）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/value_placeholder
source_version: 0.8.0
---

# 值占位符事实（Value Placeholder Fact）

根据占位符计算得出的[事实](../../../../docs/creating-stories/facts.md)。
该占位符在读取事实时进行评估，并且可以返回任何内容。
该值将根据指定的`values`计算。

此事实仅供**读取**，无法写入，因此只适合用于条件判断。

## 用途示例 {#how-could-this-be-used}

如果你只想在玩家处于创造模式时运行某些操作。
或者根据天气情况，改变NPC的对话。

## 字段 {#fields}

## 备注（Comment）

继承 · 可选

用于跟踪该事实用途的注释。

## 组（Group）

必填

## 占位符

必填 · 支持占位符

要解析的占位符（例如 %player_gamemode%

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

## 值列表（Values）

必填 · 正则表达式

与占位符匹配的值及其相应的事实值。

一个例子是：

```yaml
values:
SURVIVAL: 0
CREATIVE: 1
ADVENTURE: 2
SPECTATOR: 3
```

如果占位符返回`CREATIVE`，则事实值将为`1`。
如果没有值匹配，则事实值将为`0`。

值中可以包含占位符。

[`Regular expressions`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)可用于匹配模式。例如，`^.*$`将匹配任何字符串。

---

原文：[Value Placeholder Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/value_placeholder) · 文档版本：0.8.0
