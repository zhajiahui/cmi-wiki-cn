---
title: On Bow Hit
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onBowHit
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Bow Hit {#on-bow-hit}

## 说明 {#description}

当生物的弹射物击中实体时执行技能。

> 关联的[@trigger](../targeters/trigger.md)是被击中的实体

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

## 实现示例 {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onBowHit)

## 示例 {#examples}

```yaml
NotYourAverageSkeleton:
  Type: SKELETON
  Equipment:
    - BOW HAND
  Skills:
  - modifyDamage{a=3;modifier=MULTIPLY;sync=true} ~onBowHit
```

## 别名 {#aliases}

- onBow_Hit
- onArrowHit
