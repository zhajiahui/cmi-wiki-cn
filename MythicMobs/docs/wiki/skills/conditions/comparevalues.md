---
title: Compare Values
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/CompareValues
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Compare Values {#compare-values}

## 说明 {#description}

根据指定的操作比较两个值。   比较是从`value1`与`value2`进行的：这意味着，例如，在`>`操作中，如果`value1`大于`value2`，它将返回`true`。

此条件可以比较整数、浮点数、双精度数（像往常一样）和字符串（按字典顺序）。

该条件将尝试“推断”给定值的类型，并首先比较最严格的类型，如果前一个类型不适用，则逐渐尝试更宽松的比较（整数 --> 双精度 --> 字符串）

如果你已经知道要传递的值的类型，则可以通过 `type` 属性进行指定，并且只会进行特定的比较，而不会在尝试和错误中浪费时间。如果由于值转换问题仍然无法进行比较，则条件将返回  false  

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| value1 | val1, v1 | 参与比较的第一个值。 |  |
| value2 | val2, v2 | 参与比较的第二个值。 |  |
| operator | op | 要使用的[运算符](comparevalues.md#operator-attribute)。 | EQUALS |
| type | t | 比较类型，可选。未设置时，会从严格到宽松依次尝试所有可用类型。设置后，仅按指定类型解释这些值并进行比较。接受任意[变量类型](../variables.md#variable-types)。 |  |

### Operator 属性 {#operator-attribute}

| 运算符 | 别名 |
| --- | --- |
| `==` | `EQUALS`, `EQUAL`, `EQ`, `EQL` |
| `!=` | `NOT_EQUALS`, `NOTEQUALS`, `NOTEQUAL`, `NE`, `NEQ`, `NEQL` |
| `>` | `GREATERTHAN`, `GREATER_THAN`, `GTR`, `GT` |
| `<` | `LT`, `LESSTHAN`, `LTR`, `LESS_THAN` |
| `>=` | `GTE`, `GREATERTHANOREQUALS`, `GTEO`, `GREATER_THAN_OR_EQUALS` |
| `<=` | `LTE`, `LESSTHANOREQUALS`, `LTEO`, `LESS_THAN_OR_EQUALS` |

## 示例 {#examples}

```yaml
  Conditions:
  - comparevalues{value1=%server_online%;operator=>=;value2=1/3*%bungee_total%}
```

> 若服务器玩家数大于或等于整个网络玩家数的 1/3，则返回   true  。

## 别名 {#aliases}

- comparevalue
