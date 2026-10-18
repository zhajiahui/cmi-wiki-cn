---
title: 锻造
source: https://docs.phoenixdevt.fr/mmocore/profession/smithing
source_snapshot: '2026-10-19'
---

# 锻造 {#🔨-smithing}

史密斯是副职业的一种特定类型，其中玩家在使用原版铁砧修理物品时可以获得经验。玩家获得的经验取决于玩家正在维修的物品，以及玩家正在维修的耐久度的数量。

配置文件非常不言自明：你可以设置在使用原版铁砧修复特定物品的100耐久度点时希望玩家获得多少锻造经验。

## 配置 {#configuration}

```
# Experience given by repairing 100
# durability points from a specific material.

# Warning, diamonds/iron ingots/<any material
# which repairs a specific type of tool> do
# not repair the same amount of durability!
repair-exp:

    # Swords
    DIAMOND_SWORD: 1.923 # Max durability: 1561
    GOLDEN_SWORD: 62.5 # Max durability: 32
    IRON_SWORD: 8 # Md: 250
    STONE_SWORD: 7.634 # Md: 131
    WOODEN_SWORD: 13.56 # Md: 59
    
    # Picks
    DIAMOND_PICKAXE: 1.923
    GOLDEN_PICKAXE: 62.5
    IRON_PICKAXE: 8
    STONE_PICKAXE: 7.634
    WOODEN_PICKAXE: 13.56
    
    # Add as many as you want: bows, shields..
```

## 笔记 {#note}

不同物品的最大耐久度不同，但在铁砧上用材料修复工具时，**每次都会恢复最大耐久度的 25%！**因此这里的经验数值看起来不太整齐。例如，在铁砧上用钻石修复钻石镐时，会恢复其 1561 点耐久度的 25%，约为 390 点，对应的经验为 `390 / 100 * 1,923 = 7.6 EXP`。

修复金剑时，你仅修复32耐久度点中的25%点i.e8耐久度点（代表`8 / 100 * 62.5 = 5 EXP`）。使用原版铁砧修理钻石剑比修理金剑可以获得更多的经验。

---

原文：[🔨 Smithing](https://docs.phoenixdevt.fr/mmocore/profession/smithing) · 原文归档：2026-10-19
