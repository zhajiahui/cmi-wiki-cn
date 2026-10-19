---
title: "世界生成器（矿石）"
source_url: "https://wiki.itemsadder.com/adding-content/world-generation/worlds-populators"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 世界生成器（矿石）

世界生成器允许你在世界的表面下生成自定义方块。它们主要用于矿石和装饰方块。

### 示例：两个生成器

此代码让 ItemsAdder 在名为 `world` 的世界中生成 `myitems:custom_block` 方块，只替换 `STONE`、`DIRT`、`ANDESITE`、`GRANITE`、`COBBLESTONE`、`GRAVEL` 类型的方块，且只在生物群系 `PLAINS` 中生成。

每个区块生成 1 条由 3 个方块组成的矿脉。

```yaml
info:
  namespace: my_world_populator
worlds_populators:
  custom_block:
    block: myitems:custom_block
    worlds:
    - world
    replaceable_blocks:
    - STONE
    - DIRT
    - ANDESITE
    - GRANITE
    - COBBLESTONE
    - GRAVEL
    biomes:
    - PLAINS
    chunk_chance: 70.0
    max_height: 45
    min_height: 25
    vein_blocks: 6
    chunk_veins: 1
  custom_block_2:
    block: myitems:custom_block_2
    worlds:
    - world
    replaceable_blocks:
    - DIRT
    chunk_chance: 100.0
    max_height: 64
    min_height: 40
    vein_blocks: 3
    chunk_veins: 1
```

### `vein_blocks`, `chunk_veins`, `chunk_chance`

我建议你从我在 **ItemsAdder** 文件夹中创建的 `blocks.yml` 文件中读取值。\
不要设置过高的值，否则服务器可能会卡顿。\
以我的值为例。

**`chunk_veins`**：在区块中生成的矿脉数量\
&#xNAN;**`vein_blocks`**：每个矿脉中的方块数量（或矿脉大小）\
&#xNAN;**`chunk_chance`**：在区块中生成的几率。你应该将其设置为 100 以生成普通矿石，并降低它以生成更稀有的矿石。

### 生物群系

移除此选项后，插件会在所有生物群系中生成矿石。

```yaml
  custom_block:
    block: myitems:custom_block
    worlds:
    - world
    replaceable_blocks:
    - STONE
    - DIRT
    - ANDESITE
    - GRANITE
    - COBBLESTONE
    - GRAVEL
    chunk_chance: 70.0
    max_height: 45
    min_height: 25
    vein_blocks: 6
    chunk_veins: 1
```

### 可替换方块

你可以删除此选项，插件将在每个方块中生成矿石，而不是检查它是否可以被替换。

```yaml
  custom_block:
    block: myitems:custom_block
    worlds:
    - world
    chunk_chance: 70.0
    max_height: 45
    min_height: 25
    vein_blocks: 6
    chunk_veins: 1
```
