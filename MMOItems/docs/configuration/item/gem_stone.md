---
title: item/gem_stone.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/gem_stone.yml
source_version: 6.10.1-SNAPSHOT
---

# item/gem_stone.yml

文件：`item/gem_stone.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `RUBY` { #ruby }

```yaml title="item/gem_stone.yml · RUBY"
RUBY:
  base:
    material: EMERALD
    name: "&f力量红宝石"
    critical-strike-power:
      base: 11.0
      spread: 0.028
      max-spread: 0.083
    attack-damage:
      base: 1.5
      spread: 0.083
      max-spread: 0.25
    required-level: 5.0
    disable-crafting: true
```

## `GEM_OF_ACCURACY` { #gem_of_accuracy }

```yaml title="item/gem_stone.yml · GEM_OF_ACCURACY"
GEM_OF_ACCURACY:
  base:
    material: DIAMOND
    disable-crafting: true
    name: "&f精准宝石"
    success-rate:
      base: 94.5
      spread: 0.015
      max-spread: 0.045
    attack-speed:
      base: 0.075
      spread: 0.08
      max-spread: 0.25
    tier: COMMON
    critical-strike-chance:
      base: 12.5
      spread: 0.06
      max-spread: 0.17
    gem-color: Blue
    displayed-type: "蓝色宝石"
```

## `GEM_OF_LIFE` { #gem_of_life }

```yaml title="item/gem_stone.yml · GEM_OF_LIFE"
GEM_OF_LIFE:
  base:
    material: RED_DYE
    max-health: 4.0
    name: "&f生命宝石"
    item-type-restriction:
    - ARMOR
    gem-color: Red
    displayed-type: "红色盔甲宝石"
    block-power: 3.0
    disable-crafting: true
```

## `NATURE_GIFT` { #nature_gift }

```yaml title="item/gem_stone.yml · NATURE_GIFT"
NATURE_GIFT:
  base:
    material: EMERALD
    name: "&f自然之赐"
    displayed-type: "绿色宝石"
    fire-damage-reduction:
      base: 25.0
      spread: 0.06
      max-spread: 0.17
    required-level: 6.0
```

## `SPITEFUL_OPAQUE_DIAMOND` { #spiteful_opaque_diamond }

```yaml title="item/gem_stone.yml · SPITEFUL_OPAQUE_DIAMOND"
SPITEFUL_OPAQUE_DIAMOND:
  base:
    material: DIAMOND
    name: "&9怨恨的暗钻"
    success-rate:
      base: 11.0
      spread: 0.03
      max-spread: 0.08
    attack-damage:
      base: 3.5
      spread: 0.04
      max-spread: 0.13
    armor: 2.0
    disable-crafting: true
    gem-color: Blue
    displayed-type: "蓝色宝石"
```

## `GOLDEN_RELIC` { #golden_relic }

```yaml title="item/gem_stone.yml · GOLDEN_RELIC"
GOLDEN_RELIC:
  base:
    material: GOLD_NUGGET
    name: "&e黄金遗物"
    lore:
    - "&7可镶入&e任何&7宝石孔。"
    - '&7'
    critical-strike-chance:
      base: 15.0
      spread: 0.08
      max-spread: 0.25
    required-level: 20.0
    disable-crafting: true
```

## `BLAZE_SOUL` { #blaze_soul }

```yaml title="item/gem_stone.yml · BLAZE_SOUL"
BLAZE_SOUL:
  base:
    material: ORANGE_DYE
    disable-crafting: true
    name: "&c烈焰之魂"
    required-level: 15.0
    displayed-type: "红色宝石"
    hide-enchants: true
    enchants:
      unbreaking: 1
    fire-damage-reduction:
      base: 55.0
      spread: 0.03
      max-spread: 0.08
    success-rate:
      base: 70.0
      spread: 0.042
      max-spread: 0.13
```

## `NETHER_GEM` { #nether_gem }

```yaml title="item/gem_stone.yml · NETHER_GEM"
NETHER_GEM:
  base:
    material: NETHERITE_SCRAP
    name: "§c下界宝石"
    lore:
      - "§c§o下界宝石可以镶入"
      - "§c§o带有下界宝石孔的物品。"
    success-rate:
      base: 60.0
      scale: 0.12
      spread: 0.25
    gem-color: Nether
    attack-damage:
      base: 6.0
      scale: 0.05
      spread: 0.06
      max-spread: 0.12
    weapon-damage:
      base: 14.0
      scale: 0.1
      spread: 0.09
      max-spread: 0.15
    critical-strike-chance:
      base: 4.0
      scale: 0.1
      spread: 0.09
      max-spread: 0.15
    critical-strike-power:
      base: 25.0
      scale: 0.1
      spread: 0.09
      max-spread: 0.15
    crafting:
      shaped:
        '1':
          input:
            - v AIR 0 1..|v netherite_ingot - 1.0..|v AIR 0 1..
            - v netherite_ingot - 1.0..|v magma_cream - 1.0..|v netherite_ingot - 1.0..
            - v AIR 0 1..|v netherite_ingot - 1.0..|v AIR 0 1..
    tier: RARE
```

## `RAINBOW_GEM` { #rainbow_gem }

```yaml title="item/gem_stone.yml · RAINBOW_GEM"
RAINBOW_GEM:
  base:
    material: AMETHYST_SHARD
    name: "§c§l彩§6§l§e§l§a§l虹§2§l§9§l宝§3§l§c§l§6§l石§e§l"
    lore:
      - "§e彩虹宝石可以"
      - "§e提高大量属性！"
      - "§2它还会根据物品此前的升级情况"
      - "§2进一步升级物品！"
      - "§c制作难度极高！"
    attack-damage: 2.0
    attack-speed: 0.1
    critical-strike-chance: 10.0
    critical-strike-power: 15.0
    block-power: 2.0
    block-rating: 2.0
    block-cooldown-reduction: 2.5
    cooldown-reduction: 5.0
    weapon-damage: 5.0
    magic-damage: 2.5
    tier: LEGENDARY
    unstackable: true
    gem-color: Rainbow
    gem-upgrade-scaling: HISTORIC
    max-health: 5.0
    max-mana: 5.0
    crafting:
      megashaped:
        '1':
          input:
            - v netherite_sword - 1.0..|v netherite_helmet - 1.0..|v netherite_chestplate
              - 1.0..|v netherite_leggings - 1.0..|v netherite_boots - 1.0..|v golden_sword
              - 1.0..
            - v diamond_helmet - 1.0..|v wither_skeleton_skull - 1.0..|v gold_ingot
              - 1.0..|v gold_ingot - 1.0..|v nether_star - 1.0..|v golden_helmet - 1.0..
            - v diamond_chestplate - 1.0..|v iron_ingot - 1.0..|v diamond_block - 1.0..|v
              diamond_block - 1.0..|v amethyst_shard - 1.0..|v golden_chestplate - 1.0..
            - v diamond_leggings - 1.0..|v iron_ingot - 1.0..|v diamond_block - 1.0..|v
              diamond_block - 1.0..|v amethyst_shard - 1.0..|v golden_leggings - 1.0..
            - v diamond_boots - 1.0..|v netherite_block - 1.0..|v copper_ingot - 1.0..|v
              copper_ingot - 1.0..|v heart_of_the_sea - 1.0..|v golden_boots - 1.0..
            - v iron_sword - 1.0..|v iron_helmet - 1.0..|v iron_chestplate - 1.0..|v
              iron_leggings - 1.0..|v iron_boots - 1.0..|v diamond_sword - 1.0..
    success-rate: 90.0
```
