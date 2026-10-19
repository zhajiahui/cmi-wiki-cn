---
title: "战利品"
source_url: "https://wiki.itemsadder.com/adding-content/loots"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 战利品

战利品可以用来指定何时掉落特定物品。

你可以决定创建不同类型的战利品：

* 方块
* 生物
* 钓鱼

例如，以下是本例创建的 `.yml` 文件中的战利品分类。

```yaml
info:
  namespace: my_loots
loots:
  blocks:
    ruby_ore:
      type: iasurvival:ruby_ore
      items:
        ruby:
          item: iasurvival:ruby
          min_amount: 1
          max_amount: 2
          chance: 100
    nether_quartz_ore:
      type: NETHER_QUARTZ_ORE
      drop_only_first: true
      items:
        crystal:
          item: iasurvival:crystal
          min_amount: 1
          max_amount: 2
          chance: 10
        knowledge_fragment:
          item: iasurvival:knowledge_fragment
          min_amount: 1
          max_amount: 2
          chance: 15
```

实例中在**方块**目录含有两个战利品。

第一项名为 `ruby_ore`（名称可自行决定）。破坏类型为 `iasurvival:ruby_ore` 的自定义**方块**时，以 **100% 概率**掉落 `itemsadder:ruby`，**最少数量为 1**、**最多数量为 2**。

第二项为原版**方块**的战利品。玩家破坏 `NETHER_QUARTZ_ORE` 时，会掉落 `crystal` 或 `knowledge_fragment`。\
这些**掉落物**由 **ItemsAdder** 依据你设定的**几率**决定。

## 战利品类型

### 钓鱼

```yaml
loots:
  fishing:
    loot_blue_parrotfish:
      biomes:
        - WARM_OCEAN
      items:
        item_1:
          item: iasurvival:blue_parrotfish
          min_amount: 1
          max_amount: 1
          chance: 5
    loot_green_sunfish:
      items:
        item_1:
          item: iasurvival:green_sunfish
          min_amount: 1
          max_amount: 1
          chance: 5
    loot_goldfish:
      items:
        item_1:
          item: iasurvival:goldfish
          min_amount: 1
          max_amount: 1
          chance: 5
```

### 怪物

```yaml
loots:
  mobs:
    villager:
      type: ZOMBIE
      items:
        item_1:
          item: iawearables:straw_hat
          min_amount: 1
          max_amount: 1
          chance: 100
    ender_dragon:
      type: ENDER_DRAGON
      items:
        item_1:
          item: iawearables:ender_dragon_wings
          min_amount: 1
          max_amount: 1
          chance: 100
```

### **自定义实体战利品**

要让 ItemsAdder 在击杀自定义实体时掉落物品，只需将 `type` 设为该实体带命名空间的 ID。

```yaml
loots:
  mobs:
    soul:
      type: custom:ninja_skeleton
      items:
        ruby:
          item: ruby
          min_amount: 1
          max_amount: 1
          chance: 100
```

## **战利品规则**

### （方块）`drop_only_first`

此特殊属性会在首件物品成功掉落后，停止计算其他掉落概率。\
<mark style="color:orange;">**警告**</mark><mark style="color:orange;">：这会使物品</mark> <mark style="color:orange;">**更难**</mark> <mark style="color:orange;">被</mark> <mark style="color:orange;">**掉落**</mark><mark style="color:orange;">。</mark>

```yaml
loots:
  blocks:
    nether_quartz_ore:
      type: NETHER_QUARTZ_ORE
      drop_only_first: true
      items:
        crystal:
          item: iasurvival:crystal
          min_amount: 1
          max_amount: 2
          chance: 10
        knowledge_fragment:
          item: iasurvival:knowledge_fragment
          min_amount: 1
          max_amount: 2
          chance: 15
```

### 生物群系

```yaml
loots:
  blocks:
    ruby_ore:
      type: iasurvival:ruby_ore
      biomes:
        - PLAINS
        - SUNFLOWER_PLAINS
        - MOUNTAINS
      items:
        ruby:
          item: iasurvival:ruby
          min_amount: 1
          max_amount: 2
          chance: 100
```

### 忽略时运附魔

添加 `ignore_fortune` 属性，可以让战利品忽略时运附魔。

```yaml
loots:
  blocks:
    ruby_ore:
      type: iasurvival:ruby_ore
      items:
        ruby:
          item: iasurvival:ruby
          ignore_fortune: true # <----- here
          min_amount: 1
          max_amount: 2
          chance: 100
```

### 忽略刷怪笼生成的生物

添加 `ignore_spawner` 属性，可以忽略刷怪笼生成生物的掉落物。

```yaml
loots:
  mobs:
    villager:
      type: ZOMBIE
      ignore_spawner: true # <----- here
      items:
        item_1:
          item: iawearables:straw_hat
          min_amount: 1
          max_amount: 1
          chance: 100
```

### 世界

```yaml
loots:
  blocks:
    change_me:
      enabled: true
      type: SAND
      biomes:
        - BEACH
      worlds:  # <----- here
        - "world_*"
        - "!private_*"
        - "example1"
        - "!example2"
      items:
        change_me:
          item: STONE
          min_amount: 1
          max_amount: 1
          chance: 100
```

未指定世界时，战利品会在所有世界掉落。

特殊字符 `*` 可匹配名称以指定文字开头的所有世界。\
本例会匹配所有以 `world_` 开头的世界，并在其中掉落战利品。

特殊字符 `!` 会禁止在名称以指定文字开头的所有世界中掉落战利品。\
本例会匹配所有以 `private_` 开头的世界，并禁止其中的战利品掉落。

也可以指定精确的世界名称。本例中，`example2` 不允许掉落战利品。

也可以指定精确的世界名称。本例中，`example1` 允许掉落战利品。

### **方块实体 NBT 数据**

**本例检查刷怪笼的 NBT 数据。**

```yaml
loots:
  blocks:
    change_me:
      enabled: true
      type: SPAWNER
      nbt:
        spawner_type:
          path: SpawnData.entity.id
          value: minecraft:zombie
          type: string
      items:
        change_me:
          item: ACACIA_BOAT
          min_amount: 1
          max_amount: 1
          chance: 100
          ignore_fortune: false
```

如果你想通过使用具有精准采集附魔的物品从刷怪笼那里获得物品，你必须启用此设置。

```yaml
loots:  
    allow-loots-drop-from-spawners-using-silk-touch: true
```

### **NBT**

本例检查村民的 NBT 数据（职业）。

本例设置了 **profession** 属性，并指定 **NBT 属性**路径，此处为 `VillagerData.profession`。\
再将值设为 `minecraft:farmer`，使 ItemsAdder 只匹配 `VillagerData.profession` 属性为 `minecraft:farmer` 的**村民**。

```yaml
loots:
  mobs:
    villager:
      type: VILLAGER
      nbt:
        profession:
          path: VillagerData.profession
          value: minecraft:farmer
          type: string
      items:
        item_1:
          item: itemsadder:straw_hat
          min_amount: 1
          max_amount: 1
          chance: 100
```

### 元数据

如果其他插件设置了临时元数据，也可以匹配这些元数据。

```yaml
loots:
  mobs:
    soul:
      type: HUSK
      metadata:
        my_rule_1:
          name: "YourCustomKey"
          value: "ExampleValue"
          type: "string"
      items:
        ruby:
          item: ruby
          min_amount: 1
          max_amount: 1
          chance: 100
```

**nbt** 和 **metadata** 的 type 属性非常**重要**，不要**遗漏**，否则可能无法匹配。
