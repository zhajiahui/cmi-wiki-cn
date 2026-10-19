---
title: Variableisset
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/variableisset
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variableisset {#variableisset}

## 说明 {#description}

检查给定的[变量](../variables.md)是否已设置。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| variable | name, n, var, key, k | 变量名称，可以在前面加上作用域。 |  |
| scope | s | 变量的[作用域](../variables.md#variable-scopes)，即变量所在的位置。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - variableisset{var=target.dazed} true
```

## 别名 {#aliases}

- varisset
- varset
