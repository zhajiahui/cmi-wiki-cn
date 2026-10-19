---
title: Bowtension
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/bowtension
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Bowtension {#bowtension}

## 说明 {#description}

检查实体用弓射击时的拉弓力度。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| force | f, value, v, val | 要检查的力度/拉弓力度值。接受浮点数范围，但只能在 0 到 1 之间。 | >0 |

## 示例 {#examples}

```yaml
  Conditions:
  - bowtension{value=>0.5} true
```

## 别名 {#aliases}

- bowshoottension
