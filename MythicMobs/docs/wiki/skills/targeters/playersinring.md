---
title: Players In Ring
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersInRing
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Players In Ring {#players-in-ring}

## 说明 {#description}

瞄准施法者周围一圈内的所有玩家。   目标玩家将是那些与施法者距离在最小和最大范围之间的玩家。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| minrange | min | 环形范围的最小半径。 | 5 |
| maxrange | max | 环形范围的最大半径。 | 10 |

## 示例 {#examples}

```yaml
  Skills:
  - ignite @PlayersInRing{min=2;max=10}
```

## 别名 {#aliases}

- pring
