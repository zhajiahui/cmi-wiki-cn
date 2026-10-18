---
title: 数字占位符事实（Number Placeholder Fact）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/number_placeholder
source_version: 0.8.0
---

# 数字占位符事实（Number Placeholder Fact）

根据占位符计算得出的[事实](../../../../docs/creating-stories/facts.md)。
该占位符在读取事实时进行评估，并且必须返回数字或布尔值。

此事实仅供**读取**，无法写入，因此只适合用于条件判断。

## 用途示例 {#how-could-this-be-used}

确保玩家的等级足够高。
然后允许他们开始任务或进入地牢。

## 字段 {#fields}

## 备注（Comment）

继承 · 可选

用于跟踪该事实用途的注释。

## 组（Group）

必填

## 占位符

必填 · 支持占位符

要解析的占位符。
例如%player_level%。

**注意**

仅支持返回数字或布尔值的占位符！
如果你想使用返回字符串的占位符，
请改用[值占位符事实](value_placeholder.md)。

可以使用[`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki)中的占位符。例如，你可以使用`%player_name%`作为玩家名称。

---

原文：[Number Placeholder Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/number_placeholder) · 文档版本：0.8.0
