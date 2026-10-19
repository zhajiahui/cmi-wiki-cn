---
title: "下载 Minecraft 资源失败"
source_url: "https://wiki.itemsadder.com/faq/failed-to-download-minecraft-assets"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 下载 Minecraft 资源失败

ItemsAdder 需要一些 Minecraft 资源才能工作，并会自动下载。不过，某些服务器环境可能会遇到下载问题（防火墙拦截、网络错误等）。

你可以手动下载这些资源来修复此问题。

#### 删除文件夹

删除文件夹 `ItemsAdder/storage/cache/vanilla_assets`

#### 下载资源


<div align="left"><figure><img src="../assets/7b83b52bc5b73a6ff11e.png" alt=""><figcaption></figcaption></figure></div>

#### 解压 `vanilla_assets` 文件夹

将 `vanilla_assets` 文件夹解压到 `ItemsAdder/storage/`

<div align="left"><figure><img src="../assets/be3a3169b013935aa820.png" alt=""><figcaption></figcaption></figure></div>

#### 完成

启动服务器，运行 `/iazip` 重新生成资源包。
