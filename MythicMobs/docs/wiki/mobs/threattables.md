---
title: 仇恨表
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ThreatTables
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 仇恨表 {#threat-tables}

仇恨表改变生物追踪目标的方式。原版 Minecraft 生物没有严格的目标选择系统，经常转而攻击刚刚伤害它们的对象。仇恨表改变了这种行为。

启用后，生物会记录各玩家造成的伤害，攻击伤害最高的玩家。这样可避免一名玩家打一下就跑，其他玩家却能一直跟在后面无伤攻击的情况。

仇恨表内置常见 MMORPGs 仇恨规则，让生物更合理地选择目标。玩家造成伤害会获得仇恨值；风筝 Boss、超出 MaxCombatRange，或长时间不在视线内都会降低仇恨值。离开世界或退出服务器也会清除仇恨值。

只有其他玩家的仇恨值达到当前目标的 `110%`，生物才会切换目标。

> 请注意，激活仇恨表将稍微改变你为生物指定的[AI目标选择器](custom-ai.md#ai-target-selectors)。具有激活仇恨表的生物将尝试攻击任何对其造成伤害的实体 - 即使此类实体未在AI目标选择器中列出，或者即使该生物的AI目标选择器列表已被清除并且该生物自然不会攻击任何东西或任何人。

## 启用仇恨表 {#enabling-threat-tables}

为生物启用仇恨表很简单，只需在生物配置中添加 `Modules.ThreatTable: true`，如下所示：

```yaml
BigScaryBoss:
  Type: zombie
  Display: '&6Zombie'
  Health: 20000
  Modules:
    ThreatTable: true
```

也可以在[生物选项](options.md#usethreattable)中启用仇恨表

就是这样！

## 调整仇恨值 {#manipulating-threat-levels}

启用仇恨表后，生物始终以其仇恨表中仇恨值最高的实体为目标。此过程完全自动进行，依据各实体对生物造成的伤害量计算。因此，造成伤害最多的实体（通常是玩家）会获得最高的仇恨值，并成为生物的目标。

如果想手动让生物选中特定实体，或调整它的选取目标行为，可以使用[仇恨机制](../skills/mechanics/threat.md)。

仇恨表也提供 API，包括“嘲讽”和修改仇恨值的方法，供其他插件作者编写能与仇恨值交互的技能或能力。
