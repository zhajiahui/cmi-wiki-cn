---
title: Sudo Skill
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SudoSkill
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Sudo Skill {#sudo-skill}

## 说明 {#description}

SudoSkill机制允许你强制目标实体“施放”MythicMobs[Metaskill](../metaskills.md)，即使目标实体是玩家。没有任何单一机制可以直接使用：它们必须位于[元技能](../metaskills.md)中！

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| setcasterastrigger | cat | 将被调用元技能的触发者设为此机制的施法者 | false |
| target | t | 将被调用元技能继承的目标设为指定目标 |  |
| chained | chain | 是否让机制的各个目标*依次*施放指定元技能，每次都以上一次的施法者为目标 | false |

> 该机制继承了[技能](skill.md)机制的所有属性

### SetCasterAsTrigger 属性 {#setcasterastrigger-attribute}

`setcasterastrigger` 为 `true` 时，技能触发实体设为 sudoskill 的施法者；否则触发实体就是技能的施法者。

```yaml
  Skills:
  - SudoSkill{s=SkillName;setcasterastrigger=true}
```

### Chained 属性 {#chained-attribute}

前面的一行文字并不足以完全解释正在发生的事情。那么，让我们用一个实际的例子来实现这一点。   鉴于：

- `iteration` 是一个数字，用于跟踪要在其上执行 sudoskill 的实体列表中的“我们在哪里”
- `caster` 是任何给定迭代中 sudoed 元技能的施法者
- `target` 是任何给定迭代中 sudoed 元技能的目标

```yaml
  Skills:
  - sudoskill{chained=true;skill=Example} @EIR{limit=3;radius=10}
```

施法者：`Player`
目标：`Mob_A`、`Mob_B`、`Mob_C`

| 迭代 | 施法者 | 目标 |
| --- | --- | --- |
| 0 | Mob_A | Player |
| 1 | Mob_B | Mob_A |
| 2 | Mob_C | Mob_B |

## 示例 {#examples}

```yaml
# Mob File
SudoMonkey:
  Type: villager
  Display: 'a Villager'
  Skills:
  - sudoskill{s=ExampleSudoskill;cat=true} @trigger ~onDamaged
```

```yaml
# Skills file
ExampleSudoskill:
  Skills:
  - arrowvolley{a=20;s=25;v=10;f=50;rd=200} @EIR{r=30}
  - message{msg="Triggername<&co> <trigger.name>"} @world
```

##  {#section}

该元技能将使施法者周围20方块半径内的每个实体都召唤粒子效果。由于`target`属性，元技能的继承目标将是在30方块半径内距离施法者最近的玩家

```yaml
ExampleTargetSkill:
  Skills:
  - sudoskill{
    target=@NearestPlayer{r=30};
    s=[
      - effect:particles
    ]} @EIR{r=20}
```

## 别名 {#aliases}

- sudo
