---
title: "spark"
source_kind: plugin-overview
translation_review: reviewed
---

# spark

spark 是 Minecraft 客户端、服务器和代理端的性能分析工具，可用于性能采样、内存检查及运行状况监视。

这批资料以 **spark 配置目录**随包提供，清单未列出独立 spark JAR，**版本未标明**。现有资料也未说明其具体部署来源。其他随包插件的 `depend` 和 `softdepend` 中均未出现 spark。

## 官方文档中的常用命令

以下命令依据官方现行文档整理：

| 命令 | 用途 | 权限 |
| --- | --- | --- |
| `/spark profiler start`、`/spark profiler stop` | 启动、停止性能采样 | `spark` 或 `spark.profiler` |
| `/spark tps` | 查看服务器 TPS 和 CPU 使用情况 | `spark` 或 `spark.tps` |
| `/spark health` | 生成运行状况报告，并在查看器中打开 | `spark` 或 `spark.health` |

运行参数见[配置说明](configuration/index.md)。

## 官方资料

- [spark 官方简介](https://spark.lucko.me/)
- [官方命令文档](https://spark.lucko.me/docs/Command-Usage)
- [官方配置文档](https://spark.lucko.me/docs/Configuration)
