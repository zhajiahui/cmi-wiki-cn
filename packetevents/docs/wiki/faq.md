---
title: "常见问题"
source_url: "https://docs.packetevents.com/faq/"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "packetevents-docs a2a91c32fe7ff913413072ab0e51fe95a36f4028（2026-10-19 快照）"
---

<a id="faq"></a>

# 常见问题

如果暂时还没看懂所有回答，也无需担心。本节假定你对这个库已有一定了解，可以把它当作帮助把握整体情况的简要说明；需要时也可以直接阅读详细指南。

<a id="does-packetevents-have-a-discord-server"></a>

## PacketEvents 有 Discord 服务器吗？

有。可以在 [Discord 服务器](https://discord.com/invite/DVHxPPxHZc)寻求支持。报告错误请使用 [GitHub Issues](https://github.com/retrooper/packetevents/issues)。

<a id="is-packetevents-free-software"></a>

## PacketEvents 是自由软件吗？

是。PacketEvents 是自由软件。有关其含义，请参阅[此处](https://gnu.org/philosophy/free-sw.html)。此外，PacketEvents 使用 GPLv3 许可证。

<a id="should-i-shade-the-packetevents-api-into-my-plugin"></a>

## 应该把 PacketEvents API 嵌入自己的插件吗？

不应该。TODO：有待补充说明。

<a id="why-do-i-get-a-noclassdeffounderror-when-using-the-packetevents-api-in-my-plugin"></a>

## 在插件中使用 PacketEvents API 时，为什么出现 “NoClassDefFoundError”？

<a id="cause-1"></a>

### 原因 #1

服务器可能找不到 PacketEvents API。可以把这个依赖嵌入自己的插件，或从 [SpigotMC](https://spigotmc.org/resources/80279/) 或 [Modrinth](https://modrinth.com/plugin/packetevents) 下载插件版本并安装到服务器。

<a id="cause-2"></a>

### 原因 #2

插件使用的 PacketEvents 版本，与嵌入插件或安装在服务器上的版本不兼容。
