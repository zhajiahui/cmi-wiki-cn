---
title: Stance
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/stance
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Stance {#stance}

## 说明 {#description}

检查目标生物的姿态。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| stance | s | 要匹配的姿态。 | DEFAULT |
| strict | str | 是否精确匹配。设为 false 时，检查当前姿态是否包含此词。 | true |

## 示例 {#examples}

```yaml
  Conditions:
  - stance{s=CombatStance;str=true} true
```
