---
title: Onsignal
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onsignal
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onsignal {#onsignal}

## 说明 {#description}

这个触发器有一个特殊的语法：`~onSignal:<signal>`

生物收到 [signal](../mechanics/signal.md) 机制发送的信号时执行技能。信号只能由字母和数字组成。

> 关联的[@trigger](../targeters/trigger.md)是发送信号的实体

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a signal to all mythicmob entity in a radius of 64 blocks
    # when a player right-clicks the mob
    - signal{s=MOO_FOR_ME} @EIR{r=64} ~onInteract
```

##  {#section}

```yml
DUMMY_MOB:
  Type: COW
  Skills:
    # sends a message to all the players in the world
    # when the mob receives a "MOO_FOR_ME" signal
    - message{m=MOO} @World ~onSignal:MOO_FOR_ME
```

##  {#section-2}

你也可以选择不为此触发器指定信号，在这种情况下，每次生物收到通用信号时都会触发关联的机制。

```yml
DUMMY_MOB:
  Type: COW
  Skills:
    # sends a message to all the players in the world
    # when the mob receives a signal
    - message{m=MOO...?} @World ~onSignal
```
