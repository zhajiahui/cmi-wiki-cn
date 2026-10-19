---
title: Onspawnorload
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onspawnorload
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onspawnorload {#onspawnorload}

## 说明 {#description}

当[~onSpawn](onspawn.md)或[~onLoad](onload.md)触发时执行技能。

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob spawns or when the mob is loaded after a server restart
    - message{m=SPAWNED! Or was i loaded?} @World ~onSpawnOrLoad
```
