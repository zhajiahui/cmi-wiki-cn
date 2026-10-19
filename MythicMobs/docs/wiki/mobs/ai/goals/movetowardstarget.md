---
title: Move Towards Target
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveTowardsTarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Move Towards Target

# 向目标移动 {#move-towards-target}

## 说明 {#description}

让生物向目标移动。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 移动速度。 | 0.9 |
| maxrange | range, r | 启用此行为的最大范围。 | 32.0 |

## 示例 {#examples}

```yaml
  AIGoalSelectors:
  - clear
  - moveTowardsTarget
```
