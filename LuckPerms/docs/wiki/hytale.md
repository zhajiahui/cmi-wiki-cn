---
title: "Hytale"
source_url: https://luckperms.net/wiki/Hytale
source_kind: official-wiki
translation_review: reviewed
source_version: "fc2919c3d5e6bfba82af31f9930273b00f08ddbf"
---


**[Hytale](https://hytale.com/) 版 LuckPerms** 的**测试版**现已在我们的[下载页面](https://luckperms.net/download)提供。它就是你在 Minecraft 中熟悉、也许还很喜欢（希望如此）的 LuckPerms，现在已移植到 Hytale 并完成集成！🎉

Hytale 版 LuckPerms 与其他平台的 LuckPerms 插件或模组使用同一套公共代码。我们认为，让 Hytale 版沿用现有**久经验证**的 Minecraft 版本所使用的成熟核心平台，能够为 Hytale 提供非常**稳定**、**高性能**的权限实现，质量也会高于“专门定制”的插件。🥳

本 Wiki 和项目其他地方的部分文档更新稍有滞后，少数地方仍然提到 Minecraft。不过，Hytale 的权限系统与 Minecraft 生态中广泛采用的“Bukkit”权限系统非常相似，因此 Minecraft 版 LuckPerms 中现有的概念，即便不是全部，也大多同样适用于 Hytale。太好了！

希望你在 Hytale 服务器上用 LuckPerms 用得愉快！

<a id="faqs"></a>
## 常见问题

* [我以前从没用过 LuckPerms！该如何开始？](hytale.md#ive-never-used-luckperms-before-how-do-i-get-started)
* [OP 不再生效了！](hytale.md#op-doesnt-work-anymore)
* [与其他模组或插件的兼容性](hytale.md#compatibility-with-other-modsplugins)
* [查找权限与排查问题](hytale.md#finding-permissions-and-troubleshooting)
* [聊天格式](hytale.md#chat-formatting)
* [集成 LuckPerms API](hytale.md#integrating-with-the-luckperms-api)
* [已知限制与问题](https://luckperms.net/wiki/Hytale#known-caveatsissues)

<a id="ive-never-used-luckperms-before-how-do-i-get-started"></a>
### 我以前从没用过 LuckPerms！该如何开始？

你好，欢迎使用！👋

简单来说，先查看：

* **[安装](installation.md)**页面，了解如何安装 LuckPerms，然后查看
* **[入门指南](usage.md)**页面，了解如何开始使用！

之后，如果你以前从未使用过权限插件，还想了解更多，建议从文档顶部开始依次往下阅读！更简明的命令参考见[命令用法](command-usage.md)的各个子页面。

<a id="op-doesnt-work-anymore"></a>
### OP 不再生效了！

安装 LuckPerms 后，Hytale 内置的权限系统会在很大程度上被替代，以便 LuckPerms 拦截并处理玩家的权限检查。

这意味着：

* 内置的 `/op` 命令将无法按预期工作。请改用 LuckPerms 配置权限。

* 内置的 `/perm` 命令将无法按预期工作。必须使用 LuckPerms 的 `/lp` 命令来配置玩家权限。

如果想实现类似 OP 的功能（能够完整使用**所有**命令、功能等），可以使用以下 LuckPerms 命令：

* `/lp user <user> permission set *` - 授予 `<user>` 所有权限
* `/lp group <group> permission set *` - 授予 `<group>` 中的所有用户全部权限（例如，可以为“admin”或“owner”权限组这样设置）

<a id="compatibility-with-other-modsplugins"></a>
### 与其他模组或插件的兼容性

LuckPerms 致力于兼容通过 `CommandSender#hasPermission` 或 `PermissionsModule#hasPermission` 检查权限的其他模组。如果你的其他模组使用这种方式检查权限，一切都应当能够正常工作！

默认情况下，LuckPerms 会将非玩家实体的权限检查交给 Hytale 内置的权限系统处理。这意味着，你*可以*使用内置的 `/perm` 命令，为**非玩家** NPC、“服务账号”或 Nitrado 的“anonymous”用户配置权限。玩家权限则**必须**通过 LuckPerms 配置。

<a id="finding-permissions-and-troubleshooting"></a>
### 查找权限与排查问题

如果不知道某条命令或某项功能对应的权限，可以使用 LuckPerms 的详细权限检查日志功能！详情见 Wiki 的[详细权限检查日志](verbose.md)页面。

也可以使用内置的 `/help` 命令，它会打开一个界面，列出可用命令及其对应权限。


<a id="chat-formatting"></a>
### 聊天格式

在早期测试版中，LuckPerms 内置了聊天格式功能。如今，模组与插件生态已有一定发展，也出现了更好的替代方案，因此 LuckPerms 已移除这项功能。建议使用以下方法之一设置聊天格式。

<a id="mini-chat-formatter"></a>
#### mini-chat-formatter

[mini-chat-formatter](https://github.com/lucko/mini-chat-formatter) 是一个简单的 Hytale 聊天格式模组，与 LuckPerms 由同一位作者开发，并原生集成了 LuckPerms。

下载并安装后，在 `mods/lucko_mini-chat-formatter/config.json` 中设置以下配置：

```json
{
  "Format": "<prefix><username><suffix>: <message>"
}
```

格式字符串以及前缀和后缀的值都支持使用 [MiniMessage](https://docs.papermc.io/adventure/minimessage/format/) 设置格式。（是的，这是一种 Minecraft 格式，不过它很好用，而且直接复用更方便！）

前缀和后缀中的格式会有意“*延续*”到格式字符串的后续部分。

以下是一些示例：

| 命令                                                                                              | 效果                          |
|---------------------------------------------------------------------------------------------------|-------------------------------|
| `/lp user lucko meta setprefix 10 "<red>[ADMIN] "`                                                | ![](assets/hytale-chat-1.png) |
| `/lp user lucko meta setprefix 10 "<red>[ADMIN]</red> "`<br>（注意闭合的 `</red>` 标签）。       | ![](assets/hytale-chat-2.png) |
| `/lp user lucko meta setprefix 10 "<red>[ADMIN] "`<br>`/lp user lucko meta setsuffix 10 "<gray>"` | ![](assets/hytale-chat-3.png) |


希望这些示例能帮助你理解。更多信息见：

* [mini-chat-formatter](https://github.com/lucko/mini-chat-formatter) (GitHub)
* [前缀、后缀与元数据](prefixes-suffixes-meta.md)（LP Wiki）
* [MiniMessage 格式](https://docs.papermc.io/adventure/minimessage/format/)（PaperMC 文档）

<a id="advanced-chat-formatting-options"></a>
#### 更高级的聊天格式选项

如果需要更高级的聊天格式功能，建议使用集成了 LuckPerms 的专用聊天插件。可选插件包括 HeroChat、EliteEssentials、EssentialsPlus 等。

<a id="integrating-with-the-luckperms-api"></a>
### 集成 LuckPerms API

我们制作了一个基础示例插件，演示如何从 Hytale 插件中访问 LuckPerms API。

[https://github.com/LuckPerms/api-cookbook-hytale](https://github.com/LuckPerms/api-cookbook-hytale)

关键点如下：

<a id="1-declare-luckperms-as-a-dependency-or-optional-dependency"></a>
#### 1) 将 LuckPerms 声明为依赖或可选依赖

必须在插件的 `manifest.json` 中包含以下配置之一：

```json
{
  "Dependencies": {
    "LuckPerms:LuckPerms": "*"
  }
}
```

或

```json
{
  "OptionalDependencies": {
    "LuckPerms:LuckPerms": "*"
  }
}
```

这是因为 Hytale 的插件管理器会隔离各插件的类加载器，只有声明了依赖时才例外。

<a id="2-obtain-the-api-instance-from-javapluginstart-or-later"></a>
#### 2) 在 JavaPlugin.start() 中或更晚的阶段获取 API 实例

LuckPerms 会在“start”阶段完成最后的初始化，在“setup”阶段**尚未**就绪。

```java
  @Override
  protected void setup() {
    // doesn't work! ❌
    LuckPerms luckPerms = LuckPermsProvider.get();
  }

  @Override
  protected void start() {
    // works! ✅
    LuckPerms luckPerms = LuckPermsProvider.get();
  }
```

<a id="3-playeradapter-and-contextmanager-expect-playerref"></a>
#### 3) PlayerAdapter 和 ContextManager 接受的是 `PlayerRef`

LuckPerms API 中接受“玩家”对象的方法，需要传入 `PlayerRef`，**而不是** `Player`。

例如：

```java
// PlayerAdapter is a convenience class for converting
// between Hytale's PlayerRef and LuckPerms' User objects
PlayerAdapter<PlayerRef> playerAdapter = LuckPermsProvider.get().getPlayerAdapter(PlayerRef.class);

User user = playerAdapter.getUser(playerRef);
CachedPermissionData permissionData = playerAdapter.getPermissionData(playerRef);
CachedMetaData metaData = playerAdapter.getMetaData(playerRef);

// Get the players prefix, for example :)
String prefix = metaData.getPrefix();
```

<a id="other"></a>
### 其他

如需帮助，欢迎到 [Discord](https://discord.gg/luckperms) 与我们交流。那里有专门讨论 Hytale 问题的频道 :)
