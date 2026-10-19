---
title: Follow Route
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/FollowRoute
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Follow Route

# 沿路线移动 {#follow-route}

## 说明 {#description}

让生物沿特定路径移动，仅走一次。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| points | p | 路径点，使用 x1,y1,z1;x2,y2,z2;x3,y3,z3; 格式。 |  |
| speed | s | 移动速度。 |  |
| tolerance | t | 生物前往下一个路径点前，与当前路径点的最小距离。 | 3 |

## 示例 {#examples}

```yaml
  AIGoalSelectors:
  - clear
  - followRoute{p=1,0,0;12,0,10}
```

## 别名 {#aliases}

- followPath
