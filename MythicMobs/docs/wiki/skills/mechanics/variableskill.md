---
title: Variableskill
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/variableskill
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variableskill {#variableskill}

## 说明 {#description}

执行另一个元技能，例如[技能机制](skill.md)，但允许在技能属性内使用占位符。   属性“sync=  true  ”将被任何子技能继承，并且不能在技能树中稍后设置为*  false  *。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| skill | s, $, (), m, mechanics, meta | 要执行的元技能，接受[占位符](../placeholders.md) |  |
| forcesync | sync | 是否强制技能与 Minecraft 同步执行 | false |
| branch | b, fork, f | 被调用元技能的技能树是否从调用机制的技能树中[分出分支](skill.md#branch-attribute) | false |
| executeafterdeath | continueafterdeath | 施法者死亡后是否仍可调用此元技能 | false |
| variable | var | 提供待执行元技能的 MetaSkill 变量。设置后忽略 `skill` |  |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - vskill{s=ExampleSkill_<random.1to3>} @self

ExampleSkill_1:
  Skills:
  - effect:particles{particle=reddust;color=#FF0000;amount=10}
ExampleSkill_2:
  Skills:
  - effect:particles{particle=reddust;color=#FFFFFF;amount=10}
ExampleSkill_3:
  Skills:
  - effect:particles{particle=reddust;color=#00FF00;amount=10}
```

在示例中，`ExampleSkill`元技能一旦触发，将执行名称由`ExampleSkill_`和1到3之间随机生成的数字组成的技能。

##  {#section}

```yaml
Example_StanceSkill:
  Skills:
  - vskill{s=ExampleMob_<caster.stance>_<random.1to2>} @self
```

本例用 VariableSkill 根据姿态快速调用技能，无需使用姿态条件。

##  {#section-2}

```yaml
Example_VariablePlaceholder:
  Skills:
  - vskill{s=Fireball_<skill.var.fireballtype>} @self
```

在此示例中，VariableSkill 机制会执行一个元技能，其名称取决于此前设置的技能作用域变量

## 别名 {#aliases}

- metavariableskill
- vskill
