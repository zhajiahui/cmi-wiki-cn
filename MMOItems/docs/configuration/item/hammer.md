---
title: item/hammer.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/hammer.yml
source_version: 6.10.1-SNAPSHOT
---

# item/hammer.yml

文件：`item/hammer.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `SANTAMMER` { #santammer }

```yaml title="item/hammer.yml · SANTAMMER"
SANTAMMER:
  base:
    material: IRON_AXE
    item-particles:
      particle: REDSTONE
      type: HELIX
      color:
        red: 50
        green: 255
        blue: 50
    name: "&7圣&f&7&f诞&f&7之&f&7锤&f"
    attack-damage: 9.7
    attack-speed: 0.6
    enchants:
      unbreaking: 3
    required-level: 15.0
    critical-strike-power: 10.0
    ability:
      on-hit:
        type: STUN
        mode: ATTACK
        cooldown: 15.0
    lore:
    - "&e于 2018 年圣诞节获得！"
```

## `THOR_HAMMER` { #thor_hammer }

```yaml title="item/hammer.yml · THOR_HAMMER"
THOR_HAMMER:
  base:
    material: IRON_AXE
    max-durability: 80000.0
    name: "§b§l雷神之锤"
    lore:
      - "§b驾驭风暴的力量！"
      - "§e攻击时播放自定义音效！"
      - "§a死亡时不会掉落！"
    element:
      thunder:
        damage: 150.0
    magic-damage:
      base: 15.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    attack-speed: 1.4
    required-level: 60.0
    attack-damage:
      base: 80.0
      scale: 0.15
      spread: 0.1
      max-spread: 0.2
    tier: MYTHICAL
    stamina-cost: 15.0
    mana-cost: 10.0
    blunt-power: 6.0
    blunt-rating: 75.0
    gem-sockets:
      - Thunder
    sounds:
      on-attack:
        sound: entity.lightning_bolt.thunder
        volume: 2.0
        pitch: 0.2
    enchants:
      sharpness: 3.0
      fire_aspect: 3.0
    ability:
      ability1:
        type: SMITE
        mode: RIGHT_CLICK
        damage: 100.0
        cooldown: 12.0
    additional-experience: 15.0
    unbreakable: true
    disable-death-drop: true
```

## `HEAVY_HAMMER` { #heavy_hammer }

```yaml title="item/hammer.yml · HEAVY_HAMMER"
HEAVY_HAMMER:
  base:
    material: IRON_AXE
    name: "§7§l重锤"
    max-durability: 3650.0
    lore:
      - "§f一把非常沉重的锤子。"
      - "§7你几乎无法移动，但"
      - "§7这一切都值得！"
    perm-effects:
      SLOW: 4.0
    attack-damage:
      base: 35.0
      scale: 0.15
      spread: 0.1
      max-spread: 0.2
    critical-strike-chance:
      base: 10.0
      scale: 0.15
      spread: 0.1
      max-spread: 0.2
    critical-strike-power:
      base: 20.0
      scale: 0.15
      spread: 0.1
      max-spread: 0.2
    required-level: 10.0
    required-class:
      - Warrior
    stamina-cost: 4.0
    blunt-power: 5.0
    blunt-rating: 85.0
    tier: RARE
```
