---
title: item/gauntlet.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/gauntlet.yml
source_version: 6.10.1-SNAPSHOT
---

# item/gauntlet.yml

文件：`item/gauntlet.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `FIGHTING_GAUNTLETS` { #fighting_gauntlets }

```yaml title="item/gauntlet.yml · FIGHTING_GAUNTLETS"
FIGHTING_GAUNTLETS:
  base:
    material: IRON_SHOVEL
    lore:
      - "§7厌倦了近身格斗时"
      - "§7打断自己的骨头？"
      - "§e这就是你的解决办法！"
    name: "§e格斗拳套"
    attack-damage:
      base: 3.0
      scale: 0.15
      spread: 0.05
      max-spread: 0.1
    blunt-power: 2.0
    blunt-rating: 25.0
    pve-damage:
      base: 15.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.12
    pvp-damage:
      base: 20.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.12
    tier: RARE
    required-level: 15.0
    critical-strike-chance:
      base: 10.0
      spread: 0.1
      max-spread: 0.5
    physical-damage:
      base: 10.0
      scale: 0.06
      spread: 0.1
      max-spread: 0.2
```
