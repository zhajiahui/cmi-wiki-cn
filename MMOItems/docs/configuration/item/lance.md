---
title: item/lance.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/lance.yml
source_version: 6.10.1-SNAPSHOT
---

# item/lance.yml

文件：`item/lance.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `FIRE_GREATLANCE` { #fire_greatlance }

```yaml title="item/lance.yml · FIRE_GREATLANCE"
FIRE_GREATLANCE:
  base:
    material: BLAZE_ROD
    required-level: 30.0
    attack-damage:
      base: 14.5
      spread: 0.01
      max-spread: 0.03
    attack-speed: 1.1
    name: "&f火焰巨骑枪"
    ability:
      on-hit:
        type: LIFE_ENDER
        mode: ATTACK
        damage: 10.0
        cooldown: 30.0
    lore:
    - "&7战斗中每隔 40s，会施放"
    - "&7一颗毁灭性的&6火焰彗星"
    - "&7在落地时消灭"
    - "&7附近的一切生命。"
    item-particles:
      type: DOUBLE_RINGS
      particle: FLAME
      radius: 1.3
      rotation-speed: 0.4
    disable-crafting: true
    two-handed: true
```
