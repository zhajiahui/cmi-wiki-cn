---
title: Skylightlevel
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/skylightlevel
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Skylightlevel {#skylightlevel}

## 说明 {#description}

检查目标位置的天空光照等级，只计算天空提供的光照。它不同于 `lightlevel`（总光照）或 `lightlevelfromblocks`（方块光照）。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| level | l | 要匹配的天空光照等级范围。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - skylightlevel{l=10} true
```

```yaml
  Conditions:
  - skylightlevel{l=>10} true
```

```yaml
  Conditions:
  - skylightlevel{l=1to10} true
```
