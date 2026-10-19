---
title: On Death
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDeath
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Death {#on-death}

## 说明 {#description}

生物死亡时执行技能。如果使用 Paper 服务端，可以通过同步执行 cancelevent 机制取消死亡事件。取消后生物的生命值由 `ReviveHealth` 选项决定。

> 关联的[@trigger](../targeters/trigger.md)是杀死施法者的实体

## 实现示例 {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onDeath)
- [MythicRPG](https://wiki.mythiccraft.io/mythicrpg/Skills/Triggers/onDeath)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob dies
    - message{m=DEATH} @World ~onDeath
```

```yaml
ImmortalCow:
  Type: COW
  Display: '&eImmortal Cow'
  Health: 20
  Options:
    ReviveHealth: -1
  Skills:
  - skill{s=[
    - cancelevent
    - particle{p=HEART;hs=0.5;vs=0.5;y=1.5}
    - speak{m=Call an ambulance, but not for me!}
    ];sync=true} @self ~onDeath
```
