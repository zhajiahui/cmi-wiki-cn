---
title: Move Towards Target Conditional
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveTowardsTargetConditional
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Move Towards Target Conditional

# 满足条件时向目标移动 {#move-towards-target-conditional}

## 说明 {#description}

寻路前往满足某些条件的实体。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 速度修饰值。 | 1 |
| minrange | minr, mr | 与目标实体的最小距离。生物进入此距离范围后停止移动。 | 0 |
| maxrange | range, r | 与目标实体的最大距离。 | 32.0 |
| targetconditions | conditions, cond, c | 目标实体必须满足的条件。 |  |
| mobconditions | mconditions, mcond, mc | 生物自身必须满足的条件。 |  |

## 示例 {#examples}

```yaml
  AIGoalSelectors:
  - clear
  - MoveTowardsTargetConditional{s=2;maxrange=6;targetConditions=[
    - isPlayer true
    ]}
```

## 别名 {#aliases}

- moveTowardsTargetCond
