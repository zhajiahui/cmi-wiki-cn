---
title: NeigeItems 概览来源
source_kind: plugin-overview
translation_review: reviewed
---

# NeigeItems 1.22.0 概览来源

核对日期：2026-10-19。固定来源为[官方 1.22.0 标签](https://github.com/ankhorg/NeigeItems-Kotlin/tree/1.22.0)，提交为 8791487eeec1866b30f45c34a60fbc0e738c9ecf。以下文件均取得实际正文。

## 官方仓库与简介

公开链接：[README](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/README.md)。

原文摘录：

> A bukkit item manage plugin.
>
> Javadoc: https://ankhorg.github.io/NeigeItems-Kotlin/

官方 README 另说明 Wiki 为付费资料。本次没有确认公开的当前版本 Wiki 地址，故未将历史站点作为当前官方 Wiki。

物品包、物品动作、函数、JavaScript 扩展的范围，分别由此标签中的 ItemPacks、ItemActions、Functions、Expansions 目录及自带中文帮助确认。

## 官方中文帮助

公开链接：[src/main/resources/config.yml](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/config.yml)。原文已是中文，概览保留其命令、参数及说明。

原文摘录：

```yaml
get:
  command: §e/ni §fget [物品ID] (数量) (是否反复随机) (指向数据)
  description: 根据ID获取NI物品
give:
  command: §e/ni §fgive [玩家ID] [物品ID] (数量) (是否反复随机) (指向数据)
  description: 根据ID给予NI物品
givePack:
  command: §e/ni §fgivePack [玩家ID] [物品包ID] (数量) (指向数据)
  description: 根据ID给予NI物品包
save:
  command: §e/ni §fsave [物品ID] (保存路径)
  description: 将手中物品以对应ID保存至对应路径
reload:
  command: §e/ni §freload
  description: 重新加载NI物品
```

同文件的帮助前缀说明 `[]为必填, ()为选填`，并列出 `/ni help (页数)` 和 `/ni list (页码)`。

## 命令与权限的源码核对

公开链接：[Command.kt](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/kotlin/pers/neige/neigeitems/command/Command.kt)。

原文关键行：

```kotlin
private val COMMAND_NAME = NeigeItems::class.java.simpleName.lowercase()
permission = "$COMMAND_NAME.command"
```

同文件通过类名中的大写字母构造别名。因此注册的根命令是 `neigeitems`，别名为 `ni`，根权限为 `neigeitems.command`。这些内容由运行时注册，不能因为 plugin.yml 没有 commands/permissions 段就省略。

另取得 [Give.kt](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/kotlin/pers/neige/neigeitems/command/subcommand/Give.kt)和 [Reload.kt](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/kotlin/pers/neige/neigeitems/command/subcommand/Reload.kt)。前者确认 get/give 参数顺序；后者使用 ReloadTypeArgument，但中文帮助未列类型参数，概览未补造枚举。

## 官方依赖声明

公开链接：[plugin.yml](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/plugin.yml)。

原文摘录：

```yaml
softdepend:
  - 'ProtocolLib'
  - 'PlaceholderAPI'
  - 'MythicMobs'
  - 'Oraxen'
  - 'Vault'
  - 'MagicGem'
  - 'ItemsAdder'
```

该文件没有声明 depend，与随包版本一致。随包版本号 1.22.0 与官方固定标签一致；没有进行服务器或客户端运行验证。
