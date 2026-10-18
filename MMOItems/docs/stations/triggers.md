---
title: 触发器
source: https://docs.phoenixdevt.fr/mmoitems/stations/triggers
source_snapshot: '2026-10-19'
---

# 触发器 {#🔧-triggers}

配方触发器是不显示在配方GUI物品中的配方选项。它们指示玩家使用配方时执行的操作。

```yml
recipes:
    steel-sword:
        ....
        triggers:
        - 'vanilla{type=STICK,amount=3}'
```

## 可用的触发器 {#available-triggers}

|触发|描述 |格式/示例 |
| --- | --- | --- |
| `message` | 向玩家发送消息。 | `message{format="&aYour message here... "}` |
| `command` | 使控制台执行命令。 | `command{format="give dirt",sender=OP}`*- 可用发送器：玩家、CONSOLE、OP* |
| `sound` | 向玩家广播声音。 | `sound{sound=<SOUND_NAME>;volume=<VOLUME>;pitch=<PITCH>}` |
| `vanilla` | 将原版物品赋予玩家。 | `vanilla{type=DIAMOND;amount=3}` |
| `mmoitem` | 向玩家提供 mmoitem 。 | `mmoitem{type=SWORD;id=FALCON_BLADE;amount=1}` |
| `mmskill` | 铸造MythicMobs技能。 | `mmskill{id=MythicMobsSkillInternalName}` |
| `experience` | 给出玩家MMOCore经验。 | `exp{profession=<PROFESSION>;amount=<AMOUNT>}` |

---

原文：[🔧 Triggers](https://docs.phoenixdevt.fr/mmoitems/stations/triggers) · 原文归档：2026-10-19
