---
title: Zdiff
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/zdiff
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Zdiff {#zdiff}

## 说明 {#description}

检查目标实体和施法者之间的 z 值差异。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| difference | diff, d | 要检查的 z 坐标差。 |  |

## 示例 {#examples}

```yaml
  TargetConditions:
  - zDiff{diff=>5} true
```
