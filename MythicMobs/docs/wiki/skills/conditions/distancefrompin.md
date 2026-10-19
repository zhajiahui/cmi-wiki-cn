---
title: Distance From Pin
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/DistanceFromPin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Distance From Pin {#distance-from-pin}

## 说明 {#description}

检查目标是否在指定 [pin](../../pins.md) 的一定距离内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| pin | p | 用于检查的定位点。 |  |
| distance | d | 用于检查的距离，可以是范围。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - distanceFromPin{pin=example_pin;d=>10} true
```
