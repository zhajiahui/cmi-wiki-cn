---
title: item/crossbow.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/crossbow.yml
source_version: 6.10.1-SNAPSHOT
---

# item/crossbow.yml

文件：`item/crossbow.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `MEDIEVAL_CROSSBOW` { #medieval_crossbow }

```yaml title="item/crossbow.yml · MEDIEVAL_CROSSBOW"
MEDIEVAL_CROSSBOW:
  base:
    material: WOODEN_PICKAXE
    name: "§6§l中世纪弩"
    lore:
      - "§6仿佛回到旧日时光。"
      - "§e为了更逼真，它还能使目标中毒，"
      - "§e并发出不同的声音！"
    tier: UNCOMMON
    weapon-damage:
      base: 15.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    attack-damage:
      base: 9.0
      scale: 0.1
      spread: 0.05
      max-spread: 0.1
    arrow-velocity: 2.0
    arrow-potion-effects:
      POISON:
        duration: 10.0
        amplifier: 1
    projectile-damage:
      base: 20.0
      scale: 0.05
      spread: 0.05
      max-spread: 0.2
    sounds:
      on-right-click:
        sound: item.crossbow.hit
        volume: 2.0
        pitch: 0.0
```

## `HANDGUN` { #handgun }

```yaml title="item/crossbow.yml · HANDGUN"
HANDGUN:
  base:
    material: IRON_HORSE_ARMOR
    name: "§7手枪"
    attack-damage: 30.0
    required-biomes:
      - plains
    lore:
      - "§c出于安全考虑，这把枪"
      - "§c只能在§3平原§c使用。"
    attack-speed: 1.4
    arrow-velocity: 4.0
    required-level: 20.0
    weapon-damage:
      base: 15.0
      scale: 0.06
      spread: 0.08
      max-spread: 0.15
    gem-sockets:
      - Red
      - Red
    max-durability: 2650.0
    tier: RARE
```
