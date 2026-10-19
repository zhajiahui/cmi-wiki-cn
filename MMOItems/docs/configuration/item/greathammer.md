---
title: item/greathammer.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/greathammer.yml
source_version: 6.10.1-SNAPSHOT
---

# item/greathammer.yml

文件：`item/greathammer.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `UNRELIABLE_HAMMER` { #unreliable_hammer }

```yaml title="item/greathammer.yml · UNRELIABLE_HAMMER"
UNRELIABLE_HAMMER:
  base:
    material: DIAMOND_AXE
    name: "§3不可靠的巨锤"
    required-level: 10.0
    tier: UNCOMMON
    lore:
      - "§7这把锤子的属性随机性很大，"
      - "§7可能有§c极低的耐久度§7，也可能"
      - "§7有§c极高的耐久度§7！耐久归零时它会§c损坏§7，"
      - "§7一旦归零便会如此。"
      - "§7如果它已经升级，则会§c降级§7，"
      - "§7以降级代替损坏。"
    max-durability:
      base: 150.0
      spread: 0.8
      max-spread: 0.9
    attack-damage:
      base: 14.0
      scale: 0.08
      spread: 0.1
      max-spread: 0.2
    attack-speed: 1.4
    critical-strike-chance:
      base: 12.0
      spread: 0.05
      max-spread: 0.09
    critical-strike-power:
      base: 10.0
      spread: 0.05
      max-spread: 0.09
    blunt-power: 3.0
    blunt-rating: 30.0
    will-break: true
    break-downgrade: true
    durability-bar: true
```
