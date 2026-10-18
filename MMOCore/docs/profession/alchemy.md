---
title: 炼金
source: https://docs.phoenixdevt.fr/mmocore/profession/alchemy
source_snapshot: '2026-10-19'
---

# 炼金 {#🍹-alchemy}

默认炼金术副职业允许玩家在酿造任何类型的药水时获得经验：飞溅药水、滞留药水、升级的原版药水。这是 alchemy副职业配置文件中最重要的部分。

```yml
exp-sources:
- 'brewpotion{effect=SPEED}'

# When brewing a potion, players earn Alchemy experience.
# Experience earned depends on the effect you give to your
# potion, if you upgrade/extend its duration, etc.
alchemy-experience:

    special:
        
        # When brewing a potion into a splash potion,
        # only 40% of the base EXP is earned.
        splash: 40
        
        # When brewing a potion into a splash potion,
        # only 40% of the base EXP is earned.
        lingering: 40
        
        # When extending a pot duration,
        # only 40% of base EXP is earned.
        extend: 40
        
        # When upgrading a potion level,
        # only 40% of base EXP is earned.
        upgrade: 40

    # Base EXP of potions
    effects:
        
        # Water bottles
        AWKWARD: 5
        MUNDANE: 5
        THICK: 5
        
        # Potion effects
        NIGHT_VISION: 10
        INVISIBILITY: 10
        JUMP: 10
        FIRE_RESISTANCE: 10
        SPEED: 10
        SLOWNESS: 10
    
        #....
```

正如你所看到的，唯一的炼金源经验是酿造（酿造台）。你还可以指定玩家必须酿造什么类型的药水才能使用`brewitem`**经验源** 在该特定副职业中获得经验。如果你希望玩家在仅酿造速度和再生药水时获得经验，请使用`'brewpotion{effect=SPEED,REGEN}'`（使用逗号分隔药水类型）。

`alchemy-experience`配置部分规定了玩家从酿造任何药水中可以获得多少经验。玩家从酿造中获得的经验**直接取决于药水效果类型**：稀有药水i.e需要更稀有成分的药水，例如恶魂之泪（在闪闪发光的瓜上）应该会提供更多的炼金术经验。

另一方面，普通、浓稠和笨拙的药水应该会提供较少的经验，因为玩家必须在酿造任何其他药水之前酿造它们。

## 基础经验值 {#base-exp}

每种药水类型都有一个基础 EXP，玩家在酿造台中酿造该类型的1、2或3药水（同时）时会获得该 EXP，例如玩家将通过酿造抗火药水获得15EXP和20EXP酿造跳跃药水*（使用默认设置）*。

## 炼金术 EXP 修改器 {#alchemy-exp-modifiers}

使用**红石延长药水效果的持续时间**时，玩家会获得该药水效果基础经验的 X%。例如，延长跳跃药水的效果时，会获得 `40% * 20 = 5EXP`。此百分比通过 `special.extend` 设置。使用**荧石提升药水效果等级**时，也会获得该效果基础经验的 X%，对应设置为 `special.upgrade`。

当使用**火药酿造飞溅药水**或**龙息酿造滞留药水**时，玩家将获得X%的药水效果基础经验（百分比可使用`special.splash`和`special.lingering`进行配置）。

---

原文：[🍹 Alchemy](https://docs.phoenixdevt.fr/mmocore/profession/alchemy) · 原文归档：2026-10-19
