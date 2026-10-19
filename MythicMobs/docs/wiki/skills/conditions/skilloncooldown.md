---
title: Skilloncooldown
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/skilloncooldown
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Skilloncooldown {#skilloncooldown}

## 说明 {#description}

检查目标实体的给定技能是否处于冷却状态

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| skill | s | 要检查的元技能。 |  |

## 示例 {#examples}

```yaml
  TargetConditions:
  - skillOnCooldown{skill=TestSkill}
```
