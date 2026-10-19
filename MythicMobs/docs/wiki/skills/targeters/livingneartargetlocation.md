---
title: Living Near Target Location
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingNearTargetLocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Living Near Target Location {#living-near-target-location}

## 说明 {#description}

以继承目标附近的所有生物为目标

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |

## 示例 {#examples}

此机制执行时，会对生物目标周围半径 2 格内的所有实体造成伤害

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @target

ExampleSkill2:
  Skills:
  - damage{a=10} @LivingNearTargetLocation{r=2}
```

## 别名 {#aliases}

- livingentitiesneartargetlocation
- LNTL
- ENTL
- ENT
