---
title: Setglobalscore
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setglobalscore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setglobalscore {#setglobalscore}

## 说明 {#description}

修改假玩家`__GLOBAL__`的记分板目标值。这是一个无目标技能，不会影响任何其他玩家的得分。工作原理与 ModifyGlobalScore 机制完全相同，但只能执行 **set** 操作。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| objective | obj, o | 指定要更改的记分项。如果记分项不存在，机制会自动创建。 |  |
| value | v | 执行运算时使用的数值。 |  |

## 示例 {#examples}

```yaml
SetSomeScore:
  Skills:
  - setglobalscore
      {
      objective=someobjective;
      v=2
      }
```

## 别名 {#aliases}

- sgs
