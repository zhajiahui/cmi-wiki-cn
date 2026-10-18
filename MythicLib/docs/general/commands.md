---
title: 命令
source: https://docs.phoenixdevt.fr/mythiclib/general/commands
source_snapshot: '2026-10-19'
---

# 命令 {#💾-commands}

|命令 |描述 |
| --- | --- |
| `/ml reload` | 重新加载插件和配置文件。 |
| `/ml damage <source> <target> <value>` | 强制源玩家对目标实体（名称或UUID）造成伤害 |
| `/ml stat [...]` | 详见[此页](../features/stats.md#using-commands)。 |
| `/ml debug cast <skill_id>` | 调试命令以使用给定的ID投射技能。 |
| `/ml debug logs` | 将最新服务器日志转储到`mclo.gs` |
| `/ml debug stats <player>` | 打开GUI来探索目标玩家的属性 |
| `/ml debug attributes <player>` | 打开GUI来探索目标玩家的基础属性 |
| `/ml debug versions` | 转储插件版本以进行聊天 |
| `/ml debug healthscale set <amount> <player>` | 设置给定玩家的生命值比例 |
| `/ml debug healthscale reset <player>` | 重置给定玩家的生命值比例 |
| `/ml debug test` | 开发者命令，请勿使用 |
| `/ml debug parse ` | 开发者命令，请勿使用 |

## 命令配置 {#command-config}

> **警告**
>
> 目前仅适用于MythicLib和MMOCore。

MMO 插件允许你编辑本机插件命令的基本信息，包括名称、描述、用法、别名和权限。所有这些选项都可以在位于主插件文件夹中的`commands.yml`文件中进行编辑。

以下以`MMOCore/commands.yml`文件的内容为例：

```yml
mmocore:
  verbose: PLAYER
cast:
  main: cast
  aliases: []
  description: 'Enter casting mode'
  permission: 'mmocore.cast'
  verbose: ALL
player:
  main: player
  aliases: [ p, profile ]
  description: 'Displays player stats'
  permission: 'mmocore.profile'
  verbose: ALL

# [...]
```

`main`选项定义命令名称或标签。如果设置为`player`，则玩家必须键入`/player`才能执行命令。`aliases`选项允许你为同一命令定义替代标签。在上面的示例中，玩家还可以键入`/p`或`/profile`来执行与`/player`相同的命令。

`permission`选项定义执行命令所需的权限。在上例中，只有玩家和`mmocore.profile`权限才能执行`/player`命令。

## 命令详细 {#command-verbose}

> **警告**
>
> 目前仅适用于MythicLib和MMOCore。

在同一个配置文件中，你还可以为每个命令定义`verbose`等级。此选项允许你控制命令执行消息的发送位置。有多个可用的详细等级：

| Level | 描述 |
| --- | --- |
| `ALL` | 消息被发送到玩家和控制台。 |
| `PLAYER` | 消息仅发送到执行命令的玩家。此模式可避免使用`/ml stat add`等命令时控制台垃圾邮件。 |
| `CONSOLE` | 消息仅发送到控制台。 |
| `REDIRECT_TO_CONSOLE` | 所有消息都会发送到控制台。这对于记录重要的命令执行非常有用。 |
| `NONE` | 没有发送任何消息。 |

例如，以下代码片段将主`/mythiclib`命令及其所有子命令的详细等级设置为`PLAYER`。

```yml
# MythicLib/commands.yml
mythiclib:
  verbose: PLAYER
```

---

原文：[💾 Commands](https://docs.phoenixdevt.fr/mythiclib/general/commands) · 原文归档：2026-10-19
