---
title: 常见问题
source_url: https://worldedit.enginehub.org/en/latest/faq/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 常见问题 { #common-questions }

<a id="contents"></a>

- [常规](#general)



  - [为什么所有命令都无法使用？](#why-don-t-any-commands-work)

  - [WorldEdit 有多久的历史？](#how-old-is-worldedit)

  - [谁在开发 WorldEdit？](#who-works-on-worldedit)

- [世界编辑](#world-editing)



  - [命令总是返回“0 blocks changed”，但本应修改方块。](#commands-all-return-0-blocks-changed-even-though-they-should-be-changing)

  - [进行大型编辑（100 万个及以上方块）时，服务器崩溃！](#my-server-crashes-when-i-do-large-edits-1-million-blocks-or-more)

  - [单人游戏中进行大型编辑（100 万个及以上方块）时，客户端崩溃！](#my-client-crashes-when-i-do-large-edits-1-million-blocks-or-more-in-single-player)

  - [如何移除手持物品上的工具或笔刷？](#how-do-i-remove-a-tool-brush-from-the-item-i-m-holding)

  - [为什么告示牌文字、箱子内容、实体等无法正常使用？](#why-isn-t-sign-text-chest-contents-entities-etc-working)

  - [选择范围时，为什么 WorldEdit 还会选中 (-1, -1, -1)？](#when-i-select-worldedit-also-selects-1-1-1)

## 常规 { #general }

### 为什么所有命令都无法使用？ { #why-don-t-any-commands-work }

所有命令都无法使用时，可能是 WorldEdit 未能启动：

- 确认运行的是 Bukkit、Forge、Sponge 等平台。原版 Minecraft 服务器不会加载插件或模组！



  - 可运行 `version`（Bukkit）、`sponge version`（Sponge）或 `forge help`（Forge），确认服务器使用了正确软件。单人游戏的主菜单应有“Mods”按钮，且列表中应包含 WorldEdit！

- 确认 WorldEdit 版本与当前 Minecraft 版本匹配。

如果上述方法无效，就需要检查启动日志：

- 使用游戏服务器托管服务时，请打开服务商提供的日志查看器。

- 也可以打开服务器目录中 logs 文件夹下的“latest.log”。旧版 Minecraft 的日志是服务器根目录中的“server.log”。

如果阅读服务器日志后仍找不到原因，可以[寻求帮助或提交缺陷报告](support.md)。

### WorldEdit 有多久的历史？ { #how-old-is-worldedit }

[sk89q](http://www.sk89q.com) 于 2010 年 9 月为“hMod”模组平台创建了 WorldEdit，后来将其移植到 Bukkit，之后又支持了 Forge 等平台。

### 谁在开发 WorldEdit？ { #who-works-on-worldedit }

许多人参与过 WorldEdit 的开发，其中大量代码来自社区贡献。主要贡献者列表可在 [GitHub](https://github.com/EngineHub/WorldEdit/graphs/contributors) 上查看。

## 世界编辑 { #world-editing }

### 命令总是返回“0 blocks changed”，但本应修改方块。 { #commands-all-return-0-blocks-changed-even-though-they-should-be-changing }

如果之前用 `//gmask <mask>` 设置过全局蒙版，需要再执行 `//gmask` 清除，避免它继续限制编辑。

### 进行大型编辑（100 万个及以上方块）时，服务器崩溃！ { #my-server-crashes-when-i-do-large-edits-1-million-blocks-or-more }

!!! note "注意"

    如果只是客户端断开或超时，以下方法无法解决。目前 WorldEdit 不会在处理编辑期间尝试维持客户端连接；这些说明仅用于让服务器真正完成编辑。

最可能的两个原因是 watchdog 使服务器崩溃，或服务器内存不足。

请分配大约 1 GB 供服务器本身使用，再为每编辑 1000 万个方块增加 2 GB。例如，编辑约 5000 万个方块时，先算 `50 / 10` 得到 `5`，再算 `1 + 2 * 5`，共需 11 GB。用 `-Xmx11G` 为服务器分配该内存。Bukkit、Spigot 和 Paper 可参考[示例说明](https://bukkit.gamepedia.com/Setting_the_Java_Virtual_Machine_Heap_Size)；NeoForge/Fabric 的操作也类似。

如果是 watchdog 导致服务器崩溃，可尝试提高服务器的 watchdog 超时时间。Spigot/Paper 对应 `spigot.yml` 中的 `timeout-time`；NeoForge/Fabric 对应 `server.properties` 中的 `max-tick-time`。不过大多数情况下不需要，因为 WorldEdit 会自动更新 watchdog。

### 单人游戏中进行大型编辑（100 万个及以上方块）时，客户端崩溃！ { #my-client-crashes-when-i-do-large-edits-1-million-blocks-or-more-in-single-player }

可以使用上方服务器情形中的方法，但无需考虑 watchdog，因为单人游戏不使用 watchdog。

### 如何移除手持物品上的工具或笔刷？ { #how-do-i-remove-a-tool-brush-from-the-item-i-m-holding }

手持该物品，执行 `/tool none` 或 `/brush none`。两者目前实际上是同一个命令，任选其一即可。

### 为什么告示牌文字、箱子内容、实体等无法正常使用？ { #why-isn-t-sign-text-chest-contents-entities-etc-working }

在所有 WorldEdit 版本中，设置方块实体都需要 `worldedit.setnbt` 权限，可通过 OP 身份获得。

由于 Bukkit 的工作方式，WorldEdit 需要使用与服务器版本相关的适配器，才能完整访问许多功能。这些适配器用于方块实体（带有额外数据的方块，如告示牌、容器等）、实体及部分其他功能。因此，Minecraft 每次发布新版本，通常都需要更新 WorldEdit。WorldEdit 一般会很快更新，可通过[首页](index.md)链接获取新发布版或实验性构建。

### 选择范围时，为什么 WorldEdit 还会选中 (-1, -1, -1)？ { #when-i-select-worldedit-also-selects-1-1-1 }

这是与 MrCrayFish 的 Enchantable 模组冲突造成的，详见[这里](https://github.com/MrCrayfish/Enchantable/issues/18)。

可以移除该模组，或改用[远程选区工具](usage/tools/tools.md#long-range-wand)。
