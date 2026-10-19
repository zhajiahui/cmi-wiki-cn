---
title: item/tome.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/tome.yml
source_version: 6.10.1-SNAPSHOT
---

# item/tome.yml

文件：`item/tome.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `AMPLIFICATION_TOME` { #amplification_tome }

```yaml title="item/tome.yml · AMPLIFICATION_TOME"
AMPLIFICATION_TOME:
  base:
    material: ENCHANTED_BOOK
    name: "&9增幅之书"
    required-level: 9.0
    lore:
    - "&7它散发着强烈的魔法气息。"
    - "&7手持时可&5大幅增强"
    - "&7你的魔法力量。"
    magic-damage:
      base: 85.0
      spread: 0.02
      max-spread: 0.06
```

## `WYVERN_FEATHER` { #wyvern_feather }

```yaml title="item/tome.yml · WYVERN_FEATHER"
WYVERN_FEATHER:
  base:
    material: FEATHER
    disable-crafting: true
    name: "&f飞龙羽毛"
    fall-damage-reduction: 65.0
```

## `WYVERN_SOUL` { #wyvern_soul }

```yaml title="item/tome.yml · WYVERN_SOUL"
WYVERN_SOUL:
  base:
    material: ENDER_EYE
    name: "&f飞龙之魂"
    disable-interaction: true
    disable-crafting: true
    enchants:
      unbreaking: 1
    perm-effects:
      LEVITATION: 2
    hide-enchants: true
```

## `TOME_OF_ACCURACY` { #tome_of_accuracy }

```yaml title="item/tome.yml · TOME_OF_ACCURACY"
TOME_OF_ACCURACY:
  base:
    material: ENCHANTED_BOOK
    disable-repairing: true
    name: "&e精准之书"
    critical-strike-power:
      base: 27.5
      spread: 0.03
      max-spread: 0.08
    critical-strike-chance:
      base: 7.5
      spread: 0.08
      max-spread: 0.25
    lore:
    - "&7提高你的暴击伤害。"
```

## `NAUGHTY_SPELL_BOOK` { #naughty_spell_book }

```yaml title="item/tome.yml · NAUGHTY_SPELL_BOOK"
NAUGHTY_SPELL_BOOK:
  base:
    material: ENCHANTED_BOOK
    disable-repairing: true
    name: "&8顽皮法术书"
    required-level: 20.0
    ability:
      right-click:
        type: CURSED_BEAM
        mode: RIGHT_CLICK
        cooldown: 30.0
        damage: 6.0
    lore:
    - "&7右键点击可施放&5诅咒光束&7。"
    - "&7这枚魔法投射物会对第一个命中的敌人造成 &57"
    - "&5点伤害 &7。"
```

## `CELESTIAL_TOME` { #celestial_tome }

```yaml title="item/tome.yml · CELESTIAL_TOME"
CELESTIAL_TOME:
  base:
    material: BOOK
    enchants:
      luck_of_the_sea: 1.0
    disable-interaction: true
    lore:
      - "§f§o由天使亲自赐予！"
      - "§b众神不会让别人将它"
      - "§b从你手中夺走。死亡时不会掉落。"
    name: "§b§l天界之书"
    tier: EPIC
    ability:
      ability1:
        type: HOLY_MISSILE
        mode: RIGHT_CLICK
        duration: 5.0
        damage: 9.0
        cooldown: 8.0
    disable-death-drop: true
```

## `OMNIELEMENTAL_TOME` { #omnielemental_tome }

```yaml title="item/tome.yml · OMNIELEMENTAL_TOME"
OMNIELEMENTAL_TOME:
  base:
    material: BOOK
    name: "§c§l全§6§l§e§l§a§l元§2§l§3§l§9§l素§b§l§f§l§e§l魔§a§l§6§l§c§l法§6§l§e§l§a§l书§2§l"
    required-level: 30.0
    tier: VERY_RARE
    magic-damage:
      base: 30.0
      scale: 0.15
      spread: 0.1
      max-spread: 0.3
    element:
      wind:
        damage: 25.0
      earth:
        damage: 25.0
      thunder:
        damage: 25.0
      water:
        damage: 25.0
    lore:
      - "§7混沌是万物创造的源头。"
    ability:
      ability1:
        type: SWIFTNESS
        duration: 6.0
        amplifier: 1.0
        cooldown: 10.0
        mode: SHIFT_RIGHT_CLICK
      ability2:
        type: SHOCKWAVE
        cooldown: 10.0
        knock-up: 2.0
        length: 5.0
        mode: SHIFT_RIGHT_CLICK
      ability3:
        type: SMITE
        mode: SHIFT_RIGHT_CLICK
        damage: 8.0
        cooldown: 10.0
      ability4:
        type: HEAL
        mode: SHIFT_RIGHT_CLICK
        heal: 10.0
        cooldown: 10.0
```
