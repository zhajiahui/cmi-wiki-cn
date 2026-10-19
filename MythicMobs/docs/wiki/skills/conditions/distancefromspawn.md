---
title: Distancefromspawn
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/distancefromspawn
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Distancefromspawn {#distancefromspawn}

## 说明 {#description}

世界出生点到目标的距离是否在给定范围内

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 要匹配的距离。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - distancefromspawn{d=<100} true
```

```yaml
  Conditions:
  - distancefromspawn{d=>50} true
```
