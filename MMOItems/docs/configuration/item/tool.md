---
title: item/tool.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/tool.yml
source_version: 6.10.1-SNAPSHOT
---

# item/tool.yml

文件：`item/tool.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `STEEL_PICKAXE` { #steel_pickaxe }

```yaml title="item/tool.yml · STEEL_PICKAXE"
STEEL_PICKAXE:
  base:
    material: IRON_PICKAXE
    name: "&f钢镐"
    max-durability: 1000
    tier: COMMON
    lore:
    - "&7一把耐用得多的铁镐。"
    will-break: true
    unbreakable: true
```

## `STEEL_SHOVEL` { #steel_shovel }

```yaml title="item/tool.yml · STEEL_SHOVEL"
STEEL_SHOVEL:
  base:
    material: IRON_SHOVEL
    name: "&f钢锹"
    max-durability: 1000
    tier: COMMON
    lore:
    - "&7一把耐用得多的铁锹。"
    will-break: true
    unbreakable: true
```

## `CRACK_PICKAXE` { #crack_pickaxe }

```yaml title="item/tool.yml · CRACK_PICKAXE"
CRACK_PICKAXE:
  base:
    material: DIAMOND_PICKAXE
    name: "§7§l裂隙镐"
    enchants:
      fortune: 2.0
      efficiency: 1.0
    max-durability: 3650.0
    tier: RARE
    attack-damage: 6.0
    attack-speed: 1.5
    pickaxe-power: 4.0
    bouncing-crack: true
    lore:
      - "§c会破坏相邻的方块！"
```

## `AUTOSMELT_PICKAXE` { #autosmelt_pickaxe }

```yaml title="item/tool.yml · AUTOSMELT_PICKAXE"
AUTOSMELT_PICKAXE:
  base:
    material: NETHERITE_PICKAXE
    name: "§c自动熔炼镐"
    lore:
      - "§7正如其名，它会§c熔炼§7矿石，"
      - "§7并且可以配合附魔使用。"
    attack-damage: 7.5
    attack-speed: 1.6
    tier: UNCOMMON
    required-level: 5.0
    pickaxe-power: 5.0
    autosmelt: true
    crafting:
      shaped:
        '1':
          input:
            - v magma_cream - 1.0..|v netherite_block - 1.0..|v magma_cream - 1.0..
            - v AIR 0 1..|v stick - 1.0..|v AIR 0 1..
            - v AIR 0 1..|v stick - 1.0..|v AIR 0 1..
```

## `SILK_SHEARS` { #silk_shears }

```yaml title="item/tool.yml · SILK_SHEARS"
SILK_SHEARS:
  base:
    material: SHEARS
    enchants:
      silk_touch: 1.0
    lore:
      - "§7如果你厌倦了不停制作新剪刀，"
      - "§7就试试这一把！它还可以"
      - "§7采集§9玻璃§7或§2草§7！"
    tier: UNCOMMON
    required-level: 5.0
```

## `FAST_PICK` { #fast_pick }

```yaml title="item/tool.yml · FAST_PICK"
FAST_PICK:
  base:
    material: WOODEN_PICKAXE
    mining-efficiency: 100.0
    max-item-damage: 100.0
    lore:
      - "&7&o速度快得惊人，但不会掉落物品"
```
