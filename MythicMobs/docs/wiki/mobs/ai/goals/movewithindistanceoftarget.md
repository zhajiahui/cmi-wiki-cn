---
title: Move Within Distance Of Target
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveWithinDistanceOfTarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Move Within Distance Of Target

# 移动到距目标一定距离的位置 {#move-within-distance-of-target}

## 说明 {#description}

向目标移动，直到进入特定距离内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 速度修饰值。 | 1 |
| minrange | minrange, range, r, distance, d | 与目标实体的最小距离。 | 10.0 |
| maxrange | maxrange, maxr | 与目标实体的最大距离。 | 32.0 |

## 示例 {#examples}

```yaml
  AIGoalSelectors:
  - clear
  - MoveWithinDistanceOfTarget{s=2;minrange=3;maxrange=6}
```

## 别名 {#aliases}

- moveWithin
