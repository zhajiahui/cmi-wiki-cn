---
title: 生成自定义方块
source: https://docs.phoenixdevt.fr/mmoitems/features/world-gen-templates
source_snapshot: '2026-10-19'
---

# 生成自定义方块 {#🌱-spawning-custom-blocks}

*世界生成模板*用于使你的自定义块在新生成的世界中生成。自定义块在随机数量的块的矿脉中生成。它们可能只会在世界的一组生物群落列表中生成。 Gen 模板还具有本 wiki 页面将概述的更具体的选项。

**如果你希望在你的世界中生成自定义块，请确保在主MMOItems配置文件中启用`custom-blocks.enable-world-gen`选项！**

## 基本生成模板示例 {#basic-gen-template-example}

```yml
basic-template:
  replace: [STONE]
  chunk-chance: 0.7
  depth: -64=255
  vein-size: 5
  vein-count: 2
```

当生成世界时，每个块都有一定的机会被选择以生成块（`chunk-chance`）。你还可以配置块放置的深度。`replace`选项定义你的自定义块将替换哪些原版块。这意味着自定义方块无法在半空中生成，因此自定义矿石可以像原版矿石一样在石墙内生成。

`vein-count`是将在选定块内生成的矿脉数量，`vein-size`是将在每个块矿脉中生成的自定义块数量。

## 具体选项 {#specific-options}

使用`slime-chunk`选项，这样你的方块只能生成粘液块。

```yml
template-id:
  slime-chunk: true
```

使用`bordering`或`not-bordering`选项，以便你的块仅在自定义块周围的特定块满足其条件时生成。

```yml
end-debris:
  replace: [END_STONE]
  chunk-chance: 0.4
  depth: 0=255
  vein-size: 2
  vein-count: 20
  bordering:
  - AIR
  worlds:
  - world_the_end
```

在此示例中，`end-debris`仅当其中一个面接触空气时才会生成。

## 生物群落/世界黑/白名单 {#biome-world-black-whitelist}

通过向`worlds`列表添加条目，你可以将任何自定义块限制到一组特定的世界。如果你在世界名称前使用`!`，世界白名单将变成黑名单，并且自定义块将在指定世界之外的任何地方生成。

```yml
template-id:
  worlds:
  - world_nether # Just like nether quartz
```

生物群落的格式相同，只需使用`biomes`而不是`worlds`并输入生物群落名称（[Spigotjavadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html)）。

```yml
template-id:
  biomes:
  - mountains # Just like emerald
```

---

原文：[🌱 Spawning Custom Blocks](https://docs.phoenixdevt.fr/mmoitems/features/world-gen-templates) · 原文归档：2026-10-19
