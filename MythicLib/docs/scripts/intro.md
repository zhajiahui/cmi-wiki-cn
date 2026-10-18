---
title: 介绍
source: https://docs.phoenixdevt.fr/mythiclib/scripts/intro
source_snapshot: '2026-10-19'
---

# 介绍 {#📜-introduction}

MythicLib提供自定义脚本语言，允许你执行操作、检查条件...为所有 MMO 插件创建自定义行为。脚本可用于发送消息、播放粒子效果、检查条件、损坏其他实体以及许多其他事情。

脚本执行称为[机制](mechanics/intro.md)的特定操作。你还可以设置[脚本运行必须满足的条件](mechanics/intro.md)。某些机制需要实体或位置等参数：例如，如果你想在给定位置生成粒子，则需要指定确切位置，这是使用 [目标选择器](targeters/intro.md)完成的。实体和位置都有目标选择器。

MythicLib脚本还具有 [变量](variables.md)，你可以使用它来保存临时信息或进行计算。例如，MythicLib具有多种可用于矢量计算的机制。

MythicLib脚本也可以变成MMOCore职业技能或MMOItems物品能力，更多信息请参见此 [wiki 页面](../skills/custom/mythiclib.md)。

## 非常重要！ {#very-important}

> **警告**
>
> **脚本不是技能！** 你可以将脚本转换为技能，但反之则不行。MythicLib脚本是实现技能的一种方法，然后将在MMOCore或MMOItems中使用。Fabled和MythicMobs还提供其脚本/技能系统。总体而言，MythicLib脚本语言的能力较差，但非常适合处理基本任务和not-too-complex技能。你无需安装任何其他内容即可使用MythicLib脚本，它们是built-in并且可以使用。

MythicLib定制技能系统的主要目标是能够使用你最喜欢用来编程的插件注册技能。如果MMOItems或MMOCore要求你使用 ML 脚本，你始终可以使用MythicMobs或Fabled来执行自定义脚本。

由于脚本用于MMOCore和MMOItems，因此它们主要面向创建自定义能力、技能或攻击效果。因此，它们具有预制工具，例如形状力学，可让你轻松显示炫酷的粒子效果、光线投射、投射物等。

## 脚本示例 {#script-example}

```yml
teststaff: # The name of your script/the skill ID for MMOCore usage, this should be in full caps for MMOCore. (also called up with /ml cast *skill ID*)
    mechanics:
        raycast: # This is a mechanic name. (this name can be whatever you want as long as it isn't the same as any other mechanic name in the file.)
            type: raytrace # This tells the script what mechanic to use, a list of mechanics can be found in the mechanics tab.
            hit_entity: teststaff_hit_entity # This calls upon another script when hitting an entity.
            tick: teststaff_tick # This calls upon another script on every tick. (A second is 20 ticks.)
            size: 1

teststaff_hit_entity: # The name of a script, used to call upon this script in another script.
    mechanics:
        dealdamage: 
            type: damage # What mechanic to use.
            amount: 10 # Sets the damage/mechanic parameter.
        showparticles: # This is another mechanic name.
            type: particle # What mechanic to use.
            particle: LAVA # This sets which particle it should show/parameter 1.
            amount: 32 # This sets the amount of particles to use/parameter 2.

teststaff_tick: # The name of a script, used to call upon this script in another script.
    mechanics:
        showparticles:
            type: particle
            particle: REDSTONE 
            amount: 4 
            x: .5 # This sets how far the particles can move on the x-axis on both sides around the source.
            y: .5 # This sets how far the particles can move on the y-axis on both sides around the source.
            z: .5 # This sets how far the particles can move on the z-axis on both sides around the source.
```

当玩家运行`teststaff`脚本时，它会向施法者视线中的第一个实体发送一束红石粒子，然后向该实体发送一束红石粒子，并造成10伤害。

然后，你可以使用`/ml reload`重新加载 ML 脚本，并使用`/ml cast YOUR_SCRIPT_NAME_HERE`投射新的技能

## 数值参数 {#numeric-parameters}

```yml
dealdamage:
    type: damage
    amount: '10 + <var.damage> / 2'
    target:
        type: caster
    knockback: false
    type: MAGIC,ON_HIT
```

许多机制都包含“数字参数”：`damage`机制造成的伤害量、应用药水效果的持续时间（以刻为单位）、粒子球体的半径……

99%这些力学完全支持数学公式。这意味着你可以将数字与常用运算符、数学函数甚至 PAPI占位符结合使用，以解锁自定义技能的完整可配置性。数值公式还支持[内部变量](variables.md)，如下所述。

## 文本参数 {#text-parameters}

需要字符串的机制支持PlaceholderAPI中的占位符，尽管这些并不是你可以使用的唯一占位符。MythicLib还具有[内部变量](variables.md)，你可以使用`<...>`访问它们，而不是PlaceholderAPI中通常的`%...%`格式。

```yml
tellmsg:
    type: tell
    format: 'Skill was cast at <source.x> - <source.y> - <source.z> by %player_name%!!'
    target:
        type: caster
```

## JSON/YAML语法 {#json-yaml-syntaxes}

技能的以下两种格式完全等效，并且都可以正常工作，因此你可以使用你最喜欢的一种。如果你更熟悉MythicMobs，请使用第二个。如果你更熟悉纯YAML甚至Fabled，请使用第一个。第二种JSON-ish 格式仅从MythicLib1.6.2+ 开发版本开始可用。

```yml
staff_attack:
    mechanics:
        raycast:
            type: raytrace
            hit_entity: staff_attack_hit_entity
            tick: staff_attack_tick
            size: 1
    conditions: {}
```

第二种格式使用字符串列表来存储脚本机制和条件，而不是配置部分。这种格式更紧凑，但可读性可能有点困难。

```yml
staff_attack:
    mechanics:
    - 'raytrace{type=raytrace;hit_entity=staff_attack_hit_entity;tick=staff_attack_tick;size=1}'
    conditions: []
```

---

原文：[📜 Introduction](https://docs.phoenixdevt.fr/mythiclib/scripts/intro) · 原文归档：2026-10-19
