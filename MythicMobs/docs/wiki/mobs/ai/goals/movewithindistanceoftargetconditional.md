---
title: Move Within Distance Of Target Conditional
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveWithinDistanceOfTargetConditional
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Move Within Distance Of Target Conditional

# 满足条件时移动到距目标一定距离的位置 {#move-within-distance-of-target-conditional}

## 说明 {#description}

作用与 [MoveWithinDistanceOfTarget](movewithindistanceoftarget.md) 相似，但只有目标和生物都满足给定条件时，生物才会移动。

## 属性 {#attributes}

接受 [MoveWithinDistanceOfTarget](movewithindistanceoftarget.md) 的所有属性，并额外支持：

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| targetconditions | conditions, cond, c | 生物开始并持续移动时，目标必须满足的条件。 |  |
| mobconditions | mconditions, mcond, mc | 生物开始并持续移动时，自身必须满足的条件。 |  |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
  - 0 clear
  - 1 moveWithinDistanceOfTargetConditional{s=1;minrange=4;maxrange=24;targetConditions=[ - isPlayer true ]}
```

## 别名 {#aliases}

- moveWithinConditional
- moveWithinDistanceOfTargetCond
- moveWithinCond
