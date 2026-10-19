---
title: 技能机制示例
source_url: https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/ExampleMechanic
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 技能机制示例

# Example 技能机制 {#example-mechanic}

## 说明 {#description}

技能机制的说明：它有什么作用、如何实现，以及可能需要的备注。

> **这是一个[仅支持 Paper](https://papermc.io/downloads/all)机制！**

> **这是[仅限高级版](../premium-features.md) 机制！**

> **这是一个无目标机制，受影响的实体将始终是施法者**

| [已实现的占位符](../skills/placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.example1>` |
| `<skill.var.example2>` |

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| attribute1 | alias1, alias2 | 各参数作用的说明 | 默认值 |
| attribute2 | alias3 | 各参数作用的说明 | 默认值 |
| attribute3 |  | 各参数作用的说明 | 默认值 |
| attribute4 |  | 属性作用的说明 **<[Premium-Only](../premium-features.md)>** | 默认值 |

> 该机制继承了 [ExampleMechanic2](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ExampleMechanic2) 机制的每个*可继承*属性
>

> > - `attribute4` 属性的**默认值**为 `0`
> > - `attribute5` 属性被**固定设置**为 `0`，无法修改

> *此技能机制没有属性。*

### Attribute1 属性 {#attribute1-attribute}

进一步解释属性的作用、实现方式、可接受的值等。此部分可选，仅在必要时填写。

## 示例 {#examples}

以下示例的描述。

```yaml
  Skills:
  - examplemechanic{attribute1=value1} @targeter
```

##  {#section}

另一个例子：

```yaml
  Skills:
  - examplemechanic{attribute1=value1;attribute2=value2} @targeter
```

## 别名 {#aliases}

- mechanic_alias_1
- mechanic_alias_2
