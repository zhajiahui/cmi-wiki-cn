---
title: Variablemath
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/variablemath
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variablemath {#variablemath}

## 说明 {#description}

将变量设置为数学方程的结果，其中“x”是[变量](../variables.md)的当前值。

基本上就是增加了一些功能的 setvariable 机制。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| equation | eq, e | 要执行的运算，必须放在引号内 | x |

> 该机制继承了 [SetVariable](setvariable.md) 机制的所有*可继承*属性

## 示例 {#examples}

将占位符存储在变量中

```yaml
    MMOVar:
      Skills:
      - variableMath{var=target.exp;equation="%mmocore_level%"}
```

做数学

```yaml
    Math1:
      Skills:
      - variableMath{var=caster.damage;equation="<caster.hp>*5"}
    Math2:
      Skills:
      - variableMath{var=caster.speed;equation="(<caster.var.age>/5)+1"}
```

## 别名 {#aliases}

- mathvariable
- varmath
- mathvar
