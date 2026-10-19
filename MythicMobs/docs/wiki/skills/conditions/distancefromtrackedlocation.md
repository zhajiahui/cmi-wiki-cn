---
title: Distancefromtrackedlocation
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/distancefromtrackedlocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Distancefromtrackedlocation {#distancefromtrackedlocation}

## 说明 {#description}

检查施法者与其跟踪位置之间的距离是否在指定值范围内

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 要检查的数值，可以是范围。 |  |

## 示例 {#examples}

```yml
Conditions:
  - DistanceFromTrackedLocation{d=5} true
```

```yml
Conditions:
  - DistanceFromTrackedLocation{d=2to10} true
```

## 别名 {#aliases}

- distanceFromTL
