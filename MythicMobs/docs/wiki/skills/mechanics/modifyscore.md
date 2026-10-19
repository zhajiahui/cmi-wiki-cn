---
title: Modifyscore
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/modifyscore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Modifyscore {#modifyscore}

## 说明 {#description}

修改假玩家姓名的记分板目标值。   也可用于修改特定玩家的分数。

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
| action | a | 要执行的运算。 | SET |
| value | v | 执行运算时使用的数值。 | 0 |
| name, entry | n, e | 玩家或虚拟玩家的名称。 | dummy |

## 示例 {#examples}

此示例将为目标“TestScore”的名为“Bob”的玩家的分数加一，即使该玩家在服务器上不存在。如果目标当前不存在，它将创建该目标。

```yaml
  Skills:
  - modifyscore{o=TestScore;e=Bob;a=add;v=1} ~onInteract 
```

![](https://i.imgur.com/0HKvAUM.png)

[^mod]：modulo（取模）的缩写。
