---
title: Randomskill
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/randomskill
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Randomskill {#randomskill}

## 说明 {#description}

从给定[技能](skill.md)列表中随机执行一个技能，忽略仍在冷却或条件未满足的技能。列表中的技能数量不限。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| skills | s, m, meta, metas | 要执行的技能列表，必须用 `,` 分隔 |  |
| fallbackskill | fbskill, fbs | randomskill 列表中的所有技能都未通过条件检查时执行的元技能 |  |

## 权重 {#weight}

你还可以通过权重系统使你的技能以不同的机会执行，只需在技能名称后添加空格和数字即可。没有权重的技能将默认权重1。数字越高，技能被选择的机会就越高。

在这个例子中，SkillOne被选中的机会最高，然后是SkillFour，因为它的默认权重为1，然后是SkillTwo，其权重为0.5，最后，SkillThree的机会最低。

```yaml
Skills:
- randomskill{skills=SkillOne 10,SkillTwo 0.5,SkillThree 0.1,SkillFour}
```

## 示例 {#examples}

```yaml
Skills:
- randomskill{skills=skill1,skill2,skill3}
```

在概述你的随机技能语法时遇到问题？试试这个：

```yaml
Skills:
- randomskill{
    skills=
    superskill,
    green_skill,
    skill3,
    grandSkill,
    7331
    }
```

随机技能也可以完全内联编写！

```yaml
Skills:
- randomskill{skills=
    [- message{m="&7Pleasant afternoon we're having!"} @trigger],
    [- message{m="&7A nice sunny afternoon."} @trigger],
    [- message{m="&7Good Afternoon <trigger.name>! Good to see you!"} @trigger]} @trigger
```

## 别名 {#aliases}

- randommeta
