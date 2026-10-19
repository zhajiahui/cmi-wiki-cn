---
title: 迁移
source_url: https://luckperms.net/wiki/Migration
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

LuckPerms 可以自动从其他插件导入权限数据，我们将这一系统称为“迁移”。

<a id="intro"></a>
### 简介
需要注意，这些脚本并非十全十美。它们能够较好地转换现有的全部数据，并且在*大多数情况下*都能正常工作。不过，数据情况各不相同，有时仍会遇到作者未考虑到的情形。

LuckPerms 与其他权限插件有一些相似之处，但某些部分在根本上有所不同，因此自动迁移有时比较棘手。

另外，让插件代为迁移所有数据，意味着你没有机会学习 LuckPerms 的命令，这在以后可能会成为问题。😉 如果从 PermissionsEx 或 GroupManager 迁移，[这个页面可能会对你有帮助](migrating-from-groupmanager-or-permissionsex.md)。

如果原有权限设置比较陈旧，或者你对现有设置并不完全满意，现在也许正适合重新整理和清理，并在这个过程中学习 LuckPerms 命令！


<a id="supported-plugins"></a>
#### 支持的插件
支持从以下插件迁移：

* GroupManager
* PermissionsEx（仅限 Bukkit/Spigot）
* zPermissions
* bPermissions
* PermissionsBukkit
* PowerRanks
* UltraPermissions
* BungeePerms（迁移只能在代理端执行）

<a id="the-process"></a>
## 迁移流程
迁移流程比较简单，不过各平台之间略有不同。

<a id="step-1-install-luckperms"></a>
#### 第 1 步：安装 LuckPerms

首先，需要[安装 LuckPerms](installation.md)。暂时不要移除旧权限插件。

确认旧权限插件仍能正常启用。如果原有权限系统已经损坏，迁移过程就无法正常工作。

如果打算更换数据[存储类型](storage-types.md)，例如改用 mysql，现在进行更改最为方便。如果决定在迁移后再更换存储类型，请按照[切换存储类型](switching-storage-types.md)中的说明操作。

<a id="step-2-install-the-correct-migration-plugin"></a>
#### 第 2 步：安装对应的迁移插件

从下表下载与你现有权限插件对应的 JAR，并将其也放入 plugins 文件夹。

| 插件 | 迁移 JAR | 迁移命令 |
| ----------------- | ------------------------------------------------------------ | ---------------------------- |
| GroupManager      | [luckperms-migration-groupmanager.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/groupmanager/build/libs/luckperms-migration-groupmanager.jar) | `/migrate-groupmanager`      |
| PermissionsEx     | [luckperms-migration-permissionsex.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/permissionsex/build/libs/luckperms-migration-permissionsex.jar) | `/migrate-permissionsex`     |
| zPermissions      | [luckperms-migration-zpermissions.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/zpermissions/build/libs/luckperms-migration-zpermissions.jar) | `/migrate-zpermissions`      |
| bPermissions      | [luckperms-migration-bpermissions.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/bpermissions/build/libs/luckperms-migration-bpermissions.jar) | `/migrate-bpermissions`      |
| PermissionsBukkit | [luckperms-migration-permissionsbukkit.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/permissionsbukkit/build/libs/luckperms-migration-permissionsbukkit.jar) | `/migrate-permissionsbukkit` |
| PowerRanks        | [luckperms-migration-powerranks.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/powerranks/build/libs/luckperms-migration-powerranks.jar) | `/migrate-powerranks`        |
| UltraPermissions  | [luckperms-migration-ultrapermissions.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/ultrapermissions/build/libs/luckperms-migration-ultrapermissions.jar) | `/migrate-ultrapermissions` |
| BungeePerms       | [luckperms-migration-bungeeperms.jar](https://ci.lucko.me/job/luckperms-migration/lastSuccessfulBuild/artifact/bungeeperms/build/libs/luckperms-migration-bungeeperms.jar) | `/migrate-bungeeperms`       |

<a id="step-3-restart-your-server-then-run-the-migration-command"></a>
#### 第 3 步：重启服务器，然后执行迁移命令。

重启服务器，让原有插件、LuckPerms 和迁移插件正确加载。

然后进入服务器控制台，执行上表列出的迁移命令。

接下来稍作等待，让 LuckPerms 完成剩余工作！迁移过程中会显示进度，完成后还会再次通知你。

迁移完成后，停止服务器，移除旧权限插件和迁移 JAR，然后重新启动服务器。

如果从 GroupManager 或 PermissionsEx 迁移，[这里](migrating-from-groupmanager-or-permissionsex.md)还有一些可能有用的补充资料！