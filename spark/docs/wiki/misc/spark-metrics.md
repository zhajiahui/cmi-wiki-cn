---
title: "关于 spark 指标"
source_url: "https://spark.lucko.me/docs/misc/About-spark-metrics"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "spark-docs 07dc48b059e25731294c9ca6f713c358dfabb8fc（2026-10-19 快照）"
---

<a id="about-spark-metrics"></a>

# 关于 spark 指标

spark 可以报告并计算多种指标。

所有指标的原始数据都来自其他来源。如果某项数值看起来有误，很可能是 spark 接收到的原始数据不正确。

| 指标名称         | 数据来源                                             |
| --------------------|---------------------------------------------------------|
| TPS                 | 服务端事件（通过 spark 的 `TickHook` 接口）         |
| MSPT                | 服务端事件（通过 spark 的 `TickReporter` 接口）     |
| CPU 使用率           | Java API ([jdk.management/OperatingSystemMXBean](https://docs.oracle.com/en/java/javase/17/docs/api/jdk.management/com/sun/management/OperatingSystemMXBean.html)) |
| 内存使用量        | Java API ([jdk.management/OperatingSystemMXBean](https://docs.oracle.com/en/java/javase/17/docs/api/jdk.management/com/sun/management/OperatingSystemMXBean.html)) & `/proc/meminfo` (仅限 Linux) |
| 磁盘使用量          | Java API ([java.base/FileStore](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/file/FileStore.html)) |
| GC                  | Java API ([jdk.management/GarbageCollectorMXBean](https://docs.oracle.com/en/java/javase/17/docs/api/jdk.management/com/sun/management/GarbageCollectorMXBean.html)) |
| 网络使用量       | `/proc/net/dev` (仅限 Linux)                            |
| 玩家延迟         | 服务端 API（通过 spark 的 `PlayerPingProvider` 接口） |
| CPU 名称            | `/proc/cpuinfo` （Linux）, `wmic cpu` （Windows）         |
| 操作系统名称与版本 | `/etc/os-release` （Linux）, `wmic os` （Windows）        |

<a id="containers-and-docker"></a>

### 容器与 Docker
当服务器及其中的 spark 运行在容器内，例如 Pterodactyl 环境时，有时会出现指标报告错误，主要涉及 CPU 或内存使用情况。 

spark 对此能做的有限。如上所示，spark 只是使用标准 Java 和操作系统 API 获取原始指标数据。如果数据不准确，原因可能是你的环境设置，也可能是 Java、Docker 或操作系统的错误。
