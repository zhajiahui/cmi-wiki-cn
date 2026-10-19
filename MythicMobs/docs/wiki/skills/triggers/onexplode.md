---
title: Onexplode
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onexplode
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onexplode {#onexplode}

## 说明 {#description}

生物爆炸时执行技能。`mobGriefing` 游戏规则必须设为   true   才能生效。此触发器通常只适用于苦力怕和 TNT，因为只有它们会真正发生爆炸

> 没有关联的[@trigger](../targeters/trigger.md)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # sends a message to all the players in the world
    # when the mob explodes
    - message{m=EXPLODE} @World ~onExplode
```
