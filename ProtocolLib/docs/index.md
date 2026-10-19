---
title: "ProtocolLib"
source_kind: plugin-overview
translation_review: reviewed
---

# ProtocolLib

ProtocolLib 为其他插件提供数据包事件 API，用于监听、修改或取消服务器与客户端之间发送和接收的数据包，并封装底层实现细节。

随包版本为 **`5.5.0-SNAPSHOT-d89a5de`**。ProtocolLib 自身未声明其他必需插件或软依赖。本批 ItemsAdder 将其列为必需依赖（`depend`）；CrackShotX、NeigeItems、packetevents 将其列为软依赖（`softdepend`）。

## 管理命令与权限

- `/protocol config`：重载配置文件。
- `/protocol version`：显示当前运行的 ProtocolLib 版本。

这两条管理命令要求 `protocol.admin`。`protocol.info` 用于接收相应的更新通知和聊天警告，不是管理命令权限。

自动更新、聊天警告和调试等选项见[配置说明](configuration/index.md)。

## 官方资料

- [ProtocolLib 项目简介](https://github.com/dmulloy2/ProtocolLib/blob/d89a5deb3eb625b16846da57fbbb04bfdd0d031d/Readme.md)
- [作者发布页：命令与配置](https://www.spigotmc.org/resources/protocollib.1997/)
- [与随包版本提交后缀对应的默认配置](https://github.com/dmulloy2/ProtocolLib/blob/d89a5deb3eb625b16846da57fbbb04bfdd0d031d/src/main/resources/config.yml)
