---
title: Entities In Ring
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesInRing
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Entities In Ring {#entities-in-ring}

## 说明 {#description}

以施法者周围的环内的所有实体为目标。   目标实体将是距施法者的距离在最小和最大范围之间的实体。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| minrange | min | 环形范围的最小半径。 | 5 |
| maxrange | max | 环形范围的最大半径。 | 10 |

## 示例 {#examples}

```yaml
  Skills:
  - ignite @EIRR{min=2;max=10}
```

## 别名 {#aliases}

- EIRR
