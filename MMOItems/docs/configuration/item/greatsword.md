---
title: item/greatsword.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/greatsword.yml
source_version: 6.10.1-SNAPSHOT
---

# item/greatsword.yml

文件：`item/greatsword.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `HARDENED_STEEL_CLAYMORE` { #hardened_steel_claymore }

```yaml title="item/greatsword.yml · HARDENED_STEEL_CLAYMORE"
HARDENED_STEEL_CLAYMORE:
  base:
    material: IRON_SWORD
    name: "&f淬硬钢制双刃大剑"
    required-level: 13.0
    tier: RARE
    required-class:
      - Warrior
      - Paladin
    attack-damage:
      base: 5.5
      spread: 0.03
      max-spread: 0.08
    attack-speed:
      base: 1.3
      spread: 0.02
      max-spread: 0.07
    critical-strike-chance: 12.0
    critical-strike-power: 24.0
    two-handed: true
    unbreakable: true
    enchants:
      sharpness: 4
      knockback: 2
    gem-sockets:
      - Red
      - Blue
    perm-effects:
      FAST_DIGGING: 3
    ability:
      right-click:
        type: CIRCULAR_SLASH
        mode: RIGHT_CLICK
        damage: 7.2
        cooldown: 19.0
      on-hit:
        type: SHOCK
        mode: ATTACK
        duration: 1.3
        cooldown: 25.0
    max-durability: 1000.0
```

## `CANDY_CANE_SWORD` { #candy_cane_sword }

```yaml title="item/greatsword.yml · CANDY_CANE_SWORD"
CANDY_CANE_SWORD:
  base:
    material: WOODEN_SWORD
    name: "&f拐&c&f&c&f杖&c&f&c糖&f&c&f&c剑&f&c"
    attack-damage: 8.0
    unbreakable: true
    attack-speed:
      base: 1.7
      spread: 0.02
      max-spread: 0.06
    lore:
      - "&7这把剑蕴含着圣诞精神。"
      - "&7攻击怪物即可释放它！"
      - ''
      - "&e于 2018 年圣诞节获得！"
    critical-strike-chance: 20.0
    critical-strike-power: 60.0
    ability:
      on-hit:
        type: DEATH_MARK
        mode: ATTACK
        cooldown: 10.0
```

## `MOLTEN_BLADE` { #molten_blade }

```yaml title="item/greatsword.yml · MOLTEN_BLADE"
MOLTEN_BLADE:
  base:
    material: GOLDEN_SWORD
    enchants:
      knockback: 2
    name: "&c熔融之刃"
    attack-speed: 1.3
    attack-damage: 11.0
    crafting:
      shaped:
        '1':
          - AIR MATERIAL.FIRE_ESSENCE AIR
          - MATERIAL.FIRE_ESSENCE MATERIAL.FIRE_ESSENCE MATERIAL.FIRE_ESSENCE
          - AIR BLAZE_ROD AIR
    ability:
      ability1:
        type: MAGMA_FISSURE
        mode: ATTACK
        cooldown: 13.0
    lore:
      - "&7每隔 13s，你的下一次近战"
      - "&7攻击会召唤毁灭性的"
      - "&c岩浆裂隙&7，朝着"
      - "&7目标疾冲，使其&c着火&7，并"
      - "&7在命中时造成&c伤害&7。"
    magic-damage: 30.0
    unbreakable: true
    two-handed: true
```

## `TWO_HANDED_STEEL_SWORD` { #two_handed_steel_sword }

```yaml title="item/greatsword.yml · TWO_HANDED_STEEL_SWORD"
TWO_HANDED_STEEL_SWORD:
  base:
    material: IRON_SWORD
    name: "&f双手钢剑"
    enchants:
      sharpness: 4
      knockback: 1
      unbreaking: 6
    two-handed: true
    unbreakable: true
    attack-damage:
      base: 8.5
      spread: 0.05
      max-spread: 0.15
    attack-speed:
      base: 0.9
      spread: 0.03
      max-spread: 0.01
    critical-strike-chance:
      base: 8.5
      spread: 0.05
      max-spread: 0.15
    critical-strike-power:
      base: 190.0
      spread: 0.03
      max-spread: 0.1
    required-level: 2.0
    element:
      ice:
        damage: 7.0
    gem-sockets:
      - Blue
      - Blue
    tier: UNCOMMON
    ability:
      right-click:
        type: CIRCULAR_SLASH
        mode: RIGHT_CLICK
        cooldown: 8.0
        damage: 4.0
    lore:
      - "&7右键点击可&c&n重击&7附近的"
      - "&7敌人，造成 &c4&7 点伤害。"
    hide-enchants: true
```

## `EARTHLY_GREATSWORD` { #earthly_greatsword }

```yaml title="item/greatsword.yml · EARTHLY_GREATSWORD"
EARTHLY_GREATSWORD:
  base:
    material: STONE_SWORD
    max-durability: 8400.0
    required-level: 30.0
    attack-damage:
      base: 32.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    critical-strike-chance:
      base: 10.0
      scale: 0.1
      spread: 0.2
    critical-strike-power:
      base: 60.0
      scale: 0.1
      spread: 0.2
    required-class:
      - Warrior
    tier: EPIC
    name: "§2大地巨剑"
    gem-sockets:
      - Green
    element:
      earth:
        damage: 50.0
    attack-speed: 1.45
    perm-effects:
      SLOW: 1.0
    two-handed: true
    lore:
      - "§7手持时获得§c缓慢 I§7。"
      - "§7需要§c双手§7持握。"
    ability:
      ability1:
        type: CIRCULAR_SLASH
        damage: 15.0
        cooldown: 3.0
        knockback: 2.0
        radius: 4.0
        mode: RIGHT_CLICK
```
