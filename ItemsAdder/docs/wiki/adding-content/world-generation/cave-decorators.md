---
title: "洞穴装饰器"
source_url: "https://wiki.itemsadder.com/adding-content/world-generation/cave-decorators"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 洞穴装饰器

## 在洞穴中生成装饰

ItemsAdder 可以在世界洞穴中生成装饰，让服务器更有特色。

例如新的蘑菇、小型植物、岩石和装饰物。

![](../../assets/443282d72a8131fda455.png)

## 创建洞穴生成器

### 创建配置

例如，创建会在世界中生成的一组小岩石。

```yaml
info:
  namespace: myitems
cave_decorators:
  small_rocks:
    block: small_rocks
    bottom_blocks:
    - DIRT
    - GRASS_BLOCK
    - STONE
    - COBBLESTONE
    - MOSSY_COBBLESTONE
    biomes:
    - PLAINS
    - SUNFLOWER_PLAINS
    - RIVER
    - MOUNTAINS
    - MOUNTAIN_EDGE
    - BIRCH_FOREST
    - BIRCH_FOREST_HILLS
    - TALL_BIRCH_FOREST
    - TALL_BIRCH_HILLS
    worlds:
      - world
    chance: 100
    max_height: 255 
    min_height: 0
    amount: 4
    position: SURFACE
```

本例设置了以下属性：

`block` 是要生成为装饰的 ItemsAdder 方块。

`bottom_blocks` 属性用于决定装饰可以生成的方块类型。

`biomes` 属性用于决定装饰可以生成的有效生物群系。

`worlds` 属性决定装饰可以生成的世界。

`chance` 是每个世界区块中生成装饰的几率。

`max_height` 是装饰可以生成的最大世界高度。

`min_height` 是装饰可以生成的最小世界高度。

`amount` 是一组装饰物生成的方块数量。例如设为 5，即可生成一组 5 个彼此相连的装饰物。

`position` 是一个属性，用于指定方块必须在洞穴的 `SURFACE`（表面）还是 `CEILING`（天花板）。

## 创建方块

接着按教程创建方块即可。可以按需使用 `REAL_NOTE`、`REAL_WIRE` `REAL_TRANSPARENT` 和 `REAL` 方块。

[my-first-block.md](../../plugin-usage/beginners/my-first-block.md)
