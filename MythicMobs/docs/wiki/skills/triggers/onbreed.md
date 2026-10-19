---
title: On Breed
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onBreed
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Breed {#on-breed}

## 说明 {#description}

当该生物与另一个生物繁殖时执行该技能。

> 此触发器提供 [`@Father`](../targeters/father.md) 和 [`@Mother`](../targeters/mother.md) 目标选择器。

> 关联的 [@trigger](../targeters/trigger.md) 是使施法者繁殖的玩家

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob breeds
    - message{m=LET'S GET THIS BREAD} @World ~onBreed
```
