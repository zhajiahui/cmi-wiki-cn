---
title: item/bow.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/bow.yml
source_version: 6.10.1-SNAPSHOT
---

# item/bow.yml

文件：`item/bow.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `COMPOSITE_BOW` { #composite_bow }

```yaml title="item/bow.yml · COMPOSITE_BOW"
COMPOSITE_BOW:
  base:
    material: BOW
    name: "&f复合弓"
    critical-strike-chance: 30.0
    attack-damage:
      base: 7
      scale: 0.3
      spread: 0.1
      max-spread: 0.3
    required-level:
      base: 0
      scale: 1
  modifiers:
    swiftness:
      weight: 3
    heavy:
      chance: 0.05
      weight: 3
    impending-doom:
      weight: 5
```

## `HELL_BOW` { #hell_bow }

```yaml title="item/bow.yml · HELL_BOW"
HELL_BOW:
  base:
    material: BOW
    enchants:
      unbreaking: 10
      infinity: 1
    hide-enchants: true
    unbreakable: true
    tier: RARE
    attack-damage:
      base: 11.5
      spread: 0.038
      max-spread: 0.12
    critical-strike-chance:
      base: 35.0
      spread: 0.14
      max-spread: 0.42
    critical-strike-power:
      base: 12.5
      spread: 0.06
      max-spread: 0.17
    element:
      fire:
        damage: 14.0
    ability:
      right-click:
        type: FIREBOLT
        mode: SHIFT_LEFT_CLICK
        cooldown: 20.0
        damage: 4.0
        ignite: 6.0
    gem-sockets:
      - Red
      - Red
      - Green
    name: "&c地狱之弓"
    pve-damage:
      base: 25.0
      spread: 0.06
      max-spread: 0.17
    arrow-particles:
      amount: 5
      offset: 0.05
      particle: FLAME
      speed: 0.08
```

## `MARKING_BOW` { #marking_bow }

```yaml title="item/bow.yml · MARKING_BOW"
MARKING_BOW:
  base:
    material: BOW
    enchants:
      unbreaking: 3
    name: "&8标记之弓"
    attack-damage: 7.0
    arrow-particles:
      particle: SMOKE_NORMAL
      amount: 3
      speed: 0.05
    ability:
      ability1:
        type: WEAKEN_TARGET
        mode: ATTACK
        extra-damage: 60.0
    dodge-rating: 10.0
    damage-reduction: -5.0
    required-level: 10.0
    lore:
      - "&7射中实体即可将其&c标记&7。"
      - "&7下一次对该实体的攻击"
      - "&7会额外造成 &c60%&7 伤害。"
```

## `NETHERITE_BOW` { #netherite_bow }

```yaml title="item/bow.yml · NETHERITE_BOW"
NETHERITE_BOW:
  base:
    material: BOW
    max-durability: 8500.0
    name: "§c§l暗黑下界合金弓"
    lore:
      - "§6§o\"金属做的弓根本没法用。\""
      - "§8§o可这只是电子游戏！"
    attack-damage: 25.0
    arrow-velocity: 1.5
    pvp-damage:
      base: 25.0
      scale: 0.1
      spread: 0.2
    projectile-damage:
      base: 10.0
      scale: 0.08
      spread: 0.14
    tier: RARE
    ability:
      ability1:
        type: WITHER
        mode: ATTACK
        duration: 6.0
        cooldown: 5.0
        amplifier: 1.0
    element:
      darkness:
        damage:
          base: 60.0
          scale: 0.2
          spread: 0.35
          max-spread: 0.0
      fire:
        damage:
          base: 20.0
          scale: 0.05
          spread: 0.1
          max-spread: 0.0
    gem-sockets:
      - Nether
      - Nether
    crafting:
      smithing:
        '1':
          input: v bow - 1.0..|m material dark_netherite 1.0..
    required-level: 14.0
```

## `PRECISION_BOW` { #precision_bow }

```yaml title="item/bow.yml · PRECISION_BOW"
PRECISION_BOW:
  base:
    material: BOW
    name: "§7§l精准之弓"
    lore:
      - "§7精准之弓的射程远得多。"
    critical-strike-chance:
      base: 15.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    critical-strike-power:
      base: 40.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    required-level: 5.0
    arrow-velocity: 2.0
    attack-damage:
      base: 16.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    projectile-damage:
      base: 5.0
      scale: 0.2
      spread: 0.2
      max-spread: 0.4
    tier: RARE
    max-durability: 2400.0
    required-class:
      - Archer
```
