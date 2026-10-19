---
title: item/thrusting_sword.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/thrusting_sword.yml
source_version: 6.10.1-SNAPSHOT
---

# item/thrusting_sword.yml

文件：`item/thrusting_sword.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `SKILLED_SWORD` { #skilled_sword }

```yaml title="item/thrusting_sword.yml · SKILLED_SWORD"
SKILLED_SWORD:
  base:
    material: GOLDEN_SWORD
    name: "§f高手之剑"
    tier: EPIC
    dodge-rating: 15.0
    parry-rating: 40.0
    parry-cooldown-reduction: 30.0
    dodge-cooldown-reduction: 20.0
    cooldown-reduction: 20.0
    attack-damage: 17.0
    attack-speed: 1.65
    critical-strike-chance: 70.0
    critical-strike-power:
      base: 50.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    lore:
      - "§6仅供大师使用。"
    required-dexterity: 14.0
    required-level: 14.0
    ability:
      ability1:
        type: THRUST
        mode: RIGHT_CLICK
        damage: 15.0
        cooldown: 4.0
        stamina: 2.0
```
