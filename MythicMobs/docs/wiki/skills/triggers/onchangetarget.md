---
title: Onchangetarget
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onchangetarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onchangetarget {#onchangetarget}

## 说明 {#description}

当生物改变目标时执行技能。

> **必须启用[仇恨表](../../mobs/threattables.md)**

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Modules:
    ThreatTable: true
  Skills:
    # sends a message to all the players in the world
    # when the mob's target changes
    - message{m=Target Changed} @World ~onChangeTarget
```

## 别名 {#aliases}

- onTargetChange
