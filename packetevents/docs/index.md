---
title: "PacketEvents"
source_kind: plugin-overview
translation_review: reviewed
---

# PacketEvents

PacketEvents 是面向 Minecraft Java 版的数据包协议库，用于处理和发送数据包。它在插件元数据中的名称为 `packetevents`。

随包版本为 **`2.14.0`**。本批 Citizens 和 CrackShotX 将 packetevents 列为软依赖（`softdepend`），未列为必需依赖。

packetevents 自身未声明必需插件，软依赖为 ProtocolLib、ProtocolSupport、ViaVersion、ViaBackwards、ViaRewind、Geyser-Spigot。这些插件均为可选联动。

官方 Spigot 插件声明未列出管理命令或权限节点。随包未提供独立配置。

## 官方资料

- [PacketEvents 项目简介](https://github.com/retrooper/packetevents/blob/7ceabaef7350e512c4b4cd88f9eb982d93f77029/README.md)
- [官方 Spigot 插件声明](https://github.com/retrooper/packetevents/blob/7ceabaef7350e512c4b4cd88f9eb982d93f77029/spigot/src/main/resources/plugin.yml)
- [官方文档](https://docs.packetevents.com/)：开发环境、嵌入方式、数据包处理和发送等内容。
