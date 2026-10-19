---
title: item/miscellaneous.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/miscellaneous.yml
source_version: 6.10.1-SNAPSHOT
---

# item/miscellaneous.yml

文件：`item/miscellaneous.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `GOLD_COIN` { #gold_coin }

```yaml title="item/miscellaneous.yml · GOLD_COIN"
GOLD_COIN:
  base:
    material: GOLD_NUGGET
    name: "&f金币"
    lore:
    - "&7一枚闪亮的金币。"
    enchants:
      unbreaking: 1
    hide-enchants: true
    disable-crafting: true
```

## `HUMAN_SOUL` { #human_soul }

```yaml title="item/miscellaneous.yml · HUMAN_SOUL"
HUMAN_SOUL:
  base:
    material: PHANTOM_MEMBRANE
    disable-repairing: false
    disable-enchanting: false
    hide-enchants: true
    enchants:
      unbreaking: 1
    name: "&6人类灵魂"
    disable-crafting: true
    lore:
    - "&7&o你听见敌人的尖叫……"
    - "&7&o也可能是朋友的。"
```

## `MYSTERIOUS_PEARL` { #mysterious_pearl }

```yaml title="item/miscellaneous.yml · MYSTERIOUS_PEARL"
MYSTERIOUS_PEARL:
  base:
    material: ENDER_PEARL
    enchants:
      luck_of_the_sea: 1.0
    hide-enchants: true
    name: "§9神秘珍珠"
    lore:
      - "§7§o谁知道它藏着什么秘密……"
      - "§3无法堆叠。"
    unstackable: true
    tier: RARE
```

## `LEVEL_1_KEY` { #level_1_key }

```yaml title="item/miscellaneous.yml · LEVEL_1_KEY"
LEVEL_1_KEY:
  base:
    material: SHEARS
    name: "§3§n等级 1§3 钥匙"
    lore:
      - "§7获得 §cmmoitems.key§7 权限，条件是"
      - "§7手持此物品。"
    granted-permissions:
      - mmoitems.key
    tier: UNIQUE
    unstackable: true
    disable-interaction: true
    disable-repairing: true
    disable-enchanting: true
    disable-smelting: true
    disable-smithing: true
    unbreakable: true
```
