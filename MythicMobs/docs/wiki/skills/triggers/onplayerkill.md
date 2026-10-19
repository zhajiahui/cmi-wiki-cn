---
title: Onplayerkill
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onplayerkill
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onplayerkill {#onplayerkill}

## 说明 {#description}

当怪物杀死玩家时执行该技能。

> 关联的[@trigger](../targeters/trigger.md)是已被杀死的玩家

## 实现示例 {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onKillPlayer)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob kills a player
    - message{m=PLAYER KILLED} @World ~onPlayerKill
```

## 别名 {#aliases}

- onKillPlayer
