---
title: "命令用法"
source_url: "https://spark.lucko.me/docs/Command-Usage"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "spark-docs 07dc48b059e25731294c9ca6f713c358dfabb8fc（2026-10-19 快照）"
---

<a id="command-usage"></a>

# 命令用法

!!! note "注意"

    在 BungeeCord、Velocity 和 Forge/Fabric 客户端上，必须分别用 `/sparkb`、`/sparkv` 和 `/sparkc` 代替 `/spark`。

<a id="profiler"></a>

## 性能采样

### `/spark profiler`

`profiler` 子命令用于控制 spark 性能采样器。

需要权限 `spark` 或 `spark.profiler`.

如果性能采样器已在后台运行：
* `/spark profiler open`：**打开**性能报告查看器页面，保持采样继续运行。
* `/spark profiler stop`：**停止**采样并查看结果。
* `/spark profiler cancel`：**取消**采样，停止运行且不上传结果。

基本操作：
* `/spark profiler start`：以默认模式**启动**性能采样。
* `/spark profiler stop`：**停止**采样并查看结果。
* `/spark profiler info`：检查采样器当前的**状态**。

还可以用以下参数调整采样器的行为：
* `/spark profiler start --timeout <seconds>`：开始采样，并在 x 秒后**自动停止**。
* `/spark profiler start --thread *`：开始采样，跟踪**所有线程**。
* `/spark profiler start --alloc`：开始采样，分析内存分配（内存压力），而非 CPU 使用情况。

<details markdown="1">
<summary>高级用法参数</summary>


<a id="execution-profiler"></a>

#### 执行性能采样

* `/spark profiler start --interval <milliseconds>`：以指定间隔开始采样，默认间隔为 4
* `/spark profiler start --thread *`：开始采样并跟踪所有线程。
* `/spark profiler start --thread <thread name>`：开始采样，仅跟踪指定线程。
* `/spark profiler start --thread <thread name pattern> --regex`：开始采样，仅跟踪符合给定正则表达式的线程。
* `/spark profiler start --only-ticks-over <milliseconds>`：开始采样，仅记录耗时超过指定时长的游戏刻。
* `/spark profiler start --combine-all`：开始采样，把所有线程合并到同一个根节点下。
* `/spark profiler start --not-combined`：开始采样，禁用对同一线程池内线程的合并分组。
* `/spark profiler start --ignore-sleeping`：开始采样，仅记录未处于“休眠”状态的线程。
* `/spark profiler start --force-java-sampler`：开始采样，强制使用 Java 采样器，替代异步采样器。
* `/spark profiler stop --comment <comment>`：停止采样，并在查看器中附上指定备注。
* `/spark profiler stop --save-to-file`：将性能报告保存为配置目录下的文件，而非上传。

<a id="allocation-profiler"></a>

#### 内存分配采样

* `/spark profiler start --alloc --alloc-live-only`：开始内存分配采样，仅保留采样结束时尚未被垃圾回收的对象的统计信息
* `/spark profiler start --alloc --interval <bytes>`：开始内存分配采样，按指定字节数间隔采样，默认值为 `524287`，即 *512 KB*


</details>



<a id="health"></a>

## 运行状况

### `/spark health`
`health` 子命令生成服务器运行状况报告，包括 TPS、CPU、内存和磁盘使用情况。

需要权限 `spark` 或 `spark.health`.

要生成运行状况报告并在查看器中打开：
* `/spark health`：以“实时仪表盘”模式打开报告，数据每 10 秒自动更新。
* `/spark health upload`：上传静态运行状况报告，数据不会自动更新。

要生成报告并输出到控制台：
* `/spark health show`：显示基本报告。
* `/spark health show --memory`：额外显示 JVM 内存使用信息。
* `/spark health show --network`：额外显示系统网络使用信息。

___
### `/spark ping`
`ping` 子命令输出玩家的平均延迟往返时间，或指定玩家的延迟往返时间。

可以使用：
* `/spark ping`：查看所有玩家的平均延迟。
* `/spark ping --player <username>`：查看指定玩家当前的延迟 RTT。

需要权限 `spark` 或 `spark.ping`.

___
### `/spark tps`
`tps` 子命令输出服务器的 TPS（每秒游戏刻数）和 CPU 使用情况。

需要权限 `spark` 或 `spark.tps`.

___
### `/spark tickmonitor`
`tickmonitor` 子命令控制游戏刻监控系统。

需要权限 `spark` 或 `spark.tickmonitor`.

不带额外参数执行此命令，即可切换系统的开启或关闭状态。

可以使用：
* `/spark tickmonitor --threshold <percent>`：启动游戏刻监控器，仅报告相对平均游戏刻耗时的增幅超过指定百分比的游戏刻。
* `/spark tickmonitor --threshold-tick <milliseconds>`：启动游戏刻监控器，仅报告耗时超过指定毫秒数的游戏刻。
* `/spark tickmonitor --without-gc`：启动游戏刻监控器，并关闭 GC 活动报告。



<a id="memory"></a>

## 内存

### `/spark gc`
`gc` 子命令输出服务器的 GC（垃圾回收）历史记录。

需要权限 `spark` 或 `spark.gc`.

___
### `/spark gcmonitor`
`gcmonitor` 子命令控制 GC（垃圾回收）监控系统。

需要权限 `spark` 或 `spark.gcmonitor`.

直接执行此命令，即可切换系统的开启或关闭状态。

___
### `/spark heapsummary`
`heapsummary` 子命令生成新的内存（堆）转储摘要，并上传到查看器。

需要权限 `spark` 或 `spark.heapsummary`.

可以使用：
* `/spark heapsummary --run-gc-before`：建议 JVM 在生成堆摘要前运行垃圾回收器。*（已弃用）*

___
### `/spark heapdump`
`heapdump` 子命令生成新的堆转储文件（.hprof 快照），并保存到磁盘。

需要权限 `spark` 或 `spark.heapdump`.

可以使用：
* `/spark heapdump --compress <type>`：按指定格式压缩堆转储文件。支持 gzip、xz 和 lzma。
* `/spark heapdump --include-non-live`：包含“非存活”对象，即已无法访问、可以被垃圾回收的对象。*（已弃用）*
* `/spark heapdump --run-gc-before`：建议 JVM 在生成堆转储前运行垃圾回收器。*（已弃用）*



<a id="misc"></a>

## 其他

### `/spark activity`
`activity` 子命令输出 spark 最近执行的活动。

需要权限 `spark` 或 `spark.activity`.

可以使用：
* `/spark activity --page <page no>`：查看指定页。
