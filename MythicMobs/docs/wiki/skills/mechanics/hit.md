---
title: Hit
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/hit
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Hit {#hit}

## 说明 {#description}

模拟施法者的一次物理攻击，计算时会考虑物品（包括附魔）、近战属性、属性修正和药水效果。
继承 [Damage](damage.md) 机制的全部属性。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| multiplier | m | 要造成的伤害百分比。 | 1 |
| forcedDamage | fd, forced | 设置此属性后，指定值将作为造成的固定伤害量，不考虑属性修饰符及其他类似修饰符。 |  |
| triggerSkills | ts | 伤害机制是否也可以触发与 `onAttack` 相关的触发器。 | true |
| scaleByAttackCooldown | sbac | 是否根据武器的攻击冷却缩放伤害。 | false |

> 该机制继承了[伤害](damage.md)机制的所有属性
>

> > - `amount`属性被忽略
> > - `triggerSkills` 属性**默认为** `true`。
> > - `damagecause` 属性**固定为** `ENTITY_ATTACK`。
> > - `tags` 属性将始终具有 `melee` 标签。

## 示例 {#examples}

此示例将使生物在受到攻击时对其目标造成 150% 其配置的近战伤害。无视铠甲。在这种情况下，它会造成总计 15 伤害，因为该生物的近战伤害为 10。

```yaml
HitMob:
  Type: Zombie
  Damage: 10
  Skills:
    - hit{m=1.5;ia=true} @target ~onDamaged
```

## 别名 {#aliases}

- physicalDamage
- meleeHit
