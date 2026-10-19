---
title: Ontame
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ontame
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ontame {#ontame}

## 说明 {#description}

当玩家驯服生物时执行技能。

> 关联的 [@trigger](../targeters/trigger.md) 是驯服生物的玩家

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: WOLF
  Skills:
    # sends a message to all the players in the world
    # when a player tames the mob
    - message{m=I GOT TAMED} @World ~onTame
```
