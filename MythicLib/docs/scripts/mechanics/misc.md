---
title: 其他功能
source: https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/misc
source_snapshot: '2026-10-19'
---

# 其他功能 {#🔧-miscellaneous}

> **警告**
>
> 建设中

## 适用冷却时间 {#apply-cooldown}

在MMOItems/MMOCore中，任何具有冷却时间的对象（物品、招架、闪避、技能等）都有一个与其关联的冷却时间密钥（请参阅[此处](../variables.md#cooldownmap)）。只要它没有在MMOItems/MMOCore中使用，你就可以为你的插件声明任何字符串密钥并将其用于任何用途。

MythicLib完全允许你设置冷却时间。与冷却时间条件配合使用，你可以在脚本内全面检查、计算和应用冷却时间。

冷却时间值以秒为单位。

```yml
example_mechanic:
  mechanics:
  - 'apply_cooldown{path=myplugin_someskill;value=10}'
```

## 减少目标的冷却时间 {#reduce-cooldown-of-target}

> **提示**
>
> 首先学习上面的机制。

`value`确定冷却时间减少的量，默认以秒为单位。参数`reduction`确定“缩减模式”，如下所述。

如果模式设置为`FLAT`，目标冷却时间将减少设定的秒数。如果模式设置为`INITIAL`，目标冷却时间将减少其初始值的 X%。对于10s的初始冷却时间，使用模式`INITIAL`进行20%冷却时间缩减将把目标冷却时间缩减`20% * 10 = 2s`。

如果模式设置为`REMAINING`，目标冷却时间将减少其剩余（不是总计）值的 X%。对于10s冷却时间，如果3s已通过，则剩余的冷却时间为7s。20%剩余的冷却时间减少相当于`20% * (10 - 3) = 1.4s`冷却时间的固定减少。

```yml
example_mechanic:
  mechanics:
  - 'reduce_cooldown{path=myplugin_someskill;value=5;reduction=FLAT}'
```

## 为脚本添加延迟 {#adding-delay-to-your-script}

延迟以**刻**为单位。机器学习将在执行下一个机制之前等待一定数量的时钟周期。确保延迟参数大于零。

```yml
example_mechanic:
  mechanics:
  - 'delay{amount=10}'
```

## 发送命令 {#dispatch-a-command}

将`from_console`设置为`true`以使命令改为由控制台调度，否则 ML 将采用脚本目标实体。将`op`设置为true以使命令作为 op 运行。`target`是可选的。

```yml
example_mechanic:
  mechanics:
  - 'dispatch_command{from_console=true;op=false;format="mmocore admin skill-points add <caster.name> 10";target=caster}'
```

## 播放实体效果 {#play-an-entity-effect}

实体效果可用[在Spigotjavadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/EntityEffect.html)上。例如，`HURT`非常有用，它只是模拟0损坏攻击 - 非常适合通过non-damaging效果改进技能-。`target`是将播放效果的实体。如果未提供，则默认为脚本目标实体或脚本施法者。

```yml
example_script:
  mechanics:
  - 'entity_effect{effect=HURT;target=target}'
```

## 引发雷击 {#trigger-a-lightning-strike}

将`effect`设置为`false`使闪电不会造成伤害。

```yml
example_script:
  mechanics:
  - 'lightning_strike{effect=false;target_location=target}'
```

## 投射另一个剧本 {#cast-another-script}

这个机械师非常特别。它可用于投射具有特定目标实体和位置的另一个脚本。它还可用于修改脚本的源位置。

它的所有参数都是可选的。你可以提供一个实体目标选择器（对于脚本目标实体，通过`target`）和两个位置目标选择器（一个通过`source`用于脚本源位置，一个通过`target_location`用于脚本目标位置）。

```yml
example_script:
  mechanics:
  - 'script{name=other_script_name;target=......;target_location=.....;source=.....}'

# Other script being called
other_script_name:
  # ..
```

这也可用于连续多次投射同一脚本，同时计算迄今为止已投射的次数。以下脚本将12乘以名为`ite`的脚本。变量`iteration_count`用于计算到目前为止脚本已被投射的次数。因此可以使用占位符`<iteration_count>`对其进行访问。

```yml
example_script:
  mechanics:
  - 'script{name=iterated_script;iterations=12;counter=iteration_count}'

# Script ran multiple times
iterated_script:
  mechanics:
  # Can use variable "iteration_count" inside this script
  - 'give_item{material=DIAMOND;amount=<var.iteration_count>;target=caster}'
```

## 给一个物品 {#give-an-item}

将原版物品赋予玩家。

```yml
example_script:
  mechanics:
  - 'give_item{amount=<modifier.amount>;material=DIAMOND;target=caster}'
```

## 射箭 {#shoot-an-arrow}

让玩家射箭。`from_item`由MMOItems用于武器类型。`player_attack_damage`使箭头使用玩家的攻击伤害基础属性作为基础伤害。`velocity`是箭头速度的乘数。默认为1.0（正常速度）。

`damage_types`是应用于箭头的伤害类型comma-separated列表。默认情况下，除非在MythicLib配置文件中进行修改，否则箭头会造成物理/武器伤害。

`hit`是当箭头击中实体或块时要执行的脚本的名称。`land`是当箭头落在地面上但没有击中任何物体时要执行的脚本的名称。`tick`是箭头飞行时每个刻执行的脚本的名称。

```yml
example_script:
  mechanics:
  - 'shoot_arrow{from_item=false;player_attack_damage=false;hit=on_hit_script;land=on_land_script;tick=on_tick_script;velocity=1.5;damage_types="physical,weapon"}'

on_hit_script:
  #.....

on_land_script:
  #.....

on_tick_script:
  mechanics:
  - 'particle{effect=FLAME}'
```

## 取消活动 {#cancel-event}

如果脚本是由事件（如 EntityDamageByEntityEvent、PlayerInteractEvent 等）触发的，则此机制将取消该事件。否则，会打印出错误。

例如，这可以用于防止实体损坏事件期间的损坏。

```yml
example_script:
  mechanics:
  - 'cancel_event{}'
```

---

原文：[🔧 Miscellaneous](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/misc) · 原文归档：2026-10-19
