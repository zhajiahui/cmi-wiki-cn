---
title: Variablesubtract
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/variablesubtract
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variablesubtract {#variablesubtract}

## 说明 {#description}

从指定作用域的[变量](../variables.md)减去给定数值。

> 该机制根据变量类型有不同的行为。 [更多信息在这里](../variables.md#variable-types-behavior)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a, value, val, v | 要减去的值 | 0 |

> 该机制继承了 [SetVariable](setvariable.md) 机制的所有*可继承*属性

## 示例 {#examples}

```yaml
  Skills:
  - variablesubtract{var=skill.testVar;amount=1} ~onInteract
```

## 别名 {#aliases}

- variableSub
- subtractVariable
- subVar
- reduceVariable
