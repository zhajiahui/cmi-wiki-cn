---
title: 常见问题
source_url: https://worldguard.enginehub.org/en/latest/faq/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 常见问题 { #common-questions }

<a id="contents"></a>

- [常规](#general)



  - [为什么所有命令都无法使用？](#why-don-t-any-commands-work)

  - [WorldGuard 有多久的历史？](#how-old-is-worldguard)

  - [谁在开发 WorldGuard？](#who-works-on-worldguard)

- [无法建造](#can-t-build)



  - [为什么玩家无法破坏或放置方块？](#why-can-t-players-break-or-place-blocks)

  - [设置区域后，为什么所有人都无法建造？](#after-setting-up-some-regions-why-can-no-one-build)

- [未能阻止建造](#building-not-blocked)



  - [为什么保护不生效，而且玩家没有收到提示？](#why-is-protection-not-working-players-receive-no-message)

  - [为什么保护不生效，但玩家收到了提示？](#why-is-protection-not-working-players-do-receive-a-message)

- [区域保护](#region-protection)



  - [为什么活塞无法工作？](#why-do-pistons-not-work)

  - [如何通过区域保护实现 __________？](#how-do-i-do-with-region-protection)

!!! tip "提示"

    关于区域保护的常见问题，也请查看[常见场景](regions/common-scenarios.md)页面。

## 常规 { #general }

### 为什么所有命令都无法使用？ { #why-don-t-any-commands-work }

所有命令都无法使用时，可能是 WorldGuard 未能启动：

- 确认所用服务器软件支持 Bukkit，例如 [Spigot](https://spigotmc.org) 或 [Paper](https://papermc.io)。在控制台或游戏内执行 `version`，检查当前运行的服务器软件。

- 确认已安装与当前 Minecraft 版本相匹配的 [WorldEdit](https://www.enginehub.org/worldedit)。

- 确认 WorldGuard 版本与当前 Minecraft 版本匹配。

如果以上方法没有解决问题，就需要检查启动日志：

- 使用游戏服务器托管服务时，请打开服务商提供的日志查看器。

- 也可以打开服务器目录中 logs 文件夹下的“latest.log”。旧版 Minecraft 的日志是服务器根目录中的“server.log”。

如果阅读服务器日志后仍找不到原因，可以[寻求帮助](support.md)。

### WorldGuard 有多久的历史？ { #how-old-is-worldguard }

[sk89q](http://www.sk89q.com) 于 2010 年 11 月为“hMod”模组平台创建了 WorldGuard，后来将其移植到 Bukkit。

### 谁在开发 WorldGuard？ { #who-works-on-worldguard }

许多人参与过 WorldGuard 的开发，其中大量代码来自社区贡献。主要贡献者列表可在 [GitHub](https://github.com/EngineHub/WorldGuard/graphs/contributors) 上查看。

## 无法建造 { #can-t-build }

<a id="cannot-build"></a>

### 为什么玩家无法破坏或放置方块？ { #why-can-t-players-break-or-place-blocks }

!!! note "注意"

    新安装的 WorldGuard 默认关闭大多数功能，因此遇到这种情况时，问题通常并非由 WorldGuard 引起。

最简单的排查方法之一，是查看无法建造时收到的提示。WorldGuard 通常使用暗红或深红色消息，或类似“Hey! Sorry, but you can’t _____ here.”的提示。如果没有任何消息，通常不是 WorldGuard 导致的。

如果暂时看不出是 WorldGuard 导致：

- 确认没有启用 Minecraft 的“出生点保护”。它会阻止任何人在世界出生点一定半径内进行修改。可将 server.properties 文件中的 `spawn-protection` 设为 `0` 来调整出生点保护。

- 确认没有在冒险模式下测试。

- 更新服务器软件，如 Spigot 或 Paper。

如果以上方法无效，WorldGuard 有命令可以代表玩家模拟操作，并报告哪个插件阻止了它。使用[命令](commands.md)页面介绍的“testbreak”和“testplace”来找出对应插件。

如果原因是 WorldGuard：

- 使用[区域查询工具](regions/wand.md)，查看是否有区域保护相关方块。如果有区域，但不清楚原因，请参阅[设置区域后，为什么所有人都无法建造？](#troubleshooting-region-protection)

- 检查是否启用了[建造权限](build-perms.md)。

- 检查是否启用了其他会阻止此操作的[配置选项](config.md)。

- 如果找不到原因，可以[寻求帮助](support.md)。

如果命令列出的是其他插件：

- 检查是否需要为该插件授予额外权限，或修改它的配置。

如果测试命令没有列出任何插件，先确认已完成上述检查（出生点保护等），再[寻求帮助](support.md)。

<a id="troubleshooting-region-protection"></a>

### 设置区域后，为什么所有人都无法建造？ { #after-setting-up-some-regions-why-can-no-one-build }

使用[区域查询工具](regions/wand.md)右键点击受影响的方块，列出该位置的区域。再使用 `/rg info` 查看每个列出区域的信息。

- 检查所有区域的成员设置。

- 确认没有将 `build` 旗标设为 `deny`。

是否只有一个全局区域？

- 确认[全局区域](regions/global-region.md)的 `build` 没有设为 deny。

- 确认[全局区域](regions/global-region.md)的 `passthrough` 没有设为 deny。

- 确认[全局区域](regions/global-region.md)没有成员或所有者。

## 未能阻止建造 { #building-not-blocked }

### 为什么保护不生效，而且玩家没有收到提示？ { #why-is-protection-not-working-players-receive-no-message }

- 你拥有 OP 身份或全部权限，因此绕过了保护。

- 你将某个区域的 `build` 旗标设为了“allow”。

- 你将某个区域的 `passthrough` 旗标设为了“allow”。

- 你将该区域的其他相关旗标（如 `pvp`、`ride` 等）设为了“allow”。

- 相关物品来自模组或第三方插件，详见[保护范围](regions/scope.md)。

- WorldGuard 尚未保护你正在尝试的这种操作；普通方块的放置和破坏不属于这种情况。请先确认使用最新版 WorldGuard；如果问题依旧，请[提交缺陷报告](support.md)。

- 当前服务器软件版本存在缺陷。

如果仍然找不到原因，可以[寻求帮助](support.md)。

### 为什么保护不生效，但玩家收到了提示？ { #why-is-protection-not-working-players-do-receive-a-message }

即使 WorldGuard 阻止了某项操作，其他插件仍可能*解除*阻止。但由于 WorldGuard 已发送“无法建造”的消息，玩家仍会看到提示。

可以使用[命令](commands.md)中介绍的“testbreak”和“testplace”找出原因。如果列表中 WorldGuard 上方的插件旁标有“ALLOW”，该插件就是原因。

另一种可能是服务器软件（如 Spigot 或 Paper）的当前版本存在缺陷，请使用可获取的最新版本。如果仍找不到原因，可以[寻求帮助](support.md)。

## 区域保护 { #region-protection }

### 为什么活塞无法工作？ { #why-do-pistons-not-work }

很可能是不应设置 `build` 为 `deny`，却设置了它。更多信息见[常见场景](regions/common-scenarios.md)。

### 如何通过区域保护实现 __________？ { #how-do-i-do-with-region-protection }

请参阅[常见场景](regions/common-scenarios.md)。
