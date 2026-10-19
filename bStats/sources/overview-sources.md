---
title: "bStats 官方资料摘录"
source_kind: plugin-overview
translation_review: reviewed
---

# bStats 官方资料摘录

核对日期：2026-10-19。随包形态为共享配置目录，没有独立 bStats JAR 的版本记录，组件版本未标明。

## 插件使用统计服务

来源：[bStats 官方服主说明](https://bstats.org/docs/server-owners)。

> bStats is a free metrics service for Minecraft and Hytale server plugins.

> When plugin authors integrate bStats into their plugins, they can see how many servers use their work, which server versions are popular, and how their plugins are configured.

对应中文：插件作者可通过接入 bStats 了解服务器使用数量、服务器版本分布以及插件配置使用情况。

## 共享配置与统计开关

同一官方页面说明，bStats 目录包含多个插件共用的配置文件，并给出关闭方式：

> You can disable bStats globally for all plugins on your server:

> Open the file with any text editor and change enabled to false:

```yaml
enabled: false
```

以上为官方公开说明中的配置示例，不代表随包配置的实际取值。

## 随包形态与调用方

随包清单列有 bStats 配置目录，没有独立 bStats JAR。其他随包插件也未在 `depend` 或 `softdepend` 中声明 bStats。官方说明其可集成在插件中，因此未将未声明依赖理解为没有使用统计，也未指认创建目录的具体插件。
