---
title: Playit.gg
source: https://docs.typewritermc.com/docs/troubleshooting/playitgg
source_version: 0.8.0
---

# Playit.gg

**未测试**

这些文档尚未经过 100% 测试。这可能行不通。如果是这样，请在我们的[不和谐](https://discord.gg/gs5QYhfv9x)中提出问题。

**高级版**

Playit.gg在其免费计划中仅允许你转发 2 个端口。你将需要高级计划来转发更多端口！

在本教程中，你将学习如何使Typewriter与 playit.gg 一起工作

## Playit.gg 是什么？ {#what-is-playitgg}

Playit.gg是一项服务，允许你将本地主机的 minecraft 服务器公开以供任何人连接。这对于与朋友一起测试你的服务器或在短时间内创建公共服务器非常有用。

## 如何让 Typewriter 配合 Playit.gg 使用 {#how-to-make-typewriter-work-with-playitgg}

首先转到[playit.gg](https://playit.gg/)并创建一个代理并连接你的 Minecraft 服务器。互联网上有很多关于如何执行此操作的教程。

### 创建隧道 {#creating-a-new-tunnel}

在隧道选项卡中，你可以单击`+ Add tunnel`。

![隧道](../../assets/e80f0c001946-tunnels.323af52.1201.avif)

在弹出窗口中选择你的区域并使用隧道类型`TCP (protocol)`，然后将本地端口设置为`8080`（或你在 config.yml 中配置的端口），然后单击`Add tunnel`。

![创建隧道](../../assets/e70e423243e9-create-tunnel.e6136dc.743.avif)

现在你的隧道应该处于待处理状态，几秒钟后它应该可以工作。

### 连接 Typewriter 面板 {#connecting-to-the-tw-panel}

现在，你可以使用隧道选项卡中显示的 URL 连接到面板。

![隧道地址](../../assets/11b38d01cf1e-ip.22d12cd.1232.avif)

---

原文：[Playit.gg](https://docs.typewritermc.com/docs/troubleshooting/playitgg) · 文档版本：0.8.0
