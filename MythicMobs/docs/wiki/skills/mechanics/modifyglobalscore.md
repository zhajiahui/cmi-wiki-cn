---
title: Modifyglobalscore
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/modifyglobalscore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Modifyglobalscore {#modifyglobalscore}

## 说明 {#description}

修改假玩家`__GLOBAL__`的记分板目标值。这是一项无目标技能，不会影响任何其他玩家的得分。

操作语法的可能操作列表：

- `SET`
- `ADD`
- `SUBTRACT`
- `MULTIPLY`
- `DIVIDE`
- `MOD` [^mod]

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| objective | obj, o | 指定要更改的记分项。如果记分项不存在，机制会自动创建。 |  |
| action | a | 要执行的运算。 | ADD |
| value | v | 执行运算时使用的数值。 |  |

## 示例 {#examples}

```yaml
  Skills:
  - modifyglobalscore{objective=someobjective;action=multiply;v=2} ~onAttack
```

## 别名 {#aliases}

- mgs

[^mod]：modulo（取模）的缩写。
