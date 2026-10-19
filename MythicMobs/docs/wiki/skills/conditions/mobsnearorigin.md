---
title: Mobs Near Origin
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MobsNearOrigin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mobs Near Origin {#mobs-near-origin}

## 说明 {#description}

将范围与 [origin](../targeters/origin.md) 周围给定半径内的生物数量相匹配

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要匹配的生物数量，可以是范围。 | 1 |
| radius | r | 匹配生物的半径。 | 5 |
| types | type, t | 要匹配的生物类型，可以是列表。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - mobsnearorigin{type=ExampleMob,SuperDuperStrongMob;r=10;amount=>5}
```
