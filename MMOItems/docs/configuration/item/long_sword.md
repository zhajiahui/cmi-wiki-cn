---
title: item/long_sword.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/long_sword.yml
source_version: 6.10.1-SNAPSHOT
---

# item/long_sword.yml

文件：`item/long_sword.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `DUAL_LONGSWORD` { #dual_longsword }

```yaml title="item/long_sword.yml · DUAL_LONGSWORD"
DUAL_LONGSWORD:
  base:
    material: WOODEN_SWORD
    max-durability: 8400.0
    name: "§f§l§o双持长§8§l§o剑"
    lore:
      - "§e愿光明拯救你！"
      - "§8也愿黑暗吞噬你……"
    tier: EPIC
    required-level: 45.0
    required-class:
      - Paladin
    critical-strike-chance: 10.0
    critical-strike-power:
      base: 15.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    attack-damage:
      base: 24.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    attack-speed: 1.5
    weapon-damage: 10.0
    stamina-cost: 2.0
    parry-rating: 30.0
    parry-cooldown-reduction: 10.0
    armor: 2.0
    gem-sockets:
      - White
      - Black
    perm-effects:
      SPEED: 1.0
      SLOW: 1.0
    ability:
      ability1:
        type: HOLY_MISSILE
        mode: SHIFT_RIGHT_CLICK
        duration: 4.0
        cooldown: 8.0
        damage: 25.0
      ability2:
        type: CURSED_BEAM
        mode: SHIFT_LEFT_CLICK
        duration: 4.0
        cooldown: 8.0
        damage: 25.0
```
