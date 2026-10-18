---
title: 玩家修正器
source: https://docs.phoenixdevt.fr/mythiclib/misc/player-modifiers
source_snapshot: '2026-10-19'
---

# 玩家修正器 {#📌-player-modifiers}

> **警告**
>
> 此功能尚不可用。将来将用于MMOCore/副职业经验牌桌、MMOItems套装奖金、MMOCore技能树等。

## 概览 {#overview}

玩家修改器可以是任何类型的被动行为，可以修改你的玩家以使其更强或更弱。属性修正器、技能、永久药水效果均被视为玩家修饰符，并且可以使用物品、全部物品套装奖金、MMOCore队伍、MMOCore授予玩家玩家职业...

|玩家修改器 |描述 |标识符 |
| --- | --- | --- |
| 属性修正器 | 修改玩家属性值 | `stat` |
| 基础属性修改器 | 修改MMOCore基础属性 | `attribute` |
| 技能 | 为玩家提供一些可触发的技能 | `skill` |
| 药水效果 | 像 Speed II 这样的永久药水效果 | `potion` |
| 粒子效果 | 永久粒子效果 | `particle` |

配置MMOItems或MMOCore时，有时会要求你在特定场景中定义玩家修饰符，例如在MMOItems中创建物品套装时，以及定义在佩戴同一组中的3物品时为玩家提供哪些修饰符。

## 属性修正器 {#stat-modifiers}

当应用于玩家时，属性修正器会使玩家属性的值增加一定量。它可以是平坦的属性修正器(+10Atk Dmg) 或乘法修饰符 (+10%Atk Dmg)，其按初始玩家的属性值缩放。

```yml
modifierId:
    type: stat # This indicates the modifier is a stat modifier
    stat: ATTACK_DAMAGE
    value: 10
    multiplicative: false
    key: mmocoreParty
```

## 技能 {#skills}

技能是玩家修饰符的特殊类型。阅读 [此 wiki 页面](../skills/intro.md)，了解有关 MMO 插件中的技能的更多信息。

```yml
modifierId:
    type: item_skill # This indicates the modifier is an item skill
    skill: FIREBOLT
    trigger: RIGHT_CLICK    
    modifiers:
        damage: 10
        mana: 3
```

---

原文：[📌 Player Modifiers](https://docs.phoenixdevt.fr/mythiclib/misc/player-modifiers) · 原文归档：2026-10-19
