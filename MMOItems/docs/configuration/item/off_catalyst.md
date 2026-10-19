---
title: item/off_catalyst.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/off_catalyst.yml
source_version: 6.10.1-SNAPSHOT
---

# item/off_catalyst.yml

文件：`item/off_catalyst.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `SCOPE` { #scope }

```yaml title="item/off_catalyst.yml · SCOPE"
SCOPE:
  base:
    material: DIAMOND
    name: "ยง7精准瞄准镜"
    lore:
      - "ยง3将它握在副手，"
      - "ยง3可提高远程伤害！"
    critical-strike-power:
      base: 10.0
      scale: 0.05
      spread: 0.1
      max-spread: 0.4
    projectile-damage:
      base: 30.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.3
    tier: RARE
    required-level: 10.0
    pve-damage:
      base: 10.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.3
    pvp-damage:
      base: 10.0
      scale: 0.1
      spread: 0.2
      max-spread: 0.3
```

## `QUICKCASTER_CATALYST` { #quickcaster_catalyst }

```yaml title="item/off_catalyst.yml · QUICKCASTER_CATALYST"
QUICKCASTER_CATALYST:
  base:
    material: PRISMARINE_CRYSTALS
    name: "§b§l§o速咏者触媒"
    lore:
      - "§d对新手法师很有用。"
    handworn: true
    magic-damage: 10.0
    cooldown-reduction: 25.0
    skill-damage: 15.0
    max-mana: 5.0
    mana-regeneration: 1.0
    required-class:
      - Mage
    required-level: 5.0
    tier: RARE
```

## `CHARM_OF_LEVITATION` { #charm_of_levitation }

```yaml title="item/off_catalyst.yml · CHARM_OF_LEVITATION"
CHARM_OF_LEVITATION:
  base:
    material: IRON_NUGGET
    enchants:
      luck_of_the_sea: 1.0
    hide-enchants: true
    name: "§9漂浮护符"
    handworn: true
    lore:
      - "§b人人都需要短暂飞行一下！"
      - "§9不过你大概是为了粒子效果才拿它的！"
      - "§c显示为“护符”。需要握在副手。"
      - "§a增加 +10 Stellium！"
    ability:
      ability1:
        type: MAGICAL_PATH
        mode: RIGHT_CLICK
        duration: 8.0
        mana: 10.0
        cooldown: 15.0
    item-particles:
      type: GALAXY
      particle: END_ROD
    displayed-type: "护符"
    disable-crafting: true
    max-stellium: 10.0
    tier: RARE
    unstackable: true
```
