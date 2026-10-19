---
title: item/dagger.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/dagger.yml
source_version: 6.10.1-SNAPSHOT
---

# item/dagger.yml

文件：`item/dagger.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `STEEL_DAGGER` { #steel_dagger }

```yaml title="item/dagger.yml · STEEL_DAGGER"
STEEL_DAGGER:
  base:
    material: IRON_SWORD
    name: "&f钢匕首"
    attack-damage:
      base: 4.75
      spread: 0.017
      max-spread: 0.05
    attack-speed:
      base: 1.9
      spread: 0.017
      max-spread: 0.05
    pvp-damage:
      base: 17.5
      spread: 0.042
      max-spread: 0.13
    movement-speed: 0.02
    critical-strike-chance:
      base: 55.0
      spread: 0.028
      max-spread: 0.08
    gem-sockets:
    - Uncolored
    - Blue
    ability:
      right-click:
        type: THRUST
        mode: RIGHT_CLICK
        damage: 4.3
        cooldown: 5.0
        stamina: 20.0
    tier: COMMON
    required-level: 5.0
    required-class:
    - Rogue
    - Archer
```

## `DRACULA_DAGGER` { #dracula_dagger }

```yaml title="item/dagger.yml · DRACULA_DAGGER"
DRACULA_DAGGER:
  base:
    material: IRON_SWORD
    tier: RARE
    required-level: 15.0
    attack-damage:
      base: 7.5
      spread: 0.02
      max-spread: 0.06
    name: "&f德古拉的匕首"
    attack-speed:
      base: 1.65
      spread: 0.01
      max-spread: 0.03
    critical-strike-chance: 15.0
    fall-damage-reduction: 43.0
    gem-sockets:
    - Uncolored
    - Red
    ability:
      on-hit:
        type: VAMPIRISM
        mode: ATTACK
        drain: 3.0
        cooldown: 4.0
    lore:
    - "&7每隔 4sec，击中"
    - "&7敌人会&c吸取&7其生命值，"
    - "&7为你恢复 &c1.5 颗心&7。"
    enchants:
      unbreaking: 10
    hide-enchants: true
```

## `VERY_SHARP_DAGGER` { #very_sharp_dagger }

```yaml title="item/dagger.yml · VERY_SHARP_DAGGER"
VERY_SHARP_DAGGER:
  base:
    material: IRON_SWORD
    tier: RARE
    max-durability: 1800.0
    will-break: true
    name: "§7§l§o极锋利的匕首"
    displayed-type: "§c锋利匕首"
    required-level: 12.0
    required-class:
      - Assassin
    attack-damage:
      base: 10.0
      scale: 0.13
      spread: 0.1
      max-spread: 0.23
    attack-speed: 1.9
    critical-strike-chance:
      base: 30.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.23
    critical-strike-power:
      base: 80.0
      scale: 0.09
      spread: 0.08
      max-spread: 0.2
    weapon-damage:
      base: 15.0
      scale: 0.2
      spread: 0.2
      max-spread: 0.3
    movement-speed: 0.02
    gem-sockets:
      - White
    upgrade:
      template: weapon-default
    physical-damage:
      base: 30.0
      scale: 0.1
      spread: 0.3
      max-spread: 0.6
    lore:
      - "§f§o经过漫长的精炼，"
      - "§f§o变得极其锋利。"
```

## `POISONOUS_DAGGER` { #poisonous_dagger }

```yaml title="item/dagger.yml · POISONOUS_DAGGER"
POISONOUS_DAGGER:
  base:
    material: WOODEN_SWORD
    name: "§2§l§o剧毒匕首"
    lore:
      - "§7谁知道是什么感染了它……"
    max-durability: 4500.0
    attack-damage:
      base: 22.0
      scale: 0.15
      spread: 0.15
      max-spread: 0.25
    attack-speed: 1.75
    critical-strike-chance:
      base: 25.0
      scale: 0.05
      spread: 0.08
      max-spread: 0.13
    critical-strike-power:
      base: 40.0
      scale: 0.09
      spread: 0.11
      max-spread: 0.18
    pvp-damage:
      base: 15.0
      scale: 0.03
      spread: 0.15
      max-spread: 0.2
    weapon-damage:
      base: 10.0
      spread: 0.1
      max-spread: 0.2
    tier: LEGENDARY
    gem-sockets:
      - Green
      - Green
    magic-damage:
      base: 12.0
      spread: 0.1
      max-spread: 0.2
    required-level: 32.0
    upgrade:
      template: weapon-default
    break-downgrade: true
    element:
      earth:
        damage:
          base: 30.0
          scale: 0.0
          spread: 0.1
          max-spread: 0.2
    ability:
      ability1:
        type: POISON
        mode: ATTACK
        duration: 4.0
        stamina: 0.0
        cooldown: 6.0
        amplifier: 2.0
```

## `SNEAKY_DAGGER` { #sneaky_dagger }

```yaml title="item/dagger.yml · SNEAKY_DAGGER"
SNEAKY_DAGGER:
  base:
    material: STONE_SWORD
    name: "§8§l潜行匕首"
    lore:
      - "&7&o用它潜行到目标背后！"
    tier: UNCOMMON
    attack-damage: 11.0
    attack-speed: 0.9
    critical-strike-chance:
      base: 9.0
      scale: 0.1
      spread: 0.01
      max-spread: 0.05
    critical-strike-power:
      base: 20.0
      scale: 0.1
      spread: 0.01
      max-spread: 0.05
    required-level: 5.0
    ability:
      ability1:
        type: BACKSTAB
        mode: ATTACK
        cooldown: 3.0
        extra: 50.0
    sneaking-speed: 2.0
```
