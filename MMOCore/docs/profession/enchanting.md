---
title: 附魔
source: https://docs.phoenixdevt.fr/mmocore/profession/enchanting
source_snapshot: '2026-10-19'
---

# 附魔 {#🧙‍♂️-enchanting}

附魔是MMOCore中副职业的一种特定类型。它允许玩家通过在原版附魔台上附魔物品来获得经验和等级的附魔副职业。附魔物品时获得的经验直接取决于你的物品获得的新附魔，以及新附魔的等级。

## 迷人的体验 {#enchanting-experience}

有些附魔比其他附魔更难获得，因此应该比其他附魔提供更多的经验。每个附魔都有一定数量的经验值**每个附魔等级**，每当玩家滚动该附魔时，都会将其提供给他。因此，获得的经验是每个附魔获得的所有经验值的加权总和，并按附魔等级加权。

## 配置 {#configuration}

```yml
base-enchant-exp:
    fire_protection: 10
    sharpness: 10
    flame: 10
    aqua_affinity: 10
    punch: 10
    loyalty: 10
    depth_strider: 10
    vanishing_curse: 10
    unbreaking: 10
    knockback: 10
    luck_of_the_sea: 10
    binding_curse: 10
    fortune: 30
    protection: 10
    efficiency: 40
    mending: 10
    frost_walker: 10
    lure: 10
    looting: 10
    piercing: 10
    blast_protection: 10
    smite: 10
    multishot: 10
    fire_aspect: 10
    channeling: 10
    sweeping: 10
    thorns: 10
    bane_of_arthropods: 10
    respiration: 10
    riptide: 10
    silk_touch: 50
    quick_charge: 10
    projectile_protection: 10
    impaling: 10
    feather_falling: 10
    power: 10
    infinity: 10
```

## 示例 {#example}

玩家为钻石剑附魔*效率 IV*、*坚不可摧 III* 和 *丝触*。因此给予玩家的经验是：

```
efficiency exp = 4 * 40 = 160
unbreaking exp = 3 * 10 = 30
silk touch exp = 1 * 50 = 50

total exp      = sum of exp from all enchants
               = 240 exp
```

---

原文：[🧙‍♂️ Enchanting](https://docs.phoenixdevt.fr/mmocore/profession/enchanting) · 原文归档：2026-10-19
