---
title: ItemsAdder 插件简介
source_kind: plugin-overview
translation_review: reviewed
---

# ItemsAdder

ItemsAdder 用于配置和创建自定义物品及资源包内容。[官方文档](https://wiki.itemsadder.com/)分别介绍物品、方块、家具、实体、字体图片、HUD、音乐和音效等内容。

本次随包版本为 **4.0.18**。官方 Wiki 持续更新，下面仅列基础命令和已核实的依赖信息。

## 依赖

必需插件为 **ProtocolLib**，与随包版本的声明及[官方安装说明](https://wiki.itemsadder.com/plugin-usage/first-install/)一致。

官方说明 **4.0.9 及以上版本不再必需 LoneLibs**，因此 LoneLibs 不是本次 4.0.18 的必需插件。

随包版本声明的软依赖为 ViaVersion、WorldGuard、GriefPrevention、Towny、Essentials、Realistic_World、EpicWorldGenerator、EpicNetherGenerator、Skript、MythicMobs、PlaceholderAPI、PermissionsEx、LuckPerms、Vault、MMOItems、Slimefun、Orebfuscator、ExecutableItems、Mimic、Citizens、ItemBridge、ModelEngine、Denizen、Vulcan。

## 核心命令和权限

以下依据[官方命令表](https://wiki.itemsadder.com/plugin-usage/plugin-configuration/commands/)。

| 命令 | 用途 | 权限 |
| --- | --- | --- |
| `/ia` | 打开物品列表界面 | `ia.user.ia` |
| `/iaget <item> [amount]` | 按带命名空间的 ID 或 ID 获取物品 | `ia.admin.iaget` |
| `/iareload` | 重载配置 | `ia.admin.iareload` |
| `/iazip` | 执行 `/iareload` 并生成资源包 | `ia.admin.iazip` |
| `/iatexture` | 让客户端重新加载资源包 | `ia.user.iatexture` |
| `/iatexture [all\|player]` | 为所有玩家或指定玩家重新加载资源包 | `ia.user.iatexture.all` |
| `/iarecipe [item]` | 打开配方界面 | `ia.user.iarecipe` |

[官方权限页](https://wiki.itemsadder.com/plugin-usage/plugin-configuration/permissions/)另列出配方权限 `ia.user.recipe.PERMISSION`、物品列表显示权限 `ia.user.ia.seeitem.PERMISSION` 和搜索权限 `ia.user.ia.search`。前两种权限可使用对应的 `.*` 形式；官方要求使用支持此通配写法的权限插件，例如 LuckPerms。

## 官方资料

- [官方 Wiki](https://wiki.itemsadder.com/)
- [安装说明](https://wiki.itemsadder.com/plugin-usage/first-install/)
- [命令](https://wiki.itemsadder.com/plugin-usage/plugin-configuration/commands/)
- [权限](https://wiki.itemsadder.com/plugin-usage/plugin-configuration/permissions/)
- [官方默认资源包仓库](https://github.com/ItemsAdder/DefaultPack)

[查看配置文件及中文说明](configuration/index.md)。
