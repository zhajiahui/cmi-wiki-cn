---
title: On Load
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onLoad
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Load {#on-load}

## 说明 {#description}

服务器重启后加载生物时执行技能。

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob is loaded after a server restart
    - message{m=LOADED} @World ~onLoad
```
