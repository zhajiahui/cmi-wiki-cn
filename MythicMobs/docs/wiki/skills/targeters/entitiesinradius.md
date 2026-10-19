---
title: Entities In Radius
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesInRadius
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Entities In Radius {#entities-in-radius}

## 说明 {#description}

瞄准施法者周围给定半径内的所有实体

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| shape |  | 获取实体所使用的形状，可以是任意[形状](../../enum/shape.md)。 | SPHERE |
| livingonly | living, l | 目标选择器是否仅以活体实体为目标。 | true |

## 示例 {#examples}

```yaml
  Skills:
  - ignite @EIR{r=10}
```

## 别名 {#aliases}

- livingEntitiesInRadius
- livingInRadius
- allInRadius
- EIR
- entitiesnearby
- nearbyentities
