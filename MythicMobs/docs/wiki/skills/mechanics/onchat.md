---
title: On Chat
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/OnChat
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Chat {#on-chat}

## 说明 {#description}

为目标玩家施加[光环](aura.md)，在其发送聊天消息时触发[元技能](../metaskills.md)。

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.input>` |

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onChatSkill | onchat, oc, then | 玩家聊天时执行的[元技能](../metaskills.md)。 |  |

> 该机制继承了[光环](aura.md)机制的所有属性

## onChatSkill 属性 {#onchatskill-attribute}

执行元技能时，会设置名为 `input` 的[技能作用域变量](../variables.md)，保存聊天输入内容，可通过 `<skill.var.input>` 取得。

## 示例 {#examples}

`ExampleSkill`元技能将为20方块半径内的每个玩家创建光环。如果这些玩家在10秒的时间内聊天，就会向他们发送一条消息，然后他们就会被点燃。

```yaml
ExampleSkill:
  Skills:
  - onChat{onChat=ExampleSkill2;d=200} @PIR{r=20}

ExampleSkill2:
  Skills:
  - message{m="SILENCE!"} @trigger
  - ignite @trigger
```

下面的示例使用 [StringEquals](../conditions/stringequals.md) 条件来检查玩家输入的内容！仅当玩家输入`QueenOfAnts is a noob`时，消息机制才会出现。

```yaml
YourMob:
  Type: ZOMBIE
  Skills:
  - onChat{onChat=ChatSkill;d=1000} @trigger ~onInteract

ChatSkill:
  Conditions:
  - stringequals{val1="<skill.var.input>";val2="QueenOfAnts is a noob"} true
  Skills:
  - message{m=She is indeed!} @trigger
```

## 别名 {#aliases}

- chatprompt
