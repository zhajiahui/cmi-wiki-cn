---
title: Variable Contains
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/VariableContains
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variable Contains {#variable-contains}

## 说明 {#descriptions}

检查给定变量是否包含特定值。

- 对于字符串变量，是否检查变量是否包含子字符串。根据使用的compareType，还可以检查变量是否“以给定值开始”或“以给定值结束”。
- 对于 List 或 Set 变量：
  - 如果值是简单字符串，则检查 List 或 Set 是否包含该值
  - 如果条目是另一个列表或集合，则根据 compareType 检查变量是否包含该值的所有或任何元素。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| variable | name, n, var, key, k | 变量名称，可以在前面加上作用域。 |  |
| scope | s | 变量的[作用域](../variables.md#variable-scopes)，即变量所在的位置。 |  |
| compareType | compare, comp | 使用的比较类型，可以为 `ALL`、`ANY`、`EXACT_ENTRY`、`STARTS_WITH` 或 `ENDS_WITH`。 | ALL |
| value | val, v | 参与比较的值。 |  |

### CompareType 属性 {#comparetype-attribute}

如果变量是字符串，则可以使用 `STARTS_WITH` 或 `ENDS_WITH` 来检查变量是否以给定值开头或结尾

如果变量是List或Set并且值也是List或Set，则可以使用`ALL`检查变量中是否存在该值的所有元素，或使用`ANY`检查是否至少存在一个元素

`EXACT_ENTRY`（别名 `EXACTENTRY`、`EE`）检查给定值是否与变量中某个逗号分隔的条目完全匹配。比较前会移除条目和值两端的空白，所以值为 `apple, banana` 的字符串变量会匹配 `banana`。给定值作为单个条目处理：`apple,banana` 会整体比较，不会匹配；要检查多个条目请用 `ALL` 或 `ANY`。对于字符串变量，此模式不同于默认的子字符串检查。

## 示例 {#examples}

```yaml
  Conditions:
  - variablecontains{var=skill.examplelist;val=hello}

  - variablecontains{var=skill.examplelist;val=hello,world;compareType=ANY}

  - variablecontains{var=skill.examplestring;val=pizza}

  - variablecontains{var=skill.examplestring;val=dungeon_;compareType=STARTS_WITH}

  - variablecontains{var=skill.examplestring;val=pizza;compareType=EXACT_ENTRY}
```

## 别名 {#aliases}

- variableContain
- varContains
- varContain
- varCont
