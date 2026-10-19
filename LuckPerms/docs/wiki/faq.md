---
title: 常见问题
source_url: https://luckperms.net/wiki/FAQ
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

<a id="frequently-asked-questions"></a>
# 常见问题
这里收集了一些经常被问到的问题。寻求支持前，请先查看这里是否已经解答了你的问题。

**提示：服务器启动时，或出现任何异常时，都要查看控制台中是否有报错！**

***

<a id="why-are-permissions-not-working"></a>
### 为什么权限没有生效？
首先，*确认 LuckPerms 是你唯一安装的权限插件！* 我们遇到过很多这类问题：安装 LuckPerms 后，没有移除 PermissionsEx 等其他权限管理插件。你*必须*移除所有其他权限插件，否则权限检查就不会使用 LuckPerms。唯一的例外是迁移期间，此时必须同时安装两个权限插件，但迁移完成后要记得移除旧插件。

如果 LuckPerms 是唯一的权限插件，问题可能是你没有为所需功能添加正确的权限。请查阅所用插件的文档，确认有哪些可用权限。如果文档不完整，或找不到相关文档，可以使用[详细日志模式](verbose.md)，实时查看正在检查哪些权限，以及 LuckPerms 为被检查用户返回的值。

如果你在 Fabric 服务器上使用 LuckPerms，**无法通过权限控制原版命令**。与 Bukkit/Spigot 和 Sponge 不同，Fabric 不会为原版命令添加权限检查。这并不是 LuckPerms 的问题。不过，Fabric 支持修改游戏本体，因此可以安装额外的模组来添加这些权限检查，例如 [Minecraft Command Permissions](https://github.com/lucko/minecraft-command-permissions-fabric) 或 [Command Hider](https://github.com/LoganDark/fabric-command-hider)。

另外，个别模组也可能不支持权限，因为 Fabric 中的权限机制还不像 Bukkit/Spigot 或 Sponge 那样标准化。

***

<a id="why-are-prefixessuffixes-not-working"></a>
### 为什么前缀或后缀没有生效？
大多数情况下，这其实不是 LuckPerms 本身的问题。可以按以下方法排查：

- LuckPerms *不是*聊天格式插件，需要另一个插件来设置聊天或 Tab 玩家列表的格式，才能在其中显示前缀和后缀。
  - 如果使用基于 Bukkit 的服务端（CraftBukkit、Spigot、Paper），还需要安装 [Vault](https://dev.bukkit.org/bukkit-plugins/vault/)。
  - [这里](prefixes-suffixes-meta.md#displaying-prefixes-and-suffixes)列出了一些常用的聊天格式插件。
- 首先，检查是否确实已通过 LuckPerms 设置前缀或后缀：执行 `/lp user <user> info`，查看前缀或后缀是否显示正确。如果正确，说明 LuckPerms 已完成它的工作，接下来就需要聊天、Tab 玩家列表或其他格式插件正确显示它。如果没有，则需要[设置前缀或后缀](prefixes-suffixes-meta.md)。
- 如果使用 Essentials，请确认安装的是 [EssentialsX 和 EssentialsXChat](https://ci.ender.zone/job/EssentialsX/)。名称中的 X 很重要！其他版本的 Essentials 可能无法与 LuckPerms 正常配合。
  - 执行 `/ess version` 可以快速查看 Essentials 的安装情况，其中也会报告是否安装了 Vault，以及正在使用哪个权限插件——最好是 LuckPerms！如果命令只返回类似 "Reloaded Essentials [version]" 的消息，说明你使用的是不受支持的 Essentials 版本，应更新为 EssentialsX（链接见上文）。
  - Essentials 在聊天格式中提供 `{DISPLAYNAME}` 占位符，它会将前缀、昵称和后缀合并为一个整体。如果不希望这样显示，可以将 Essentials 配置中的 `add-prefix-suffix` 选项设为 `false`。
- 前缀或后缀显示出来了，但不是你想要的那个？通常需要正确设置优先级或权重。如果执行 `/lp user <user> meta info` 后看到一堆零，或者部分或全部数字（优先级）相同，LuckPerms 会选用遇到的第一个最高优先级条目，作为该用户的前缀或后缀。要修改它们，需要[使用正确的命令重新设置前缀](meta-commands.md#lp-usergroup-usergroup-meta-setprefix-priority-prefix-context)，也可以直接在网页编辑器中修改数字。前缀和后缀与其他数据一样，以权限的形式存储，格式类似 `prefix.100.[Admin]`。其中的 `100` 就是优先级，修改这个数字即可调整优先级。
- 最后，LuckPerms 配置中的 `meta-formatting` 部分非常重要，只应在确有需要时修改（例如设置[前缀或后缀叠加](prefix-suffix-stacking.md)）。这一部分被改动可能会导致前缀或后缀失效。如果要恢复默认设置，请确认 `format` 如下所示：
```
    format:
      - "highest"
```

***

<a id="how-do-i-get-permissions-to-sync-across-multiple-servers"></a>
### 如何让权限在多台服务器之间同步？
[多服务器安装](network-installation.md)页面对此有详细说明。也请阅读[在服务器之间同步数据](syncing-data-between-servers.md)。以下是简要说明：

- 满足以下任意条件时，需要在代理端安装 Bungeecord 版 LuckPerms：
  - 你想管理 Bungeecord 权限（大多数情况下都需要）；或者
  - 你将 messaging-service 设为 `pluginmsg`（使用 SQL 数据库时不推荐这样设置）。
- 需要在每一台后端服务器（Spigot、Sponge）上安装 LuckPerms。
- 必须在 Bungeecord 上启用 IP 转发，并在各 Spigot 服务器的 spigot.yml 文件中设置 `bungeecord: true`。
- **所有** LuckPerms 实例都必须使用相同的[远程存储方式](storage-types.md#remote-databases)（例如 MySQL）。这要求设置 `storage-method` 属性，并让所有服务器使用完全相同的数据库凭据。
- 执行 `/lp info`，检查存储方式是否正确，确认所有服务器都连接到了正确的数据库。Bungeecord 上使用 `/lpb info`（如果遇到权限错误，请从控制台执行）。
- 如果使用 MySQL 或 MariaDB，请在所有服务器上将 [`messaging-service`](configuration.md#messaging-service) 设为 `sql`。这样，数据库发生变化时，所有服务器都会进行同步。

***

<a id="mysql-errors"></a>
### MySQL 错误

例如：

* LuckPerms 无法连接到我的 MySQL 服务器
* 出现烦人的 SSL 警告消息
* 出现 "No operations allowed after connection closed" 错误

请查看[此处](storage-system-errors.md)。

***

<a id="i-use-spongeforge-and-when-i-install-luckperms-i-lose-all-my-permissions-why"></a>
### 我使用 SpongeForge，安装 LuckPerms 后失去了所有权限，这是为什么？
这是 SpongeForge 的预期行为。一旦安装权限插件，它就会禁用 OP 系统。  
要解决这个问题，需要为权限组和用户授予所需权限。如果想获得类似 OP 的权限，可以使用通配符 `*`，但[不推荐这样做](https://nucleuspowered.org/docs/nowildcard.html)。

***

<a id="what-versions-does-luckperms-support"></a>
### LuckPerms 支持哪些版本？
LuckPerms 支持从 Minecraft 1.8.8 到最新正式版的所有版本。  

如果想在 Bukkit 1.7.10 服务器上使用 LuckPerms，需要使用 Bukkit-Legacy JAR，可在[此处](https://luckperms.net/download)下载。

***

<a id="when-i-install-luckperms-my-server-shuts-down"></a>
### 安装 LuckPerms 后，我的服务器关闭了
LuckPerms 从不会关闭你的服务器。  

如果使用 AuthMe，请检查控制台中是否有以下内容：  
```
[AuthMe] Aborting initialization of AuthMe: [InjectorReflectionException]: Could not invoke method 'setup' for fr.xephi.authme.permission.PermissionsManager@xxxxxxxx
[AuthMe] THE SERVER IS GOING TO SHUT DOWN AS DEFINED IN THE CONFIGURATION!
```

如果出现这些内容，说明服务器是被 AuthMe 关闭的，原因是它的一项默认配置设置。

要解决这个问题，请打开 AuthMe 的 config.yml，将 `forceVaultHook` 从 false 改为 true。

***

<a id="luckperms-cannot-download-dependencies"></a>
### LuckPerms 无法下载依赖
LuckPerms 需要连接互联网才能下载依赖。如果 LuckPerms 没有网络连接，或连接被服务器托管商阻止，插件就**不会**工作。

> me.lucko.luckperms.common.dependencies.DependencyDownloadException: java.net.ConnectException: Connection refused (Connection refused)

出现这样的错误，意味着 **a)** 服务器没有互联网连接，或 **b)** 服务器托管商阻止了连接。

可以通过以下任一方法解决：

- 在本地（能够连接互联网的环境中）安装 LP，然后将 `/LuckPerms/libs/` 目录中的内容复制到另一台服务器的 `/LuckPerms/libs/` 文件夹中。

- 联系服务器托管商，允许来自 [libraries.luckperms.net](https://libraries.luckperms.net/) 和 [repo1.maven.org](https://repo1.maven.org/maven2/) 的连接。


