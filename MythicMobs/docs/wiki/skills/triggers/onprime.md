---
title: Onprime
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onprime
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onprime {#onprime}

## 说明 {#description}

生物被点燃、进入爆炸准备状态时执行技能，例如用打火石点燃时。生物必须是苦力怕。

> 关联的 [@trigger](../targeters/trigger.md) 是施法者本身

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # sends a message to all the players in the world
    # when the mob is primed
    - message{m=OOO I'M GONNA EXPLODE} @World ~onPrime
```
