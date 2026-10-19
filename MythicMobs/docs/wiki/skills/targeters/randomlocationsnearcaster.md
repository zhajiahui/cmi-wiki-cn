---
title: Random Locations Near Caster
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RandomLocationsNearCaster
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Random Locations Near Caster {#random-locations-near-caster}

## 说明 {#description}

瞄准施法者附近的随机位置

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 点数。 | 5 |
| radius | r, maxradius, maxr | 生成目标点的半径。 | 5 |
| minradius | minr | 生成目标点的最小半径。 | 0 |
| spacing | s | 所选目标之间的最小间隔。 | 0 |
| onSurface | onsurf, os | 仅选择实心方块上方的位置为目标。 | false |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - effect:particles @RandomLocationsNearCaster{a=5;r=2}
```

## 别名 {#aliases}

- randomLocations
- RLNC
