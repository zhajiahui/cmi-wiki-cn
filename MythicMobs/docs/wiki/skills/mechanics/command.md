---
title: 命令
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/command
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 命令

# Command {#command}

## 说明 {#description}

为提供的每个目标执行命令。

允许使用[颜色代码](../placeholders.md#color-codes)和[变量](../variables.md)。

如果指定的命令包含双引号 " 或大括号 {}，则该命令将无法正常运行，并且必须用各自的[消息变量](../placeholders.md#special-characters) 替换。发生这种情况是因为双引号和大括号是为 MythicMobs 本身尝试读取你提供的语法而保留的。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| command | c, cmd | 要执行的命令 |  |
| asCaster | ac, caster, sudo, asmob | 为 true 时，命令由施法者执行，而不是控制台。 | false |
| asOp | op | 是否以全部权限执行命令。 | false |
| asTarget | at, target, sudotarget | 以目标实体的身份执行命令。 | false |
| requireTarget | rt | 仅在技能具有目标时执行。 | asTarget 的值 |

## 示例 {#examples}

### 正确编写的命令技能 {#correctly-written-command-skills}

```yaml
  Skills:
  - command{c="give <target.name> gold_ingot 20"} @trigger ~onInteract
  - command{c="minecraft:tp <target.name> <mob.uuid>"} @self ~onDamaged
  - command{c="say HELLO <target.name>";asTarget=true;asOp=true} @NearestPlayer{r=10}
```

### 无效的命令技能 {#invalid-command-skills}

下面的示例将不起作用，因为某些符号尚未替换为消息变量。

```yaml
  Skills:
  - command{c="minecraft:summon Zombie ~ ~ ~ {NoAI:true,CustomName:"Summoned Zombie"}"}
```

> 在这种特定情况下，`~`符号是一个问题：虽然通常，在普通版本中，它仅表示“正在执行命令的位置”，但对于这种特定设置来说这是不可能的，因为它是正在执行命令的控制台，因此没有可以使用的“位置”。解决此问题的一种方法是使用 `<caster.l.x>`、`<caster.l.y>` 和 `<caster.l.z>` 占位符

### 让玩家执行命令 {#making-a-player-execute-a-command}

此示例将为与生物交互的玩家执行“say”命令

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - command{c="say <target.name>";asTarget=true;asOp=true} @trigger ~onInteract
```

## 别名 {#aliases}

- cmd
