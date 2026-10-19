---
title: Origin Location
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/OriginLocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Origin Location {#origin-location}

## 说明 {#description}

检查 [origin](../targeters/origin.md) 是否位于给定位置

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| location | loc, l, c | 要匹配的位置，格式为 `x,y,z`。 |  |
| x |  | 位置的 x 坐标。设置了 location 属性时忽略此项。 | 0 |
| y |  | 位置的 y 坐标。设置了 location 属性时忽略此项。 | 0 |
| z |  | 位置的 z 坐标。设置了 location 属性时忽略此项。 | 0 |
| exact | e | 是否精确匹配位置。 | false |

## 示例 {#examples}

```yaml
  Conditions:
  - originLocation{loc=10,20,30} true
```
