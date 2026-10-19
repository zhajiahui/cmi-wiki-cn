---
title: Ondespawn
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ondespawn
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ondespawn {#ondespawn}

## 说明 {#description}

当生物消失时执行技能。

> 关联的 [@trigger](../targeters/trigger.md) 是施法者本身

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob despawns
    - message{m=DESPAWNED} @World ~onDespawn
```

## 别名 {#aliases}

- onDespawned
