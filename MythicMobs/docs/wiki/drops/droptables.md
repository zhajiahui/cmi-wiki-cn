---
title: 掉落表
source_url: https://wiki.mythiccraft.io/mythicmobs/drops/DropTables
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 掉落表 {#drop-tables}

掉落表是多个掉落项的集合，可以分配给生物。生物需要掉落多种物品时，使用掉落表通常更方便整理。

掉落表保存在 /MythicMobs/DropTables 下各自独立的配置文件中。它支持[条件](../skills/conditions.md)和多种特殊选项，也可由多个生物共用，无须重复定义。

可以在 DropTables 文件夹中创建任意数量的文件，名称任意，只要以 `.yml` 结尾即可。

掉落表可以嵌套，一个掉落表可以包含多个其他掉落表。

```yaml
internal_mobname:
  Type: <mobtype>
  Drops:
  - <internal_droptablename>
```

完整配置的掉落表结构如下：

```yaml
#Lets you specify exactly how many items will drop from this table
internal_droptablename: 
  TotalItems: <amount>
  MinItems: <amount> #defaults to TotalItems' value
  MaxItems: <amount> #defaults to TotalItems' value
  BonusLuckItems: <multiplier>
  BonusLevelItems: <multiplier>
  BiasStat: <stat>
#Conditions of the dropper
  Conditions:
  - condition 1
  - condition 2
  - ...
#Conditions of the person that triggered the drop (i.e. the killer of the mob)
  TriggerConditions:
  - condition 1
  - ...
  Drops:
  - <item/exp/droptable> <amount> <chance>
  - ...
```

## DropTable 选项 {#droptable-options}

> 下文中的“掉落项”指一行掉落配置，而不是该行实际生成的物品数量。例如，`bone 5` 虽然生成 5 个骨头，但仍算作一个掉落项，因为它由一行掉落配置生成

**TotalItems: [number]**

- 精确规定掉落表生成多少个掉落项
- 设置此项后，物品概率会按权重计算

**MaxItems: [number]**

- 规定最多生成多少个掉落项
- 如果只设置此项，会依次检查掉落列表，直到达到最大物品数量

**MinItems: [number]**

- 规定最少生成多少个掉落项
- 如果只设置此项，会依次检查掉落列表，直到达到最小物品数量
- **同时**启用 `MinItems` 和 `MaxItems` 时，掉落表各条目的概率会改为*权重*。

**BonusLevelItems: [number]/[range]**

- 根据生物等级修正生成的掉落项数量
- 可设置为范围，例如 `0.2to0.5`
- 计算方式：`amount = amount + (mob_level * bonus_level_items)`
- 需要在掉落表中设置 `TotalItems`、`MinItems` 或 `MaxItems`

**BonusLuckItems: [number]/[range]**

- 根据击杀者的幸运属性修正生成的掉落项数量
- 可设置为范围，例如 `0.15to8`
- 适用于 Luck 属性、影响幸运的附魔和诅咒，以及幸运药水效果
- 计算方式：`amount = amount + (luck * bonus_luck_items)`
- 需要在掉落表中设置 `TotalItems`、`MinItems` 或 `MaxItems`

**BiasStat: [Stat]**

- 用于此物品战利品偏向计算的[属性](../stats.md)
- 战利品偏向可以提高权重掉落表中稀有掉落的概率
- 设为 0 时没有变化，设为 100 时稀有掉落的概率大约翻倍
- 默认使用 `LOOT_BIAS` 属性

### 示例 {#examples}

这个生物总会掉落大量经验和一些腐肉，同时也使用了下文介绍的掉落表。

```yaml
snow_loving_zombie:
  Type: zombie
  Health: 100
  Equipment:
  - snowsword HAND
  Drops:
  - exp 75-125 1
  - rare_snowsword_droptable
```

这个示例掉落表有 5 % 的概率掉落一把自定义剑，但前提是生物在 "ICE_PLAINS" 生物群系中被击杀，且有玩家位于 20 格范围内。

```yaml
rare_snowsword_droptable:
  Conditions:
  - biome{b=ICE_PLAINS}
  - playerwithin{d=20}
  Drops:
  - snowsword 1 0.05
```

在这个示例中，如果玩家没有幸运效果，掉落表会掉落 5 个金粒/钻石；如果玩家具有幸运 V 效果，则会掉落 15-27 个金粒/钻石。

```yaml
LuckyDroptable:
  TotalItems: 5
  BonusLuckItems: 2to5
  Drops:
  - GOLD_NUGGET 1 1
  - DIAMOND 1 0.2
```

## 装备掉落表 {#equipment-droptables}

也可以使用掉落表配置装备搭配。这类掉落表既可以直接用于生物的 [Equipment 元素](../mobs/mobs.md#equipment)，也可以通过 [Equip 机制](../skills/mechanics/equip.md)使用。语法与“普通”掉落表相似，但这里必须指定装备槽位。

### 示例 {#examples-2}

```yaml
# Droptable Config
Example_EquipmentDropTable:
  Drops:
  - LEATHER_HELMET HELMET 1 1
  - LEATHER_CHESTPLATE CHEST 1 1
  - CHAINMAIL_CHESTPLATE CHEST 1 0.5
  - DIAMOND_CHESTPLATE CHEST 1 0.1
  - NETHERITE_CHESTPLATE CHEST 1 0.05
```

```yaml
# Mob Config
ExampleMob:
  Type: ZOMBIE
  Equipment:
  - Example_EquipmentDropTable
```

这些配置会让 `ExampleMob`：

- 始终佩戴皮革头盔。
- 始终至少穿着皮革胸甲，并在满足概率时换上更强的装备。
