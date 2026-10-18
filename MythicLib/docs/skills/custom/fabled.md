---
title: 使用 Fabled
source: https://docs.phoenixdevt.fr/mythiclib/skills/custom/fabled
source_snapshot: '2026-10-19'
---

# 使用 Fabled {#using-fabled}

Fabled，原名 ProSkillAPI ，或SkillAPI，是一个强大的技能创建和管理插件。你可以在Fabled内创建自定义技能并在MythicLib内使用它们。

> **信息**
>
> 从MythicLib1.6.2快照开始，不再支持SkillAPI和 ProSkillAPI，因为这两个插件都不再得到积极维护。我们要求用户改用Fabled。

## 定制技能注册 {#custom-skill-registration}

与MythicMobs类似，你可以使用Fabled技能编辑器将自定义技能注册到MythicLib中。除了MythicLib技能配置文件的格式之外，该过程与[本教程](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic#custom-skill-registration)中的过程完全相同。

首先，使用Fabled技能编辑器对技能进行编码。假设你编码的技能具有ID`Firebolt`。打开`MythicLib/skill`文件夹中的 YML 配置文件并粘贴以下内容：

```yml
FIREBOLT:
  source: 'fabled:<Fabled_skill_identifier>'
  name: 'Firebolt'

  # Parameters/modifiers are not supported.
  #parameters: {}
```

## 技能修饰符 {#skill-modifiers}

目前，使用Fabled技能时无法检索技能修饰符，这与使用MythicMobs时不同。因此可以省略上面配置片段中的`parameters`部分。

## 技能等级 {#skill-level}

也就是说，所有使用Fabled注册的技能都有一个`level`技能修饰符，它直接挂钩到Fabled技能关卡系统。你可以将技能机械数值参数设置为在技能等级上线性缩放。使用MythicMobs，你可以设置你想要的任何类型的缩放（不限于线性缩放）。

就像`cooldown` `mana`和`stamina`一样，`level`修饰符会自动注册。

> **提示**
>
> 虽然Fabled仍然是自定义技能创建的选项，但我们仍然建议使用MythicMobs

---

原文：[Using Fabled](https://docs.phoenixdevt.fr/mythiclib/skills/custom/fabled) · 原文归档：2026-10-19
