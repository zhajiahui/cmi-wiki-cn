---
title: "LuckPerms 官方资料摘录"
source_kind: plugin-overview
translation_review: reviewed
---

# LuckPerms 官方资料摘录

核对日期：2026-10-19。随包版本为 `5.5.71`；以下官方资料用于核对功能、命令和配置行为。

## 权限管理功能

来源：[官方 README](https://github.com/LuckPerms/LuckPerms/blob/5fc3d583c412854e050b1e4ba8aa5036d8daf982/README.md)。

> LuckPerms is a permissions plugin for Minecraft servers. It allows server admins to control what features players can use by creating groups and assigning permissions.

> easy to use - setup permissions using commands, directly in config files, or using the web editor.

对应中文：通过权限组和权限控制玩家功能，提供命令、配置文件和网页编辑器三种管理方式。

## 命令与配置重载

来源：[General Commands](https://github.com/LuckPerms/wiki/blob/fc2919c3d5e6bfba82af31f9930273b00f08ddbf/pages/General-Commands.md)、[Permissions](https://github.com/LuckPerms/wiki/blob/fc2919c3d5e6bfba82af31f9930273b00f08ddbf/pages/Permissions.md)。

官方命令页分别列出：

- `/lp`：`Permission: n/a`。
- `/lp editor [type] [filter]`：`Permission: luckperms.editor`。
- `/lp sync`：`Permission: luckperms.sync`。
- `/lp reloadconfig`：`Permission: luckperms.reloadconfig`。

> Not all entries are reloaded by this command, and some require a full server reboot to take effect. (storage settings, for example)

来源：[官方配置文档](https://luckperms.net/wiki/Configuration)及其[页面源码](https://github.com/LuckPerms/wiki/blob/fc2919c3d5e6bfba82af31f9930273b00f08ddbf/pages/Configuration.md)。

> Please note that the configuration file does not automatically update when new options are added. The default options are used if nothing is found in the file.

## 随包依赖声明

以下关系来自随包 JAR 的 `plugin.yml`：LuckPerms 的 `depend` 为空，`softdepend` 为 LilyPad-Connect、ViaVersion；ItemsAdder 的 `softdepend` 包含 LuckPerms。软依赖没有改写为必需插件。
