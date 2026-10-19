---
title: item/catalyst.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/catalyst.yml
source_version: 6.10.1-SNAPSHOT
---

# item/catalyst.yml

文件：`item/catalyst.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `NATURES_GIFT` { #natures_gift }

```yaml title="item/catalyst.yml · NATURES_GIFT"
NATURES_GIFT:
  base:
    material: OAK_SAPLING
    disable-crafting: true
    name: "&9魔法触媒"
    lore:
      - "&7没人知道它是在哪里被发现的。"
    magic-damage:
      base: 15.0
      spread: 0.084
      max-spread: 0.25
    required-level: 4.0
    required-class:
      - Wizard
      - Paladin
    hide-enchants: true
    enchants:
      unbreaking: 1
```

## `LUCKY_CHARM` { #lucky_charm }

```yaml title="item/catalyst.yml · LUCKY_CHARM"
LUCKY_CHARM:
  base:
    material: RABBIT_FOOT
    name: "&f幸运护符"
    tier: NORMAL
    critical-strike-chance: 2.5
```

## `WARRIOR_AMULET` { #warrior_amulet }

```yaml title="item/catalyst.yml · WARRIOR_AMULET"
WARRIOR_AMULET:
  base:
    material: GRAY_DYE
    name: "&f战士护身符"
    disable-crafting: true
    hide-enchants: true
    enchants:
      unbreaking: 1
    damage-reduction: 5.0
```

## `FORGOTTEN_IDOL` { #forgotten_idol }

```yaml title="item/catalyst.yml · FORGOTTEN_IDOL"
FORGOTTEN_IDOL:
  base:
    material: GOLD_NUGGET
    enchants:
      unbreaking: 1
    hide-enchants: true
    name: "&e遗忘神像"
    required-level: 19.0
    weapon-damage:
      base: 35.0
      spread: 0.042
      max-spread: 0.13
```

## `FIRE_TOTEM` { #fire_totem }

```yaml title="item/catalyst.yml · FIRE_TOTEM"
FIRE_TOTEM:
  base:
    material: BLAZE_ROD
    hide-enchants: true
    enchants:
      unbreaking: 1
    name: "&f火焰图腾"
    tier: RARE
    fire-damage-reduction:
      base: 85.0
      spread: 0.02
      max-spread: 0.06
    required-level: 10.0
    disable-crafting: true
```

## `ENCHANTED_SHULKER_SHELL` { #enchanted_shulker_shell }

```yaml title="item/catalyst.yml · ENCHANTED_SHULKER_SHELL"
ENCHANTED_SHULKER_SHELL:
  base:
    material: SHULKER_SHELL
    name: "§d附魔潜影壳"
    enchants:
      luck_of_the_sea: 1.0
    hide-enchants: true
    lore:
      - "§5§o潜影贝的力量尽在你手中！"
      - "§b宇宙魔杖的组件。"
    disable-crafting: true
    ability:
      ability1:
        type: SHULKER_MISSILE
        mode: RIGHT_CLICK
        duration: 5.0
        damage: 6.0
        cooldown: 4.5
        effect-duration: 3.0
    tier: RARE
    required-level: 5.0
    item-particles:
      type: DOUBLE_RINGS
      particle: END_ROD
      amount: 1.0
```

## `PERFECT_ENDER_PEARL` { #perfect_ender_pearl }

```yaml title="item/catalyst.yml · PERFECT_ENDER_PEARL"
PERFECT_ENDER_PEARL:
  base:
    material: ENDER_PEARL
    disable-interaction: true
    name: "§5§l完美末影珍珠"
    lore:
      - "§5§o从末影人的精华中提取。"
      - "§b宇宙魔杖的组件。"
    tier: RARE
    ability:
      ability1:
        type: BLINK
        mode: RIGHT_CLICK
        range: 38.0
        cooldown: 8.0
    enchants:
      luck_of_the_sea: 1.0
    hide-enchants: true
    disable-crafting: true
    item-particles:
      type: AURA
      particle: PORTAL
    required-level: 5.0
```

## `POWER_CRYSTAL` { #power_crystal }

```yaml title="item/catalyst.yml · POWER_CRYSTAL"
POWER_CRYSTAL:
  base:
    material: PRISMARINE_SHARD
    name: "§9§l力量水晶"
    tier: RARE
    handworn: true
    fire-damage-reduction: 100.0
    magic-damage-reduction: 100.0
    unbreakable: true
    knockback-resistance: 1.0
    magic-damage:
      base: 40.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.3
    sounds:
      on-right-click:
        sound: minecraft:block.beacon.activate
        volume: 2.0
        pitch: 0.0
    ability:
      ability1:
        type: MAGICAL_PATH
        mode: RIGHT_CLICK
        duration: 12.0
        cooldown: 20.0
    required-level: 5.0
```

## `LUCK_CHARM` { #luck_charm }

```yaml title="item/catalyst.yml · LUCK_CHARM"
LUCK_CHARM:
  base:
    material: GOLD_NUGGET
    name: "§e§l幸运护符"
    lore:
      - "§7提供§2幸运 III§7、§e+50%§7 附魔技能经验"
      - "§7以及§e+25%§7 怪物经验掉落"
      - "§7手持时生效。"
      - "§c死亡时不会掉落，且无法堆叠！"
    perm-effects:
      LUCK: 3.0
    additional-experience: 25.0
    tier: MAGICAL
    required-level: 5.0
    required-class:
      - Mage
    disable-crafting: true
    disable-smelting: true
    disable-interaction: true
    handworn: true
    additional-experience-enchanting: 50.0
    crafting:
      shaped:
        '1':
          input:
            - v gold_block - 1.0..|v emerald - 1.0..|v gold_block - 1.0..
            - v emerald - 1.0..|v nether_star - 1.0..|v emerald - 1.0..
            - v gold_block - 1.0..|v emerald - 1.0..|v gold_block - 1.0..
    disable-death-drop: true
```

## `THIN_TRANSPARENT_GLOVES` { #thin_transparent_gloves }

```yaml title="item/catalyst.yml · THIN_TRANSPARENT_GLOVES"
THIN_TRANSPARENT_GLOVES:
  base:
    material: LEATHER
    name: "§7轻薄透明手套"
    set: PSYCHIC
    required-class:
      - Mage
    attack-damage: 15.0
    magic-damage: 100.0
    tier: MAGICAL
```

## `ICE_GOLEM_HEART` { #ice_golem_heart }

```yaml title="item/catalyst.yml · ICE_GOLEM_HEART"
ICE_GOLEM_HEART:
  base:
    material: PRISMARINE_SHARD
    name: "§b冰傀儡之心"
    lore:
      - "§7不满消散，希望升起。"
      - "§c手持时可免受熔岩伤害。"
      - "§2可与双手武器"
      - "§2同时使用！"
    magic-damage: 15.0
    amphibian: LAVA
    perm-effects:
      FIRE_RESISTANCE: 1.0
    element:
      ice:
        defense: -100.0
      fire:
        defense: 100.0
    handworn: true
    fire-damage-reduction: 100.0
```

## `SHRINKIFIKATOR` { #shrinkifikator }

```yaml title="item/catalyst.yml · SHRINKIFIKATOR"
SHRINKIFIKATOR:
  base:
    material: PRISMARINE_SHARD
    name: "缩小器"
    scale: -0.5
    max-health: -10.0
    movement-speed: -0.03
```
