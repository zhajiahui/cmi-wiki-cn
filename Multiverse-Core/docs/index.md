---
title: Multiverse-Core
source_kind: plugin-overview
translation_review: reviewed
---

# Multiverse-Core

Multiverse-Core 用于管理多个世界，可创建、导入、加载和卸载世界，并管理世界属性、出生点及传送。

随包版本：`5.8.1`。本页命令与权限已对照该版本对应的源码提交 `4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be`。

## 前置要求

Multiverse-Core 是 Bukkit 多世界插件。本版本没有声明必须安装的其他插件，`Vault` 和 `PlaceholderAPI` 为可选软依赖。

官方安装页将权限插件列为可选前置。Multiverse 的子插件需要 Core，各子模块应使用相同的大版本；Multiverse-Portals 和 Multiverse-NetherPortals 可按需要安装。

## 常用命令与权限

| 命令基本形式 | 用途 | 相关权限 |
| --- | --- | --- |
| `/mv list` | 列出世界 | `multiverse.core.list.worlds` |
| `/mv info [world]` | 查看世界信息 | `multiverse.core.info` |
| `/mv create <name> <environment>` | 创建世界 | `multiverse.core.create` |
| `/mv import <name> <environment>` | 导入世界 | `multiverse.core.import` |
| `/mv teleport [player] <destination>`，也可用 `/mvtp` | 传送到指定目的地 | 区分 `multiverse.teleport.self.<type>` 与 `multiverse.teleport.other.<type>` |
| `/mv spawn [player]`，也可用 `/mvspawn` | 传送到世界出生点 | 区分 `multiverse.core.spawn.self` 与 `multiverse.core.spawn.other` |
| `/mv setspawn`，也可用 `/mvsetspawn` | 设置世界出生点 | `multiverse.core.spawn.set` |
| `/mv reload` | 重载配置 | `multiverse.core.reload` |

启用细分传送权限后，传送权限还会追加目标后缀，出生点传送权限会追加世界名。例如 `multiverse.teleport.self.w.world2` 与 `multiverse.core.spawn.self.<worldname>`。完整规则见[权限页][MV-PERM]和[配置参考][MV-CONFIG]。

世界访问权限为 `multiverse.access.<worldname>`；绕过世界游戏模式限制使用 `mv.bypass.gamemode.<worldname>`。两个节点的前缀不同，不要相互替换。是否检查访问权限由相应配置控制。

## 配置说明

[查看配置文件中文说明](configuration/index.md)。全局设置见 [官方配置参考][MV-CONFIG]，世界属性见 [世界属性说明][MV-PROPS]。运行期间手动修改配置后，按原注释执行 `/mv reload`；标为需要重启的选项仍需重启服务器。

## 官方资料

- [Multiverse-Core 官方文档][MV-INTRO]
- [Multiverse-Core 官方命令参考][MV-CMD]
- [Multiverse-Core 官方仓库](https://github.com/Multiverse/Multiverse-Core)
- [5.8.1 对应源码的插件描述文件][MV-PLUGIN]
- [官方安装说明][MV-INSTALL]
- 世界管理命令源码：[世界列表][MV-LIST]、[世界信息][MV-INFO]、[创建世界][MV-CREATE]、[导入世界][MV-IMPORT]
- 传送与配置命令源码：[传送][MV-TP]、[出生点传送][MV-SPAWN]、[设置出生点][MV-SETSPAWN]、[重载配置][MV-RELOAD]
- 权限源码：[节点定义][MV-CONSTANTS]、[世界访问与传送检查][MV-CHECK]

[MV-PLUGIN]: https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/resources/plugin.yml
[MV-CMD]: https://mvplugins.org/core/fundamentals/commands-usage/
[MV-PROPS]: https://mvplugins.org/core/fundamentals/world-properties/
[MV-CREATE]: https://github.com/Multiverse/Multiverse-Core/blob/5.8.1/src/main/java/org/mvplugins/multiverse/core/commands/CreateCommand.java
[MV-INSTALL]: https://mvplugins.org/core/fundamentals/installation/
[MV-LIST]: https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/ListCommand.java
[MV-INFO]: https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/InfoCommand.java
[MV-IMPORT]: https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/ImportCommand.java
[MV-TP]: https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/TeleportCommand.java
[MV-CHECK]: https://github.com/Multiverse/Multiverse-Core/blob/5.8.1/src/main/java/org/mvplugins/multiverse/core/permissions/CorePermissionsChecker.java
[MV-SPAWN]: https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/SpawnCommand.java
[MV-SETSPAWN]: https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/SetSpawnCommand.java
[MV-RELOAD]: https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/ReloadCommand.java
[MV-PERM]: https://mvplugins.org/core/reference/permissions-list/
[MV-CONFIG]: https://mvplugins.org/core/reference/configuration-file/
[MV-CONSTANTS]: https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/permissions/CorePermissions.java
[MV-INTRO]: https://mvplugins.org/core/
