---
title: MMOItems
source: https://docs.phoenixdevt.fr/mmocore/compatibility/mmoitems
source_snapshot: '2026-10-19'
---

# MMOItems {#🏹-mmoitems}

MMOCore构建为与MMOItems([Polymart](https://polymart.org/product/3413/mmoitems)/ [Spigot](https://www.spigotmc.org/resources/mmoitems-premium.39267)) 一起使用，尽管它不是依赖项。MMOCore为MMOItems提供了很多兼容性选项，这里是详细列表。

### 额外MMOItems属性 {#extra-mmoitems-stats}

当同时使用MMOCore和MMOItems时，额外的物品属性将自动启用，并将添加到MMOItems物品版本GUI中。

|属性|描述 |
| --- | --- |
| 最大魔力 | 默认属性，但它确实支持MMOCore |
| 最大耐力 | 额外提供MMOCore耐力。 |
| 最大星群 | 提供额外的MMOCore群星。 |
| 资源* 再生 | 增加固定资源*再生。 |
| 最大资源* 再生 | 每秒重新生成最大资源* 的 %。 |
| 额外经验 | 增加获得的经验值。 |
| 技能冷却时间还原 | 默认属性，但它确实支持MMOCore |

*资源代表生命值、魔力、耐力或 stellium。

### 任务目标和触发因素 {#quest-objectives-triggers}

MMOItems在MMOCore任务中添加了新任务 [目标](../features/quests.md)，其中玩家必须获得物品并将其交给特定的公民 NPC。你还可以设置任务[触发](../features/quests.md)，当完成特定任务目标时会给出 MMOItem。

### MMOCore掉落表 {#mmocore-drop-tables}

你可以将物品从 MI 添加到MMOCore[删除表](../features/drop-tables.md)。

### 物品限制，魔力 {#item-restrictions-mana}

MMOItems 的物品等级限制和职业限制**都支持** MMOCore。MMOItems 的技能和魔杖类武器还可以消耗魔力或耐力/stellium，这些资源也受 MMOCore 支持。

### MMOItemsCrafting 的额外功能 {#extra-features-for-mmoitems-crafting}

在MMOItems中，一些配方具有特定条件，玩家必须满足这些条件才能使用合成配方。MMOCore添加了副职业等级制作限制i.e玩家在某些副职业中必须至少达到 Lvl X，例如锻造或采矿，才能使用配方。有关MMOItems配方条件的更多信息 [在MMOItemswiki](../../mmoitems/stations/conditions.md)中。

**配方示例**，其中 *Smithing* 中的玩家必须至少达到 Lvl5。

```
    steel-sword:
        output:
            type: SWORD
            id: STEEL_SWORD
        conditions:
        - 'profession{profession=smithing,level=5}'
        ingredients:
        - 'vanilla{type=STICK,amount=2}'
        - 'mmoitem{type=MATERIAL,id=STEEL_INGOT,amount=4}'
```

MMOCore还添加了一种新型的制作触发器（使用配方时执行的操作），可用于将经验赋予玩家（主要经验或特定副职业中的经验）。有关MMOItems配方触发器的更多信息 [在MMOItemswiki](../../mmoitems/stations/triggers.md)中。

**相同的示例**，使用时授予10Smithing EXP

```
    steel-sword:
        output:
            type: SWORD
            id: STEEL_SWORD
        ...
        triggers:
        - 'exp{profession=smithing,amount=10}'
```

---

原文：[🏹 MMOItems](https://docs.phoenixdevt.fr/mmocore/compatibility/mmoitems) · 原文归档：2026-10-19
