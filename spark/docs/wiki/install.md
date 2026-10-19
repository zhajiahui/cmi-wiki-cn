---
title: 安装
source_url: https://spark.lucko.me/docs/Installation
source_kind: official-wiki
translation_review: reviewed
source_version: spark-docs 07dc48b059e25731294c9ca6f713c358dfabb8fc（2026-10-19 快照）
---

<a id="installation"></a>

# 安装

## Minecraft 服务端

从[下载页面](https://spark.lucko.me/download)下载最新的 spark **.jar** 文件，放入服务端的 `mods` 或 `plugins` 文件夹即可。

下次启动或重启服务器时，spark 就会加载。

使用 `/spark` 命令控制 spark。

你可能需要先为自己授予 `spark` 权限，或确认自己是服务器管理员（OP）。

!!! note "注意"

    如果使用 [Paper](https://papermc.io/software/paper) 1.21 或更新版本，spark **已内置在服务端中**，无需安装插件 JAR！

    要用 spark 插件覆盖 Paper 内置的 spark 版本，需要在服务器启动参数中加入 `-Dpaper.preferSparkPlugin=true`。详见 [Paper 文档](https://docs.papermc.io/paper/profiling)。

## Minecraft 客户端

从[下载页面](https://spark.lucko.me/download)下载最新的 spark **.jar** 文件，放入客户端的 `mods` 文件夹即可。

使用 `/sparkc` 命令控制 spark。

## Minecraft 代理端

从[下载页面](https://spark.lucko.me/download)下载最新的 spark **.jar** 文件，放入代理端的 `plugin` 文件夹即可。

下次启动或重启代理端时，spark 就会加载。

BungeeCord 使用 `/sparkb` 命令，Velocity 使用 `/sparkv` 命令。

你可能需要先为自己授予 `spark` 权限。
