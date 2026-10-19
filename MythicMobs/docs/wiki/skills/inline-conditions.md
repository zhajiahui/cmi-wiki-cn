---
title: 内联条件
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/Inline-Conditions
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 内联条件

内联条件可以直接用于单个技能机制和目标选择器，简单逻辑无需专门创建元技能，也能让已有元技能更灵活。标准条件检查施法者，TriggerCondtions 检查触发实体，TargetConditions 检查目标。

内联条件可用于生物文件和技能文件；安装 Crucible 后，也能用于物品文件。

1. [条件](inline-conditions.md#conditions)
2. [TriggerConditions](inline-conditions.md#triggerconditions)
3. [TargetConditions](inline-conditions.md#targetconditions)

# 条件 {#conditions}

这些条件检查施法者本身，放在机制行末尾，以 `?` 开头。下面的示例只有在下雨时才发送消息。

```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - message{m="You hit me in the rain?"} @trigger ~onDamaged ?raining
```

对于条件为   true  ，你可以使用 `?`，对于条件为   false  ，你可以使用 `?!`

- `?raining`：检查条件为 True，即*正在*下雨。
- `?!raining`：检查条件为 False，即*没有*下雨。

# TriggerConditions {#triggerconditions}

也可以检查技能机制的触发实体，写法相同，但在 ? 后加上 `~`。下面的示例仅在攻击生物的玩家手持木剑时，才向该玩家发送消息。

```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - message{m="You hit me with a wooden sword?"} @trigger ~onDamaged ?~holding{m=WOODEN_SWORD}
```

就像标准条件一样，对于  true  ，你可以使用`?~`，对于  false  ，你可以使用`?~!`

- `?~holding{m=WOODEN_SWORD}`：True，玩家*正手持*木剑。
- `?~!holding{m=WOODEN_SWORD}`：False，玩家*未手持*木剑。

### 多个条件 {#multiple-conditions}

你可以在机制中根据需要使用任意数量的内联条件和TriggerConditions。请记住，必须满足*所有*条件才能运行机制，在下面的示例中，只有在下雨、*和*夜晚、*和*攻击怪物的玩家拿着木剑时才会发送消息。

```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - message{m="You hit me with a wooden sword? in the rain?? at night???"} @trigger ~onDamaged ?raining ?night ?~holding{m=WOODEN_SWORD}
```

# TargetConditions {#targetconditions}

**内联 TargetConditions 仅限 Premium 版！**

内联目标条件可以给目标选择器附加条件，只选择所需的实体或位置。先看格式：

本例中，生物每秒对 10 格内具有 `Plagued` 光环的玩家造成 1 点伤害。

```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - damage{a=1} @PIR{r=10;conditions=[  - hasaura{aura=Plagued} true ]} ~onTimer:20
```

内联目标条件的空格非常重要。`conditions=[` 与 `- hasaura{aura=Plagued} true` 之间必须有两个空格，`true` 与 `]}` 之间也必须有一个空格。

你还可以在单个目标选择器上使用多个条件，有 2 方法可以做到这一点。

下拉一行并缩进的示例：

```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - damage{a=1} @PIR{r=10;conditions=[
                              - hasaura{aura=Plagued} false
                              - haspotioneffect{type=WITHER;d=1to999999;l=0to254} true 
                              ]} ~onTimer:20
```

请注意，第二个条件末尾的   true   后面仍然有一个空格。

将多个条件保留在一行上的示例：

```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - damage{a=1} @PIR{r=10;conditions=[  - hasaura{aura=Plagued} true  - haspotioneffect{type=WITHER;d=1to999999;l=0to254} true ]} ~onTimer:20
```

注意，`conditions=[`和第一个条件之间有两个空格，那么第一个条件和第二个条件之间也有两个空格。最后，第二个条件末尾的  true  后面还有一个空格。
