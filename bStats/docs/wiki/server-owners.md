---
title: "服主说明"
source_url: "https://bstats.org/docs/server-owners"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "官方服务文档 2026-10-19 快照"
---

<a id="for-server-owners"></a>

# 服主说明

了解 bStats 如何收集统计、分享哪些数据，以及如何管理你的偏好。

<a id="bstats-is-a-free-open-source-hobby-project"></a>

## bStats 是免费、开源的业余项目

bStats 是出于兴趣维护的项目，完全[开源](https://github.com/Bastian/bStats)，可以免费使用。背后没有公司，没有付费套餐，也无意通过你的数据获利。

<a id="what-is-bstats"></a>

## bStats 是什么？

bStats 为 Minecraft 和 Hytale 服务端插件提供免费统计服务。插件作者在插件中接入 bStats 后，就能了解有多少服务器使用自己的作品、哪些服务端版本较常见，以及插件的配置使用情况。

安装使用 bStats 的插件后，服务器会自动向插件作者分享基本使用统计。这个过程在后台完成，不影响服务器性能。所收集的数据是匿名的，不会关联到你的某一台服务器。

<a id="what-data-is-collected"></a>

## 收集哪些数据？

bStats 只收集非个人数据，并以汇总统计展示。它不会收集玩家名称、聊天记录、世界数据或任何可识别个人身份的信息。

<a id="example-of-collected-data"></a>

### 收集的数据示例

- 当前在线玩家数
- 服务端软件及版本，例如 Spigot 1.20.1
- Java 版本
- 操作系统类型
- 服务器所在位置，仅精确到国家

<a id="plugin-specific-data"></a>

### 插件特定数据

有些插件会收集自定义统计，了解你如何使用其功能。例如，统计哪些配置选项最常用，帮助作者决定优先开发哪些功能。

所有收集的数据都是公开的，可以在对应插件的仪表盘查看。

<a id="why-keep-metrics-enabled"></a>

## 为什么保持统计开启？

bStats 从几个方面帮助 Minecraft 和 Hytale 服务端社区：

<a id="supports-the-community"></a>

### 支持社区

许多作者免费维护插件。使用统计是一种具体的支持方式，能让作者看到他们为社区投入的时间确实产生了价值。

<a id="guides-development-priorities"></a>

### 帮助确定开发重点

作者可以知道哪些服务端版本最常见、哪些功能使用频繁，以及应该将开发精力投入哪里，从而改善插件。

<a id="privacy-first-and-community-run"></a>

### 注重隐私，由社区运营

bStats 开源，由志愿者而非公司运营。只收集最少量的匿名数据，源码公开，你可以检查到底分享了什么。

<a id="motivates-developers"></a>

### 鼓励开发者

真实的使用统计能鼓励插件作者继续维护和改进作品。看到其他人确实在使用自己的作品，会带来很大的动力。

<a id="how-to-disable-bstats"></a>

## 如何关闭 bStats

如果你不想分享统计，bStats 尊重你的选择。可以为服务器上的全部插件统一关闭 bStats：

<a id="step-1-locate-the-config-file"></a>

### 第 1 步：找到配置文件

进入服务器目录，找到 bStats 配置文件，通常位于：

`/plugins/bStats/config.yml`，具体位置可能因服务端平台而异。

<a id="step-2-edit-the-config"></a>

### 第 2 步：编辑配置

用任意文本编辑器打开文件，将 `enabled` 改为 `false`：

```
enabled: false
```

<a id="frequently-asked-questions"></a>

## 常见问题

<a id="does-bstats-affect-server-performance"></a>

### bStats 会影响服务器性能吗？

不会。bStats 在后台异步发送数据，性能影响可以忽略。每 30 分钟发送一次，每次只需几毫秒。

<a id="can-i-view-what-data-my-server-sends"></a>

### 可以查看服务器发送了哪些数据吗？

可以。bStats 的全部数据都是公开的。访问任意插件的 bStats 页面，就能查看收集了哪些指标，以及汇总所有服务器数据的图表。

也可以在 bStats 配置文件中开启调试日志，查看服务器发送的原始数据。

<a id="is-bstats-gdpr-compliant"></a>

### bStats 符合 GDPR 吗？

符合。bStats 不收集可识别个人身份的信息。IP 地址只用于限流，绝不会关联到统计数据。所有数据均为匿名汇总。

<a id="who-can-see-my-servers-data"></a>

### 谁能看到我的服务器数据？

没有人能从中识别你的特定服务器。所有数据都会汇总，以展示整体趋势的图表呈现。

<a id="why-do-i-see-a-bstats-folder-in-my-plugins-directory"></a>

### 为什么 plugins 目录中出现 bStats 文件夹？

`/plugins/bStats/` 文件夹中保存了所有插件共用的配置文件，因此可以统一开启或关闭统计，而无需逐个插件配置。

<a id="learn-more"></a>

## 了解更多

如果对 bStats 有疑问或顾虑，可以通过以下入口寻求帮助：

[查看文档](getting-started.md) · [隐私政策](privacy-policy.md) · [加入 Discord](https://discord.gg/qTXtXuf)
