---
title: Oncreepercharge
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/oncreepercharge
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Oncreepercharge {#oncreepercharge}

## 说明 {#description}

施法的苦力怕被充能时执行技能。

> 关联的 [@trigger](../targeters/trigger.md) 是施法者本身

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CREEPER
  Skills:
    # sends a message to all the players in the world
    # when the mob gets charge
    - message{m=CHARGED} @World ~onCreeperCharge
```

## 别名 {#aliases}

- onCreeper_Charge
- onCharged
- onCharge
