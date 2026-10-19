---
title: CrackShot 概览来源
source_kind: plugin-overview
translation_review: reviewed
---

# CrackShot 概览来源

核对日期：2026-10-19。随包版本为 0.98.13-x6；下列公开文档属于 Shampaggon 上游，尚未核实 -x6 分支的出处及改动。

## 官方项目页与仓库

公开链接：[BukkitDev 项目页](https://dev.bukkit.org/projects/crackshot)、[Shampaggon/CrackShot](https://github.com/Shampaggon/CrackShot)。已取得项目介绍及仓库 README 正文。

项目页原文摘录：

> Create your own melee or ranged weapons and replicate any first-person shooter.
>
> Reloads: replicate reload-animations with CrackShot's reloading system - press Q to reload!
>
> Custom sounds: choose what sounds your weapons make!
>
> Custom recipes: create crafting recipes for your weapons!
>
> Mechanics: deal bonus damage on headshots, backstabs or critical hits!

上述摘录用于近战/远程武器、装填、声音、配方及攻击机制的简介。商店及爆炸物也列在该页 Features 正文中。

README 将 [The Complete Guide to CrackShot](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot)列为 Documentation。完整指南本次请求不稳定；命令页已成功取得，不依据未取得的完整指南内容补写功能。

## 官方命令和权限

公开链接：[Commands and Permissions](https://github.com/Shampaggon/CrackShot/wiki/Commands-and-Permissions)。

原文摘录：

```text
/shot, /cra, /cs
/shot list all - Lists all weapons, excluding the ones that are hidden.
/shot list <page> - Lists weapons by page number, excluding the ones that are hidden.
/shot config reload - Reloads the configuration.
/shot give <user> <weapon> <amount> - Gives another player a weapon. You may specify an amount.
/shot get <weapon> <amount> - Gives the player a weapon. You may specify an amount.
/shot reload - Reloads the weapon in hand.
```

权限正文摘录：

> By default, users can craft, buy and use all weapons.
>
> crackshot.reloadplugin - Permission to reload the plugin.
>
> crackshot.list - Permission to list weapons.
>
> crackshot.give.all - Permission to give any weapon to players.
>
> crackshot.get.all - Permission to get any weapon.

同页分别列出 `crackshot.use.all`、`crackshot.craft.all`、`crackshot.buy.all`（Default），以及 `crackshot.shops.all`、`crackshot.bypass.all` 和针对指定武器的 `.<weapon>` 形式。概览保留原文参数写法。

## 随包描述信息与待确认项

```yaml
name: CrackShot
version: 0.98.13-x6
depend: []
softdepend: []
```

CrackShotX 声明 `depend: [CrackShot]`，这是将 CrackShot 与附属插件分开说明的依据。

原文问题：官方 `crackshot.buy.<weapon>` 的说明写成 “Permission to craft a specific weapon.”，与 `buy.all` 行和节点名冲突。概览没有把这一疑似笔误写成确定的合成权限。原文用尖括号列出数量，同时写 “You may specify an amount.”，不能将数量写成已确认必填。
