---
title: 安装
source_url: https://worldguard.enginehub.org/en/latest/install/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 安装 { #installation }

## 前置要求 { #requirements }

WorldGuard 需要支持 [Bukkit API](https://dl.bukkit.org/) 的 Minecraft 服务器，包括 Spigot 和 Paper。“原版”Minecraft 服务器无法运行插件；Forge、Sponge 等其他服务器实现也不受 WorldGuard 支持。

另一个必需前置是 [WorldEdit](https://www.enginehub.org/worldedit) 的 Bukkit 插件版，它是同样由我们开发的轻量级游戏内地图编辑器。请注意，必须使用 Bukkit 版 WorldEdit，而不是其他实现。

## 安装 { #id1 }

可以从 [Bukkit 开发者网站下载 WorldGuard](https://dev.bukkit.org/bukkit-plugins/worldguard/)。

1. 如果服务器目录中还没有“plugins”文件夹，请先创建它。

2. 将 WorldGuard 的 .jar 文件复制到 plugins 文件夹。别忘了同时安装 WorldEdit！

3. 启动服务器。

检查服务器日志是否有错误。如果出现错误，请参阅[常见问题](faq.md)。
