---
title: item/halberd.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/halberd.yml
source_version: 6.10.1-SNAPSHOT
---

# item/halberd.yml

文件：`item/halberd.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `DOUBLE_OR_NOTHING` { #double_or_nothing }

```yaml title="item/halberd.yml · DOUBLE_OR_NOTHING"
DOUBLE_OR_NOTHING:
  base:
    material: IRON_AXE
    lore:
    - "&7&o威力强大，却难以"
    - "&7&o操控的武器……"
    - "&7&o务必小心！"
    critical-strike-power:
      base: 850.0
      spread: 0.02
      max-spread: 0.06
    critical-strike-chance:
      base: 50.0
      spread: 0.02
      max-spread: 0.04
    attack-damage:
      base: 1.45
      spread: 0.01
      max-spread: 0.03
    attack-speed:
      base: 1.05
      spread: 0.02
      max-spread: 0.05
    required-level: 10.0
    enchants:
      unbreaking: 5
    hide-enchants: true
    name: "&b&l&o\"要么翻倍，要么归零\""
    gem-sockets:
    - Red
    - Uncolored
    - Green
    - Blue
    ability:
      on-hit:
        type: SLOW
        mode: ATTACK
        cooldown: 30.0
        duration: 4.0
        amplifier: 2.0
    pvp-damage: 12.0
```

## `BRAVE_HALBERD` { #brave_halberd }

```yaml title="item/halberd.yml · BRAVE_HALBERD"
BRAVE_HALBERD:
  base:
    material: IRON_AXE
    name: "§e勇者之戟"
    lore:
      - "§7§o没人知道他的真名……"
      - "§7§o但他是如此§e§o勇敢§7§o！"
    attack-damage:
      base: 14.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    critical-strike-chance:
      base: 20.0
      spread: 0.1
      max-spread: 0.2
    critical-strike-power:
      base: 35.0
      spread: 0.1
      max-spread: 0.2
    weapon-damage: 25.0
    tier: RARE
    attack-speed: 1.55
    pvp-damage: 25.0
    max-durability: 6540.0
    gem-sockets:
      - Cyan
    ability:
      ability1:
        type: HEAVY_CHARGE
        mode: RIGHT_CLICK
        damage: 20.0
        cooldown: 10.0
        knockback: 2.5
        stamina: 5.0
    crafting:
      shaped:
        '1':
          input:
            - m material steel_ingot 1.0..|v iron_block - 1.0..|m material steel_ingot
              1.0..
            - m material steel_ingot 1.0..|v stick - 1.0..|m material steel_ingot 1.0..
            - v AIR 0 1..|v stick - 1.0..|v AIR 0 1..
```
