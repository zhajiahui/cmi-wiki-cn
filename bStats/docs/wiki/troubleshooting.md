---
title: "排错指南"
source_url: "https://bstats.org/docs/troubleshooting"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "官方服务文档 2026-10-19 快照"
---

<a id="troubleshooting"></a>

# 排错指南

这里列出接入 bStats 时的常见问题和解决方法。阅读后仍有问题，可以在 [Discord](https://discord.gg/qTXtXuf) 求助，或在 GitHub 提交 Issue。

<a id="how-long-until-data-appears"></a>

## 数据多久会显示？

数据在 bStats 上可见的时间取决于以下过程：

<a id="initial-delay"></a>

### 首次延迟

服务器启动后，会随机延迟 **3-6 分钟**再首次发送数据。

<a id="publication-schedule"></a>

### 发布时间

bStats 网站在 **hh:00 和 hh:30** 发布更新，即每半小时一次。数据发出后，可能还需**最多 30 分钟**才会在插件仪表盘显示。

<a id="total-time"></a>

### 总计时间

因此，服务器启动后，预计需要等待 **3-36 分钟**，仪表盘才会出现第一个数据点。

<a id="data-not-showing-up"></a>

## 数据没有显示

如果已经等待了上述时间，仍然没有数据，请检查以下常见问题：

<a id="enable-debug-logging"></a>

### 开启调试日志

在 bStats 配置文件中，将 `logFailedRequests`、`logSentData` 和 `logResponseStatusText` 设为 `true`，开启调试日志。

<a id="ratelimits"></a>

### 限流

每个插件在每个 30 分钟区间内（hh:00 和 hh:30）只能发送一次数据。如果开启调试日志后看到 `429 Too Many Requests`，表示插件正在被限流。**这完全正常**，可以忽略。

<a id="metrics-class-not-instantiated"></a>

### 没有实例化 Metrics 类

检查插件初始化代码中是否确实创建了 `Metrics` 实例。仅包含类文件还不够，必须使用你的插件 ID 实例化它。

<a id="wrong-plugin-id"></a>

### 插件 ID 错误

仔细核对代码中的插件 ID，确认与插件仪表盘显示的 ID 相同。

<a id="metrics-disabled-in-config"></a>

### 配置中关闭了统计

服主可以通过编辑配置关闭 bStats。请检查 `enabled` 是否设为 `true`。

<a id="firewall-or-network-blocking"></a>

### 防火墙或网络拦截

确认服务器能连接 bStats 服务器。常见原因是 PiHole 或其他广告拦截软件阻止了连接。

<a id="still-having-issues"></a>

## 仍然有问题？

如果已检查上述各项，仍然看不到数据，请寻求帮助：

[加入 Discord](https://discord.gg/qTXtXuf) · [提交 GitHub Issue](https://github.com/Bastian/bStats/issues)
