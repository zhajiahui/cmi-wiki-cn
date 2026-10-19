---
title: item/katana.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/katana.yml
source_version: 6.10.1-SNAPSHOT
---

# item/katana.yml

文件：`item/katana.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `FLOWING_KATANA` { #flowing_katana }

```yaml title="item/katana.yml · FLOWING_KATANA"
FLOWING_KATANA:
  base:
    material: IRON_SWORD
    max-durability: 2400.0
    tier: RARE
    element:
      earth:
        defense:
          base: 15.0
          scale: 0.0
          spread: 0.02
          max-spread: 0.1
      water:
        defense:
          base: 30.0
          scale: 0.0
          spread: 0.05
          max-spread: 0.12
    gem-sockets:
      - White
      - White
    name: "§3§l流动武士刀"
    lore:
      - "§7§o用水做的武器？真荒唐！"
    attack-damage:
      base: 9.0
      scale: 0.08
      spread: 0.03
      max-spread: 0.1
    attack-speed: 1.6
    critical-strike-chance:
      base: 20.0
      spread: 0.04
      max-spread: 0.11
    critical-strike-power:
      base: 39.0
      spread: 0.03
      max-spread: 0.7
    parry-rating:
      base: 12.0
      spread: 0.04
      max-spread: 0.085
    parry-cooldown-reduction:
      base: 7.0
      spread: 0.04
      max-spread: 0.085
    weapon-damage:
      base: 8.0
      spread: 0.04
      max-spread: 0.06
    required-level: 4.0
    movement-speed: 0.035
```

## `MASTER_KATANA` { #master_katana }

```yaml title="item/katana.yml · MASTER_KATANA"
MASTER_KATANA:
  base:
    material: IRON_SWORD
    name: "§f§l§o大师武士刀"
    required-dexterity: 20.0
    required-level: 20.0
    tier: EPIC
    attack-damage:
      base: 20.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    critical-strike-chance: 30.0
    critical-strike-power:
      base: 30.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    weapon-damage:
      base: 10.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    pvp-damage: 25.0
    max-durability: 9000.0
    gem-sockets:
      - Cyan
      - Cyan
    disable-enchanting: true
    disable-repairing: true
    lore:
      - "§7一把§b完美的§7武士刀，若你的"
      - "§7敏捷不足，就无法使用这把需要§b敏捷的武士刀。"
      - "§7它不会§b损坏§7，也无法§b附魔§7。"
    durability-bar: true
    unbreakable: true
    enchants:
      sharpness: 3.0
      sweeping: 3.0
```
