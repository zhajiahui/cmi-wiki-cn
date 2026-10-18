---
title: 其他功能
source: https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/misc
source_snapshot: '2026-10-19'
---

# 其他功能 {#miscellaneous}

> **警告**
>
> 建设中

## 如果脚本施法者可以损坏/目标实体 {#if-script-caster-can-damage-target-entity}

这是 MMO 插件的集中检查。它用于确定玩家是否可以损坏/增强另一个实体，而此操作不违法。想象一下，你不希望你的玩家技能损坏同一方内的玩家，可以使用此条件来完成。同样，你也不希望玩家能够对敌人使用治疗或增益效果。

MMOCore/MMOItems技能检查相同的条件，以确保它们不会被投射到错误的目标上，从而构成游戏缺陷。

这会检查很多事情：

- 如果目标是生物体（如果有生命条则为i.e）
- 如果目标不是Citizens中不可杀死的 NPC
- 如果玩家与脚本目标不在同一队伍/行会中
- WorldGuard/住宅/bukkit原版PvP标志。

有四种不同的交互类型：

- `OFFENSE_SKILL`(技能造成伤害)
- `OFFENSE_ACTION`（基本/近战/武器攻击）
- `SUPPORT_SKILL`（技能增益或治疗，对目标施加积极效果）
- `SUPPORT_ACTION`（尚未使用）每次使用`can_target`条件时，你需要指定交互类型，以便MythicLib知道要检查什么，以防你碰巧使用受支持的队伍/guild 插件！

以下技能称为`slash`，对附近的实体造成100伤害**仅当它们实际上可以被脚本运行程序损坏**时。

```
slash:
    mechanics:
        execute_skill_onto_nearby_entities:
            type: skill
            name: slash_subskill
            target:
                type: nearby_entities
                radius: 3
                height: 1

slash_subskill:
    conditions: # Filters untargetable entities
        cantarget:
            type: can_target
            interaction_type: OFFENSE_SKILL
    mechanics:
        deal_damage:
            type: damage
            amount: 100
```

## 检查玩家冷却时间 {#check-for-a-player-cooldown}

这会检查玩家上是否有冷却时间上的内容。你必须为MythicLib选择一些字符串标识符（称为冷却时间路径）来保存你的冷却时间信息。

如果你想检查MMOItems或MMOCorei.e物品或技能冷却时间中的冷却时间，请参阅[此 wiki 部分](../variables.md#cooldownmap)，其中提供了你需要的冷却时间路径用于哪个对象。

MythicLib完全允许你设置冷却时间。与冷却时间机制配合使用（在 *Mechanics* wiki 部分了解更多信息），你可以在脚本内全面检查、计算和应用冷却时间。

```
example_condition:
    type: cooldown
    path: 'skill_life_ender' # This checks if the Life Ender skill is on cooldown!
```

## 检查脚本施法者的食物水平 {#check-for-the-script-caster-s-food-level}

检查脚本施法者是否有足够的食物。你可以使用`compare`通用条件执行完全相同的条件，但我们保留这一条件是为了向后兼容。

```
example_condition:
    type: food
    amount: '10 + <caster.health> / 2'
```

## 检查触发脚本的攻击是否具有某种损坏类型 {#check-if-attack-which-triggered-the-script-has-some-damage-type}

请先了解一下【触发器](../../skills/triggers.md)。使用`ATTACK`触发器类型时，由于脚本是由攻击触发的，因此你实际上可以使用`<attack>`内部变量访问有关此攻击的信息。

此条件可用于检查触发脚本的攻击是否包含某种类型的损坏。这对于玩家技能非常有用，例如，它应该仅适用于武器攻击：你只需检查攻击是否包含一些`WEAPON`损坏。

你可以使用多种伤害类型。如果攻击包含任何损坏类型，则满足条件。如果脚本不是由实体攻击触发的，它将抛出控制台错误。

```
example_condition:
    type: has_damage_type
    types: 'WEAPON,PHYSICAL,PROJECTILE'
```

## 检查目标实体是否还活着 {#check-if-the-target-entity-is-living}

检查目标实体是否有生命值条。

```
example_condition:
    type: is_living
```

## 检查目标实体是否着火 {#check-if-the-target-entity-is-on-fire}

用它来检查脚本目标实体是否着火。这将检查脚本施法者是否将`caster`设置为true（默认情况下为false）；

```
example_condition:
    type: on_fire
    caster: false
```

## 权限检查 {#permission-check}

使用它来检查脚本施法者是否具有特定的权限。

```
example_condition:
    type: condition
    name: 'mmoitems.ability.fireball'
```

## 时间检查 {#time-check}

检查脚本世界是否在特定时间段内：`DAY`（0到12000刻），`DUSK`（12000到13000），`NIGHT`（13000到23000） ）或`DAWN`（23000至24000）。根据 wiki，Minecraft一天持续20分钟，相当于24k刻。

这可以用于酷狼人/黑暗法师被动技能，它只在夜间触发！

```
example_condition:
    type: time
    period: NIGHT
```

---

原文：[Miscellaneous](https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/misc) · 原文归档：2026-10-19
