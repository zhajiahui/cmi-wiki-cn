---
title: item/spear.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/spear.yml
source_version: 6.10.1-SNAPSHOT
---

# item/spear.yml

文件：`item/spear.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `SHARP_SPEAR` { #sharp_spear }

```yaml title="item/spear.yml · SHARP_SPEAR"
SHARP_SPEAR:
  base:
    material: TRIDENT
    name: "§7锋利长矛"
    lore:
      - "§7一支为近身作战打造的矛。"
    critical-strike-chance:
      base: 6.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    critical-strike-power:
      base: 15.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    required-level: 5.0
    tier: UNCOMMON
    attack-damage:
      base: 9.0
      scale: 0.1
      spread: 0.05
      max-spread: 0.1
    attack-speed: 1.7
    ability:
      ability1:
        type: WEAKEN_TARGET
        mode: ATTACK
        duration: 2.0
        cooldown: 0.5
        extra-damage: 25.0
    gem-sockets:
      - Uncolored
    upgrade:
      reference: universal
    stamina-cost: 4.0
```

## `WARRIOR_SPEAR` { #warrior_spear }

```yaml title="item/spear.yml · WARRIOR_SPEAR"
WARRIOR_SPEAR:
  base:
    material: TRIDENT
    required-level: 20.0
    tier: EPIC
    projectile-damage: 1000.0
    attack-damage: 2.0
    attack-speed: 1.5
    critical-strike-chance:
      base: 5.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    critical-strike-power:
      base: 20.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.2
    lore:
      - "§7投掷时造成§c极高伤害§7！"
    enchants:
      loyalty: 3.0
    unbreakable: true
    gem-sockets:
      - Red
      - Red
    movement-speed: -0.02
    name: "§6§l战士之矛"
```
