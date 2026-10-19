---
title: Fleeconditional
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleeconditional
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Fleeconditional {#fleeconditional}

## 说明 {#description}

****此功能仅限 Premium****  
让生物根据给定条件逃跑。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 其他生物与该生物自身的距离。 | 4 |
| speed | s | 逃离的速度。 | 1.2 |
| safespeed | ss | 到达安全距离（50 格）后逃离的速度。 | 1 |
| targetconditions | fleeconditions, conditions, cond, c | 生物逃离某个实体时，该实体必须满足的条件。 |  |
| mobconditions | mconditions, mcond, mc | 生物逃离时，自身必须满足的条件。 |  |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleeConditional{distance=5;speed=2;safespeed=2;conditions=[ - inlineofsight true ]}
```

## 别名 {#aliases}

- fleeif
