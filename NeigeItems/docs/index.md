---
title: NeigeItems 插件简介
source_kind: plugin-overview
translation_review: reviewed
---

# NeigeItems

NeigeItems 是 Bukkit 物品管理插件，可按 ID 获取、给予和保存物品，并提供物品包、物品动作、函数及 JavaScript 扩展。上述内容见[官方仓库](https://github.com/ankhorg/NeigeItems-Kotlin/tree/1.22.0)和[该版本自带的中文帮助](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/config.yml)。

本次随包版本为 **1.22.0**。以下内容固定参考官方 `1.22.0` 标签，对应提交 `8791487eeec1866b30f45c34a60fbc0e738c9ecf`。

## 依赖

随包版本及官方 `1.22.0` 的 [plugin.yml](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/plugin.yml)均没有声明必需插件。

软依赖为 ProtocolLib、PlaceholderAPI、MythicMobs、Oraxen、Vault、MagicGem、ItemsAdder。

## 核心命令和权限

以下保留该版本官方中文帮助中的写法：**`[]` 为必填，`()` 为选填**。

| 命令 | 官方说明 |
| --- | --- |
| `/ni help (页数)` | 查看帮助信息 |
| `/ni list (页码)` | 查看所有NI物品 |
| `/ni get [物品ID] (数量) (是否反复随机) (指向数据)` | 根据ID获取NI物品 |
| `/ni give [玩家ID] [物品ID] (数量) (是否反复随机) (指向数据)` | 根据ID给予NI物品 |
| `/ni givePack [玩家ID] [物品包ID] (数量) (指向数据)` | 根据ID给予NI物品包 |
| `/ni save [物品ID] (保存路径)` | 将手中物品以对应ID保存至对应路径 |
| `/ni reload` | 重新加载NI物品 |

根命令为 `/neigeitems`，别名为 `/ni`。根权限为 **`neigeitems.command`**，依据该版本 [Command.kt 的命令注册代码](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/kotlin/pers/neige/neigeitems/command/Command.kt)核实。

## 官方资料

- [官方仓库的 1.22.0 标签](https://github.com/ankhorg/NeigeItems-Kotlin/tree/1.22.0)
- [1.22.0 自带中文配置与帮助](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/config.yml)
- [官方 Javadoc](https://ankhorg.github.io/NeigeItems-Kotlin/)

官方 README 说明 Wiki 为付费资料；本页未将历史站点当作当前公开 Wiki。

[查看配置文件及中文说明](configuration/index.md)。
