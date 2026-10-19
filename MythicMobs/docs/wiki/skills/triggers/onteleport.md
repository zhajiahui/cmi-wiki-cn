---
title: Onteleport
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onteleport
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onteleport {#onteleport}

## 说明 {#description}

当生物传送时执行技能。

> 没有关联的[@trigger](../targeters/trigger.md)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: ENDERMAN
  Skills:
    # sends a message to all the players in the world
    # when the mob teleports
    - message{m=TELEPORT} @World ~onTeleport
```
