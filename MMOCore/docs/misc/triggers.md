---
title: 触发器
source: https://docs.phoenixdevt.fr/mmocore/misc/triggers
source_snapshot: '2026-10-19'
---

# 触发器 {#🔧-triggers}

> **警告**
>
> 此功能将在不久的将来与MythicLib[脚本机制](../../mythiclib/scripts/mechanics/intro.md)合并（此更新将向后兼容）。该页面将被删除并移至MythicLibwiki。

**这是一个非常技术性的功能，通过单独阅读此页面（断章取义），你不会学到任何东西。仅当其他 wiki 页面将你重定向到此页面时才应阅读。**

MMOCore使用触发器在满足某些条件时执行操作。它们用于任务和副职业，并且每个都有一组可以“触发”它们的动作或目标。

### 触发表（自1.9.5起） {#trigger-tables-since-1-9-5}

从1.9.5开始，你可以在`triggers.yml`中定义触发器表。你可以使用每个触发器列表的 id 来引用它，这将触发所有相应的触发器。

```
#Example
test-trigger:
 - 'command{format="broadcast Triggered!"}'
 #Will fire the 2 commands in test-trigger-2
 - 'from{source="test-trigger-2"}'


test-trigger-2:
 - 'command{format="mmocore admin skill-points give %player_name% 1"}'
 - 'command{format="mmocore admin atr-realloc-points give %player_name% 3"}'
```

## 可用的触发器类型 {#available-trigger-types}

|触发|描述 |格式/示例 |
| --- | --- | --- |
| stat | 为玩家提供永久的属性。 FLAT 类型只是将金额添加到属性中。相对使得属性有%的提升。 | `stat{stat=<STAT_NAME>;amount=<amount>;type=FLAT/RELATIVE}` |
| skill_buff | 通过改变某个修饰符的值（冷却时间，伤害，魔力...），为所有匹配公式的技能提供永久的增益效果。有关技能增益效果的更多信息 [此处](../skills/intro.md#skill-buffs)。 | `skill_buff{formula="<FORMULA>";modifier=<MODIFIER>;amount=<amount>;type=FLAT/RELATIVE}` |
| unlock_skill | 为玩家解锁技能。有关技能解锁的更多信息 [此处](../skills/unlocking.md)。 | `unlock_skill{skill=FIREBALL}` |
| unlock_slot | 为玩家解锁特定的[技能插槽](../skills/binding.md#skill-slots)。 | `unlock_slot{slot="<SLOT>"}` |
| bind_skill | 将技能绑定到特定插槽。 | `bind_skill{skill=FIREBALL;slot=10}` |
| levelup_skill | 提高玩家的技能等级。 | `levelup_skill{skill=<NAME>;amount=1}` |
| message | 向玩家发送消息。 | `message{format="&aYour message here... "}` |
| command | 使控制台执行命令。 | `command{format="tellraw @a {"text":"Hello!"}"}` |
| experience | 在副职业中给出经验。 | `exp{profession=<PROFESSION>;amount=<AMOUNT>}` |
| experience | 给出主职业经验。 | `exp{amount=<AMOUNT>}` |
| sound | 向玩家广播声音。 | `sound{sound=<SOUND_NAME>;volume=<VOLUME>;pitch=<PITCH>}` |
| item | 将物品赋予玩家。 | `item{type=DIAMOND;amount=3}` |
| mmoitem | 向玩家提供 mmoitem 。 | `mmoitem{type=SWORD;id=FALCON_BLADE;amount=2}` |
| mana | 给予/获取/设置玩家魔力。 | `mana{operation=<GIVE/SET/TAKE>;amount=2-3}` |
| stamina | 给予/获取/设置玩家耐力。 | `stamina{operation=<GIVE/SET/TAKE>;amount=2-3}` |
| stellium | 给予/获取/设置玩家群星。 | `stellium{operation=<GIVE/SET/TAKE>;amount=2-3}` |
| mmskill | 铸了MythicMobs技能。 | `mmskill{id=MythicMobsSkillInternalName}` |
| money | 给予/获取/设置玩家余额。 | `money{operation=<GIVE/SET/TAKE>;amount=2-3}` |

大多数这些类型和触发器都显示在默认配置中，以及如何正确使用它们。消息和命令触发器支持 [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/)中的占位符。

---

原文：[🔧 Triggers](https://docs.phoenixdevt.fr/mmocore/misc/triggers) · 原文归档：2026-10-19
