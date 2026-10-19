---
title: Modifytargetscore
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/modifytargetscore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Modifytargetscore {#modifytargetscore}

## 说明 {#description}

修改指定目标选择器所选目标的记分板计分项值。

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

本例记录战斗中谁伤害了施法生物，以及各自的攻击次数。

```yaml
  Skills:
  - modifytargetscore{objective=damagescore;action=add;value=1} @trigger ~onDamaged
```

## 别名 {#aliases}

- mts

[^mod]：modulo（取模）的缩写。
