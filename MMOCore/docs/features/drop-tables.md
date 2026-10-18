---
title: 掉落表
source: https://docs.phoenixdevt.fr/mmocore/features/drop-tables
source_snapshot: '2026-10-19'
---

# 掉落表 {#💰-drop-tables}

`/drop-tables`文件夹是你为 [方块](mining.md)和 [战利品箱](loot-chests.md)] 设置所有自定义掉落表的位置。由于它们的用途不仅限于块掉落，因此我们决定为它们提供一个单独的文件夹，以便你可以在那里设置它们，并且仅在其他配置中使用它们的引用，以使它们更轻/更易于阅读和设置。

删除表可用于删除原版物品、 mmoitems 或另一个MMOCore删除表的内容。你可以将删除表封装在其他删除表内以创建复杂的删除表。

## 默认配置 {#default-config}

```yml
# You may create as many drop tables as you want. You can also
# make drop tables refer to other drop tables.
#
# DON'T try to create recursive drop tables (drop tables which
# call themselves to multiply items dropped). It will work, but
# if you put a probability of 1 it will crash your server
# instantly. The more the probability, the higher your chance
# to slow down your server performances. Fun fact though :p

diamond-drop-table:
    items:
    - 'vanilla{type=DIAMOND} 1 1-3'
    - 'mmoitem{type=material;id=RARE_DIAMOND} .1 1-3'
    - 'droptable{id=other-drop-table} .1'

other-drop-table:
    items:
    - 'vanilla{type=STONE} 1 1-3'
```

这个默认文件是非常不言自明的。第一个删除表示例展示了你可以在任何删除表内使用的所有删除物品。要创建删除表，只需向`/drop-tables`文件夹中的任何文件添加一个新部分即可。然后为你的drop表找到一个ID（这个标识符必须是唯一的，稍后将用作参考）。

`diamond-drop-table`示例是[采矿副职业](mining.md)]开采钻石矿石时使用的掉落表。它可能掉落的物品是原版钻石，是MMOItems中的稀有钻石，表中的所有内容称为`other-drop-table`（一块石块）。

物品后面的数字表示机会，然后是金额（可以是整数范围）。每滴物品的格式如下：

```
droptype{<parameter1>=<value1>;<parameter2>=<value2>} <drop-chance> <min-max> <weight>
```

你不必指定最后三个参数中的任何一个（掉落机会/数量/重量），尽管你需要指定，例如，如果你想利用权重系统（在页面底部解释），则需要指定掉落机会。

## 可用的掉落类型 {#available-drop-types}

|掉落物品|格式|
| --- | --- |
| 另一个掉落表 | `droptable{id=drop-table-id} <chance> <amount>` |
| 原版物品 | `vanilla{type=ITEM_MATERIAL} <chance> <amount>` |
| 金币 | `gold{} <chance> <amount>` |
| 注意 | `note{min=MIN_WORTH;max=MAX_WORTH} <chance> <amount>` |
| mmoitem | `mmoitem{type=MMOITEM_TYPE;id=MMOITEM_ID} <chance> <min-max>` |
| gentemplate | `gentemplate{id=TEMPLATE_ID;tier=TIER_NAME;level=<int>;match-level=<true/false>} <chance> <min-max>` |
| miloot | `miloot{type=ITEM_TYPE_ID;class="Class Name";match-class=<true/false>;tier=TIER_ID;level=<int>;match-level=<true/false>} <chance> <min-max>` |

`mmoitem`、`gentemplate`和`miloot`仅在使用MMOItems时可用。对于`gentemplate`和`miloot`掉落表物品，请参考 [此MMOItemswiki 页面](../../mmoitems/items/obtain-item.md)。

## 工作台容量，物品重量 {#table-capacity-items-weights}

物品权重和掉落表容量用于处理同一掉落表中两件稀有物品同时掉落的情况。通过物品权重，可以设定每项掉落相对于其他项的“重量”，限制单个玩家运气极好、一次从 Boss 身上获得所有稀有物品的极端情况。

```yml
weighted-drop-table:
    items:
    - 'vanilla{type=DIAMOND} .33 1-3 1'
    - 'vanilla{type=EMERALD} .5 1-3 1'
    - 'vanilla{type=GOLD_INGOT} 1 1-3 1'
```

示例场景：你希望仅掉落这三个物品之一，并且每个物品都有1/3机会被选择。

每个掉落物物品的物品权重为1，这意味着如果该掉落表由容量为1的战利品箱（或支持MMOCore掉落表的任何其他系统）使用，则只会选择一个物品。

**当调用掉落表来生成随机战利品时，所有选定掉落物品权重的总和不能超过给定的容量。** 相同的掉落表可以用于不同的容量（出于实际原因）。如果你使用上面设置的删除表，容量为3，则可以同时删除三个物品。如果你以2的容量使用它，则最多会生成2物品。

请记住，你可以对物品权重使用任何值。你还可以在同一个掉落表中拥有物品和0重量以及加权物品（事实上，这是你可能会用来设置稀有 Boss 掉落的设置）。

当调用删除表时，将按照配置设置给出的顺序读取删除物品。在设置物品掉落机会时必须牢记这一点，因为这就是为什么靠近末端的物品被挑选的机会更高。最后一个物品的概率始终为1，因为如果之前的所有物品掷骰都失败，则保证会选中它。

### 在哪里配置战利品表容量 {#where-to-configure-the-loot-table-capacity}

如果你在战利品箱内使用掉落表，请参阅[本页](loot-chests.md#loot-chest-tiers)来配置战利品箱的战利品表容量。

否则，你可以使用`capacity`选项指定任何战利品表的默认容量：

```yml
some-drop-table:
    capacity: 2
    items:
    - 'vanilla{type=DIAMOND} .33 1-3 1'
    - 'vanilla{type=EMERALD} .5 1-3 1'
    - 'vanilla{type=GOLD_INGOT} 1 1-3 1'
```

如果绝对没有指定容量，MMOCore将使用默认容量100。

## 删除表条件 {#drop-table-conditions}

使用以下语法将条件添加到删除表中。了解有关条件系统的更多信息 [此处](../misc/conditions.md)。

```yml
diamond-drop-table:
    items:
    - 'vanilla{type=DIAMOND} 1 1-3'
    - 'mmoitem{type=material;id=RARE_DIAMOND} .1 1-3'
    - 'droptable{id=other-drop-table} .1'
    conditions:
    - 'level{profession=mining;amount=10}'
    - ...
```

## 额外选项 {#extra-options}

切换`shuffle`选项将打乱物品在掉落表中被掠夺的顺序。这可以用来轻松增加删除表的随机性。

```yml
some-drop-table:
    shuffle: true
    items:
    - 'vanilla{type=DIAMOND} 1 1-3'
    - 'mmoitem{type=material;id=RARE_DIAMOND} .1 1-3'
```

---

原文：[💰 Drop Tables](https://docs.phoenixdevt.fr/mmocore/features/drop-tables) · 原文归档：2026-10-19
