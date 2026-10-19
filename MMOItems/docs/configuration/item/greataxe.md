---
title: item/greataxe.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/greataxe.yml
source_version: 6.10.1-SNAPSHOT
---

# item/greataxe.yml

文件：`item/greataxe.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `BARBARIAN_AXE` { #barbarian_axe }

```yaml title="item/greataxe.yml · BARBARIAN_AXE"
BARBARIAN_AXE:
  base:
    material: NETHERITE_AXE
    name: "§c§l野蛮人巨斧"
    attack-damage:
      base: 42.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    attack-speed: 0.9
    pvp-damage: 25.0
    weapon-damage:
      base: 80.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    required-level: 70.0
    required-class:
      - Warrior
    critical-strike-chance:
      base: 30.0
      spread: 0.1
      max-spread: 0.2
    critical-strike-power:
      base: 45.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    tier: LEGENDARY
    knockback-resistance: 1.0
    ability:
      ability1:
        type: VAMPIRISM
        mode: ATTACK
        drain: 10.0
        cooldown: 0.2
      ability2:
        type: OVERLOAD
        mode: RIGHT_CLICK
        damage: 30.0
        cooldown: 8.0
        radius: 8.0
    gem-sockets:
      - Red
      - Red
    physical-damage: 30.0
    lore:
      - "§7是时候§c狂怒§7了！"
    disable-interaction: true
    max-durability: 19800.0
```
