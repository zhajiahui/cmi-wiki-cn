---
title: Random Locations Near Targets
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RandomLocationsNearTargets
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Random Locations Near Targets {#random-locations-near-targets}

## 说明 {#description}

瞄准继承目标附近的随机位置

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 点数。 | 5 |
| radius | r, maxradius, maxr | 生成目标点的半径。 | 5 |
| minradius | minr | 生成目标点的最小半径。 | 0 |
| spacing | s | 所选目标之间的最小间隔。 | 0 |
| onsurface | surface | 所选位置是否必须位于非空气的表面上。 | false |

## 示例 {#examples}

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @PIR{r=10}

ExampleSkill2:
  Skills:
  - effect:particles @RandomLocationsNearTargets{a=5;r=2}
```

## 别名 {#aliases}

- randomLocationsNearTarget
- randomLocationsNearTargetEntities
- randomLocationsNearTargetLocations
- RLNT
- RLNTE
- RLNTL
