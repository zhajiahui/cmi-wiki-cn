---
title: Living In Radius
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/LivingInRadius
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Living In Radius {#living-in-radius}

## 说明 {#description}

检查指定半径内的活体实体数量是否在范围内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要检查的数量。 | 1 |
| radius | r | 搜索半径。 | 5 |

## 示例 {#examples}

```yaml
  Conditions:
  - livinginradius{a=<5;r=10} true
```
