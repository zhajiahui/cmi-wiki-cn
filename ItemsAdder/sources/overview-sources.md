---
title: ItemsAdder 概览来源
source_kind: plugin-overview
translation_review: reviewed
---

# ItemsAdder 概览来源

核对日期：2026-10-19。随包版本为 4.0.18。旧入口 itemsadder.devs.beer 在本次访问中重定向至 wiki.itemsadder.com。

## 官方介绍与安装

公开链接：[官方首页](https://wiki.itemsadder.com/)、[First Install](https://wiki.itemsadder.com/plugin-usage/first-install/)。均已取得正文。

首页原文摘录：

> This website helps you configure and create custom items for my plugin.

首页文档导航包含 Items、Blocks、Furnitures、Entities、Font Images / Glyphs、Font HUDs、Music & Sounds 等分类，用于概览中的内容范围。

安装页原文摘录：

> v3 is only for 1.20.4 and lower
>
> v4 is only for 1.20.6 and greater
>
> Put ProtocolLib JAR inside the plugins folder
>
> Put LoneLibs JAR inside the plugins folder (not required on 4.0.9 and greater)

因此，ProtocolLib 是本次版本的必需插件；LoneLibs 不应再列为 4.0.18 的必需插件。

安装页直接链接 [ItemsAdder/DefaultPack](https://github.com/ItemsAdder/DefaultPack)。本次仅据此确认官方资源仓库入口，未继续抓取仓库内容。

## 官方命令与权限

公开链接：[Commands](https://wiki.itemsadder.com/plugin-usage/plugin-configuration/commands/)、[Permissions](https://wiki.itemsadder.com/plugin-usage/plugin-configuration/permissions/)。

命令表原文摘录：

| 命令与权限 | 原文说明 |
| --- | --- |
| `/ia` — `ia.user.ia` | Opens items list GUI |
| `/iaget <item> [amount]` — `ia.admin.iaget` | Get custom item by namespaced id or by id |
| `/iareload` — `ia.admin.iareload` | Reloads configuration files |
| `/iazip` — `ia.admin.iazip` | Executes /iareload and generates pack file |
| `/iatexture` — `ia.user.iatexture` | Force the client to reload resourcepack |
| `/iarecipe [item]` — `ia.user.iarecipe` | Show item recipe GUI |

权限页原文摘录：

> You must use a permission manager like LuckPerms which supports .* permissions notation. Bukkit doesn't support this notation by default!

该页列出 `ia.user.recipe.PERMISSION` / `ia.user.recipe.*`、`ia.user.ia.seeitem.PERMISSION` / `ia.user.ia.seeitem.*` 及 `ia.user.ia.search`，分别对应配方、物品列表可见性和搜索。

## 随包描述信息

```yaml
name: ItemsAdder
version: 4.0.18
depend: [ProtocolLib]
softdepend: [ViaVersion, WorldGuard, GriefPrevention, Towny, Essentials, Realistic_World, EpicWorldGenerator, EpicNetherGenerator, Skript, MythicMobs, PlaceholderAPI, PermissionsEx, LuckPerms, Vault, MMOItems, Slimefun, Orebfuscator, ExecutableItems, Mimic, Citizens, ItemBridge, ModelEngine, Denizen, Vulcan]
```

## 未采用的存疑用法

当前官方 `/iagive` 行说明 “Give custom item to player”，但 Usage 为 `/iagive <item> [amount] [silent]`，没有玩家参数。概览未静默补入参数，也未照搬存疑语法。当前 Wiki 可能含 4.0.18 之后新增的命令，不能全量作为该版本清单。
