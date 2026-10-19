---
title: Crossbow Attack Conditional
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/crossbowAttackConditional
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Crossbow Attack Conditional

# 条件弩箭攻击 {#crossbow-attack-conditional}

## 说明 {#description}

作用与 [crossbowAttack](crossbowattack.md) 相似，但只有目标和生物都满足给定条件时，生物才会射击。条件不再满足时，生物会停止射击，但保留目标。只有猪灵和掠夺者可以使用。

## 属性 {#attributes}

接受 [crossbowAttack](crossbowattack.md) 的所有属性，并额外支持：

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| targetconditions | conditions, cond, c | 攻击开始和持续进行时，目标必须满足的条件。 |  |
| mobconditions | mconditions, mcond, mc | 攻击开始和持续进行时，生物自身必须满足的条件。 |  |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: PILLAGER
  Equipment:
  - crossbow HAND
  AIGoalSelectors:
  - 0 clear
  - 1 crossbowAttackConditional{attackradius=16;targetConditions=[ - isPlayer true ]}
```

## 别名 {#aliases}

- crossbowAttackCond
