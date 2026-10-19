---
title: "spark 功能与在线查看器"
source_url: "https://spark.lucko.me/"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "spark-docs 07dc48b059e25731294c9ca6f713c358dfabb8fc（2026-10-19 快照）"
---

# spark 功能与在线查看器

<a id="about"></a>

## 关于

spark 是一款性能分析工具，由三个主要部分组成。

<a id="profiler"></a>

### 性能采样器

spark 内置的性能采样器可以帮助诊断性能问题和瓶颈。

<a id="memory-inspection"></a>

### 内存检查

spark 可以生成完整堆转储，汇总哪些内容占用的内存最多，并监控 GC 活动。

<a id="health-reporting"></a>

### 运行状况报告

spark 监控并报告多项关键指标，可用于持续跟踪性能变化。

更多信息见 [GitHub](https://github.com/lucko/spark)，也欢迎来 [Discord](https://discord.gg/PAGT2fu) 交流。

<a id="viewer"></a>

## 查看器

此网站同时也是 spark 数据的在线查看器。

使用方法：

1. 使用相应的 spark 命令生成[性能报告](commands.md#spark-profiler)或[堆摘要](commands.md#spark-heapsummary)。
2. 数据上传后，点击链接打开查看器。

也可以生成或导出 `.sparkprofile` 或 `.sparkheap` 文件，然后将文件拖入下方区域打开。

将性能报告或堆文件拖放到这里，或点击选择文件。

*（仅接受 `.sparkprofile` 或 `.sparkheap` 文件）*

此网站和查看器使用 JavaScript 与 React 框架编写，源码已在 GitHub 开放，欢迎提交拉取请求。
