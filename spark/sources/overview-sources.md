---
title: "spark 官方资料摘录"
source_kind: plugin-overview
translation_review: reviewed
---

# spark 官方资料摘录

核对日期：2026-10-19。随包仅列有 spark 配置目录，没有独立 spark JAR 的版本记录，组件版本未标明。

## 性能分析工具

来源：[spark 官网](https://spark.lucko.me/)。

> A performance profiler for Minecraft clients, servers, and proxies.

> spark is a performance profiler, made up of three main components.

官网列出的三个部分为 Profiler、Memory Inspection 和 Health Reporting，对应性能采样、内存检查和运行状况报告。

## 命令与权限

来源：[官方 Command Usage](https://spark.lucko.me/docs/Command-Usage)。

> Requires the permission spark or spark.profiler.

> The tps subcommand prints information about the servers TPS (ticks per second) rate and CPU usage.

> Requires the permission spark or spark.tps.

> The health subcommand generates a health report for the server, including TPS, CPU, Memory and Disk Usage.

> Requires the permission spark or spark.health.

命令页列有 `/spark profiler start`、`/spark profiler stop`、`/spark tps` 和 `/spark health`。

## 配置入口与随包形态

来源：[官方 Configuration](https://spark.lucko.me/docs/Configuration)。官方文档支持通过 `config.json`、环境变量和 Java 系统属性覆盖默认配置。

随包清单列有 spark 配置目录，但未列出独立 spark JAR。随包插件的 `depend` 和 `softdepend` 中均未出现 spark；没有据此推断其来自哪个平台、是否由其他组件集成，或指定版本号。
