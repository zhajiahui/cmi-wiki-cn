---
title: On Attack
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onAttack
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Attack {#on-attack}

## 说明 {#description}

当生物攻击实体时执行技能。

> 关联的 [@trigger](../targeters/trigger.md) 是被攻击的实体

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

## 实现示例 {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onAttack)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Damage: 1
  Skills:
    # sends a message to all the players in the world
    # when the mob attacks an entity
    - message{m=ATTACK} @World ~onAttack
```

## 别名 {#aliases}

- onHit
