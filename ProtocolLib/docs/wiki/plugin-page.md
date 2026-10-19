---
title: "ProtocolLib 官方服主说明"
source_url: "https://www.spigotmc.org/resources/protocollib.1997/"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "ProtocolLib d89a5deb3eb625b16846da57fbbb04bfdd0d031d；官方 Wiki 与发布页 2026-10-19 快照"
---

# ProtocolLib 官方服主说明

**主要适配的 MC 版本：** 1.21

**已测试的 MC 主要版本：** `1.8`、`1.9`、`1.10`、`1.11`、`1.12`、`1.13`、`1.14`、`1.15`、`1.16`、`1.17`、`1.18`、`1.19`、`1.20`、`1.20.6`、`1.21`

**源码：** <https://github.com/dmulloy2/ProtocolLib/>

**贡献者：** dmulloy2 和 aadnk

**捐赠链接：** <https://github.com/sponsors/dmulloy2>

**1.8 至 26.2 请使用[开发构建](https://github.com/dmulloy2/ProtocolLib/releases/tag/dev-build)。**

*下载量已超过 300 万次，感谢大家！*

如果 ProtocolLib 对你有帮助，或让事情方便了许多，可以考虑一次性[捐赠](https://paypal.me/dmulloy2)、[赞助](https://github.com/sponsors/dmulloy2)，或在下方留下好评。这些支持对作者很重要。

标准 Bukkit API 无法完成某些任务，这时可能需要直接操作甚至修改 Minecraft。常见做法是修改收发的数据包，或向数据流注入自定义数据包。但这种实现相当繁琐，而且主要受混淆影响，Minecraft 一发布新版本，大多数实现就会失效。

ProtocolLib 提供对 Minecraft 协议的读写能力，处理反射和通道注入所需的大部分工作，并通过封装简化数据包修改。它会随多数 Minecraft 更新而更新，让使用它的插件理想情况下无需逐一适配。小更新通常无需更新 ProtocolLib，尤其是代码改动较少时，例如 1.8 的安全更新。

## 实用链接

- [正式版本](https://github.com/dmulloy2/ProtocolLib/releases)
- [源代码](https://github.com/dmulloy2/ProtocolLib)
- [问题追踪器](https://github.com/dmulloy2/ProtocolLib/issues)
- [JavaDoc](https://dmulloy2.net/ProtocolLib/javadoc/)

## 支持

报告错误前：

- 检查 ProtocolLib 是否有更新，问题很可能已经修复。
- [**阅读堆栈**](https://bukkit.org/threads/how-to-read-stack-traces-and-troubleshoot-your-own-plugins-by-yourself.32457/)，确认错误来自 ProtocolLib。其包名为 com.comphenix.protocol；如果堆栈中完全没有它，问题就*不是* ProtocolLib。
- **[检查常见错误 Wiki](common-errors.md)。**

报告错误时：

- 使用[**问题追踪器**](https://github.com/dmulloy2/ProtocolLib/issues)，*不要在评价区报告错误*。提交新问题前先搜索是否重复。
- 尽量提供完整信息，包括 ProtocolLib 和 Spigot 版本。
- 用 **[pastebin](http://pastebin.com/)** 提供堆栈或错误内容。

## 面向服主

从上方链接下载 ProtocolLib 即可。它本身不执行其他功能，而是让依赖它的插件正常工作。

## 命令

### Protocol

主要的管理命令，支持以下子命令：

- *config*：重新加载配置文件。
- *check*：检查 BukkitDev 是否有新版本。
- *version*：显示当前运行的 ProtocolLib 版本。
- *timings*：切换是否测量各插件消耗的 CPU 时间。
- *listeners*：显示哪些插件在使用 ProtocolLib，以及它们正在拦截的数据包类型。

### PacketLog

将指定数据包的十六进制表示记录到文件或控制台。

语法：`/packetlog <protocol> <sender> <packet> [file/console]`。

支持的数据包见[此处](https://github.com/dmulloy2/ProtocolLib/blob/master/src/main/java/com/comphenix/protocol/PacketType.java)。

上述所有命令都需要 *protocol.admin* 权限。

## 配置

可用的配置选项不多，位于 Global 部分：

```
auto updater.notify: true #Inform any player with the permission protocol.info when a new version of ProtocolLib is out.
auto updater.download: false #Automatically download and install the newest version of ProtocolLib. The installation will take effect when the server restarts.
auto updater.delay: 43200 #The number of seconds between each check for a new update.
auto updater.last: 0 #This simply records the last time (in seconds since 01.01.1970) an update check was performed. Set it to 0 to force a new update check.
metrics: true #If TRUE, ProtocolLib will publish anonymous usage data to mcstats.org. Set it to FALSE to opt-out.
background compiler: true #If TRUE, ProtocolLib will try and improve performance by replacing reflection with compiled code on-the-fly.
ignore version check: None #Force ProtocolLib to start for a specified Minecraft version, even if it is incompatible.
```

## 兼容性

此项目的主要目标之一是尽可能兼容不同 Minecraft 版本。最终实现相当灵活。除包名变化外，它应当能承受后续版本的变化。作者认为，之后可能只需为错误修复和新功能更新 ProtocolLib。

这依赖于反射：没有硬编码任何名称，而是通过字段类型、包名或参数类型推断每个字段、方法和类。它们在不同版本之间具有很高的一致性。

## 示例插件

下面这些制作良好的插件用 ProtocolLib 实现了有趣的功能。如果提供源码，可以参考它们获得灵感。

- [Holographic Displays](https://dev.bukkit.org/projects/holographic-displays)
- [Advanced Anti Cheat](https://www.spigotmc.org/resources/aac-advanced-anti-cheat-hack-kill-aura-blocker.6442/)
- [Server List Plus](https://www.spigotmc.org/resources/serverlistplus.241/)
- [FurnitureLib](https://www.spigotmc.org/resources/furniturelibary-protectionlib.9368/)
- [AntiAura](https://www.spigotmc.org/resources/antiaura-premium-anti-cheat-plugin.1368/)
- [PremiumVanish](https://www.spigotmc.org/resources/14404/)

*如果你的插件也使用 ProtocolLib，并希望加入列表，请私信作者。*

## 统计

ProtocolLib 通过 BStats 匿名收集统计信息。参与完全自愿，随时可以退出。这些信息有助于了解插件运行环境，例如 Spigot、Java 和 ProtocolLib 的版本，便于作者调整开发工作。

## 赞助

如果 ProtocolLib 让你的工作方便了很多，或你愿意支持项目，可以考虑赞助。这能支持作者投入的大量维护时间，也能帮助作者保持维护动力。如果负担不起，请不要赞助。

<https://github.com/sponsors/dmulloy2>

非常感谢以下赞助者：

- Fanfaryy
- SimplyVanilla
- PebbleHost
- RaenCallisto
- Aternos

## 捐赠

也可以通过 PayPal 一次性捐赠，或使用上方赞助方式。

[![[​IMG]](assets/ee1c4cfd1b18-btn_donateCC_LG.gif)](https://paypal.me/dmulloy2)

非常感谢所有捐赠者！ ![:)](assets/2d83803637e9-clear.png "Smile    :)")

*如果有遗漏，或希望匿名，请私信作者。*

- nathan818 - $1000
- InstaAE - $150
- MineCove - $100
- Lael - $100
- joehot200 - $75
- Techcable - $30
- VintageDon - $25
- games647 - $25
- Photon - $15
- Ltd-Net - $11
- CultivateMC - $10
- Axzial - $10
- snapsi - $5
- Aberzhulan - $5
- Art in the Shade - $5

请不要在评价区报告错误。那里是寻求支持**最不合适**的地方，作者不会回复。请先查阅[常见错误](common-errors.md)并搜索是否已有重复问题，再使用**[问题追踪器](https://github.com/dmulloy2/ProtocolLib/issues)**，方便作者真正诊断和修复问题。
