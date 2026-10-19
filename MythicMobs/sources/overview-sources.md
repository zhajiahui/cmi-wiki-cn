---
title: MythicMobs 概览来源
source_kind: plugin-overview
translation_review: reviewed
---

# MythicMobs 概览来源

核对日期：2026-10-19。随包内部版本为 5.13.0-SNAPSHOT-1abf9862，不能以文件名中的 5.13.0 代替。

## 官方介绍

公开链接：[官方 Wiki 首页](https://wiki.mythiccraft.io/mythicmobs)。已取得正文。

原文摘录：

> Mythic allows server owners to fully modify all attributes of any non-player entity on your server
>
> giving mobs a vast arsenal of new abilities with a powerful yet simple scripting system
>
> Your custom mobs can replace vanilla mobs, be spawned randomly using a vast array of spawn conditions, or you can set up custom mob spawners that activate under certain conditions or by commands.

首页还列出 Mob Skills、Mob Attributes、Equipment、Mob AI Controls、Spawning Control 等分类，作为简介中技能、属性、装备、AI 和生成方式的依据。

[官方产品页](https://mythiccraft.io/index.php?resources/mythicmobs.1/)由该站的下载入口链接确认归属，未进一步抓取购买或账户页面。

## 官方命令和权限

公开链接：[Commands and Permissions](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)。旧 git.mythiccraft.io Wiki 链接在本次请求中重定向至此。已取得正文，页面标注 Updated Oct 4, 2026。

原文摘录：

> All command parameters surrounded by []'s are required, while <>'s are optional.
>
> /mm (alias: /mythicmobs) — Base command for the plugin. Displays all other commands.
>
> /mm reload (alias: /mm r) — Reloads the plugin.
>
> /mm version — Displays MythicMobs version.

其余概览用法对应的原文命令为：

```text
/mm mobs list
/mm mobs info [mob_name]
/mm mobs spawn [mob_name]:<level> <amount> <world,x,y,z,yaw,pitch>
/mm items get [item_name] <amount>
/mm items give [player] [item_name] <amount>
```

权限原文摘录：

> mythicmobs.admin - Grants full access to the plugin's commands.
>
> Access to individual commands can be given using mythicmobs.command.<command>
>
> mythicmobs.command.mobs.list - Access to the /mm mobs list command.

## 随包描述信息

```yaml
name: MythicMobs
version: 5.13.0-SNAPSHOT-1abf9862
depend: []
softdepend: [Multiverse-Core, Heroes, PhatLoots, Vault, MagicSpells, MiniaturePets, LibsDisguises, WorldGuard, Holograms, HolographicDisplays, PlaceholderAPI, PlotSquared, Residence]
permissions: [mythicmobs.admin, mythicmobs.reload, mythicmobs.signal]
```

## 版本及原文差异

在线文档持续更新，其中后来新增的功能不作为此 SNAPSHOT 的版本承诺。

信号命令用法 `/mm signal <UUID> <signal>` 的尖括号与页面顶部通用约定不一致，但正文要求生物 UUID，不能按尖括号推断它可以省略。因此概览没有展开此项；研究记录保留了这处差异。
