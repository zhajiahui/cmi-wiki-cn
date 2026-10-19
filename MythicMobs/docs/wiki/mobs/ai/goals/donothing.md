---
title: Do Nothing
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/doNothing
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Do Nothing

# 不执行任何动作 {#do-nothing}

## 说明 {#description}

****此功能仅限 Premium****  
根据给定条件，让生物停止所有行动。

**使用此功能时，条件似乎是反转的。例如，`day true` 会让生物在夜间执行 doNothing，而 `day false` 会让生物在白天执行 doNothing。**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| conditions | c, cond, fleeconditions | 使用的条件。 |  |

## 示例 {#examples}

这会让生物在满足 [day](https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/day) 条件时停止其 AI。

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - doNothing{conditions=[ - day true ]}
```

## 别名 {#aliases}

- nothing
