---
title: "Vault 安装与项目说明"
source_url: "https://github.com/MilkBowl/Vault/blob/460cb21c6215433da526192720de40b6662f5f99/README.md"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "Vault 460cb21c6215433da526192720de40b6662f5f99；官方项目页 2026-10-19 快照"
---

<a id="vault-abstraction-library-for-bukkit-build-statushttpsapptravis-cicommilkbowlvault"></a>

# Vault 安装与项目说明

Vault 是 Bukkit 的抽象库。

[![Build Status](assets/4eb903681f04-Vault.svg)

<a id="for-developers"></a>

## 面向开发者

使用 Vault API 开发的相关信息，请参阅 [VaultAPI](https://www.github.com/MilkBowl/VaultAPI)。以前开发时使用的构建产物与服务器安装的相同；现在 API 已从主项目拆分，并采用不同的构件名称。请在构建流程中相应调整。

<a id="installing"></a>

## 安装

将提供的 “Vault.jar” 复制到 `<bukkit-install-dir>/plugins` 目录即可，剩下的会自动完成。如果想调整配置，可以通过配置文件修改，但大多数情况下无需改动。更多信息请参阅 “Advanced Configuration” 部分。

<a id="why-vault"></a>

## 为什么选择 Vault？

作者不偏向哪一个库，适合插件及开发需求即可。比起只关注某一类插件，作者认为集中提供一套解决方案，也就是 Vault，是更合适的方向。Vault 的想法由此产生。

作者认为你可能会喜欢以下特点：

- 无需把作者的源码包含在自己的插件中。
  Vault 的全部功能运行在独立插件里，只需获取它的实例即可。这能减少多个插件使用同一命名空间带来的问题。把 Vault.jar 加入下载 ZIP 就可以。
- 广泛的插件支持。
  作者希望抽象层不仅服务于经济插件，也服务于权限插件。
- 选择自由。
  Bukkit 的乐趣有一半就在于可以自由选择。更多选择不会妨碍开发者。

<a id="permissions"></a>

## 权限

- vault.admin
  - 决定玩家是否应收到更新通知。

<a id="license"></a>

## 许可证

Copyright (C) 2011-2018 Morgan Humes <morgan@lanaddict.com>

Vault 是自由软件，你可以依据自由软件基金会发布的 GNU 宽通用公共许可证（GNU Lesser General Public License）第 3 版，或自行选择的任何更新版本，重新分发或修改它。

Vault 的发布旨在提供帮助，但**不提供任何保证**，甚至不包含对适销性或特定用途适用性的默示保证。详情请参阅 GNU 宽通用公共许可证。

你应当随 Vault 一同收到 GNU 宽通用公共许可证副本。若没有，请参阅 <http://www.gnu.org/licenses/>。

<a id="building"></a>

## 构建

Vault 附带从当前分支构建所需的全部库，同时提供 Apache Ant 构建文件（build.xml）和 Maven 构建文件（pom.xml）。目前首选 Maven 构建方式。

<a id="dependencies"></a>

## 依赖

Vault 为其他插件提供桥接，因此构建时需要这些插件的二进制文件。为方便使用，它们已包含在 lib 文件夹中，并会不定期更新。插件开发者在接入 Vault 时无需使用这些库，只需针对 Vault 编译。

<a id="supported-plugins"></a>

## 支持的插件
Vault 为以下类别和插件提供抽象层。如果你开发的插件也需要支持，请在自己的插件中添加连接器，因为 Vault 已不再维护新的插件连接器。

* 权限
  - bPermissions
  - bPermissions 2 (https://dev.bukkit.org/projects/bpermissions)
  - DroxPerms
  - Group Manager (Essentials) (https://forums.bukkit.org/threads/15312/)
  - LuckPerms (https://www.spigotmc.org/resources/luckperms-an-advanced-permissions-plugin.28140/)
  - OverPermissions (https://dev.bukkit.org/projects/overpermissions)
  - Permissions 3 (https://forums.bukkit.org/threads/18430/)
  - PermissionsBukkit
  - Permissions Ex (PEX) (https://forums.bukkit.org/threads/18140/)
  - Privileges
  - rscPermissions
  - SimplyPerms
  - SuperPerms（Bukkit 默认）
  - TotalPermissions (https://dev.bukkit.org/projects/totalpermissions)
  - XPerms
  - zPermissions

* 聊天
  - bPermissions
  - Group Manager (Essentials) (https://forums.bukkit.org/threads/15312/)
  - iChat
  - LuckPerms (https://www.spigotmc.org/resources/luckperms-an-advanced-permissions-plugin.28140/)
  - mChat
  - mChatSuite
  - OverPermissions (https://dev.bukkit.org/projects/overpermissions)
  - Permissions 3 (https://forums.bukkit.org/threads/18430/)
  - Permissions Ex (PEX) (https://forums.bukkit.org/threads/18140/)
  - rscPermissions
  - TotalPermissions (https://dev.bukkit.org/projects/totalpermissions)
  - zPermissions
