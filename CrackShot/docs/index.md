---
title: CrackShot 插件简介
source_kind: plugin-overview
translation_review: reviewed
---

# CrackShot

CrackShot 用于创建自定义近战和远程武器，提供射击、装填、自定义声音、合成配方、商店，以及爆头、背刺、暴击和爆炸物等功能。这些功能列于 [Shampaggon 的官方项目页](https://dev.bukkit.org/projects/crackshot)。

本次随包版本为 **0.98.13-x6**。`-x6` 是随包版本号的一部分，其分支来源和改动尚未核实。以下核心命令依据上游官方文档整理。

CrackShot 是主插件；随包的 CrackShotX 是依赖 CrackShot 的附属插件，二者各有配置。

## 依赖

随包 CrackShot 没有声明必需插件或软依赖。

## 核心命令和权限

[官方命令页](https://github.com/Shampaggon/CrackShot/wiki/Commands-and-Permissions)列出 `/shot`、`/cra`、`/cs` 别名。

| 命令 | 用途 | 权限 |
| --- | --- | --- |
| `/shot` | 显示插件信息 | 官方该项未单列权限 |
| `/shot list all` | 列出所有未隐藏的武器 | `crackshot.list` |
| `/shot list <page>` | 按页列出未隐藏的武器 | `crackshot.list` |
| `/shot config reload` | 重载配置 | `crackshot.reloadplugin` |
| `/shot give <user> <weapon> <amount>` | 给予其他玩家武器 | `crackshot.give.all` 或 `crackshot.give.<weapon>` |
| `/shot get <weapon> <amount>` | 获取武器 | `crackshot.get.all` 或 `crackshot.get.<weapon>` |
| `/shot reload` | 装填手持武器 | 官方该项未单列权限 |

表中保留官方参数写法；官方另说明 `give`、`get` 的数量可以指定。

官方说明，玩家默认具有制作、购买和使用所有武器的权限，对应 `crackshot.craft.all`、`crackshot.buy.all`、`crackshot.use.all`。商店建立与移除使用 `crackshot.shops.all`，绕过区域检查使用 `crackshot.bypass.all`；也有针对指定武器的 `.<weapon>` 形式。

## 官方资料

- [BukkitDev 官方项目页](https://dev.bukkit.org/projects/crackshot)
- [Shampaggon/CrackShot 仓库](https://github.com/Shampaggon/CrackShot)
- [官方完整指南](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot)
- [官方命令和权限](https://github.com/Shampaggon/CrackShot/wiki/Commands-and-Permissions)

[查看配置文件及中文说明](configuration/index.md)。
