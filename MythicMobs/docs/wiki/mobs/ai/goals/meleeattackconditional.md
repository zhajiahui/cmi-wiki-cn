---
title: Melee Attack Conditional
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/meleeAttackConditional
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Melee Attack Conditional

# 条件近战攻击 {#melee-attack-conditional}

## 说明 {#description}

让生物接近目标并进行近战攻击，但仅在目标满足给定条件时生效。与 [MoveTowardsTargetConditional](movetowardstargetconditional.md) 及其 `minrange` 属性搭配，可以让生物保持距离，直到目标靠近。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speedmodifier | speed, s | 执行此动作期间生物的速度修饰值。 | 1 |
| followUnseen | fu | 即使目标不在视野中，是否仍然跟随。 | false |
| targetconditions | conditions, cond, c | 攻击开始和持续进行时，目标实体必须满足的条件。 |  |
| mobconditions | mconditions, mcond, mc | 攻击开始和持续进行时，生物自身必须满足的条件。 |  |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
  - 0 clear
  - 1 meleeAttackConditional{targetConditions=[ - distance{d=<3} ]}
  - 2 MoveTowardsTargetConditional{s=1;minrange=10;maxrange=80;targetConditions=[ - isPlayer true ]}
```

## 别名 {#aliases}

- meleeAttackCond
