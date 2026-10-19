---
title: Citizens
source_kind: plugin-overview
translation_review: reviewed
---

# Citizens

Citizens 是基于 Bukkit API 的 NPC 插件，提供 NPC 的创建、选择、外观设置和行为功能，并提供供其他插件使用的 API。

随包真实版本：`2.0.43-SNAPSHOT (build 4210)`。官方构建 4210 的产物为 `Citizens-2.0.43-b4210.jar`，对应源码提交为 `3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2`。

## 前置要求

Citizens 使用 Bukkit API。本构建没有声明必须安装的其他 Bukkit 插件；以下插件为可选软依赖：`Vault`、`PlaceholderAPI`、`WorldGuard`、`packetevents`、`Denizen`。描述文件还声明 Citizens 在 Denizen 之前加载。

## 常用命令与权限

`/npc` 根命令的入口权限为 `citizens.npc.help`，`/citizens` 根命令的入口权限为 `citizens.citizens.help`；子命令还会检查各自的权限及适用的 NPC 所有权。下表列出基本形式，未展开所有参数。

| 命令 | 用途 | 相关权限或检查 |
| --- | --- | --- |
| `/npc create [name]` | 创建 NPC | `citizens.npc.create` |
| `/npc select`，子命令别名 `sel` | 按 ID 或名称选择 NPC | `citizens.npc.select` |
| `/npc list` | 列出 NPC | `citizens.npc.list` |
| `/npc skin` | 设置 NPC 皮肤 | `citizens.npc.skin` |
| `/npc lookclose` | 切换 NPC 是否注视附近玩家 | `citizens.npc.lookclose` |
| `/npc tp` | 传送到 NPC 前方 | `citizens.npc.tp` |
| `/npc tphere` | 将 NPC 传送到自己所在位置 | `citizens.npc.tphere` |
| `/npc remove` | 删除已选中的 NPC | `citizens.npc.remove` 或 `citizens.admin`，并检查所有权 |
| `/npc remove all` | 删除所有 NPC | `citizens.admin.remove.all` 或 `citizens.admin` |
| `/citizens reload` | 重载 Citizens | `citizens.admin` |
| `/citizens save` | 保存 NPC 和配置 | `citizens.admin` |
| `/trait` | 特征相关命令入口 | `citizens.trait.help` |
| `/waypoints`，别名 `/wp` | 路径点命令入口 | `citizens.waypoints.help` |
| `/template`，别名 `/tpl` | 模板命令入口 | `citizens.templates.help` |

NPC 子命令及删除权限已对照[构建 4210 的 NPC 命令源码][C-NPC]，管理命令已对照 [管理命令源码][C-ADMIN]；命令用途也可查[官方命令页][C-CMD]。`/npc remove` 的其他参数分支有各自检查，完整用法应查看对应构建源码。

## 配置说明

[查看配置文件中文说明](configuration/index.md)。官方配置参考为 [官方配置参考][C-CONFIG]，本构建设置及其原生注释见 [配置项与原生注释][C-SETTINGS]。

## 官方资料

- [Citizens 官方站点](https://www.citizensnpcs.co/)
- [Citizens 官方 Wiki][C-INTRO]
- [Citizens 官方仓库](https://github.com/CitizensDev/Citizens2)
- [官方构建 4210][C-BUILD]
- [构建 4210 的插件描述文件][C-PLUGIN]

[C-INTRO]: https://wiki.citizensnpcs.co/Main_Page
[C-CMD]: https://wiki.citizensnpcs.co/Commands
[C-BUILD]: https://ci.citizensnpcs.co/job/Citizens2/4210/
[C-PLUGIN]: https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/resources/plugin.yml
[C-NPC]: https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/java/net/citizensnpcs/commands/NPCCommands.java
[C-ADMIN]: https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/java/net/citizensnpcs/commands/AdminCommands.java
[C-CONFIG]: https://wiki.citizensnpcs.co/Configuration
[C-SETTINGS]: https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/java/net/citizensnpcs/Settings.java
