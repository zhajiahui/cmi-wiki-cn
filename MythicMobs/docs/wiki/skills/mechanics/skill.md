---
title: Skill
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Skill
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Skill {#skill}

## 说明 {#description}

执行另一个[元技能](../metaskills.md)，该元技能必须位于 */MythicMobs/Skills*。如果未指定目标选择器，被执行的技能会继承目标。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| skill | s, $, (), m, mechanics, meta, spell | 要执行的元技能 |  |
| forcesync | sync | 是否强制技能与 Minecraft 同步执行 | false |
| branch | b, fork, f | 被调用元技能的技能树（skilltree）是否从调用机制的技能树分出独立分支。分支最初会复制原技能树，但对分支的修改不会影响原技能树 | false |
| executeafterdeath | continueafterdeath | 施法者死亡后是否仍可调用此元技能 | false |
| snapshotcasterstats | snapshotstats, scs | 是否缓存技能执行时施法者的属性，使后续每次检查或获取都返回当时保存的值。元技能包含较长延迟、且施法者属性可能在技能执行期间变化时，此项会有用 | false |

### Branch 属性 {#branch-attribute}

每次从生物文件通过触发器触发技能，都会创建 `SkillTree`。`SkillTree` 保存许多信息，包括[技能作用域变量](../variables.md#variable-scopes)、[技能参数](../metaskills.md#skill-parameters-premium-feature)及其值。

同一技能树中的任何机制或元技能，都能访问这些值，但它们也具有**唯一性**：同一 `SkillTree` 中，同名的 `Skill Scoped Variable` 或 `Skill Parameter` 只能有一个，重复设置会覆盖原值。

##  {#section}

```yaml
TestSkill_1:
  Skills:
  - setvariable{var=skill.sharedvalue;val=1}
  - skill{s=TestSkill_2}
  - skill{s=TestSkill_3}
  - message{m="<skill.var.sharedvalue>"} @World

TestSkill_2:
  Skills:
  - setvariable{var=skill.sharedvalue;val=2}

TestSkill_3:
  Skills:
  - setvariable{var=skill.sharedvalue;val=3}
```

> 在本例中，你可以看到这一切是如何实现的：技能作用域变量的值在所有调用的元技能上设置，但由于技能树只有一个，因此该值被覆盖多次，直到最后返回值“3”

##  {#section-2}

`branch` 属性会改变上述行为（不再为   true  ）：在 skill 机制中将它设为   true  ，会为调用的元技能创建全新的 `SkillTree`，不共享技能作用域变量或技能参数。

```yaml
TestSkill_1:
  Skills:
  - setvariable{var=skill.sharedvalue;val=1}
  - skill{s=TestSkill_2}
  - skill{s=TestSkill_3;branch=true}
  - message{m="<skill.var.sharedvalue>"} @World

TestSkill_2:
  Skills:
  - setvariable{var=skill.sharedvalue;val=2}

TestSkill_3:
  Skills:
  - setvariable{var=skill.sharedvalue;val=3}
```

> 此示例与前一个示例类似，但调用 TestSkill_3 MetaSkill 的行除外：由于分支属性设置为   true  ，因此该变量设置在另一技能树上，而原始技能树对此没有“任何了解”。因此，最终打印的值将是“2”

## 示例 {#examples}

```yaml
  Skills:
  - skill{skill=AnotherSkill} @Target ~onAttack
  - skill{s=AnotherSkill} @Trigger ~onSpawn
  - skill:OtherSkill @Trigger ~onDeath
```

属性“sync=  true  ”将被任何子技能继承，并且不能在技能树中稍后设置为*  false  *。

##  {#section-3}

```yaml
  Skills:
  - skill{s=AnotherSkill;sync=true} @Target ~onAttack
  - skill{s=ice_bolt;sync=true} @Target ~onTimer:100
  - skill{sync=true;s=flamethrower} @TargetLocation ~onTimer:200
  - skill:Onemechainc @Target ~onDamaged
  - skill{
      skill=leafs;
      sync=true
      }
```

## 别名 {#aliases}

- metaskill
- meta
