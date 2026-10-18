---
title: 安装指南（Installation Guide）
source: https://docs.typewritermc.com/docs/getting-started/installation
source_version: 0.8.0
---

# 安装指南（Installation Guide）

**平台兼容性**

Typewriter 仅适用于 **Paper** 服务端，不支持 Spigot 或 Bukkit 服务端。

## 安装 Typewriter 插件 {#installing-the-typewriter-plugin}

按以下步骤在 Paper Minecraft 服务器上安装 Typewriter。

### 安装插件 {#plugin-installation}

1. 通过[此 Modrinth 链接](https://modrinth.com/plugin/typewriter/version/0.8.0)下载**最新版本**。
2. 将下载的插件放入服务器的 `plugins` 文件夹。

### 安装依赖 {#handling-dependencies}

Typewriter 需要安装额外的依赖插件才能正常运行。

3. 下载 Typewriter 的依赖 [PacketEvents](https://modrinth.com/plugin/packetevents/versions?l=paper)，放入 `plugins` 目录。
4. 确认未安装 [InteractiveChat](https://www.spigotmc.org/resources/interactivechat-show-items-inventory-in-chat-custom-chat-keywords-bungee-velocity-support.75870/) 或 [CustomNamePlates](https://polymart.org/resource/customnameplates.2543)（3.0.15 或更低版本）；这些插件可能与 Typewriter 冲突。

### 基础扩展（Basic Extension） {#basic-extension}

Typewriter 提供多种扩展，其中必须安装 `BasicExtension`。

5. 通过[此 Modrinth 链接](https://modrinth.com/plugin/typewriter/version/0.8.0)，从**最新版本**中下载最新的 `BasicExtension`，放入 `plugins/Typewriter/extensions` 文件夹。

可用扩展的完整列表见[扩展](../../adapters.md)。

6. 全部组件放好后，重启 Minecraft 服务器，完成 Typewriter 安装。

**版本不匹配**

更新插件时，**每次都要**安装与该版本对应的扩展。扩展与插件版本不匹配，可能导致插件无法正常工作！

## 配置网页面板 {#configuring-the-web-panel}

**外部服务器服务商**

Typewriter 的网页面板**不兼容**部分外部服务器服务商，包括 **Minehut**、**Aternos** 和 **Apex**。这些服务商通常不支持多个端口，但可以尝试联系其客服申请开放额外端口。

如果无法开放额外端口，Typewriter 的其他功能仍可使用；也可以在本地搭建安装了 Typewriter 的服务器。

需要进一步帮助时，可在 [Discord](https://discord.gg/HtbKyuDDBw) 提问。

**资源占用**

网页面板和 WebSocket 会占用服务器资源，建议将面板放在开发服务器上，而非正式服务器。

安装插件后，继续配置网页面板。

网页面板至少需要额外开放两个端口，端口号可以修改。
默认端口为 `8080` 和 `9092`。

按以下步骤启用网页面板：

### 启用网页面板 {#enabling-the-web-panel}

1. 打开 `plugins/Typewriter/config.yml` 文件。
2. 将配置改为以下内容：

plugins/Typewriter/config.yml

```yaml
# Whether the web panel and web sockets are enabled.
enabled: true
# The hostname of the server. CHANGE THIS to your server's IP.
hostname: "127.0.0.1"
# The panel uses web sockets to sync changes to the server and allows you to work with multiple people at the same time.
websocket:
  # The port of the websocket server. Make sure this port is open.
  port: 9092
  # The authentication that is used. Leave unchanged if you don't know what you are doing.
  auth: "session"
panel:
  # The panel can be disabled while the sockets are still open. Only disable this if you know what you are doing.
  # If the web sockets are disabled, then the panel will always be disabled.
  enabled: true
  # The port of the web panel. Make sure this port is open.
  port: 8080
```

3. 用 [portchecker](https://portchecker.co/) 检查端口是否开放。如果没有开放，请自行开放端口，或联系服务器服务商处理。
4. 重启服务器，完成安装。

## 连接网页面板 {#connecting-to-the-web-panel}

连接网页面板的步骤如下：

1. 在游戏中执行 `/typewriter connect`，获取网页面板的访问链接。

![连接命令](../../assets/d1e40a02ae79-connect-command-00f3ad6eb18bd0022adde6278b4cfab7.gif)

2. 用浏览器打开链接。

![连接到书中的网页面板](../../assets/45067219a5da-connect-book.1adde74.445.avif)

连接成功后，就可以在网页面板中创建和配置任务、NPC 对话等内容，也可以查看、编辑服务器已有的玩家交互。

## 疑难解答 {#troubleshooting}

遇到问题时，可查看[疑难解答](../troubleshooting.md)中的常见问题处理方法。
如果仍有问题，可在 [Discord](https://discord.gg/HtbKyuDDBw) 求助。

## 下一步 {#whats-next}

按照[第一个交互](../creating-stories/interactions.md)创建第一个交互。如有疑问，可在 [Discord](https://discord.gg/HtbKyuDDBw) 提问。

---

原文：[Installation Guide](https://docs.typewritermc.com/docs/getting-started/installation) · 文档版本：0.8.0
