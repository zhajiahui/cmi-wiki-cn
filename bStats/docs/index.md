---
title: "bStats"
source_kind: plugin-overview
translation_review: reviewed
---

# bStats

bStats 是面向服务器插件的使用统计服务。插件作者接入 bStats 后，可以查看服务器使用数量、版本分布和插件自定义统计。

这批资料以 **bStats 共享配置目录**随包提供，未列出独立 bStats JAR，**版本未标明**。该目录保存供接入插件共用的统计配置。

随包插件元数据未通过 `depend` 或 `softdepend` 指明 bStats 调用方。这类统计组件可集成在插件中，现有资料未说明由哪个随包插件创建或使用该目录。

服主可通过共享配置管理统计开关。官方说明将 `enabled` 设为 `false` 可以为服务器上的所有接入插件关闭 bStats；具体选项见[配置说明](configuration/index.md)。

## 官方资料

- [bStats 官方服主说明](https://bstats.org/docs/server-owners)：统计用途、共享配置和关闭方式。
