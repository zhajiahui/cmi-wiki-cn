---
title: Food Level
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/FoodLevel
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Food Level {#food-level}

## 说明 {#description}

检查目标的食物量

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a, food, f | 要检查的饥饿值范围。 | 0 |

## 示例 {#examples}

```yaml
  TargetConditions:
  - FoodLevel{a=<10} true
```

## 别名 {#aliases}

- hunger
- food
- hungerlevel
