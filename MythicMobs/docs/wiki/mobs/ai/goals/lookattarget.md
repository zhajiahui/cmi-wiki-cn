---
title: Look At Target
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/LookAtTarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Look At Target

# 看向目标 {#look-at-target}

## 说明 {#description}

让生物看向目标。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| maxrange | range, r | 此 AI 行为生效时，目标必须位于的最大范围。 | 32 |
| speed | s | 运动速度。 | 0.9 |
| onlyhorizontal | horizontal, h | 生物看向目标时，是否不改变俯仰角。 | false |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - lookAtTarget{r=12;h=true}
```
