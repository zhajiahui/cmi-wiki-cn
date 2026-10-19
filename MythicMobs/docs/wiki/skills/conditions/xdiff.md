---
title: Xdiff
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/xdiff
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Xdiff {#xdiff}

## 说明 {#description}

检查目标实体和施法者之间的 x 值差异。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| difference | diff, d | 要检查的 x 坐标差。 |  |

## 示例 {#examples}

```yaml
  TargetConditions:
  - xDiff{diff=>5} true
```
