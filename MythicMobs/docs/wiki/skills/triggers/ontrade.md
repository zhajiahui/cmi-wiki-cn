---
title: Ontrade
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ontrade
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ontrade {#ontrade}

## 说明 {#description}

当村民与玩家交易时执行该技能。

> 关联的 [@trigger](../targeters/trigger.md) 是与村民进行交易的玩家

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob's target changes
    - message{m=TRADED} @World ~onTrade
```
