---
title: 钓鱼
source: https://docs.phoenixdevt.fr/mmocore/profession/fishing
source_snapshot: '2026-10-19'
---

# 钓鱼 {#🎣-fishing}

MMOCore可用于覆盖/重写默认钓鱼掉落表。

## 钓鱼体验 {#fishing-experience}

使用`fishitem`【经验源](../level/sources.md)】，可以让玩家在钓鱼特定的物品时获得一定的经验值，比如鱼、魔法书、马鞍等。物品越稀有，玩家应该获得的经验越多。

目前，`fishitem`经验源仅支持物品材料，这意味着玩家不会通过从 Power I 附魔书上抢夺修复附魔书来获得额外的经验。将特定经验金额绑定到金额的唯一方法是使用可在fishing.yml副职业配置文件中编辑的钓鱼掉落表挂钩到MMOItems物品。

**如果你不想一般使用副职业**，只需忽略钓鱼经验源并使用钓鱼掉落表而不指定任何经验。 **如果你不想使用MMOCore钓鱼掉落表**，只需使用钓鱼经验源，并删除任何默认的钓鱼掉落表。

## 配置 {#configuration}

主配置文件是`professions/fishing.yml`。

```yml
name: Fishing
experience:
    base: 20
    per-level: 3

exp-sources: {}

# Fishing drop tables which override MC default.
# When fishing, the plugin reads through all the drop tables
# and picks THE first one which all conditions are met!!
# You must put at first place the drop tables which
# have the most conditions/which are the most important.
# Number of tugs = number of times you need to click to fish.
on-fish:
    overriding-drop-table:
        conditions:
        - 'region{name="swamp,second-region"}'
        - 'biome{name=beach}'
        
        # When drop table is read, one of these
        # items will be selected randomly.
        items:
        
        # Tugs needed: 4 to 5
        # Fishing EXP earned: 1 to 6
        - 'mmoitem{type=CONSUMABLE;id=SUSHI_ROLL;tugs=30-40;experience=1-6} 1 1-1 9'
        
        # Tugs needed: 10 to 20
        # Fishing EXP earned: 20 to 30
        - 'mmoitem{type=GEM_STONE;id=SPITEFUL_OPAQUE_DIAMOND;tugs=10-15;experience=20-30} 1 1-1 1'

    # Default drop table which always apply.
    # When removing every drop table, the vanilla
    # fishing mechanism is back.
    default:
        items:
        - 'vanilla{type=SALMON;tugs=4-5;experience=1-6} 1 2-5 1'
```

*如你所见，默认的钓鱼配置设置不使用钓鱼经验源，尽管你可以根据需要将其他经验源添加到该副职业中。*钓鱼掉落表由两个选项定义：条件和物品。

当玩家钓鱼时，MMOCore会遍历所有钓鱼掉落表，并选择第一个玩家都满足条件的钓鱼掉落表。目前可用的两个条件是`region`条件，它挂接到WorldGuard上。此条件允许你为每个WorldGuard区域配置特定的删除表。这可以让你创建可以钓鱼稀有物品的特定区域。你可以并行使用[航点](../features/waypoints.md)系统，创建一个独特的钓鱼区，并获得稀有掉落！另一个条件是`biome`条件，它读取你所在的生物群落。生物群落必须以`name=<biome>`格式格式化才能运行 - 请参阅上面的示例。

如果你创建一个没有条件的删除表，请确保它是最后一个，否则它将始终被MMOCore选择。此外，创建no-condition钓鱼掉落表意味着MMOCore钓鱼掉落表**始终**覆盖默认的原版掉落表。

## 钓鱼台 {#fishing-drop-tables}

先了解一下【常规掉落表](../features/drop-tables.md)。

钓鱼掉落表与常规掉落表（用于随机箱子或方块掉落）略有不同。主要区别在于钓鱼掉落表总是需要一个且仅一个物品来随机挑选和掉落。

这改变了MMOCore选择一个随机物品的方式。事实上，`chance`选项从未被钓鱼台使用过。即使你将掉落物品的机会设置为0%，你的物品也可能会被选中。

钓鱼掉落表**使用物品重量来确定掉落几率**。每个表物品都分配有一个权重，它是一个数字。这个数字越高，掉落的几率就越高。物品被拾取和掉落的概率为`<item weight> / <sum of item weights from all the items in that drop table>`。

删除物品的通用格式如下（与常规删除表物品相同）。如上所述，`<drop-chance>`选项完全无用，可以设置为任何值。

```
droptype{<parameter1>=<value1>;<parameter2>=<value2>} <drop-chance> <min-max> <weight>
```

这种重量系统有一些优点。首先，如果你想将新的物品添加到钓鱼掉落表中，你实际上不必编辑所有先前配置的掉落机会。只需添加一些具有特定权重的新表物品，并且由于掉落机会的计算方式，这将具有“更新所有其他物品掉落机会”的效果。第二个优点是它确实适合一次只掉落一个物品的钓鱼台。

### 拖船 {#tugs}

MMOCore通过添加 **拖船** 改进了默认的捕鱼机制。当玩家钓到鱼时，鱼会试图反抗，因此玩家必须spam-click他的鱼竿直到它放弃！拖船决定了捕获鱼所需的点击次数。如果玩家在鱼抵抗时停止点击，鱼最终会消失。

要设置捕获特定物品所需的拖船数量，请将`;tugs=min-max`添加到物品线路配置中。如果你希望拖船编号始终相同，你也可以使用`;tugs=10`。

### 经验 {#experience}

要让物品在钓鱼时为玩家提供特定数量的 exp，请将`experience=min-max`添加到物品线路配置中。每次物品被玩家捕获时，两个给定边界之间任意位置的随机 exp 量都会滚动。如果你希望经验金额为常量，你也可以使用`experience=30`。

### 原版经验 {#vanilla-experience}

你还可以通过将`vanilla-exp=min-max`添加到物品线路配置来在钓鱼时提供原版exp。该字段是可选的，其工作方式与`experience`完全相同。

---

原文：[🎣 Fishing](https://docs.phoenixdevt.fr/mmocore/profession/fishing) · 原文归档：2026-10-19
