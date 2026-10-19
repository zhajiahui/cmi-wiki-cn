---
title: Ydiff
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ydiff
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ydiff {#ydiff}

## 说明 {#description}

检查目标实体和施法者之间 y 值（高度）的差异。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| difference | diff, d | 要检查的 y 坐标差。 |  |

## 示例 {#examples}

```yaml
  TargetConditions:
  - yDiff{diff=>5} true
```
