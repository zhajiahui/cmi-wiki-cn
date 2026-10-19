---
title: item/whip.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/whip.yml
source_version: 6.10.1-SNAPSHOT
---

# item/whip.yml

文件：`item/whip.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `WIND_WHIP` { #wind_whip }

```yaml title="item/whip.yml · WIND_WHIP"
WIND_WHIP:
  base:
    material: LEAD
    name: "ยง7风之鞭"
    lore:
      - "ยง7想象一根鞭子，再让它隐形。"
      - "ยง8这很荒唐，但它就是风之鞭。"
    attack-damage:
      base: 11.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    attack-speed: 1.7
    element:
      wind:
        damage: 90.0
    tier: RARE
    required-level: 10.0
    critical-strike-chance:
      base: 10.0
      spread: 0.1
      max-spread: 0.2
    critical-strike-power:
      base: 25.0
      scale: 0.1
      spread: 0.1
      max-spread: 0.2
    range: 16.0
    weapon-damage: 10.0
    crafting:
      shaped:
        '1':
          input:
            - v white_wool - 1.0..|v diamond - 1.0..|v string - 1.0..
            - v stick - 1.0..|v string - 1.0..|v AIR 0 1..
            - v AIR 0 1..|v string - 1.0..|v AIR 0 1..
```
