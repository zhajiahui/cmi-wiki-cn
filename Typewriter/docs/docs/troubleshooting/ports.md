---
title: 网页面板加载问题排查（Panel Loading Issues Troubleshooting Guide）
source: https://docs.typewritermc.com/docs/troubleshooting/ports
source_version: 0.8.0
---

# 网页面板加载问题排查（Panel Loading Issues Troubleshooting Guide）

你是否遇到Typewriter插件面板无法加载的问题？本指南将帮助你排除故障并确保正确设置以获得最佳功能。

## 正确分配端口 {#assigning-ports-correctly}

如果面板未加载，常见问题可能是缺少指定的端口。Typewriter插件需要两个开放端口：

1. 一个用于面板加载的端口。
2. websocket 与服务器通信的另一个端口。

**警告**

由于这一要求，Aternos 等仅提供单个端口的托管平台与Typewriter插件不兼容。

## 使用正确的地址 {#using-the-correct-url}

确保你使用正确的 URL 来访问面板。格式应为`ip:port`，或者，如果你使用子域，则为`url:port`。使用正确的 URL 对于成功访问面板至关重要。

## 避免配置中使用重复端口 {#avoiding-duplicate-ports-in-config}

一个常见的错误是将端口包含在`config.yml`文件的`hostname`字段中。
主机名只能是 IP 地址或域名。它不应包含端口。
这是一个例子：

config.yml

```yaml
# ...
hostname: "127.0.0.1:25565" // Incorrect line
hostname: "127.0.0.1"       // Correct line
# ...
```

从主机名字段中删除端口可以解决与面板未加载相关的问题。

---

如需进一步帮助，请通过[Discord](https://discord.gg/HtbKyuDDBw)联系我们的社区。我们随时帮助你尽可能顺利地使用Typewriter插件！

---

原文：[Panel Loading Issues Troubleshooting Guide](https://docs.typewritermc.com/docs/troubleshooting/ports) · 文档版本：0.8.0
