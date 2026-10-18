---
title: 兼容性
source: https://docs.phoenixdevt.fr/mmoprofiles/features/compatibility
source_snapshot: '2026-10-19'
---

# 兼容性 {#🦾-compatibility}

插件的主要用途是让其他插件通过 API，按档案分别保存数据。支持 MMOProfiles 的插件会将数据保存到档案下，而不是直接保存到玩家名下，因此切换档案就像换了一个账号登录。

## 大型多人在线游戏插件 {#mmo-plugins}

整个 MMO 插件系列（[MMOCore](../../mmocore/index.md)、[MMOInventory](../../mmoinventory/index.md)、[MMOItems](../../mmoitems/index.md)、[MythicLib](../../mythiclib/index.md)）**完整支持**按档案保存数据。

## Vault经济型 {#vault-economy}

MMOProfiles 会保存玩家的 Vault 余额，因此支持所有通过 Vault 接入的经济插件。

## CoreTools {#coretools}

CoreTools（[SpigotMC](https://www.spigotmc.org/resources/coretools.125126) - [Polymart](https://polymart.org/product/7372/coretools) - [Wiki](https://gitlab.com/ranetdev/CoreTools/-/wikis/home)）完整支持按档案保存数据。

## 美丽探索 新 {#beautyquests}

[BeautyQuests](https://www.spigotmc.org/resources/beautyquests.39255) 支持 MMOProfiles，可以为各个档案分别记录任务进度。要启用兼容，请下载安装 [AccountsHook](https://www.spigotmc.org/resources/accountshook.59491/)，将 MMOProfiles 的档案 API 提供给 BeautyQuests。

> **信息**
>
> 已不再需要安装名为 *AccountsHook-MMOProfiles* 的附加插件。

## 贝顿探索 {#betonquest}

BetonQuest 正在开发对 MMOProfiles 的原生支持。它已有支持玩家使用多个档案的档案系统，相关兼容仍在推进。

---

原文：[🦾 Compatibility](https://docs.phoenixdevt.fr/mmoprofiles/features/compatibility) · 原文归档：2026-10-19
