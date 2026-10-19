---
title: "Bungeecord 单一资源包不同功能"
source_url: "https://wiki.itemsadder.com/faq/bungeecord-velocity/single-resourcepack-multiple-server"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# Bungeecord 单一资源包不同功能

教程由 [@itsmemac](https://github.com/LoneDev6/Wiki-ItemsAdder/pull/35) 提供

在你按照本指南操作之前，请确保你已经完成了[**首次安装**](https://itemsadder.devs.beer/first-install)并且有一个正常运行的 IA 安装

**步骤 1**

在本地为你的服务器创建最终的资源包，其中包括你整个网络中需要的一切（每个物品、GUI、怪物、表情符号等）。\
为此，你需要在你的电脑上创建一个本地 Spigot 服务器，并在其中配置你想要的一切。

**步骤 2**

打开每个 Spigot 服务器，将 ItemsAdder 配置中的托管方法设为 `no-host`，并将物品提取选项设为 false。

```yaml
  hosting:
    no-host:
      enabled: true
  extract-default-items: false
  extract-default-resources: false
```

**步骤 3**

运行 `/iazip` 并将生成的资源包上传到一个文件托管服务，并确保它提供直接下载链接。\
例如 [**MCPACKS**](https://mc-packs.net/)**、**[**DropBox**](../../plugin-usage/plugin-configuration/resourcepack-hosting/dropbox.md)**、**[**GoogleDrive**](../../plugin-usage/plugin-configuration/resourcepack-hosting/google-drive.md)**。**

**步骤 4**

在 Bungee 上使用 [**Force resourcepack**](https://www.spigotmc.org/resources/force-resourcepacks.10499/) 等插件，让玩家进入群组服时加载资源包。

**步骤 5**

将 `ItemsAdder.jar` 和整个 `ItemsAdder` 插件文件夹从本地 Spigot 服务器复制到第一个网络服务器（例如 `lobby`）的 `/plugins` 文件夹中。

**步骤 6**

打开 ItemsAdder 的 config.yml 并禁用你不需要的功能。\
同时从 `plugins/ItemsAdder/contents/` 中删除不需要的文件。

不要删除 dictionaries, mcemojis, mcguis, mcicons, realcraft, various\_configs 文件夹。\
更多内容请参阅：[移除默认内容](../removing-default-content.md)

你基本上需要保留你想在这个特定服务器（在这个例子中是 `lobby`）中保留的功能文件夹。

**步骤 7**

重启服务器并加入。服务器应该会要求你下载资源包。\
然后你将只会看到你在 `contents` 文件夹中保留的物品。

**步骤 8**

为你的网络中的每个服务器重复步骤 5,6,7。

本教程不需要 **BungeePackFix** 插件。
