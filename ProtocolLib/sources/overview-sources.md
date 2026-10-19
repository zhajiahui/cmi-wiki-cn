---
title: "ProtocolLib 官方资料摘录"
source_kind: plugin-overview
translation_review: reviewed
---

# ProtocolLib 官方资料摘录

核对日期：2026-10-19。随包版本为 `5.5.0-SNAPSHOT-d89a5de`；下列源码提交号以 `d89a5de` 开头，与版本后缀相符。

## 数据包 API

来源：[官方 Readme](https://github.com/dmulloy2/ProtocolLib/blob/d89a5deb3eb625b16846da57fbbb04bfdd0d031d/Readme.md)。

> ProtocolLib attempts to solve this problem by providing an event API, much like Bukkit, that allows plugins to monitor, modify, or cancel packets sent and received.

## 管理命令与通知权限

来源：[作者发布页](https://www.spigotmc.org/resources/protocollib.1997/)。

> config: Reload the configuration file.

> version: Displays the currently running version of ProtocolLib.

> All of these commands require the permission protocol.admin.

来源：[同提交的默认配置](https://github.com/dmulloy2/ProtocolLib/blob/d89a5deb3eb625b16846da57fbbb04bfdd0d031d/src/main/resources/config.yml)。

> Prints certain warnings to players with the protocol.info permission

作者发布页的配置说明也将新版本通知的接收权限写为 `protocol.info`，因此将其与管理命令要求的 `protocol.admin` 分开说明。

## 随包依赖声明

随包 JAR 的 `plugin.yml` 中，ProtocolLib 的 `depend` 与 `softdepend` 均为空；ItemsAdder 的 `depend` 包含 ProtocolLib；CrackShotX、NeigeItems、packetevents 的 `softdepend` 包含 ProtocolLib。
