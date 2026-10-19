---
title: On Dismounted
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDismounted
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Dismounted {#on-dismounted}

## 说明 {#description}

骑乘者从该生物身上下来时执行技能。

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: HORSE
  Skills:
    # sends a message to the player that dismounted the entity, and prevents it from dismounting entirely with a chance
    - skill{s=[
      - cancelevent
      - message{m=Going somewhere?} @trigger
     ];sync=true} @self ~onDismounted 0.7
```

## 别名 {#aliases}

- onUnmounted
