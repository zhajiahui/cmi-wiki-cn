---
title: 掉落表
source: https://docs.phoenixdevt.fr/mmoitems/items/drop-tables
source_snapshot: '2026-10-19'
---

# 掉落表 {#👛-drop-tables}

数据存储在`drops.yml`配置文件中，位于主插件文件夹中。这是一个配置片段：

```yml
monsters:
  ZOMBIE:
    rock-table:
      coef: 7
      items:
        CONSUMABLE:
          ROCK: 50,1-3,10
    coin-table:
      coef: 1
      items:
        MISCELLANEOUS:
          GOLD_COIN: 1,1-10,0
```

删除表被分成**子表**。当读取删除表时，会在所有子表中选择一个随机子表，然后删除该子表中的物品。拥有多个子表可以让你实际上阻止两个物品同时生成。

举例来说，你希望僵尸掉落一把定制铁剑或定制皮革胸甲。由于有机会同时掉落两个物品太过强大，因此你可以将僵尸掉落表分成两个子表。在第一个子表中，你将拥有铁剑，在第二个子表中，你将拥有铁胸甲。这样，这两个物品就不能同时生成。

子表可以有不同的子表系数。系数越高，子表被选中的机会就越大。计算子表被选择的机会非常简单。如果在删除表内，第一个子表的系数为1，第二个子表的系数为2，则第一个子表的被选择机会为1和3。因此，可以使用以下公式计算子表被选择的机会。

```
chance = <subtable-coefficient> / <sum-of-all-subtable-coefficients>
```

怪物部分对应于实体死亡时掉落的物品。这是配置模板：

```yml
MOB_NAME:
first-subtable:
    coef: <subtable-coefficient>
    items:
      ITEM_TYPE: (not case sensitive):
        ITEM_ID: (drop-chance),(min)-(max),(unidentified-chance)
      ITEM_TYPE:
        ITEM_ID: (drop-chance),(min)-(max),(unidentified-chance)
        #...
      #...
  second-subtable:
    coef: <subtable-coefficient>
    items:
      ITEM_TYPE: (not case sensitive):
          ITEM_ID: (drop-chance),(min)-(max),(unidentified-chance)
          #...
      #...
  #...
```

*blocks* 配置节用于设置玩家破坏或挖掘方块时掉落的物品。格式与 monsters 配置节相同，只需将生物名称换成方块类型名称。方块类型可在 [Spigot Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html) 中查询。

**你可以为每个子表物品配置三个值：**

- **drop-chance** -物品掉落的几率。
- **最小和最大** - 滴的数量在这两个值之间随机选择。
- **unidentified-chance** - 你的物品掉落时有可能无法识别。

**附加子表选项：**

- **disable-silk-touch** - 当设置为true时，如果该块是用丝触镐开采的，这将防止子表掉落任何物品。这可以防止物品与矿石等方块发生重复故障。

```yml
blocks:
  DIAMOND_ORE:
    rare-diamond:
      coef: 1
      disable-silk-touch: true
      items:
        MATERIAL:
          RARE_DIAMOND: 100,2-3,0
```

## 将 mmoitem 添加到MythicMobs删除表 {#adding-mmoitems-to-mythicmobs-drop-tables}

将MMOItems添加到 MM 删除表非常简单。由于4.5，使用 MI 创建的物品可以使用以下格式在 MM 掉落表中调用：

```yml
TestDropTable:
  Conditions:
  - playerwithin 100
  Drops:
  - mmoitems{type=SWORD;id=CUTLASS} 1 .1
```

这告诉掉落表添加MMOItems中名为`CUTLASS`的剑，掉落几率为10%（因此 MM 掉落表中为0.1）。你可以更改你想要掉落的物品的数量，就好像该掉落物是原版掉落物一样。如果你希望物品在掉落时无法识别，则必须在括号内添加一个选项：这意味着物品在掉落时有30%的机会无法识别

```yml
TestDropTable:
  Drops:
  - mmoitems{type=SWORD;id=CUTLASS;unidentified=0.3} 1 .1
```

注意：`type`和`id`值都必须是大写。

缺点是你无法像MMOItems子表那样一次直接掉落一个物品。

---

原文：[👛 Drop Tables](https://docs.phoenixdevt.fr/mmoitems/items/drop-tables) · 原文归档：2026-10-19
