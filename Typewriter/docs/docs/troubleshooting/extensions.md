---
title: 扩展问题排查（Extensions Troubleshooting）
source: https://docs.typewritermc.com/docs/troubleshooting/extensions
source_version: 0.8.0
---

# 扩展问题排查（Extensions Troubleshooting）

你的Typewriter扩展遇到问题吗？本指南提供分步说明，以确保你的扩展正确设置并与Typewriter插件一起最佳运行。

## 扩展的正确位置 {#correct-extension-placement}

请务必注意，Typewriter插件的扩展不是标准Paper插件。它们是Typewriter专用的特殊 JAR 文件，因此需要单独存储。为确保正常运行：

1. 导航到插件目录：`/plugins/Typewriter/extensions`。
2. 如果“扩展”文件夹不存在，请创建一个来存储新扩展。
3. 将你的扩展文件放入此“扩展”文件夹中。

这个专用文件夹确保Typewriter可以正确读取和使用这些扩展，而不会将它们与常规Paper插件混淆。

## 扩展与插件的版本兼容性 {#extension-and-plugin-version-compatibility}

为了使Typewriter插件及其扩展协调工作，它们必须位于同一版本。这对于更新和降级都至关重要：

1. 更新`typewriter.jar`文件时，同时更新所有扩展至同一版本。
2. 降级时也适用同样的规则；确保插件和扩展都恢复到匹配的版本。

保持Typewriter插件及其扩展之间的版本一致性是防止兼容性问题并确保顺利运行的关键。

---

如需进一步帮助，请通过[Discord](https://discord.gg/HtbKyuDDBw)联系我们的社区。我们随时帮助你尽可能顺利地使用Typewriter插件！

---

原文：[Extensions Troubleshooting](https://docs.typewritermc.com/docs/troubleshooting/extensions) · 文档版本：0.8.0
