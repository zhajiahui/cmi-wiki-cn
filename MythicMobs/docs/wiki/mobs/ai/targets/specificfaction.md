---
title: Specificfaction
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/specificfaction
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Specificfaction {#specificfaction}

## 说明 {#description}

让生物以特定阵营为目标。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| faction | f | 要作为目标的阵营。 |  |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AITargetSelectors:
    - clear
    - specificfaction{f=somefaction}
```

## 别名 {#aliases}

- nearestspecificfaction
