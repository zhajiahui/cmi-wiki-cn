---
title: "矩形字符"
source_url: "https://wiki.itemsadder.com/faq/rectangle-character"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 矩形字符

## 看到 ▯，而不是表情或称号

您的资源包可能与配置不同步。\
在添加任何新图像后，请确保运行 `/iazip` 并重新上传资源包（如果您使用的是 Dropbox 或类似的托管方法）。

有关正确托管资源包的更多信息：[资源包托管](../plugin-usage/plugin-configuration/resourcepack-hosting.md)

确保 `y_position` 不大于图像高度（以像素为单位），并且 `y_position` 不大于（图像高度 \* `scale_ratio`）。

Minecraft 不支持这一点，它将无法工作，我也无法修复，这是游戏本身的限制。

如果您仍未解决问题，请检查您的客户端和服务器日志以确定问题的原因。

阅读此处了解如何操作：

[identify-why-textures-are-not-shown.md](identify-why-textures-are-not-shown.md)
