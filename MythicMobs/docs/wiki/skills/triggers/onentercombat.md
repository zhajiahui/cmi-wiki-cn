---
title: Onentercombat
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onentercombat
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onentercombat {#onentercombat}

## 说明 {#description}

当生物进入战斗时执行技能。

> **必须启用[仇恨表](../../mobs/threattables.md)**

> 关联的[@trigger](../targeters/trigger.md)是使施法者进入战斗的实体

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # sends a message to all the players in the world
    # when the mob enters combat
    - message{m=ENTERED COMBAT} @World ~onEnterCombat
```
