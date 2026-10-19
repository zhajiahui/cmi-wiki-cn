---
title: On Damaged
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDamaged
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Damaged {#on-damaged}

## 说明 {#description}

当生物受到伤害时执行该技能。

> 关联的 [@trigger](../targeters/trigger.md) 是造成伤害的实体

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

## 实现示例 {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onDamaged)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob takes damage
    - message{m=DAMAGED} @World ~onDamaged
```

## 别名 {#aliases}

- onHurt
