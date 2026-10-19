---
title: Specificfactionmonsters
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/specificfactionmonsters
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Specificfactionmonsters {#specificfactionmonsters}

## 说明 {#description}

让生物以特定阵营的怪物为目标。

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
    - specificfactionmonsters{f=somefaction}
```

## 别名 {#aliases}

- nearestspecificfactionmonsters
