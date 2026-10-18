---
title: 获取物品
source: https://docs.phoenixdevt.fr/mmoitems/items/obtain-item
source_snapshot: '2026-10-19'
---

# 获取物品 {#🎒-obtain-items}

> **提示**
>
> 请务必先阅读[本页](templates.md)。MMOItems物品生成系统相当复杂，需要一些时间才能完全理解。

## 使用`/mi generate` {#using-mi-generate}

`/mi generate`允许你根据作为命令参数提供的特定条件生成随机物品。命令格式如下：

```cmd
/mi generate <player> (extra-args)
```

`<player>`表示你将向其提供物品的玩家，以及将构建物品的RPG玩家数据。例如，如果运行命令的玩家等级为20，并且命令目标为等级10，则物品不会在等级20上缩放，而是在等级10上缩放。

下面列出了可用的可选命令参数：

|论证|使用 |
| --- | --- |
| `-matchlevel` | 物品等级将与目标玩家等级匹配。 |
| `-matchclass` | 目标玩家保证物品可用（职业要求）。 |
| `-gimme` | 将物品添加到你的物品栏中。 |
| `-class:<class-name>` | 物品保证可由给定的职业使用。 |
| `-level:<integer>` | 物品保证具有 X 级。 |
| `-tier:<tier-name>` | 物品保证已指定 [tier](../features/tiers.md)。 |
| `-type:<item-type>` | 选择[物品类型](../features/types.md)。 |
| `-id:<id>` | 如果你想要选择特定的 [物品模板](templates.md)，请使用该选项。 |

请记住，这些参数都是可选的（这就是物品gen 如此强大的原因），并且当MMOItems确定它将使用什么物品模板、层和物品等级时，它们充当“过滤器”。使用示例：我们为玩家提供与其等级和职业匹配的高级武器：

```cmd
/mi generate <player-level> -matchlevel -matchclass -tier:rare
```

例如，这通常在打开可掠夺的箱子时使用；它不是像完成临时圣诞节/万圣节活动或杀死老板/特殊怪物时那样的特定战利品，而是稀有、随机但可用的东西（所以他不会感到沮丧）。

如果你要向特殊怪物添加战利品，你很可能会指定你想要掠夺的物品并且不给出任何等级，因此玩家需要磨灭生物以最终找到同一武器的更高等级版本。

## 使用MythicMobs删除表 {#using-mythicmobs-drop-tables}

更多信息请参见官方[MythicMobswiki](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/drops/Drops)。

## 使用MMOCore删除表 {#using-mmocore-drop-tables}

如果你想要将特定的物品生成器模板添加到MMOCore删除表之一，请使用此MMOCore表物品。

```
gentemplate{id=TEMPLATE_ID;tier=TIER_NAME;level=<int>;match-level=<true/false>} <chance> <min-max>
```

| 论证 | 使用 |
| --- | --- |
| `id=TEMPLATE_ID` | 选择你正在使用的物品gen 模板。 |
| `level=<item-level>` | 强制物品等级在 Y 等级附近。 |
| `tier=ITEM_TIER_ID` | 强制物品为 X 层。 |
| `match-level=<true/false>` | 物品等级将与玩家等级匹配。 |

如果你不想使用特定的生成模板，而是根据特定标准从所有注册模板中随机选择一个，请使用此MMOCore表物品。所有先前的参数（`id`除外）也可以用于该格式。

```
miloot{type=ITEM_TYPE_ID;class=PLAYER_CLASS;match-class=<true/false>;tier=TIER_NAME;level=<int>;match-level=<true/false>} <chance> <min-max>
```

| 论证 | 使用 |
| --- | --- |
| `type=ITEM_TYPE_ID` | 强制物品为特定类型。 |
| `class="Class Name"` | 物品保证可由某个职业使用。 |
| `match-class=<true/false>` | 玩家保证满足物品职业要求。 |

## 使用MMOItems删除表 {#using-mmoitems-drop-tables}

请阅读[此维基页面](drop-tables.md)。

---

原文：[🎒 Obtain Items](https://docs.phoenixdevt.fr/mmoitems/items/obtain-item) · 原文归档：2026-10-19
