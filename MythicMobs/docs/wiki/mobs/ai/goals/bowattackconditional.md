---
title: Bow Attack Conditional
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/bowAttackConditional
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Bow Attack Conditional

# 条件弓箭攻击 {#bow-attack-conditional}

## 说明 {#description}

作用与 [bowattack](bowattack.md) 相似，但只有目标和生物都满足给定条件时，生物才会射击。条件不再满足时，生物会停止射击，但保留目标。

## 属性 {#attributes}

接受 [bowattack](bowattack.md) 的所有属性，并额外支持：

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| targetconditions | conditions, cond, c | 攻击开始和持续进行时，目标必须满足的条件。 |  |
| mobconditions | mconditions, mcond, mc | 攻击开始和持续进行时，生物自身必须满足的条件。 |  |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: SKELETON
  AIGoalSelectors:
  - 0 clear
  - 1 bowAttackConditional{targetConditions=[ - isPlayer true ];mobConditions=[ - health{h=>10} ]}
```

## 别名 {#aliases}

- bowAttackCond
- skeletonBowAttackConditional
- bowshootConditional
- bowmasterConditional
