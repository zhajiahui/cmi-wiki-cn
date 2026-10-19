---
title: CMILib 安装、更新与支持
source_url: https://github.com/Zrips/CMILib/blob/master/README.md
source_kind: official-wiki
translation_review: reviewed
source_version: CMILib 仓库 master，2026-10-19 官方原文快照
---


# CMILib 安装、更新与支持

<a id="introduction"></a>

## 简介

这个插件辅助库可以统一处理常用文本、十六进制颜色等功能。各个插件无需分别编写这些功能的代码，而是通过此库共用这些功能；它也提供 API，供其他开发者扩展自己的插件。

这样可以减小其他插件的总体积，让更新和维护更简单、更一致。

**注意：** Zrips 的所有插件都需要这个库。

<a id="library-releases-and-updates"></a>

## 版本发布与更新

强烈建议始终将此库保持为最新版本。最新构建可从以下位置下载：

- [开发者官网](home.md)
- [Spigot 发布页](plugin-page.md)

<a id="installation-instructions"></a>

## 安装说明

**与所有插件改动一样，先执行 `/stop` 关闭服务器，并完成完整备份。**

从[版本发布与更新](#library-releases-and-updates)中列出的发布网站下载最新版本，放入服务器的 `plugins/` 目录。

为避免冲突，建议先仅加载这个库，暂不加载依赖它的插件。这样可以确认后续出现的问题来自依赖插件，而非库本身。随后应向对应插件的开发者反馈，让其更新插件以适配库的变化。

服务器应能正常启动。首次启动后，会在服务器的 `plugins/` 文件夹中创建一个名为 `CMILib` 的文件夹，其中保存库的配置文件。可以按需要编辑，但这不是必需步骤。
如果你正在翻译语言文件，请向此仓库提交拉取请求。

完成后，再次执行 `/stop`，加入依赖此库的插件，并按各插件的要求继续设置。

<a id="support"></a>

## 支持

如果遇到此库的问题，请查看下方的[参与贡献](#contributing)，了解报告方式。

提问前，请先阅读[常见问题](faq.md)。

也可以在 [Zrips 社区 Discord](https://discord.gg/dDMamN4) 请求支持，与社区成员讨论问题。

<a id="contributing"></a>

## 参与贡献

欢迎克隆此仓库，并通过拉取请求提交错误修复或建议。

也可以[新建 Issue](https://github.com/Zrips/CMILib/issues/new) 报告错误或提出建议，但**请先**检查 [Issues](https://github.com/Zrips/CMILib/issues) 中是否已有相同内容，以及是否已在[拉取请求](https://github.com/Zrips/CMILib/pulls)中处理。

<a id="plugins-that-require-this-library"></a>

## 需要此库的插件

如果你开发了使用此库的插件，请告知作者，以便加入列表。

注意：受 Markdown 限制，点击链接会在当前页面打开。若要在新标签页打开，请右键选择“在新标签页中打开”。

|                                                   插件名称（Spigot 链接）                                                    | 起始版本 | 支持至版本 |                          插件作者                           |
|:------------------------------------------------------------------------------------------------------------------------------:|:------------:|:-------------:|:----------------------------------------------------------------:|
|                               [BottledExp](https://www.spigotmc.org/resources/bottledexp.2815/)                                |     3.x      |    最新版本     | [Zrips](https://www.spigotmc.org/resources/authors/zrips.24572/) |
| [CMI](https://www.spigotmc.org/resources/cmi-298-commands-insane-kits-portals-essentials-economy-mysql-sqlite-much-more.3742/) |     9.X      |    最新版本     | [Zrips](https://www.spigotmc.org/resources/authors/zrips.24572/) |
|                               [JobsReborn](https://www.spigotmc.org/resources/jobs-reborn.4216/)                               |     5.X      |    最新版本     | [Zrips](https://www.spigotmc.org/resources/authors/zrips.24572/) |
|     [MobFarmManager](https://www.spigotmc.org/resources/mob-farm-manager-supports-1-7-10-up-to-1-19-hopper-support.15127/)     |     2.X      |    最新版本     | [Zrips](https://www.spigotmc.org/resources/authors/zrips.24572/) |
|                                  [Recount](https://www.spigotmc.org/resources/recount.3962/)                                   |    3.5.X     |    最新版本     | [Zrips](https://www.spigotmc.org/resources/authors/zrips.24572/) |
|                       [Residence](https://www.spigotmc.org/resources/residence-1-7-10-up-to-1-19.11480/)                       |     5.X      |    最新版本     | [Zrips](https://www.spigotmc.org/resources/authors/zrips.24572/) |
|                     [SelectionVisualizer](https://www.spigotmc.org/resources/selection-visualizer.22631/)                      |   3.0.4.X    |    最新版本     | [Zrips](https://www.spigotmc.org/resources/authors/zrips.24572/) |
|           [TradeMe](https://www.spigotmc.org/resources/trademe-with-api-to-create-custom-trades-1-7-10-1-19-x.7544/)           |    6.1.X     |    最新版本     | [Zrips](https://www.spigotmc.org/resources/authors/zrips.24572/) |
|                                    [TryMe](https://www.spigotmc.org/resources/tryme.3330/)                                     |     7.X      |    最新版本     | [Zrips](https://www.spigotmc.org/resources/authors/zrips.24572/) |
