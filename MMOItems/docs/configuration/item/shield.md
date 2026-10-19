---
title: item/shield.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/shield.yml
source_version: 6.10.1-SNAPSHOT
---

# item/shield.yml

文件：`item/shield.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `PALADIN_SHIELD` { #paladin_shield }

```yaml title="item/shield.yml · PALADIN_SHIELD"
PALADIN_SHIELD:
  base:
    material: SHIELD
    name: "§e§l太阳之盾"
    tier: MAGICAL
    two-handed: false
    armor: 6.0
    armor-toughness: 3.0
    unbreakable: true
    block-power: 50.0
    block-rating:
      base: 20.0
      scale: 0.02
      spread: 0.09
      max-spread: 0.17
    perm-effects:
      SLOW: 3
    gem-sockets:
      - Yellow
      - Yellow
    required-level: 25.0
    shield-pattern:
      color: YELLOW
      '0':
        pattern: CURLY_BORDER
        color: ORANGE
      '1':
        pattern: STRIPE_MIDDLE
        color: YELLOW
    attack-damage:
      base: 6.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    attack-speed:
      base: 1.4
      spread: 0.06
      max-spread: 0.14
    block-cooldown-reduction:
      base: 10.0
      scale: 0.02
      spread: 0.09
      max-spread: 0.17
```

## `MAGICAL_SHIELD` { #magical_shield }

```yaml title="item/shield.yml · MAGICAL_SHIELD"
MAGICAL_SHIELD:
  base:
    material: SHIELD
    required-level: 5.0
    tier: MAGICAL
    perm-effects:
      SLOW: 4
      DAMAGE_RESISTANCE: 4
    gem-sockets:
      - Red
      - Red
    shield-pattern:
      color: WHITE
      '0':
        pattern: STRAIGHT_CROSS
        color: YELLOW
      '1':
        pattern: FLOWER
        color: ORANGE
      '2':
        pattern: BORDER
        color: YELLOW
    name: "&f魔法盾"
    lore:
      - "&7一面简易盾牌，"
      - "&7用于承载你的宝石。"
    block-rating: 5.0
    block-power:
      base: 6.0
      spread: 0.05
      max-spread: 0.14
```

## `ABSORBING_SHIELD` { #absorbing_shield }

```yaml title="item/shield.yml · ABSORBING_SHIELD"
ABSORBING_SHIELD:
  base:
    material: SHIELD
    required-level: 15.0
    shield-pattern:
      color: BLUE
    name: "&9吸收之盾"
    unbreakable: true
    damage-reduction:
      base: 55.0
      spread: 0.03
      max-spread: 0.08
    movement-speed: -0.03
    two-handed: true
    disable-smelting: false
    disable-crafting: true
```

## `OBSIDIAN_SHIELD` { #obsidian_shield }

```yaml title="item/shield.yml · OBSIDIAN_SHIELD"
OBSIDIAN_SHIELD:
  base:
    material: SHIELD
    name: "§8黑曜石盾"
    lore:
      - "§c这面盾牌甚至比"
      - "§c钻石还坚固。"
    crafting:
      shaped:
        '1':
          input:
            - v obsidian - 1.0..|v diamond - 1.0..|v obsidian - 1.0..
            - v obsidian - 1.0..|v obsidian - 1.0..|v obsidian - 1.0..
            - v AIR 0 1..|v obsidian - 1.0..|v AIR 0 1..
    attack-damage:
      base: 6.0
      scale: 0.2
      spread: 0.1
      max-spread: 0.18
    block-rating:
      base: 20.0
      scale: 0.15
      spread: 0.11
      max-spread: 0.19
    block-power: 100.0
    tier: UNCOMMON
    physical-damage-reduction:
      base: 20.0
      scale: 0.05
      spread: 0.2
      max-spread: 0.3
    defense:
      base: 10.0
      spread: 0.1
      max-spread: 0.2
    shield-pattern:
      color: BLACK
    handworn: true
```

## `SUPREME_SHIELD` { #supreme_shield }

```yaml title="item/shield.yml · SUPREME_SHIELD"
SUPREME_SHIELD:
  base:
    material: SHIELD
    tier: LEGENDARY
    block-power: 100.0
    block-rating:
      base: 60.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    attack-damage:
      base: 25.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    required-class:
      - Warrior
    name: "§9§l§o至尊之盾"
    lore:
      - "§7所有§e盾牌§7中最强大的一面。"
    movement-speed: -0.03
    shield-pattern:
      color: PURPLE
    element:
      earth:
        defense: 25.0
      lightness:
        defense: 25.0
      wind:
        defense: 25.0
      fire:
        defense: 25.0
    pve-damage-reduction:
      base: 30.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.3
    armor-toughness: 2.0
    armor: 8.0
    projectile-damage-reduction:
      base: 100.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.3
```
