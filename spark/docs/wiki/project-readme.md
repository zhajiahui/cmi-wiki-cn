---
title: spark 项目说明
source_url: https://github.com/lucko/spark/blob/master/README.md
source_kind: official-wiki
translation_review: reviewed
source_version: spark 项目仓库 master，2026-10-19 官方原文快照
---


<a id="spark"></a>

# spark 项目说明

![spark](assets/f30db15ccea3-banner.png)

<a id="spark-is-a-performance-profiler-for-minecraft-clients-servers-and-proxies"></a>

### spark 是面向 Minecraft 客户端、服务端和代理端的性能分析工具。

<a id="useful-links"></a>

#### 实用链接

- [**网站**](project-home.md)：浏览项目主页。
- [**文档**](home.md)：阅读文档与使用指南。
- [**下载**](https://spark.lucko.me/download)：下载最新插件或模组。

<a id="what-does-spark-do"></a>

## spark 能做什么？

spark 由三个独立部分组成：

- **CPU 性能采样器**：诊断性能问题。
- **内存检查**：诊断内存问题。
- **服务器运行状况报告**：跟踪整体运行状况。

<a id="zap-cpu-profiler"></a>

### :zap: CPU 性能采样器

spark 的性能采样器可以诊断卡顿、游戏刻速率偏低、CPU 使用率偏高等性能问题。

它具有以下特点：

- **轻量**：可以在正式运行环境中使用，影响很小。
- **易用**：无需配置或额外设置，安装插件或模组即可。
- **快速生成结果**：只运行约 ~30 秒，通常就足以了解可能存在性能问题的部分。
- **可自定义**：可以指定线程、采样间隔，或只记录卡顿时段等。
- **易读**：简单的树状结构便于分析与理解，查看器也能应用反混淆映射。

它通过对系统活动进行统计采样，再据此构建调用图。调用图会显示在在线查看器中，供用户进一步分析。

有两种性能采样引擎：

- Native/Async：使用 [async-profiler](https://github.com/async-profiler/async-profiler) 库，*仅适用于 Linux 和 macOS 系统*。
- Java：使用 `ThreadMXBean`，是 sk89q 的 [WarmRoast 性能采样器](https://github.com/sk89q/WarmRoast)的改进版本。

<a id="zap-memory-inspection"></a>

### :zap: 内存检查

spark 包含多种用于诊断服务器内存问题的工具。

- **堆摘要**：获取并分析服务器内存的基本快照。
    - 简单查看 JVM 堆，了解每个类的内存占用和实例数量。
    - 无意完全取代专门的内存分析工具，见下一项。
- **堆转储**：获取服务器内存的完整 HPROF 快照。
    - 转储 JVM 堆的完整快照，并可选择压缩。
    - 随后可使用常规分析工具检查此快照。
- **GC 监控**：监控服务器的垃圾回收活动。
    - 将 GC 活动与服务器卡死对应起来，方便查看每次回收的耗时和释放的内存。
    - 观察新生代、老年代垃圾回收的频率与耗时，帮助确定使用哪些 GC 调优参数。

<a id="zap-server-health-reporting"></a>

### :zap: 服务器运行状况报告

spark 可以报告多项指标，概括服务器的整体运行状况。

包括：

- **TPS**：每秒游戏刻数，比 /tps 命令的指示更精确。
- **游戏刻耗时**：每个游戏刻耗时，包括最小、最大和平均值。
- **CPU 使用率**：进程和整个系统分别占用多少 CPU。
- **内存使用量**：进程占用了多少内存。
- **磁盘使用量**：系统磁盘的剩余和已用空间。

除了平均游戏刻速率，spark 还可以**监控单个游戏刻**：当某个游戏刻的耗时超过指定阈值时，发送报告。这样可以结合其他系统或游戏事件，判断性能问题的趋势与性质。

spark、WarmRoast、Minecraft Timings 及其他性能分析器的比较，见文档中的[此页](misc/spark-vs-others.md)。

<a id="license"></a>

## 许可证

spark 免费且开源，采用 GNU GPLv3 许可证。更多信息见 [`LICENSE.txt`](https://github.com/lucko/spark/blob/master/LICENSE.txt)。

spark API 子模块使用更宽松的 MIT 许可证，详见 [`spark-api/LICENSE.txt`](https://github.com/lucko/spark/blob/master/spark-api/LICENSE.txt)。

spark 是 [WarmRoast](https://github.com/sk89q/WarmRoast) 的分支，后者[也采用 GPLv3 许可证](https://github.com/sk89q/WarmRoast/blob/3fe5e5517b1c529d95cf9f43fd8420c66db0092a/src/main/java/com/sk89q/warmroast/WarmRoast.java#L1-L17)。
