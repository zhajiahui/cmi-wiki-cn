---
title: Bounding Boxes Overlap
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/BoundingBoxesOverlap
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Bounding Boxes Overlap {#bounding-boxes-overlap}

## 说明 {#description}

检查施法者与目标的 BoundingBox 是否重叠。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| shiftforward | so, forwardoffset, fo, forward, f | 施法者 BoundingBox 的向前偏移量。 | 0.0 |

## 示例 {#examples}

```yaml
  TargetConditions:
  - boundingBoxesOverlap false
```

## 别名 {#aliases}

- bbsoverlap
