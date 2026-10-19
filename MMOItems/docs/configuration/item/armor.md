---
title: item/armor.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/armor.yml
source_version: 6.10.1-SNAPSHOT
---

# item/armor.yml

文件：`item/armor.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `DRAGON_HELMET` { #dragon_helmet }

```yaml title="item/armor.yml · DRAGON_HELMET"
# 巨龙套装
DRAGON_HELMET:
  base:
    material: DIAMOND_HELMET
    max-durability: 5500.0
    tier: EPIC
    max-health: 4.0
    armor-toughness: 3.0
    magic-damage-reduction:
      base: 3.0
      spread: 0.05
      max-spread: 0.17
    armor: 3.5
    element:
      fire:
        defense:
          base: 5.0
          scale: 0.0
          spread: 0.07
          max-spread: 0.2
      darkness:
        defense:
          base: 12.0
          scale: 0.0
          spread: 0.07
          max-spread: 0.2
    name: "§5§l巨龙头盔"
    enchants:
      fire_protection: 4.0
    lore:
      - "§c§o这套强大的盔甲"
      - "§c§o由龙鳞制成。"
    required-level: 12.0
    block-rating:
      base: 4.0
      scale: 0.075
      spread: 0.02
      max-spread: 0.08
    gem-sockets:
      - Magenta
      - Black
    set: DRAGON
```

## `DRAGON_CHESTPLATE` { #dragon_chestplate }

```yaml title="item/armor.yml · DRAGON_CHESTPLATE"
DRAGON_CHESTPLATE:
  base:
    material: DIAMOND_CHESTPLATE
    max-durability: 6850.0
    tier: EPIC
    max-health: 10.0
    armor-toughness: 3.0
    magic-damage-reduction:
      base: 8.0
      spread: 0.05
      max-spread: 0.17
    armor: 7.0
    element:
      fire:
        defense:
          base: 18.0
          scale: 0.0
          spread: 0.07
          max-spread: 0.2
      darkness:
        defense:
          base: 35.0
          scale: 0.0
          spread: 0.07
          max-spread: 0.2
    name: "§5§l巨龙胸甲"
    enchants:
      fire_protection: 4.0
    lore:
      - "§c§o这套强大的盔甲"
      - "§c§o由龙鳞制成。"
    required-level: 12.0
    block-rating:
      base: 5.0
      scale: 0.075
      spread: 0.02
      max-spread: 0.08
    gem-sockets:
      - Magenta
      - Black
    set: DRAGON
```

## `DRAGON_LEGGINGS` { #dragon_leggings }

```yaml title="item/armor.yml · DRAGON_LEGGINGS"
DRAGON_LEGGINGS:
  base:
    material: DIAMOND_LEGGINGS
    max-durability: 6150.0
    tier: EPIC
    max-health: 7.0
    armor-toughness: 3.0
    magic-damage-reduction:
      base: 5.0
      spread: 0.05
      max-spread: 0.17
    armor: 5.0
    element:
      fire:
        defense:
          base: 12.0
          scale: 0.0
          spread: 0.07
          max-spread: 0.2
      darkness:
        defense:
          base: 22.0
          scale: 0.0
          spread: 0.07
          max-spread: 0.2
    name: "§5§l巨龙护腿"
    enchants:
      fire_protection: 4.0
    lore:
      - "§c§o这套强大的盔甲"
      - "§c§o由龙鳞制成。"
    required-level: 12.0
    block-rating:
      base: 4.5
      scale: 0.075
      spread: 0.02
      max-spread: 0.08
    gem-sockets:
      - Magenta
      - Black
    set: DRAGON
```

## `DRAGON_BOOTS` { #dragon_boots }

```yaml title="item/armor.yml · DRAGON_BOOTS"
DRAGON_BOOTS:
  base:
    material: DIAMOND_BOOTS
    max-durability: 5500.0
    tier: EPIC
    max-health: 4.0
    armor-toughness: 3.0
    magic-damage-reduction:
      base: 3.0
      spread: 0.05
      max-spread: 0.17
    armor: 3.5
    element:
      fire:
        defense:
          base: 5.0
          scale: 0.0
          spread: 0.07
          max-spread: 0.2
      darkness:
        defense:
          base: 12.0
          scale: 0.0
          spread: 0.07
          max-spread: 0.2
    name: "§5§l巨龙靴子"
    enchants:
      fire_protection: 4.0
    lore:
      - "§c§o这套强大的盔甲"
      - "§c§o由龙鳞制成。"
    required-level: 12.0
    block-rating:
      base: 4.0
      scale: 0.075
      spread: 0.02
      max-spread: 0.08
    gem-sockets:
      - Magenta
      - Black
    set: DRAGON
```

## `SPELLCASTER_HELMET` { #spellcaster_helmet }

```yaml title="item/armor.yml · SPELLCASTER_HELMET"
# 施法者套装
SPELLCASTER_HELMET:
  base:
    material: LEATHER_HELMET
    name: "§d施法者头盔"
    lore:
      - "§d§l非常适合法师！"
    required-class:
      - Mage
    required-level: 1.0
    block-power:
      base: 10.0
      spread: 0.1
      max-spread: 0.2
    block-rating:
      base: 7.0
      spread: 0.1
      max-spread: 0.2
    tier: UNCOMMON
    max-durability: 950.0
    element:
      water:
        defense:
          base: 5.0
          scale: 0.0
          spread: 0.2
          max-spread: 0.3
    max-mana: 6.0
    magic-damage-reduction: 25.0
    armor-toughness: 1.0
    armor: 2.0
    hide-dye: true
    dye-color: 125 0 255
    set: SPELLCASTER
```

## `SPELLCASTER_CHESTPLATE` { #spellcaster_chestplate }

```yaml title="item/armor.yml · SPELLCASTER_CHESTPLATE"
SPELLCASTER_CHESTPLATE:
  base:
    material: LEATHER_CHESTPLATE
    name: "§d施法者胸甲"
    lore:
      - "§d§l非常适合法师！"
    required-class:
      - Mage
    required-level: 1.0
    block-power:
      base: 15.0
      spread: 0.1
      max-spread: 0.2
    block-rating:
      base: 10.0
      spread: 0.1
      max-spread: 0.2
    tier: UNCOMMON
    max-durability: 1450.0
    element:
      water:
        defense:
          base: 10.0
          scale: 0.0
          spread: 0.2
          max-spread: 0.3
    max-mana: 6.0
    magic-damage-reduction: 25.0
    armor-toughness: 1.0
    armor: 4.0
    hide-dye: true
    dye-color: 125 0 255
    set: SPELLCASTER
```

## `SPELLCASTER_LEGGINGS` { #spellcaster_leggings }

```yaml title="item/armor.yml · SPELLCASTER_LEGGINGS"
SPELLCASTER_LEGGINGS:
  base:
    material: LEATHER_LEGGINGS
    name: "§d施法者护腿"
    lore:
      - "§d§l非常适合法师！"
    required-class:
      - Mage
    required-level: 1.0
    block-power:
      base: 12.0
      spread: 0.1
      max-spread: 0.2
    block-rating:
      base: 8.5
      spread: 0.1
      max-spread: 0.2
    tier: UNCOMMON
    max-durability: 1450.0
    element:
      water:
        defense:
          base: 7.5
          scale: 0.0
          spread: 0.2
          max-spread: 0.3
    max-mana: 6.0
    magic-damage-reduction: 25.0
    armor-toughness: 1.0
    armor: 3.0
    hide-dye: true
    dye-color: 125 0 255
    set: SPELLCASTER
```

## `SPELLCASTER_BOOTS` { #spellcaster_boots }

```yaml title="item/armor.yml · SPELLCASTER_BOOTS"
SPELLCASTER_BOOTS:
  base:
    material: LEATHER_BOOTS
    name: "§d施法者靴子"
    lore:
      - "§d§l非常适合法师！"
    required-class:
      - Mage
    required-level: 1.0
    block-power:
      base: 10.0
      spread: 0.1
      max-spread: 0.2
    block-rating:
      base: 7.0
      spread: 0.1
      max-spread: 0.2
    tier: UNCOMMON
    max-durability: 950.0
    element:
      water:
        defense:
          base: 5.0
          scale: 0.0
          spread: 0.2
          max-spread: 0.3
    max-mana: 6.0
    magic-damage-reduction: 25.0
    armor-toughness: 1.0
    armor: 2.0
    hide-dye: true
    dye-color: 125 0 255
    set: SPELLCASTER
```

## `OMNIELEMENTAL_HELMET` { #omnielemental_helmet }

```yaml title="item/armor.yml · OMNIELEMENTAL_HELMET"
# 全元素套装
OMNIELEMENTAL_HELMET:
  base:
    material: LEATHER_HELMET
    required-level: 15.0
    lore:
      - "§b别将自己局限于一种元素。"
      - "§c死亡或损坏时，"
      - "§c它会降级。"
      - "§9穿戴时获得夜视。"
    enchants:
      luck_of_the_sea: 1.0
    hide-enchants: true
    name: "§c§l全§6§l§e§l§a§l§2§l元§3§l§9§l§b§l§f§l素§e§l§a§l§6§l§c§l头§c§l§6§l§e§l§a§l盔§2§l§3§l"
    armor-toughness: 2.5
    armor: 4.5
    max-durability: 1950.0
    element:
      fire:
        defense: 100.0
      earth:
        defense: 100.0
    block-power:
      base: 10.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    block-rating:
      base: 8.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    magic-damage:
      base: 10.0
      scale: 0.15
      spread: 0.2
      max-spread: 0.3
    dye-color: 255 255 0
    break-downgrade: true
    death-downgrade: true
    death-downgrade-chance: 100.0
    gem-sockets:
      - Rainbow
      - Rainbow
    perm-effects:
      NIGHT_VISION: 1.0
    tier: VERY_RARE
    max-health: 5.0
```

## `OMNIELEMENTAL_CHESTPLATE` { #omnielemental_chestplate }

```yaml title="item/armor.yml · OMNIELEMENTAL_CHESTPLATE"
OMNIELEMENTAL_CHESTPLATE:
  base:
    material: LEATHER_CHESTPLATE
    required-level: 15.0
    lore:
      - "§b别将自己局限于一种元素。"
      - "§c死亡或损坏时，"
      - "§c它会降级。"
      - "§9穿戴时获得抗性提升 I。"
    enchants:
      luck_of_the_sea: 1.0
    hide-enchants: true
    name: "§c§l全§6§l§e§l§a§l§2§l§3§l元§9§l§b§l§f§l§e§l§a§l素§6§l§c§l§c§l§6§l胸§e§l§a§l§2§l§3§l§9§l甲§b§l§f§l§e§l"
    armor-toughness: 2.5
    armor: 9.5
    max-durability: 3900.0
    element:
      ice:
        defense: 100.0
      water:
        defense: 100.0
    block-power:
      base: 12.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    block-rating:
      base: 10.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    magic-damage:
      base: 15.0
      scale: 0.15
      spread: 0.2
      max-spread: 0.3
    dye-color: 150 200 255
    break-downgrade: true
    death-downgrade: true
    death-downgrade-chance: 100.0
    gem-sockets:
      - Rainbow
      - Rainbow
    perm-effects:
      DAMAGE_RESISTANCE: 1.0
    tier: VERY_RARE
    max-health: 5.0
```

## `OMNIELEMENTAL_LEGGINGS` { #omnielemental_leggings }

```yaml title="item/armor.yml · OMNIELEMENTAL_LEGGINGS"
OMNIELEMENTAL_LEGGINGS:
  base:
    material: LEATHER_LEGGINGS
    required-level: 15.0
    lore:
      - "§b别将自己局限于一种元素。"
      - "§c死亡或损坏时，"
      - "§c它会降级。"
      - "§9穿戴时获得速度 I。"
    enchants:
      luck_of_the_sea: 1.0
    hide-enchants: true
    name: "§c§l全§6§l§e§l§a§l§2§l§3§l元§9§l§b§l§f§l§e§l素§a§l§6§l§c§l§c§l护§6§l§e§l§a§l§2§l腿§3§l§b§l§f§l"
    armor-toughness: 2.5
    armor: 7.0
    max-durability: 3000.0
    element:
      thunder:
        defense: 100.0
      wind:
        defense: 100.0
    block-power:
      base: 10.5
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    block-rating:
      base: 8.5
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    magic-damage:
      base: 12.0
      scale: 0.15
      spread: 0.2
      max-spread: 0.3
    dye-color: 180 180 0
    break-downgrade: true
    death-downgrade: true
    death-downgrade-chance: 100.0
    gem-sockets:
      - Rainbow
      - Rainbow
    perm-effects:
      SPEED: 1.0
    tier: VERY_RARE
    max-health: 5.0
```

## `OMNIELEMENTAL_BOOTS` { #omnielemental_boots }

```yaml title="item/armor.yml · OMNIELEMENTAL_BOOTS"
OMNIELEMENTAL_BOOTS:
  base:
    material: LEATHER_BOOTS
    required-level: 15.0
    lore:
      - "§b别将自己局限于一种元素。"
      - "§c死亡或损坏时，"
      - "§c它会降级。"
      - "§9穿戴时获得跳跃提升 I。"
    enchants:
      luck_of_the_sea: 1.0
    hide-enchants: true
    name: "§c§l全§6§l§e§l§a§l§2§l元§3§l§9§l§b§l§f§l素§e§l§a§l§6§l靴§c§l§c§l§6§l§e§l子§a§l§2§l"
    armor-toughness: 2.5
    armor: 3.0
    max-durability: 2150.0
    element:
      darkness:
        defense: 100.0
      lightness:
        defense: 100.0
    block-power:
      base: 4.5
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    block-rating:
      base: 5.5
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    magic-damage:
      base: 8.0
      scale: 0.15
      spread: 0.2
      max-spread: 0.3
    dye-color: 160 160 160
    break-downgrade: true
    death-downgrade: true
    death-downgrade-chance: 100.0
    gem-sockets:
      - Rainbow
      - Rainbow
    perm-effects:
      JUMP: 1.0
    tier: VERY_RARE
    max-health: 5.0
```

## `UNDEAD_SLAYER_HELMET` { #undead_slayer_helmet }

```yaml title="item/armor.yml · UNDEAD_SLAYER_HELMET"
# 亡灵杀手
UNDEAD_SLAYER_HELMET:
  base:
    material: NETHERITE_HELMET
    required-level: 80.0
    undead-damage: 15.0
    set: UNDEADSLAYER
    name: "§c亡灵杀手头盔"
    max-durability: 17500.0
    physical-damage: 5.0
    armor: 8.0
    armor-toughness: 4.0
    tier: MYTHICAL
    knockback-resistance: 0.25
    perm-effects:
      NIGHT_VISION: 1.0
    element:
      darkness:
        defense: 50.0
      thunder:
        defense: 25.0
    lore:
      - "§c它们会畏惧你。"
    damage-reduction: 5.0
    physical-damage-reduction: 8.0
    magic-damage-reduction: 20.0
    pve-damage-reduction: 5.0
    enchants:
      smite: 3.0
      protection: 4.0
```

## `UNDEAD_SLAYER_CHESTPLATE` { #undead_slayer_chestplate }

```yaml title="item/armor.yml · UNDEAD_SLAYER_CHESTPLATE"
UNDEAD_SLAYER_CHESTPLATE:
  base:
    material: NETHERITE_CHESTPLATE
    required-level: 80.0
    undead-damage: 15.0
    set: UNDEADSLAYER
    name: "§c亡灵杀手胸甲"
    max-durability: 19800.0
    physical-damage: 5.0
    armor: 11.0
    armor-toughness: 4.0
    tier: MYTHICAL
    knockback-resistance: 0.25
    perm-effects:
      FIRE_RESISTANCE: 1.0
      REGENERATION: 1.0
    element:
      darkness:
        defense: 80.0
      thunder:
        defense: 50.0
    lore:
      - "§c它们会畏惧你。"
    damage-reduction: 10.0
    physical-damage-reduction: 15.0
    magic-damage-reduction: 50.0
    pve-damage-reduction: 10.0
    enchants:
      smite: 3.0
      protection: 4.0
```

## `UNDEAD_SLAYER_LEGGINGS` { #undead_slayer_leggings }

```yaml title="item/armor.yml · UNDEAD_SLAYER_LEGGINGS"
UNDEAD_SLAYER_LEGGINGS:
  base:
    material: NETHERITE_LEGGINGS
    undead-damage: 15.0
    set: UNDEADSLAYER
    name: "§c亡灵杀手护腿"
    max-durability: 18800.0
    physical-damage: 5.0
    armor: 10.0
    armor-toughness: 4.0
    tier: MYTHICAL
    knockback-resistance: 0.25
    perm-effects:
      SPEED: 1.0
    element:
      darkness:
        defense: 60.0
      thunder:
        defense: 30.0
    lore:
      - "§c它们会畏惧你。"
    damage-reduction: 8.0
    physical-damage-reduction: 10.0
    magic-damage-reduction: 30.0
    pve-damage-reduction: 8.0
    enchants:
      smite: 3.0
      protection: 4.0
```

## `UNDEAD_SLAYER_BOOTS` { #undead_slayer_boots }

```yaml title="item/armor.yml · UNDEAD_SLAYER_BOOTS"
UNDEAD_SLAYER_BOOTS:
  base:
    material: NETHERITE_BOOTS
    required-level: 80.0
    undead-damage: 15.0
    set: UNDEADSLAYER
    name: "§c亡灵杀手靴子"
    max-durability: 15500.0
    physical-damage: 5.0
    armor: 8.0
    armor-toughness: 4.0
    tier: MYTHICAL
    knockback-resistance: 0.25
    perm-effects:
      JUMP: 1.0
    element:
      darkness:
        defense: 50.0
      thunder:
        defense: 25.0
    lore:
      - "§c它们会畏惧你。"
    damage-reduction: 5.0
    physical-damage-reduction: 8.0
    magic-damage-reduction: 20.0
    pve-damage-reduction: 5.0
    enchants:
      smite: 3.0
      protection: 4.0
```

## `STEEL_HELMET` { #steel_helmet }

```yaml title="item/armor.yml · STEEL_HELMET"
# 钢铁套装
STEEL_HELMET:
  base:
    material: IRON_HELMET
    block-power:
      base: 6.0
      spread: 0.048
      max-spread: 0.14
    block-rating:
      base: 6.5
      spread: 0.0625
      max-spread: 0.1875
    required-level: 3.0
    name: "&f钢盔"
    armor: 2.5
    lore:
      - "&7比铁头盔略好。"
    tier: COMMON
    knockback-resistance:
      base: 0.02
      spread: 0.11
      max-spread: 0.33
    gem-sockets:
      - Green
    set: STEEL
    crafting:
      shaped:
        '1':
          - MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT
          - MATERIAL.STEEL_INGOT AIR MATERIAL.STEEL_INGOT
          - AIR AIR AIR
        '2':
          - AIR AIR AIR
          - MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT
          - MATERIAL.STEEL_INGOT AIR MATERIAL.STEEL_INGOT
```

## `STEEL_CHESTPLATE` { #steel_chestplate }

```yaml title="item/armor.yml · STEEL_CHESTPLATE"
STEEL_CHESTPLATE:
  base:
    material: IRON_CHESTPLATE
    block-power:
      base: 6.0
      spread: 0.048
      max-spread: 0.15
    block-rating:
      base: 6.5
      spread: 0.0625
      max-spread: 0.1875
    required-level: 3.0
    name: "&f钢胸甲"
    armor: 6.5
    lore:
      - "&7比铁胸甲略好。"
    tier: COMMON
    knockback-resistance:
      base: 0.02
      spread: 0.11
      max-spread: 0.33
    gem-sockets:
      - Blue
    set: STEEL
    crafting:
      shaped:
        '1':
          - MATERIAL.STEEL_INGOT AIR MATERIAL.STEEL_INGOT
          - MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT
          - MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT
```

## `STEEL_LEGGINGS` { #steel_leggings }

```yaml title="item/armor.yml · STEEL_LEGGINGS"
STEEL_LEGGINGS:
  base:
    material: IRON_LEGGINGS
    block-power:
      base: 6.0
      spread: 0.048
      max-spread: 0.14
    block-rating:
      base: 6.5
      spread: 0.0625
      max-spread: 0.1875
    required-level: 3.0
    name: "&f钢护腿"
    armor: 5.5
    lore:
      - "&7比铁护腿略好。"
    tier: COMMON
    knockback-resistance:
      base: 0.02
      spread: 0.11
      max-spread: 0.33
    gem-sockets:
      - Blue
    set: STEEL
    crafting:
      shaped:
        '1':
          - MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT MATERIAL.STEEL_INGOT
          - MATERIAL.STEEL_INGOT AIR MATERIAL.STEEL_INGOT
          - MATERIAL.STEEL_INGOT AIR MATERIAL.STEEL_INGOT
```

## `STEEL_BOOTS` { #steel_boots }

```yaml title="item/armor.yml · STEEL_BOOTS"
STEEL_BOOTS:
  base:
    material: IRON_BOOTS
    block-power:
      base: 6.0
      spread: 0.048
      max-spread: 0.14
    block-rating:
      base: 6.5
      spread: 0.0625
      max-spread: 0.1875
    required-level: 3.0
    name: "&f钢靴"
    armor: 2.5
    lore:
      - "&7比铁靴子略好。"
    tier: COMMON
    knockback-resistance:
      base: 0.02
      spread: 0.11
      max-spread: 0.33
    gem-sockets:
      - Green
    set: STEEL
    crafting:
      shaped:
        '2':
          - AIR AIR AIR
          - MATERIAL.STEEL_INGOT AIR MATERIAL.STEEL_INGOT
          - MATERIAL.STEEL_INGOT AIR MATERIAL.STEEL_INGOT
        '1':
          - MATERIAL.STEEL_INGOT AIR MATERIAL.STEEL_INGOT
          - MATERIAL.STEEL_INGOT AIR MATERIAL.STEEL_INGOT
          - AIR AIR AIR
```

## `ARCANE_HELM` { #arcane_helm }

```yaml title="item/armor.yml · ARCANE_HELM"
# 奥术套装
ARCANE_HELM:
  base:
    material: LEATHER_HELMET
    name: "&5奥术头盔"
    tier: RARE
    required-level: 4.0
    max-mana: 10.0
    dye-color: 100 100 255
    armor: 2.0
    magic-damage: 15.0
    item-particles:
      type: GALAXY
      particle: SPELL_WITCH
    set: ARCANE
```

## `ARCANE_CHESTPLATE` { #arcane_chestplate }

```yaml title="item/armor.yml · ARCANE_CHESTPLATE"
ARCANE_CHESTPLATE:
  base:
    material: LEATHER_CHESTPLATE
    name: "&5奥术上衣"
    tier: RARE
    required-level: 4.0
    max-mana: 10.0
    dye-color: 100 100 255
    armor: 6.0
    magic-damage: 15.0
    ability:
      on-hit:
        type: WITHER
        mode: DAMAGED
        cooldown: 9.0
        amplifier: 2.0
    item-particles:
      type: GALAXY
      particle: SPELL_WITCH
    lore:
      - "&2试图攻击你的敌人"
      - "&2会受到猛烈的凋零效果，"
      - "&2持续一小段时间。"
    set: ARCANE
```

## `ARCANE_LEGGINGS` { #arcane_leggings }

```yaml title="item/armor.yml · ARCANE_LEGGINGS"
ARCANE_LEGGINGS:
  base:
    material: LEATHER_LEGGINGS
    name: "&5奥术护腿"
    tier: RARE
    required-level: 4.0
    max-mana: 10.0
    dye-color: 100 100 255
    armor: 5.0
    magic-damage: 15.0
    item-particles:
      type: GALAXY
      particle: SPELL_WITCH
    gem-sockets:
      - Blue
      - Green
    set: ARCANE
```

## `ARCANE_BOOTS` { #arcane_boots }

```yaml title="item/armor.yml · ARCANE_BOOTS"
ARCANE_BOOTS:
  base:
    material: LEATHER_BOOTS
    name: "&5奥术靴子"
    tier: RARE
    required-level: 4.0
    max-mana: 10.0
    dye-color: 100 100 255
    armor: 2.0
    magic-damage: 15.0
    item-particles:
      type: GALAXY
      particle: SPELL_WITCH
    lore:
      - "&2大幅提高你的"
      - "&2摔落伤害减免。"
    fall-damage-reduction:
      base: 45.0
      spread: 0.033
      max-spread: 0.1
    set: ARCANE
```

## `GINGERBREAD_HELM` { #gingerbread_helm }

```yaml title="item/armor.yml · GINGERBREAD_HELM"
# 姜饼套装
GINGERBREAD_HELM:
  base:
    material: LEATHER_HELMET
    dye-color: 255 150 100
    name: "&c姜饼头盔"
    required-level: 2.0
    lore:
      - "&e于 2018 年圣诞节获得！"
    set: GINGERBREAD
    parry-rating: 5.0
    max-health: 2.0
    armor: 2.0
    item-particles:
      type: OFFSET
      particle: REDSTONE
      color:
        red: 255
        green: 100
        blue: 100
```

## `GINGERBREAD_TUNIC` { #gingerbread_tunic }

```yaml title="item/armor.yml · GINGERBREAD_TUNIC"
GINGERBREAD_TUNIC:
  base:
    material: LEATHER_CHESTPLATE
    dye-color: 255 130 130
    name: "&c姜饼上衣"
    required-level: 2.0
    lore:
      - "&e于 2018 年圣诞节获得！"
    set: GINGERBREAD
    parry-rating: 5.0
    max-health: 2.0
    armor: 6.0
    item-particles:
      type: OFFSET
      particle: REDSTONE
      color:
        red: 255
        green: 100
        blue: 100
```

## `GINGERBREAD_LEGGINGS` { #gingerbread_leggings }

```yaml title="item/armor.yml · GINGERBREAD_LEGGINGS"
GINGERBREAD_LEGGINGS:
  base:
    material: LEATHER_LEGGINGS
    dye-color: 255 140 120
    name: "&c姜饼护腿"
    required-level: 2.0
    lore:
      - "&e于 2018 年圣诞节获得！"
    set: GINGERBREAD
    parry-rating: 5.0
    max-health: 2.0
    armor: 5.0
    item-particles:
      type: OFFSET
      particle: REDSTONE
      color:
        red: 255
        green: 100
        blue: 100
```

## `GINGERBREAD_BOOTS` { #gingerbread_boots }

```yaml title="item/armor.yml · GINGERBREAD_BOOTS"
GINGERBREAD_BOOTS:
  base:
    material: LEATHER_BOOTS
    dye-color: 255 150 150
    name: "&c姜饼靴子"
    required-level: 2.0
    lore:
      - "&e于 2018 年圣诞节获得！"
    set: GINGERBREAD
    parry-rating: 5.0
    max-health: 2.0
    armor: 2.0
    item-particles:
      type: OFFSET
      particle: REDSTONE
      color:
        red: 255
        green: 100
        blue: 100
```

## `SHADOWVEIL` { #shadowveil }

```yaml title="item/armor.yml · SHADOWVEIL"
# 暗影套装
SHADOWVEIL:
  base:
    material: LEATHER_HELMET
    dye-color: 0 0 0
    name: "&c黑暗面纱"
    tier: RARE
    unbreakable: true
    max-durability: 1000.0
    enchants:
      protection: 4
      unbreaking: 3
    hide-enchants: false
    disable-enchanting: true
    disable-repairing: true
    ability:
      ability1:
        type: SHADOW_VEIL
        mode: SHIFT_LEFT_CLICK
        duration: 5.0
        cooldown: 20.0
    lore:
      - "&7&o从基岩深处获得"
    max-health: 10.0
    armor: 3.0
    armor-toughness: 2.0
```

## `SHADOWROBE` { #shadowrobe }

```yaml title="item/armor.yml · SHADOWROBE"
SHADOWROBE:
  base:
    material: LEATHER_CHESTPLATE
    lore:
      - "&7&o从基岩深处获得"
    name: "&c暗影长袍"
    max-durability: 1000.0
    disable-repairing: true
    disable-enchanting: true
    enchants:
      unbreaking: 3
      protection: 4
    tier: RARE
    unbreakable: true
    magic-damage-reduction: 25.0
    armor-toughness: 2.0
    armor: 8.0
    dye-color: 0 0 0
    max-health: 16.0
    ability:
      ability1:
        type: CORRUPT
        mode: DAMAGED
        duration: 4.0
        damage: 12.0
        cooldown: 15.0
        amplifier: 1.0
```

## `SHADOWLEGGINGS` { #shadowleggings }

```yaml title="item/armor.yml · SHADOWLEGGINGS"
SHADOWLEGGINGS:
  base:
    material: LEATHER_LEGGINGS
    lore:
      - "&7&o从基岩深处获得"
    name: "&c暗影护腿"
    enchants:
      unbreaking: 3
      protection: 4
    disable-repairing: true
    disable-enchanting: true
    magic-damage-reduction: 25.0
    unbreakable: true
    tier: RARE
    armor-toughness: 2.0
    armor: 6.0
    max-health: 14.0
    dye-color: 0 0 0
```

## `SHADOWBOOTS` { #shadowboots }

```yaml title="item/armor.yml · SHADOWBOOTS"
SHADOWBOOTS:
  base:
    material: LEATHER_BOOTS
    name: "&c暗影靴子"
    lore:
      - "&7&o从基岩深处获得"
    enchants:
      unbreaking: 3
      protection: 4
    disable-repairing: true
    disable-enchanting: true
    max-durability: 1000.0
    unbreakable: true
    tier: RARE
    fall-damage-reduction: 15.0
    armor-toughness: 2.0
    armor: 3.0
    max-health: 8.0
    movement-speed: 0.01
    dye-color: 0 0 0
```

## `HELMET_OF_THE_SEA` { #helmet_of_the_sea }

```yaml title="item/armor.yml · HELMET_OF_THE_SEA"
# 杂项
HELMET_OF_THE_SEA:
  base:
    material: LEATHER_HELMET
    max-durability: 8000.0
    attack-damage:
      base: 6.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.3
    required-level: 10.0
    weapon-damage:
      base: 10.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.25
    magic-damage:
      base: 10.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.25
    physical-damage:
      base: 15.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.25
    cooldown-reduction:
      base: 15.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.25
    pve-damage:
      base: 15.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.25
    tier: RARE
    dye-color: 120 120 255
    name: "§9海洋头盔"
    hide-dye: true
    element:
      water:
        defense:
          base: 25.0
          scale: 0.0
          spread: 0.2
          max-spread: 0.4
    amphibian: DAMP
    perm-effects:
      NIGHT_VISION: 1.0
      WATER_BREATHING: 1.0
    lore:
      - "§3仅在§9§l水下§3生效。"
      - "§3提供§9夜视 §3和§9水下呼吸§3。"
```

## `MOON_BOOTS` { #moon_boots }

```yaml title="item/armor.yml · MOON_BOOTS"
MOON_BOOTS:
  base:
    material: DIAMOND_BOOTS
    lore:
      - "§b月球靴能让你体验身处月球的感觉！"
      - "§7穿戴时获得§3跳跃提升 II§7。"
      - "§c仅在 \"末地\" 生物群系中生效。"
    max-durability: 2650.0
    name: "§b§l月球靴"
    tier: UNIQUE
    armor-toughness: 1.5
    armor: 3.0
    fall-damage-reduction: 75.0
    perm-effects:
      JUMP: 2.0
    required-biomes:
      - the_end
```

## `CONTROL_DEVICES` { #control_devices }

```yaml title="item/armor.yml · CONTROL_DEVICES"
CONTROL_DEVICES:
  base:
    material: LEATHER_HELMET
    max-durability: 15000.0
    name: "§d§l控制装置"
    dye-color: 255 102 204
    ability: {}
    set: PSYCHIC
    perm-effects:
      DAMAGE_RESISTANCE: 2.0
      SPEED: 2.0
      REGENERATION: 2.0
      FIRE_RESISTANCE: 1.0
      INCREASE_DAMAGE: 2.0
    required-class:
      - Mage
    lore:
      - "§7用来约束你的力量……"
    armor-toughness: 2.0
    armor: 7.0
    tier: MAGICAL
    unbreakable: true
```

## `DEAD_PHARAOH_HELMET` { #dead_pharaoh_helmet }

```yaml title="item/armor.yml · DEAD_PHARAOH_HELMET"
DEAD_PHARAOH_HELMET:
  base:
    material: PLAYER_HEAD
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGU1NWRmOTc5YWI3OTc0OWY4YjU1MWI0MjM5YTQ2OWFhNzY5ZDliNDYwNTBhYWJkOWY2ZDFjZWU1M2VkMzYifX19
      uuid: 852deb36-af4a-412f-ac76-2b06dc123ed2
    name: "&c亡故法老头盔"
    disable-interaction: true
    item-particles:
      type: FIREFLIES
      particle: SMOKE_NORMAL
    fire-damage-reduction: 30.0
    armor: 4.0
    undead-damage: 30.0
    lore:
      - "&7这顶被遗忘的强大头盔"
      - "&7会大幅提升你"
      - "&7对抗亡灵生物的力量。"
    required-level: 9.0
```

## `MOSSY_SKELETON_SKULL` { #mossy_skeleton_skull }

```yaml title="item/armor.yml · MOSSY_SKELETON_SKULL"
MOSSY_SKELETON_SKULL:
  base:
    material: PLAYER_HEAD
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNWE2MzE0ZWFjMzQ0MTZjZTEwYWIyMmMyZTFjNGRjYjQ3MmEzZmViOThkNGUwNGQzZmJiYjg1YTlhNDcxYjE4In19fQ
      uuid: f455a085-3f09-43ac-8be1-175204d1a6ad
    name: "&8苔藓骷髅头颅"
    required-level: 6.0
    armor: 3.5
    knockback-resistance: 0.1
    movement-speed: -0.01
    disable-interaction: true
```

## `SKELETON_CROWN` { #skeleton_crown }

```yaml title="item/armor.yml · SKELETON_CROWN"
SKELETON_CROWN:
  base:
    material: PLAYER_HEAD
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGM3OGQyMTAyZGI3NWYxYjM3NDRhNWU3ZTliYWNjZjg4ZmRhNGNjNDk3OWViYzBhODFiN2Q5ZWI1NzIxYzAifX19
      uuid: ccb901e7-0919-463d-9bdd-ee9acae8e0e2
    name: "&e骷髅王冠"
    required-level: 9.0
    armor: 3.0
    movement-speed: 0.01
    ability:
      ability1:
        type: LIFE_ENDER
        mode: DAMAGED
        damage: 3.0
        cooldown: 9.0
    lore:
      - "&7每隔 9 秒，会朝攻击者召唤一颗"
      - "&c致命陨石&7，"
      - "&7造成 &c4&7 点伤害，并将其短暂"
      - "&7击退。"
    disable-interaction: true
```

## `WYVERN_CAP` { #wyvern_cap }

```yaml title="item/armor.yml · WYVERN_CAP"
WYVERN_CAP:
  base:
    material: GOLDEN_HELMET
    name: "&f飞龙帽"
    required-level: 10.0
    hide-enchants: false
    enchants:
      unbreaking: 9
    armor: 2.5
    fall-damage-reduction: 70.0
    perm-effects:
      JUMP: 2
    lore:
      - "&7提供永久的跳跃提升 II"
    crafting:
      shaped:
        '1':
          - TOME.WYVERN_FEATHER TOME.WYVERN_SOUL TOME.WYVERN_FEATHER
          - TOME.WYVERN_FEATHER AIR TOME.WYVERN_FEATHER
          - AIR AIR AIR
        '2':
          - AIR AIR AIR
          - TOME.WYVERN_FEATHER TOME.WYVERN_SOUL TOME.WYVERN_FEATHER
          - TOME.WYVERN_FEATHER AIR TOME.WYVERN_FEATHER
```

## `TRAVEL_BOOTS` { #travel_boots }

```yaml title="item/armor.yml · TRAVEL_BOOTS"
TRAVEL_BOOTS:
  base:
    material: LEATHER_BOOTS
    name: "§f旅行靴"
    movement-speed: 0.005
    dye-color: 187 118 126
    will-break: true
    max-durability: 100.0
    armor: 2.0
    fall-damage-reduction: 5.0
```

## `GARGOYLE_CHESTPLATE` { #gargoyle_chestplate }

```yaml title="item/armor.yml · GARGOYLE_CHESTPLATE"
GARGOYLE_CHESTPLATE:
  base:
    material: IRON_CHESTPLATE
    scale: 1.0
    name: "石像鬼胸甲"
    trim-material: netherite
    trim-pattern: silence
    hide-armor-trim: true
    max-health: 10.0
    armor: 6.0
    movement-speed: -0.02
```

## `SHRINKING_BOOTS` { #shrinking_boots }

```yaml title="item/armor.yml · SHRINKING_BOOTS"
SHRINKING_BOOTS:
  base:
    material: GOLDEN_BOOTS
    trim-material: redstone
    trim-pattern: silence
    hide-armor-trim: true
    scale: -0.5
    movement-speed: 0.02
    required-class:
      - Mage
    skill-damage: -50.0
    max-health: -10.0
    name: "缩小之靴"
    lore:
      - "&7&o愿这件物品帮助你"
      - "&7&o穿过最狭窄的通道……"
```

## `MYTHRIL_CHAINMAIL` { #mythril_chainmail }

```yaml title="item/armor.yml · MYTHRIL_CHAINMAIL"
MYTHRIL_CHAINMAIL:
  base:
    material: CHAINMAIL_CHESTPLATE
    name: "&b--] &f秘银锁子甲 &b[--"
    block-power:
      base: 60.0
      spread: 0.048
      max-spread: 0.14
    block-rating:
      base: 12.5
      spread: 0.06
      max-spread: 0.17
    armor: 5
    element:
      ice:
        defense: 8.0
      earth:
        defense: 6.4
    gem-sockets:
      - Red
      - Blue
    required-level: 4.0
    tier: UNCOMMON
```

## `CURSED_WITHER_SKULL` { #cursed_wither_skull }

```yaml title="item/armor.yml · CURSED_WITHER_SKULL"
CURSED_WITHER_SKULL:
  base:
    material: WITHER_SKELETON_SKULL
    name: "&7诅咒凋灵头颅"
    required-level: 30.0
    tier: UNIQUE
    gem-sockets:
      - Red
      - Blue
    armor: 3.0
    armor-toughness: 2.0
    perm-effects:
      ABSORPTION: 1
    lore:
      - "&7提供永久的 &62"
      - "&6颗心 &7伤害吸收护盾。"
    durability: 1.0
    element:
      thunder:
        defense: 67.4
      fire:
        defense: 53.4
    crafting:
      shaped:
        '1':
          - BONE BONE BONE
          - BONE MATERIAL.UNIQUE_WEAPON_ESSENCE BONE
          - BONE BONE BONE
```

## `LARGE_MOTHRON_WINGS` { #large_mothron_wings }

```yaml title="item/armor.yml · LARGE_MOTHRON_WINGS"
LARGE_MOTHRON_WINGS:
  base:
    material: ELYTRA
    max-durability: 5.0
    two-handed: false
    name: "&e大型 Mothron 翅膀"
    tier: RARE
    gravity: -0.02
    unbreakable: true
    movement-speed: -0.03
    will-break: false
```

## `FIREPROOF_JACKET` { #fireproof_jacket }

```yaml title="item/armor.yml · FIREPROOF_JACKET"
FIREPROOF_JACKET:
  base:
    material: LEATHER_CHESTPLATE
    burning-time: -0.9
    name: "防火夹克"
    enchants:
      unbreaking: 4.0
    trim-pattern: vex
    trim-material: redstone
```

## `BEE_WINGS` { #bee_wings }

```yaml title="item/armor.yml · BEE_WINGS"
BEE_WINGS:
  base:
    material: ELYTRA
    name: "蜜蜂翅膀"
    movement-speed: 0.02
    fall-damage-multiplier: -0.5
    jump-strength: 0.2
    gravity: -0.04
    safe-fall-distance: 7.0
```

## `SOULWALKER` { #soulwalker }

```yaml title="item/armor.yml · SOULWALKER"
SOULWALKER:
  base:
    material: GOLDEN_BOOTS
    name: "灵魂行者"
    movement-efficiency: 0.9
    armor: 3.0
    step-height: 0.4
    lore:
      - "&7消除灵魂沙对移动的阻碍。"
```

## `DIVING_BOOTS` { #diving_boots }

```yaml title="item/armor.yml · DIVING_BOOTS"
DIVING_BOOTS:
  base:
    material: GOLDEN_BOOTS
    name: "潜水靴"
    trim-material: copper
    trim-pattern: wild
    water-movement-efficiency: 1.0
    gravity: 2.0
    step-height: 0.5
```
