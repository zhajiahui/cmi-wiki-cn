---
title: 安装指南
source: https://docs.phoenixdevt.fr/mmoitems/install
source_snapshot: '2026-10-19'
---

# 安装指南 {#🔌-installation-guide}

## 安装MMOItems高级版 {#installing-mmoitems-premium}

将最新版本的MythicLib和MMOItems拖放到服务器上并重新启动。

## 插件：MMOMana {#addon-mmomana}

该插件已被MythicLib[原生魔力/耐力模块](../mythiclib/misc/mana-stamina.md)取代。

## 插件：MI PerWorldDrops（[下载](https://github.com/mmopluginteam/mmoitems-perworlddrops/releases)） {#addon-mi-perworlddrops-download}

MMOItemsPerWorldDrops 允许你将块和怪物的**掉落表限制在某些世界**。你可以将此插件拖放到插件文件夹中，就像MMOItems一样。重新启动服务器后，MMOItems插件文件夹中应出现 /drops 文件夹。在该文件夹中，你创建的每个 .yml 都对应于一个特定的世界（文件名必须与世界名称**完全**匹配）。为了了解如何设置这些YAML配置，请参阅此 [wiki 页面](items/drop-tables.md)。

这个插件保持最新，如果你不需要像MMOCore或MythicMobs这样巨大/复杂的删除表插件，它会很方便。

## 在旧版上安装MMOItemsPremium (<1.13) {#installing-mmoitems-premium-on-legacy-1-13}

> **信息**
>
>MMOItemsPremium (6.0.0+) 的最新版本不再支持1.12，请确保你的服务器保持最新状态，以便从MMOItems的所有功能中受益！

自4.7.6以来，MMOItemsPremium 具有1.12支持，但1.14+ 仍然是插件本机版本。需要下载 [1.12默认配置文件](https://www.dropbox.com/s/7j9gowyd32wy9cv/legacy-configs-UPDATED.zip?dl=1)，并在安装了 MI 版本后启动服务器后手动安装它们。

如果你在旧服务器上运行WorldGuard，则 **必须** 安装 **MMOItemsLegacyWG（[下载](https://github.com/mmopluginteam/mmoitems-legacywg/releases)）** 否则MMOItems在加载时会出现错误，并且无法启用。

---

原文：[🔌 Installation Guide](https://docs.phoenixdevt.fr/mmoitems/install) · 原文归档：2026-10-19
