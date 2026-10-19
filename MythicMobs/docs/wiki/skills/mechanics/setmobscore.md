---
title: Setmobscore
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setmobscore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setmobscore {#setmobscore}

## 说明 {#description}

设置施法生物的记分板计分项值。此技能没有目标选择器，始终影响施法生物，与 ModifyMobScore 相同，但只能执行 **set** 操作。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| objective | obj, o | 指定要更改的记分项。如果记分项不存在，机制会自动创建。 |  |
| value | v | 执行运算时使用的数值。 |  |

## 示例 {#examples}

这会将目标“MyScore”上的生物分数设置为零

```yaml
ResetMyMobScore:
  Skills:
  - setmobscore{o=MyScore;v=0}
```

## 别名 {#aliases}

- sms
