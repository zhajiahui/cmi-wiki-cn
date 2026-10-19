---
title: "packetevents 官方资料摘录"
source_kind: plugin-overview
translation_review: reviewed
---

# PacketEvents 官方资料摘录

核对日期：2026-10-19。随包版本为 `2.14.0`，插件名为 `packetevents`。

## 协议库用途

来源：[官方 README](https://github.com/retrooper/packetevents/blob/7ceabaef7350e512c4b4cd88f9eb982d93f77029/README.md)。

> PacketEvents is a protocol library tailored to Minecraft Java Edition, designed to facilitate the processing and transmission of packets.

## 插件声明

来源：[官方 Spigot plugin.yml](https://github.com/retrooper/packetevents/blob/7ceabaef7350e512c4b4cd88f9eb982d93f77029/spigot/src/main/resources/plugin.yml)。

```yaml
name: packetevents
main: io.github.retrooper.packetevents.PacketEventsPlugin
softdepend:
  - ProtocolLib
  - ProtocolSupport
  - ViaVersion
  - ViaBackwards
  - ViaRewind
  - Geyser-Spigot
```

上列为官方文件节选。该文件未列 `commands` 或 `permissions`；随包元数据的命令和权限列表也为空。

## 随包依赖与文档范围

随包 JAR 的 `plugin.yml` 中，packetevents 的 `depend` 为空；`softdepend` 与上列相同。Citizens 和 CrackShotX 的 `softdepend` 包含 packetevents。

[官方文档](https://docs.packetevents.com/)介绍开发环境、嵌入方式和数据包 API。本次未确认面向服主的独立 YAML 配置手册；随包也未提供独立配置，不将开发者 API 设置改写为配置键。
