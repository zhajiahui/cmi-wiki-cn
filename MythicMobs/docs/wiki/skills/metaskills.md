---
title: 元技能
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/Metaskills
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 元技能

正如 [Skills](skills.md) wiki 页面中所示，可以通过语法从生物中执行机制

```yaml
- mechanic{argument=value} @[targeter] ~on[trigger] [health_modifier] [chance]
```

如果想将多个机制“组合在一起”，让生物执行更复杂的行为，这种写法就不合适了。这时可以使用元技能。

目录：

1. [什么是元技能？](metaskills.md#what-is-a-metaskill)
2. [元技能配置分解](metaskills.md#breaking-down-the-metaskills-configuration)
   1. [内部SkillName](metaskills.md#internal-skillname)
   2. [CancelIfNoTargets](metaskills.md#cancelifnotargets)
   3. [Hidden](metaskills.md#hidden)
   4. [条件](metaskills.md#conditions)
   5. [TargetConditions](metaskills.md#targetconditions)
   6. [TriggerConditions](metaskills.md#triggerconditions)
   7. [FailedConditionsSkill](metaskills.md#failedconditionsskill)
   8. [Cooldown](metaskills.md#cooldown)
   9. [OnCooldownSkill](metaskills.md#oncooldownskill)
   10. [Skill](metaskills.md#skill)
   11. [Skills](metaskills.md#skills)
3. [目标继承和覆盖](metaskills.md#targets-inheritance-and-override)
   1. [继承](metaskills.md#inheritance)
   2. [覆盖](metaskills.md#override)
   3. [后续元技能执行](metaskills.md#subsequent-metaskills-executions)
   4. [目标过滤](metaskills.md#targets-filtering)
   5. [元目标](metaskills.md#meta-targeters)
4. [内联元技能](metaskills.md#inline-metaskills)
   1. [示例](metaskills.md#examples)
5. [技能参数（Premium 功能）](metaskills.md#skill-parameters-premium-feature)
   1. [保留参数名称](metaskills.md#reserved-parameter-names)
6. [自定义命令](metaskills.md#custom-commands)

# 什么是元技能？ {#what-is-a-metaskill}

元技能本质上是一组技能机制，由[元机制](mechanics.md#meta-mechanics)调用后执行。**保存在 `../plugins/MythicMobs/Skills` 内的 `.yml` 文件中**，组织方式与生物配置类似。

Metaskill 的语法如下：

```yaml
internal_skillname:
  CancelIfNoTargets: [true/false]
  Hidden: [true/false]
  Conditions:
  - condition1
  - condition2
  TargetConditions:
  - condition3
  - condition4
  TriggerConditions:
  - condition5
  - condition6
  FailedConditionsSkill: [the metaskill to executed if the conditions did not check]
  Cooldown: [seconds]
  OnCooldownSkill: [the metaskill to execute if this one is on cooldown]
  Skill: [an additional metaskill to execute asynchronously from this one]
  Skills:
  - mechanic1
  - mechanic2
```

一旦你配置了元技能，你就可以使用[元机制](mechanics.md#meta-mechanics)，例如[技能](mechanics/skill.md)，从生物或元技能中执行元技能：

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=internal_skillname} @self ~onInteract
```

请注意，仅需要 `internal_skillname` 元素。例如，你可以制作仅具有技能、仅具有冷却时间或仅具有某些条件的元技能。

在下面的段落中，将解释其中每个元素的作用以及如何使用它们。如果你想了解更实际的用法，还有一些相关的[示例](../examples/common-examples.md#skills)。

# 元技能配置详解 {#breaking-down-the-metaskills-configuration}

## 内部技能名称 {#internal-skillname}

用于在 MythicMobs 内部识别元技能的字符串，作用与生物的 Internal Name 相同。

内部技能名必须唯一，不能有两个技能使用同一名称，也不能包含空格。

无论通过哪种方式执行某个元技能，都需要使用它的内部技能名。

## CancelIfNoTargets {#cancelifnotargets}

如果没有向元技能提供符合条件的目标，元技能是否应取消其执行。   默认为`true`。

## 隐藏 {#hidden}

是否应将元技能排除在命令建议之外，例如 `/mm test cast` 的命令建议。对于仅被其他技能调用的内部技能很有用。该技能通过其内部SkillName保持完全可用。默认为`false`。

```yaml
my_utility_skill:
  Hidden: true
  Skills:
  - message{m="Registered, but not suggested by /mm test cast"}
```

## 条件 {#conditions}

元技能的[条件](conditions.md)。这些条件评估元技能的施法者。

根据每个条件中使用的[条件操作](conditions.md#condition-actions)，可能会发生不同的行为：阅读相关的 wiki 页面以获取更多信息

## TargetConditions {#targetconditions}

元技能的目标[条件](conditions.md)，针对继承的实体或位置目标检查。

根据每个条件中使用的[条件操作](conditions.md#condition-actions)，可能会发生不同的行为：阅读相关的 wiki 页面以获取更多信息

## TriggerConditions {#triggerconditions}

元技能的触发[条件](conditions.md)。这些条件评估触发[技能树](skilltrees.md)的实体。该实体也可以通过 [@Trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers#the-trigger-targeter) 目标选择器来定位

根据每个条件中使用的[条件操作](conditions.md#condition-actions)，可能会发生不同的行为：阅读相关的 wiki 页面以获取更多信息

## FailedConditionsSkill {#failedconditionsskill}

> 别名：`OnFailSkill`
> 如果条件不满足则执行的 Metaskill

```yaml
ExampleSkill:
  Conditions:
  - day true
  OnFailSkill: ExampleSkill2

ExampleSkill2:
  Skills:
  - message{m="So, well, it appears it's not daytime then."} @World
```

或者，这也是可能的

```yaml
ExampleSkill:
  Conditions:
  - day true
  OnFailSkill:
  - message{m="Oh my, it still isn't daytime?"} @World
  - message{m="That's quite the problem!"} @World
```

## Cooldown {#cooldown}

冷却时间是同一施法者执行元技能之间必须经过的时间（以秒为单位）。

例如：

```yaml
ExampleCooldownSkill:
  Cooldown: 10
  Skills:
  - ignite @self
```

`ExampleCooldownSkill`元技能只能由同一施法者每10秒触发一次。

冷却时间可以是：

- **通过 [SkillOnCooldown](conditions/skilloncooldown.md) 条件进行测试**
- **通过 [<caster.skill.[skill_name].cooldown>](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#caster-placeholders) 占位符获取**
- **通过 [SetSkillCooldown](mechanics/setskillcooldown.md) 机制设置**。

## OnCooldownSkill {#oncooldownskill}

如果元技能在冷却时被触发，则将改为施放此处指定的技能。

例如，在这个例子中：

```yaml
FirstSkill:
  Cooldown: 10
  OnCooldownSkill: SecondSkill
  Skills:
  - command{c="say First"}

SecondSkill:
  Cooldown: 5
  OnCooldownSkill: ThirdSkill
  Skills:
  - command{c="say Second"}

ThirdSkill:
  Skills:
  - command{c="say Third"}
```

正常施放 FirstSkill 会在聊天栏显示 First；冷却期间再次调用，会显示 Second；FirstSkill 与 SecondSkill 都在冷却时再调用，则显示 Third。

你还可以定义要执行的机制列表，而不是另一个元技能

```yaml
  OnCooldownSkills:
  - s{s=entity.village.no}
  - particle{p=VILLAGER_ANGRY;y=1.5}
```

## Skill {#skill}

不要与[技能](metaskills.md#skills)混淆。此选项允许元技能在触发后执行另一个元技能的机制。

```yaml
example1:
  Conditions:
  - night true
  Skills:
  - setvariable{var=skill.test;val=0} @self
  - message{m=1} @self
  - message{m=2} @self
  - delay 20
  - message{m=3} @self

example2:
  Skill: example1
  Skills:
  - message{m="test2 - <skill.var.test>"} @self
  - message{m=4} @self
```

此执行的行为非常具体：

- 其他元技能的机制在当前元技能的[技能](metaskills.md#skills)之前执行
- 其他元技能的条件和冷却时间将被忽略（如果存在）
- 每个机制都在同一个[技能树](skilltrees.md)中执行

所以，本质上，上面的例子相当于

```yaml
example2:
  Skills:
  - skill{s=example1}
  - message{m="test2 - <skill.var.test>"} @self
  - message{m=4} @self
```

唯一的区别是不考虑 example1 的冷却时间和条件

## 技能 {#skills}

元技能真正的核心：触发后执行的技能机制列表。这里也可使用其他[元机制](mechanics.md#meta-mechanics)，继续调用元技能。

```yaml
ExampleSkill:
  Skills:
  - message{m="Hello there!"}
  - skill{s=ExampleSkill_2}

ExampleSkill_2:
  Skills:
  - message{m="How are you doing?"}
```

此处还可以使用延迟，允许用户在使用延迟机制后为列表中的每个机制设置延迟。

```yaml
ExampleSkill:
  Skills:
  - message{m="Message 1"}
  - delay 20
  - message{m="Message 2"}
```

通常按列表从上到下执行。调用[元技能](mechanics.md#meta-mechanics)时，会先执行被调用技能中的机制，再继续原列表。若被调用元技能有延迟，则原列表先继续执行，被延迟的部分等待结束后再执行。

![](https://i.imgur.com/ZiHWeBQ.png)

> 在此图中，显示了上述行为的示例。如果我们执行`ExampleSkill_First`，机制将按照其编号顺序执行，从mechanic1到mechanic9，在mechanic7、mechanic8和mechanic9之间延迟20游戏刻

# 目标的继承与覆盖 {#targets-inheritance-and-override}

元技能的一个特点是它们能够“记住”调用它的[元技能机制](mechanics.md#meta-mechanics)传递给它的目标。这种行为可以有很多用途和应用。

## 继承 {#inheritance}

Metaskill 内没有自己的目标选择器的机制将**继承**这些目标，并以它们为目标。

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```

```yaml
#SKILL FILE
ExampleSkill:
  Skills:
  - ignite
```

在此示例中，`ignite`机制没有目标选择器，因此它“继承”了元技能中使用的目标选择器并以这些实体为目标，使其点燃10方块半径内的所有玩家。

## 覆盖 {#override}

如果元技能内的某个机制*指定了目标选择器*，原目标会被**覆盖**，改用新目标。

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```

```yaml
#SKILL FILE
ExampleSkill:
  Skills:
  - ignite
  - message{m="Why are you so close?"} @NearestPlayer{r=1}
```

在此示例中，所有玩家仍将被点燃，但只有在一个方块半径内距离生物最近的玩家才会收到消息

## 后续元技能的执行 {#subsequent-metaskills-executions}

当你从另一个元技能调用元技能时，仍然很可能不为其指定目标选择器，并且它将继承调用元技能也继承的目标。

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```

```yaml
#SKILL FILE
ExampleSkill:
  Skills:
  - skill{s=Example_Ignite}
  - skill{s=Example_Message} @NearestPlayer{r=1}

Example_Ignite:
  Skills:
  - ignite

Example_Message:
  Skills:
  - message{m="Why are you so close?"}
```

通过执行此技能，你将获得与[上一个示例](metaskills.md#override)中相同的结果

## 目标筛选 {#targets-filtering}

目标继承的另一个重要应用是可以使用 Metaskill 的 TargetConditions 跨多个元技能过滤继承的目标。

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill_1} @PIR{r=10} ~onInteract
```

```yaml
ExampleSkill_1:
  Skills:
  - message{m="Hello there!"}
  - delay 1
  - skill{s=ExampleSkill_2}

ExampleSkill_2:
  TargetConditions:
  - distance{d=<5} true
  Skills:
  - message{m="...You are pretty close, aren't you?"}
  - delay 1
  - skill{s=ExampleSkill_3}

ExampleSkill_3:
  TargetConditions:
  - distance{d=<1} true
  Skills:
  - message{m="AHHHHHH, GET AWAY FROM ME!"}
  - throw{v=10;vy=2}
```

上述技能先向 10 格内的所有玩家发送消息，再向其中 5 格内的玩家发送另一条消息，随后向 1 格内的玩家发送第三条消息并将其推开。

现在，举一个更反直觉的例子：

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill_1} @PIR{r=10} ~onInteract
```

```yaml
ExampleSkill_1:
  Skills:
  - message{m="Hello there!"}
  - delay 100
  - skill{s=ExampleSkill_2}

ExampleSkill_2:
  TargetConditions:
  - distance{d=>10} true
  Skills:
  - message{m="...You truly don't like me, don't you?"}
  - delay 20
  - message{m="Don't worry, it's fine."}
  - delay 20
  - message{m="I'm used to it."}
  - delay 20
  - message{m="T.T"}
```

在这种情况下，生物将首先向10块半径内的每个玩家发送一条消息，然后，5秒后，它将向其中同时移动到超过10块的玩家发送额外的消息

## 元目标选择器 {#meta-targeters}

另一个相关主题是 [Meta Targeter](targeters.md#special-targeters)。简而言之，这些目标选择器将评估继承的目标是什么，并基于此返回其他适当的目标本身。

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```

```yaml
ExampleSkill:
  Skills:
  - effect:particles @Line{r=0.2}
```

例如，上面的示例将在施法者和玩家之间以 10 方块半径生成一条粒子线。如果目标选择器不是`@PIR`而是另一个，那么施法者和所使用的目标选择器之间就会产生这条线。

# 行内元技能 {#inline-metaskills}

元技能还可以使用特定的内联语法编写，而无需完全创建另一个元技能。

内联元技能无法使用普通元技能的全部字段，例如条件、OnCooldownSkill 等，需要用其他方式实现相同效果，例如用 `cooldown` [通用属性]替代 Cooldown 字段。

内联 Metaskill 内的机制无法以普通方式注释掉以禁用它们，因为这会导致整个 Metaskill 停止工作。必须在机制之前使用`<#>`或`<&nm>`等字符才能获得相同的效果。

内联 Metaskill 语法可以用在 Metamechanics 内部需要正常 Metaskill 内部名称的任何地方。

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=[
    - message{m="Feeling cold? Don't you worry!"}
    - delay 40
    - ignite
    ]} @trigger ~onInteract
```

> 在此示例中，你可以看到编写内联 Metaskill 的语法以及所使用的普通 Metaskill 的一些功能（目标继承、延迟的使用）

---

```yaml
  Skills:
  - skill{s=[
    - message{m="Hello there! A pleasure to meet you!"}
    - setvariable{var=skill.examplename;type=STRING;val=<target.name>}
    - skill{s=[
      - message{m="OHI, OHI! WHO IS THAT GUY OVER THERE NAMED <skill.var.examplename>?!?"}
      ]} @Owner
    ]} @target
```

> 此示例展示了如何嵌套内联元技能，以及它们如何共享同一[技能树](skilltrees.md)，从而使用技能作用域变量

---

```yaml
  Skills:
  - skill{branch=true;s=[
    - message{m="1"}
    <#>- message{m="2"}
    - message{m="3"}
    ];executeafterdeath=true} @trigger
```

> 在此示例中，你可以看到如何从内联 Metaskill 中注释掉技能机制，以及如何在调用 Metamechanic 中正常使用普通属性

# 技能参数 [Premium 版功能] {#skill-parameters-premium-feature}

技能参数是一项功能，可让你更轻松地创建通用技能并将参数从其他技能传递给它们。如果这听起来令人困惑，这里有一个例子！

目前，大多数人会为各种生物编写许多相似的伤害技能，只稍微调整伤害差异，其他方面的作用基本相同。

**旧的做法：**

```yaml
#SKILL FILE
ShadowDamage20:
  Skills:
  - damage{amount=20}
  - some shadowy effect

#MOB FILE
Mob1:
  Skills:
  - skill{s=ShadowDamage20} ~onAttack
```

**借助技能参数，可以将这些技能合并为单个技能！新的做法：**

```yaml
#SKILL FILE
ShadowDamage:
  Skills:
  - damage{amount=<skill.damage>}

#MOB FILE
Mob1:
  Skills:
  - skill{s=ShadowDamage;damage=20} ~onAttack
```

上例仍造成 20 点伤害，但现在技能已经通用化，可以为任意生物调整伤害。技能参数系统会将 **skill/metaskill** 机制中除自身专用选项以外的**全部选项**传入技能树，供之后引用。如果后续技能传入同名参数，会覆盖原值。这些参数可用于所有支持占位符的位置。

> 技能参数可以从[技能](mechanics/skill.md)和[变量技能](mechanics/variableskill.md)机制中使用

## 保留的参数名称 {#reserved-parameter-names}

以下名称，无论大小写，*不能*用作技能参数

- `skill`
- `s`
- `meta`
- `m`
- `mechanics`
- `cooldown`
- `cd`
- `delay`
- `repeat`
- `targetinterval`
- `targeti`
- `repeatinterval`
- `repeati`
- `power`
- `powersplitbetweentargets`
- `powersplit`
- `splitpower`
- `forcesync`
- `sync`
- `targetisorigin`
- `sourceisorigin`
- `castfromorigin`
- `fromorigin`
- `fo`
- `origin`
- `branch`
- `fork`
- `snapshotcasterstats`
- `snapshotstats`
- `scs`
- `snapshottriggerstats`
- `sts`
- `targetcreative`

# 自定义命令 {#custom-commands}

可以使用元技能创建[技能命令](skill-commands.md)
