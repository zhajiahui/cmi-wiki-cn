---
title: Ondropcombat
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ondropcombat
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ondropcombat {#ondropcombat}

## 说明 {#description}

生物脱离战斗时执行技能。

> **必须启用[仇恨表](../../mobs/threattables.md)**

> 没有关联的[@trigger](../targeters/trigger.md)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # sends a message to all the players in the world
    # when the mob enters combat
    - message{m=DROPPED COMBAT} @World ~onDropCombat
```

## 别名 {#aliases}

- onLeaveCombat
- onCombatDrop
- onExitCombat
