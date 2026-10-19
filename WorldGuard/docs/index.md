---
title: WorldGuard
source_kind: plugin-overview
translation_review: reviewed
---

# WorldGuard

WorldGuard 提供区域保护、区域规则和全局保护设置，可限制区域内的建造、PvP、TNT 等行为，也可通过黑名单限制特定方块、物品及操作。

随包版本：`7.0.17+2370-e42d8bc`。对应发布提交为 `e42d8bcda767c1e57f6ca801d088535a9f0783b3`。

## 前置要求

需要支持 Bukkit API 的服务器，例如 Spigot 或 Paper，并且必须安装 **WorldEdit 的 Bukkit 版**。官方安装页明确要求 Bukkit 版 WorldEdit；对应构建也声明 `depend: [WorldEdit]`，没有列出其他必需或软依赖插件。

## 常用命令与权限

区域命令可使用 `/region` 或 `/rg`。创建区域时使用当前的 WorldEdit 选区；下面列出基本形式，完整选项见官方命令页。

| 命令 | 用途 | 相关权限 |
| --- | --- | --- |
| `/rg define <id>` | 用当前选区创建区域，可追加所有者 | `worldguard.region.define` |
| `/rg list` | 列出区域 | `worldguard.region.list`；只列自身相关区域可用 `worldguard.region.list.own` |
| `/rg info [<id>]` | 查看区域信息 | `worldguard.region.info.*` |
| `/rg addmember <id> <members...>` | 添加区域成员 | `worldguard.region.addmember.*` |
| `/rg addowner <id> <owners...>` | 添加区域所有者 | `worldguard.region.addowner.*` |
| `/rg remove <id>` | 删除区域 | `worldguard.region.remove.*` |
| `/wg reload` | 重载 WorldGuard 配置 | `worldguard.reload` |

命令与权限分别依据[区域命令页][WG-CMD]、[管理命令页][WG-GENERAL]和[权限页][WG-PERM]。区域权限还支持具体区域、所有者 `.own.` 和成员 `.member.` 的形式；表中的 `*` 用法需要权限系统支持通配符。

若删除的区域有子区域，必须指定 `-u` 或 `-f`，两者不得同时使用：`-u` 让子区域不再拥有父区域，`-f` 会连同子区域一起删除。

设置旗标的用法为 `/rg flag <id> <flag> [-w <world>] [-g <group>] [-e] [<value>]`。不提供值表示取消设置；`-e` 表示设置为空值。旗标权限分别控制可修改的区域和可设置的旗标/值，例如 `worldguard.region.flag.regions.own.*` 与 `worldguard.region.flag.flags.use.*`。

## 配置说明

[查看配置文件中文说明](configuration/index.md)。按世界设置的选项会覆盖主配置中对应的设置，未覆盖的选项继承主配置；相关说明见[官方配置页][WG-CONFIG]。黑名单语法见 [黑名单说明][WG-BLACKLIST]。

## 官方资料

- [WorldGuard 官方文档][WG-INTRO]
- [WorldGuard 官方仓库](https://github.com/EngineHub/WorldGuard)
- [7.0.17 对应构建的插件描述文件][WG-PLUGIN]
- [官方安装说明][WG-INSTALL]
- [7.0.17 发布提交][WG-RELEASE]

[WG-INTRO]: https://worldguard.enginehub.org/en/latest/
[WG-BLACKLIST]: https://worldguard.enginehub.org/en/latest/blacklist/
[WG-RELEASE]: https://github.com/EngineHub/WorldGuard/commit/e42d8bcda767c1e57f6ca801d088535a9f0783b3
[WG-INSTALL]: https://worldguard.enginehub.org/en/latest/install/
[WG-PLUGIN]: https://github.com/EngineHub/WorldGuard/blob/e42d8bcda767c1e57f6ca801d088535a9f0783b3/worldguard-bukkit/src/main/resources/plugin.yml
[WG-CMD]: https://worldguard.enginehub.org/en/latest/regions/commands/
[WG-GENERAL]: https://worldguard.enginehub.org/en/latest/commands/
[WG-PERM]: https://worldguard.enginehub.org/en/latest/permissions/
[WG-CONFIG]: https://worldguard.enginehub.org/en/latest/config/
