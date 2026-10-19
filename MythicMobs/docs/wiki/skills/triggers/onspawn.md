---
title: On Spawn
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onSpawn
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Spawn {#on-spawn}

## 说明 {#description}

当生物生成时执行技能。

> 没有关联的[@trigger](../targeters/trigger.md)

## 实现示例 {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onSpawn)
- [MythicRPG](https://wiki.mythiccraft.io/mythicrpg/Skills/Triggers/onSpawn)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob spawns
    - message{m=SPAWN} @World ~onSpawn
```
