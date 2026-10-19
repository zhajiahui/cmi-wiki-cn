---
title: Player Locations In Radius
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayerLocationsInRadius
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Player Locations In Radius {#player-locations-in-radius}

## 说明 {#description}

定位施法者周围给定半径内所有玩家的位置

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |
| yoffset | y | 目标位置的 y 轴偏移。 | 0 |

## 示例 {#examples}

```yaml
  Skills:
  - effect:particles @PlayerLocationsInRadius{r=10}
```

## 别名 {#aliases}

- LocationRadius
- PLIR
- PLR
