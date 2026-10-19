---
title: 前缀、后缀与元数据
source_url: https://luckperms.net/wiki/Prefixes,-Suffixes-&-Meta
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

本指南介绍如何使用 LuckPerms 设置和管理前缀、后缀及元数据。

如果已经熟悉这些概念，只想查看命令的用法，请阅读[命令用法：元数据](meta-commands.md)页面。

<a id="key-definitions"></a>
# 关键概念
<a id="prefix--suffix"></a>
### 前缀 / 后缀
在 Minecraft 服务器中，前缀和后缀是聊天消息里出现在用户名前后的文字。

例如，以下聊天消息：
```
[Admin] Luck the great: Hello!
```
其中，`"[Admin] "` 部分是前缀，`" the great"` 部分是后缀。

<a id="meta"></a>
### 元数据
元数据有时也称为“选项”或“变量”，是与用户或权限组关联的额外数据的统称。与权限不同，元数据分为“键”和“值”两部分。键是元数据的名称，值则是赋给该键的具体内容。

例如，我的用户可能有以下元数据，表示我最多可以设置 5 个家，并且用户名应显示为蓝色。
```
max-homes = 5
username-color: blue
```

<a id="who-provides-what"></a>
## 各类功能由谁提供？
通常，负责提供和管理服务器权限的插件，也会提供设置、管理和存储前缀、后缀及元数据的功能。LuckPerms 也是如此。

有些权限插件还会提供将这些数据应用到聊天中的功能。但 LuckPerms 不提供此功能，需要另外安装插件来设置聊天格式。后文会进一步说明。

<a id="how-do-prefixessuffixesmeta-get-stored"></a>
## 前缀、后缀和元数据如何存储
LuckPerms 会将前缀和后缀转换为权限节点后保存。给用户或权限组添加前缀或后缀时，你会发现其权限数据中出现了一个与所设值对应的新条目。为什么这样做？从编程角度看，把所有内容存放在同一位置，并使用相近的格式，会简单得多。这也意味着，可以像操作权限一样，方便地操作前缀和后缀数据。

前缀和后缀分为两部分：
* **权重** - 一个用于决定前缀或后缀优先级的数字。数字越大，权重和优先级就越高。
* **值** - 前缀的实际内容。

前缀 `"[Admin] "` 的权重设为 100 时，会转换为权限：`prefix.100.[Admin] `。

元数据采用类似的机制。元数据键值对 `favourite-color = red` 会转换为权限：`meta.favourite-color.red`。

<a id="how-does-prefixsuffix-weight-work"></a>
## 前缀和后缀的权重如何生效
前缀和后缀可以像权限一样被继承。因此，其他插件请求某个玩家的前缀或后缀时，LuckPerms 需要确定实际使用哪一个。

当其他插件查询用户的前缀或后缀时，LuckPerms 会：
* 收集用户自身拥有及继承到的所有前缀或后缀
* 按权重排序，权重数字越大，优先级越高
* 选择权重最高的前缀或后缀来代表该玩家。

如果找到两个权重相同的条目，会优先使用离用户最近的那个。“最近”指插件在继承树中查找数据时最先发现的条目。

<a id="how-do-i-actually-set-prefixes-and-suffixes-for-a-user"></a>
## 如何为用户设置前缀和后缀
例如，我希望 admin 权限组中的用户拥有 "&c[Admin] " 前缀，mod 权限组中的用户拥有 "&d[Mod] " 前缀，就会执行：

* /lp creategroup admin
* /lp creategroup mod
* /lp group admin parent add mod
* /lp group admin meta addprefix 100 "&c[Admin] "
* /lp group mod meta addprefix 90 "&d[Mod] "

如果之后想将 admin 前缀的颜色改为 "&4"，需要先移除之前设置的值，我会执行：
* /lp group admin meta removeprefix 100

这会移除 admin 上所有权重为 100 的前缀。然后就可以重新设置新的前缀值。

设置临时前缀或后缀的命令，与添加临时权限或父级权限组的命令格式相同。

完整的命令用法见[**此处**](meta-commands.md)。添加和移除元数据的命令也在该页面中说明。

<a id="how-do-i-see-the-prefixessuffixes-a-user-or-group-has"></a>
## 如何查看用户或权限组的前缀和后缀
排查前缀或后缀问题最简单的方法，是使用 info 命令。

例如：`/lp user Luck meta info`。此命令会列出用户自身拥有及继承到的所有前缀、后缀和元数据，并按权重排列条目，便于看出当前应用了哪些值。

另一个实用命令是通用的用户信息命令：`/lp user Luck info`。如果玩家当前在线，此命令会显示：当插件从 LuckPerms 读取数据时，LuckPerms 当前向它们提供的是该玩家的哪个前缀。

<a id="displaying-prefixes-and-suffixes"></a>
## 显示前缀和后缀
如前文所述，LuckPerms 不负责处理任何聊天格式。需要安装外部插件来实现。

下方列出了一些推荐的插件。

<a id="bukkitspigot"></a>
### Bukkit/Spigot
LuckPerms 支持**任何**能够从 [Vault](https://dev.bukkit.org/projects/vault) 读取数据的聊天格式插件。要让它生效，服务器上需要安装 Vault。

如果某个插件未能正确读取数据，请确认 `/vault-info` 的输出显示数据来源为 LuckPerms。

以下是一些支持 LuckPerms + Vault 的常用聊天格式插件：
* [VaultChatFormatter](https://www.spigotmc.org/resources/49016/) - 只需要简单功能时推荐使用！
* [EssentialsX Chat](https://essentialsx.net/downloads.html) - 服务器上已经安装 Essentials 时推荐使用。
* [ChatEx](https://dev.bukkit.org/projects/chatex)
* [VentureChat](https://www.spigotmc.org/resources/771/)
* [Stylizer](https://www.spigotmc.org/resources/stylizer.78327/) - 包含聊天格式和 Tab 玩家列表功能。
* [DisplayFormatter](https://github.com/MCMDEV/displayformatter) - 包含聊天格式和 Tab 玩家列表功能，专为 LuckPerms 设计。
* [CarbonChat](https://github.com/Hexaoxide/Carbon)（测试版）
* [DeluxeChat](https://www.spigotmc.org/resources/1277/)（付费）
* [ChatControl](https://builtbybit.com/resources/18217)（付费）
* [CMI](https://www.spigotmc.org/resources/cmi-298-commands-insane-kits-portals-essentials-economy-mysql-sqlite-much-more.3742/)（付费）
* [BetterPrefix](https://www.spigotmc.org/resources/betterprefix-papi-support.18096/)

以下是一些支持 LuckPerms + Vault 的常用 Tab 玩家列表或头顶名称格式插件：
* [NametagEdit](https://www.spigotmc.org/resources/3836/)
* [TAB](https://github.com/NEZNAMY/TAB)
* [Tab](https://www.spigotmc.org/resources/1448/)（付费）
* [CMI](https://www.spigotmc.org/resources/cmi-298-commands-insane-kits-portals-essentials-economy-mysql-sqlite-much-more.3742/)（付费）
* [BetterPrefix](https://www.spigotmc.org/resources/betterprefix-papi-support.18096/)


这份列表远未列出所有选择。任何支持 Vault 的插件都支持 LuckPerms！


<a id="bungeecord"></a>
### BungeeCord

以下是一些在 BungeeCord 上支持 LuckPerms 的常用聊天格式插件：
* [gChat](https://github.com/lucko/gChat) - 只需要简单功能时推荐使用。
* [BungeeChat](https://www.spigotmc.org/resources/12592/)
* [MultiChat](https://www.spigotmc.org/resources/26204/)

以下是一些在 BungeeCord 上支持 LuckPerms 的常用 Tab 玩家列表或头顶名称格式插件：
* [BungeeTabListPlus](https://www.spigotmc.org/resources/313/)
* [TAB](https://github.com/NEZNAMY/TAB)

<a id="sponge"></a>
### Sponge
* [Nucleus](https://nucleuspowered.org/) - 类似 "essentials" 的插件，也包含[聊天格式模块](https://nucleuspowered.org/docs/modules/chat.html)。

<a id="fabric"></a>
### Fabric
* [Styled Chat](https://modrinth.com/mod/styled-chat) - 包含聊天格式功能，使用 [Fabric TextPlaceholderAPI](https://placeholders.pb4.eu)。请注意，需要手动配置，并且需要使用 [LuckPerms __Fabric__ PlaceholderAPI Addon](https://luckperms.net/download)，此模组才能与 LuckPerms 配合使用。
* [Styled Player List](https://modrinth.com/mod/styledplayerlist) - 包含 Tab 玩家列表格式功能，使用 [Fabric TextPlaceholderAPI](https://placeholders.pb4.eu)。请注意，需要手动配置，并且需要使用 [LuckPerms __Fabric__ PlaceholderAPI Addon](https://luckperms.net/download)，此模组才能与 LuckPerms 配合使用。
* [GraphiXMod](https://github.com/lochnessdragon/GraphiXMod) - 包含聊天格式、全息文字、Tab 玩家列表和计分板功能。
* [Chatter](https://github.com/Axieum/Chatter) - 包含聊天格式和 Discord 集成功能

<a id="forge"></a>
### Forge
* [BetterForgeChat](https://www.curseforge.com/minecraft/mc-mods/betterforgechat-with-luckperms-support) - 包含聊天格式、Tab 玩家列表、ftbessentials 昵称以及 Markdown 样式功能。
