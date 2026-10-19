---
title: Signal
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Signal
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Signal {#signal}

## 说明 {#description}

向指定目标发送信号。当针对玩家时不会做任何事情。信号可以由任何字符串组成。接收信号的生物只有在其技能库中有专用的“~onSignal”触发器才能对其采取行动（参见示例）。

信号可以通过直接在触发器后面进行比较 (~onSignal:*ping*) 或通过新的 [lastsignal-condition](../conditions/lastsignal.md) 来匹配。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| signal | s | 要发送的信号 | ping |

## 示例 {#examples}

本例中，Master 生物受伤时，会向 20 格内的随从发送信号，让随从以自身位置为基准，向最近玩家射箭。

```yaml
# Mob file:
Master:
  Type: zombie
  Skills:
  - summon{m=Minion} @self ~onSpawn
  - signal{s=ATTACK} @MobsInRadius{r=10;t=Minion} ~onDamaged
Minion:
  Type: baby_zombie
  Skills:
  - skill{s=ShootAttacker} @NearestPlayer ~onSignal:ATTACK
```

```yaml
# Skill file:
ShootAttacker:
  Skills:
  - shoot{t=arrow}
```

## 别名 {#aliases}

- sendsignal
