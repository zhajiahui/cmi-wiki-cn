---
title: 疑难解答（Troubleshooting Guide）
source: https://docs.typewritermc.com/docs/troubleshooting
source_version: 0.8.0
---

# 疑难解答（Troubleshooting Guide）

本页汇总使用 Typewriter 时的常见问题及处理方法。向 Discord 或 GitHub 求助前，可以先按这里的说明排查。

## 面板无法加载 {#panel-not-loading}

如果你遇到面板无法加载的问题，请按照以下步骤操作：

1. 确认你的服务器正在运行并且可以访问。
2. 检查是否存在任何网络连接问题。
3. 确保你的防火墙设置没有阻止访问。

有关更详细的故障排除步骤，请参阅：[网页面板加载问题排查](troubleshooting/ports.md)。

## 未显示条目 {#no-entries-showing}

![没有条目](../assets/e21678a2ead7-no-entries.ddaef64.1877.avif)

当未安装扩展时，通常会出现此问题。要解决此问题，请确保按照**[安装指南](getting-started/installation.md#basic-extension)**中概述的步骤正确安装扩展。

## 安装扩展时提示“plugin.yml not found” {#error-pluginyml-not-found-when-installing-an-extension}

如果你在安装扩展时遇到类似以下错误消息：

```log
[08:49:35 ERROR]: [DirectoryProviderSource] Error loading plugin: Directory 'plugins/BasicExtension.jar' failed to load!
java.lang.RuntimeException: Directory 'plugins/BasicExtension.jar' failed to load!
        ...
Caused by: java.lang.IllegalArgumentException: Directory 'plugins/BasicExtension.jar' does not contain a paper-plugin.yml or plugin.yml! Could not determine plugin type, cannot load a plugin from it!
```

这通常表明扩展程序未放置在正确的文件夹中。有关正确放置的说明，请参阅[扩展问题排查](troubleshooting/extensions.md#correct-extension-placement)。

## 占位符未正确解析 {#placeholders-not-parsing-correctly}

如果PlaceholderAPI中的占位符（例如`%player_name%`）在Typewriter中未正确解析，请按照以下故障排除步骤操作：

1. 确定所需的PlaceholderAPI占位符扩展。可以在此处找到扩展列表[](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki/Placeholders)。
2. 使用`/papi ecloud download [extension_name]`安装必要的扩展。对于`%player_name%`，请使用`/papi ecloud download player`。
3. 通过运行`/papi parse me <placeholder>`检查正常使用中是否正确解析占位符。对于`%player_name%`，请使用`/papi parse me %player_name%`。
4. 如果占位符在正常使用中工作但在Typewriter中仍然不起作用，请尝试重新启动服务器。

如果这些步骤无法解决问题，请通过在我们的[Discord](https://discord.gg/HtbKyuDDBw)上创建票证来联系我们以获得进一步支持。

---

原文：[Troubleshooting Guide](https://docs.typewritermc.com/docs/troubleshooting) · 文档版本：0.8.0
