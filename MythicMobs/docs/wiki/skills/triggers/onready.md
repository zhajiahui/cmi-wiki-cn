---
title: Onready
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onready
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onready {#onready}

## 说明 {#description}

当生物准备好从[刷怪点](../../spawners.md)生成时执行技能

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob is about to spawn from a spawner
    - message{m=READY TO SPAWN FROM A SPAWNER} @World ~onReady
    - message{m=READY TO SPAWN FROM A SPAWNER} @World ~onFirstSpawn
```

## 别名 {#aliases}

- onFirstSpawn
