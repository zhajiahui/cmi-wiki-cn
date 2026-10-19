---
title: item/greatstaff.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/greatstaff.yml
source_version: 6.10.1-SNAPSHOT
---

# item/greatstaff.yml

文件：`item/greatstaff.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `STIFF_GREATSTAFF` { #stiff_greatstaff }

```yaml title="item/greatstaff.yml · STIFF_GREATSTAFF"
STIFF_GREATSTAFF:
  base:
    material: STICK
    name: "&f坚硬巨杖"
    attack-damage:
      base: 11.0
      spread: 0.03
      max-spread: 0.08
    required-level: 6.0
    attack-speed: 0.9
    ability:
      on-hit:
        type: STUN
        mode: ATTACK
        cooldown: 15.0
    lore:
    - "&7沉重得足以在命中时&c击晕&7敌人。"
    disable-crafting: true
    disable-smelting: true
    block-rating: 5.0
    blunt-rating: 75.0
    dodge-rating: -30.0
    tier: COMMON
```
