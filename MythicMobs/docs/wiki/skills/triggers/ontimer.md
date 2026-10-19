---
title: On Timer
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Timer {#on-timer}

## 说明 {#description}

这个触发器有一个特殊的语法：`~onTimer:<ticks>`

每隔 *n* 个游戏刻执行技能。间隔不能为零，20 个游戏刻等于 1 秒。

此触发器依据全局时钟运行，而不是从生物生成时开始计时。例如，使用 `~onTimer:1000` 时，首次执行可能发生在生物生成后的任意时刻，最迟不超过 1000 个游戏刻，具体取决于全局时钟的值。

> 使用此触发器时必须小心，因为它可能导致服务器/客户端性能问题！
> 例如，大量粒子效果可能导致客户端卡顿，甚至导致客户端被服务器踢出

> 没有关联的 [@trigger](../targeters/trigger.md)。

## 实现示例 {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onTimer)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world every 0.05 seconds
    - message{m=TIMER every tick (0.05 seconds)} @World ~onTimer:1
    # sends a message to all the players in the world every 2 seconds
    - message{m=TIMER every 40 ticks (2 seconds)} @World ~onTimer:40
```
