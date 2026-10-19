---
title: "spark 与其他工具的比较"
source_url: "https://spark.lucko.me/docs/misc/spark-vs-others"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "spark-docs 07dc48b059e25731294c9ca6f713c358dfabb8fc（2026-10-19 快照）"
---

<a id="spark-vs-others"></a>

# spark 与其他工具的比较

<a id="sparks-cpu-profiler-vs-others"></a>

## spark 的 CPU 性能采样器与其他工具

### WarmRoast

spark 的 CPU 性能采样器基于 WarmRoast，但经过持续改进，与上游版本有以下区别：

- 安装和使用明显更简单。
    - 无需访问服务器所在的底层机器。
    - 无需开放或访问临时 Web 服务器，例如开放端口、关闭防火墙、进入临时网页。
- 可以快速查看性能报告并分享给他人。
- 无需额外设置即可应用反混淆映射；除 MCP（Searge）名称外，还支持 CraftBukkit 和 Fabric 来源。
- 采样器和查看器都做了大量优化。
    - 可以用更高的频率采样，同时减少内存占用。
- 增加了更多自定义选项。
    - 可以只保留“卡顿游戏刻”的输出，将同一线程池中的线程合并分组等。
    - 可以将输出筛选为调用树中包含特定方法或类的部分。
- 提高了采样准确度。
    - 按不同的方法分组，而不是仅按方法名分组。

### Minecraft Timings

Aikar 的 [timings](https://github.com/aikar/timings) 系统内置于 Spigot 和 Sponge。它与 spark 类似，都会记录服务器性能数据并提供分析结果。

Timings 可以做到、而 spark 做不到的事情：

- 统计记录期间某些事情发生的次数，例如事件、实体更新等。
- 以更容易理解的方式显示结果，方便不熟悉性能采样数据的服主管理员阅读。
- 用更易读的工作描述细分服务器活动。

如果这些功能对你很重要，timings 可能更合适。

如果不太需要这些功能，spark 则有以下优势：

- 无需手动定义每个分析区域，spark 会记录所有部分的数据。
    - 例如，timings 可能发现插件 x 的某个监听器在处理 PlayerMoveEvent 时占用了大量 CPU 时间，却无法指出处理过程的哪一部分较慢；spark 可以。
- 对于想优化插件或服务端软件的程序员，以及希望报告问题的服主管理员，spark 的输出通常更有用。
    - Timings 的细节不足以指出代码中较慢的部分。

<a id="other-java-profilers"></a>

### 其他 Java 性能分析器

- 与其他分析方式，例如插桩相比，spark 这类采样式分析器在数值上通常没有那么精确，但可以让目标程序接近全速运行。
    - 实际上，采样式分析器往往能比其他方式更准确地反映目标程序的执行情况，因为它对程序的干扰较少，副作用也较少。
- 使用 spark 时，无需在启动服务器时注入 Java agent。
- 可以方便地应用反混淆映射。
- spark 足以应对 Minecraft 服务器上绝大多数性能问题，但提前分析某段代码的性能，也就是在它成为瓶颈或问题之前进行分析时，可能有所不足。
