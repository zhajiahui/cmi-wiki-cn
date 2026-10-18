---
title: 使用 CoreTools
source: https://docs.phoenixdevt.fr/mythiclib/skills/custom/coretools
source_snapshot: '2026-10-19'
---

# 使用 CoreTools {#using-coretools}

[CoreTools](https://www.spigotmc.org/resources/coretools.125126/)可用于创建可在所有 MMO 插件中运行的技能。

## 定制技能注册 {#custom-skill-registration}

首先，将技能编码为CoreTools。在本教程中，我们将使用一个非常简单的脚本；它是built-in脚本，其中ID`script3`。

```yml
script3:
  Conditions: []
  Mechanics:
    - command{c="say Hello I'm Script 3"} @Self
```

然后，打开`MythicLib/skill`文件夹中的任何 YML 配置文件并粘贴以下内容：

```yml
MY_SKILL_3:
  source: 'coretools:script3'
```

重新加载这两个插件后，你现在可以在MMOItems和MMOCore中使用技能`MY_SKILL_3`。你可以尝试使用`/ml debug cast MY_SKILL_3`来投射它，你应该会看到该消息出现在玩家聊天中。

## 技能修饰符 {#skill-modifiers}

目前，使用CoreTools技能时无法检索技能修饰符，这与使用MythicMobs时不同。

## 技能条件 {#skill-conditions}

就像MythicMobs一样，使用CoreTools在MythicLib中注册的技能也可以有条件。如果不满足任何CoreTools条件，则不会施放技能，不会消耗魔力，不会应用冷却时间等。

---

原文：[Using CoreTools](https://docs.phoenixdevt.fr/mythiclib/skills/custom/coretools) · 原文归档：2026-10-19
