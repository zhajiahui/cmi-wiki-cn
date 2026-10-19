---
title: Players Near Target Locations
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersNearTargetLocations
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Players Near Target Locations {#players-near-target-locations}

## 说明 {#description}

以继承目标位置附近的所有玩家为目标

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |

## 示例 {#examples}

此机制执行时，会对生物目标周围半径 2 格内的每位玩家造成伤害

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @target

ExampleSkill2:
  Skills:
  - damage{a=10} @PlayersNearTargetLocations{r=2}
```

## 别名 {#aliases}

- playersNearTargetLocation
- PNTL
