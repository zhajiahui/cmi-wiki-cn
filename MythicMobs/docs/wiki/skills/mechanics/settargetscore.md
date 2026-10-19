---
title: Settargetscore
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/settargetscore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Settargetscore {#settargetscore}

## 说明 {#description}

修改指定目标选择器所选目标的记分板计分项值。作用与 ModifyTargetScore 机制相同，但只能执行 **set** 操作。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| objective | obj, o | 指定要更改的记分项。如果记分项不存在，机制会自动创建。 |  |
| value | v | 执行运算时使用的数值。 |  |

## 示例 {#examples}

本例记录战斗中谁伤害了施法生物，以及各自的攻击次数。

```yaml
  Skills:
  - settargetscore{
      objective=damagescore;
      value=1
      } @trigger ~onDamaged
```

## 别名 {#aliases}

- sts
