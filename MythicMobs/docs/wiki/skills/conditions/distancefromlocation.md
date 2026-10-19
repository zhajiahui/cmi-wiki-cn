---
title: Distance From Location
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/DistanceFromLocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Distance From Location {#distance-from-location}

## 说明 {#description}

目标与指定位置的距离是否在一定范围内

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| x |  | 位置的 x 分量。 | 0 |
| y |  | 位置的 y 分量。 | 0 |
| z |  | 位置的 z 分量。 | 0 |
| world | w | 位置所在的世界，默认为目标所在世界。 |  |
| distance | d | 用于检查的距指定位置的距离。 |  |

## 示例 {#examples}

```yaml
  TargetConditions:
  - distanceFromLocation{x=10;y=20;z=30;distance=<20} true
```
