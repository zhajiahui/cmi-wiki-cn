---
title: "ProtocolLib 项目说明与构建"
source_url: "https://github.com/dmulloy2/ProtocolLib/blob/d89a5deb3eb625b16846da57fbbb04bfdd0d031d/Readme.md"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "ProtocolLib d89a5deb3eb625b16846da57fbbb04bfdd0d031d；官方 Wiki 与发布页 2026-10-19 快照"
---

# ProtocolLib 项目说明与构建

标准 Bukkit API 无法完成某些任务，这时可能需要直接操作甚至修改 Minecraft。常见做法是修改收发的数据包，或向数据流注入自定义数据包。但这种实现相当繁琐，而且主要受混淆影响，Minecraft 一发布新版本，大多数实现就会失效。

更关键的是，不同插件采用这种方式时，可能会挂接到相同的类，结果难以预测。常见后果是插件崩溃，也可能产生更隐蔽的错误。

<a id="resources"></a>

## 相关资源

* [Spigot 页面](https://spigotmc.org/resources/protocollib.1997/)
* [正式版本](https://github.com/dmulloy2/ProtocolLib/releases)
* [开发构建](https://github.com/dmulloy2/ProtocolLib/releases/tag/dev-build)
* [JavaDoc](https://dmulloy2.net/ProtocolLib/javadoc/)
* [协议 Wiki](https://minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge/Protocol)

`ProtocolLib.jar` 是主要的 Paper 插件。Spigot 服务器必须使用兼容版本 `ProtocolLib-Spigot.jar`。Maven 构件则是两个发行版本共用的平台无关库。

<a id="compilation"></a>

## 编译

ProtocolLib 使用 [Gradle](https://gradle.org/) 构建。安装 Gradle 后，在项目根目录执行 `./gradlew build` 即可。其他可能用到的 Gradle 目标包括 `clean`、`test` 和 `shadowJar`。`shadowJar` 会为 Paper 和 Spigot 分别生成包含全部依赖（ByteBuddy）的 JAR。



<a id="a-new-api"></a>

## 新的 API

**ProtocolLib** 提供类似 Bukkit 的事件 API，允许插件监听、修改或取消发送与接收的数据包。更重要的是，API 通过简单的索引式读写系统隐藏了复杂、混淆过的类，无需再引用 CraftBukkit。

<a id="compatibility"></a>

## 兼容性

此项目的主要目标之一是尽可能兼容 CraftBukkit。最终实现相当灵活，作者认为，之后可能只需为错误修复和新功能更新 ProtocolLib。

这依赖于反射：没有硬编码任何名称，而是通过字段类型、包名或参数类型推断每个字段、方法和类。它们在不同版本之间具有很高的一致性。
