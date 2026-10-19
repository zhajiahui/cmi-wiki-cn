---
title: Oninteract
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/oninteract
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Oninteract {#oninteract}

## 说明 {#description}

当玩家与生物互动或“右键单击”生物时执行技能。

> 关联的[@trigger](../targeters/trigger.md)是与施法者互动的玩家

## 实现示例 {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onInteract)
- [MythicRPG](https://wiki.mythiccraft.io/mythicrpg/Skills/Triggers/onInteract)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when a player right-clicks the mob
    - message{m=INTERACTED} @World ~onInteract
```
