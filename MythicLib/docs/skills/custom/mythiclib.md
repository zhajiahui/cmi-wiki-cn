---
title: 使用 MythicLib
source: https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythiclib
source_snapshot: '2026-10-19'
---

# 使用 MythicLib {#using-mythiclib}

MythicLib[脚本](../../scripts/intro.md)可以轻松转换为可在MMOItems或MMOCore中使用的自定义技能。我们首先需要编写一个MythicLib脚本，然后将其声明为技能。脚本基本上说“发生了什么”，而技能提供更多元数据，包括其魔力成本、冷却时间、损坏、GUI描述、图标......

## 1/ 编写MythicLib脚本 {#_1-code-a-mythiclib-script}

首先，导航到`MythicLib/script`文件夹并打开现有/创建新的 YML 配置文件以开始编写MythicLib脚本。

在本教程中，我们将使用MythicLib附带的内置`staff_attack`脚本。你可以在`MythicLib/script/example_skills.yml`文件中找到它。该脚本发射一枚魔法射弹，对其击中的第一个实体造成10伤害。

```yml
# The script that you cast to peform the staff attack
staff_attack:
  mechanics:
    - 'raytrace{hit_entity=staff_attack_hit_entity;tick=staff_attack_tick;size=1}'
    - 'sound{sound=ENTITY_BLAZE_SHOOT;pitch=1;volume=1}'

# The effect when the attack hits an entity
staff_attack_hit_entity:
  conditions:
    - 'can_target'
  mechanics:
    - 'damage{amount=10;ignore_immunity=true}'
    - 'particle{particle=LAVA;amount=32}'

# The tick effect while the raytrace is ongoing
staff_attack_tick:
  mechanics:
    - 'particle{particle=REDSTONE;amount=4;x=.5;y=.5;z=.5}'
```

## 2/ 将脚本声明为技能 {#_2-declare-the-script-as-a-skill}

现在我们有了名为`staff_attack`的MythicLib脚本，我们需要将其声明为技能并提供其他元数据。现在，导航到`MythicLib/skill`文件夹并创建一个新的/打开现有的 YML 配置。将以下代码复制到文件中：

```yml

# This will register a skill with ID 'MY_NEW_SKILL'
STAFF_ATTACK:

  # This points to the MythicLib script you want to use
  # located in the MythicLib/scripts folder
  source: 'mythiclib:staff_attack'

  name: 'Staff Attack' # The skill name shown in the GUI
  icon: 'BLAZE_ROD' # The skill icon shown in the GUI
  lore:
    - '§7Shoot a magic projectile'
    - '§7that deals damage to'
    - '§7the first entity it hits.'

  # This is optional. These are the skill parameters/modifiers
  # that will be passed to MMOItems/MMOCore when the skill is executed.
  # You can add as many as you need.
  parameters:
    damage:
      name: Damage
      player: 10
      item: 10
    slow_duration:
      name: Effect Duration
      player: 5
      item: 5
```

## 3/ 重新加载MythicLib {#_3-reload-mythiclib}

使用`/ml reload`重新加载MythicLib脚本和技能。你可以使用以下命令测试新的技能：

```
/ml debug cast staff_attack
```

---

原文：[Using MythicLib](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythiclib) · 原文归档：2026-10-19
