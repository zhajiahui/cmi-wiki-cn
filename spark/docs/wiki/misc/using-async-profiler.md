---
title: "使用 async-profiler 引擎"
source_url: "https://spark.lucko.me/docs/misc/Using-async-profiler"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "spark-docs 07dc48b059e25731294c9ca6f713c358dfabb8fc（2026-10-19 快照）"
---

<a id="using-async-profiler-engine"></a>

# 使用 async-profiler 引擎

spark 有两种性能采样引擎：

- Java（基于 WarmRoast）
- async-profiler

async-profiler 引擎不受安全点采样偏差问题影响，因此比 Java/WarmRoast 引擎更准确。如果系统支持，spark 会自动使用它。

<a id="system-requirements"></a>

## 系统要求

async-profiler 引擎模式支持使用 **Linux** 或 **macOS** 操作系统、采用 **x86_64**（amd64）或 **aarch64**（arm64）架构的系统。

大多数独立服务器、VPS 和共享托管服务器都符合其中一种情况。

<a id="containers"></a>

## 容器

如果服务器运行在容器中，例如使用 Pterodactyl 面板，可能需要调整一些设置，才能让 async-profiler 引擎正常工作。

先直接尝试使用。如果遇到错误，再尝试下面的步骤。

<a id="install-libstdc"></a>

### 安装 libstdc++

async-profiler 依赖 libstdc++。如果镜像中尚未包含它，可能需要手动安装。

出现以下错误时，就表示存在这个问题：

> java.lang.UnsatisfiedLinkError: /tmp/spark-xxxx-libasyncProfiler.so.tmp: Error loading shared library libstdc++.so.6: No such file or directory (needed by /tmp/spark-xxxx-libasyncProfiler.so.tmp)

在 Alpine 上安装 libstdc++：

```bash
apk add libstdc++
```

在 Debian/Ubuntu 上安装 libstdc++：

```bash
apt install libstdc++6
```

如果使用基于 Alpine 的 Java Docker 镜像，在 Dockerfile 中加入：

```docker
RUN apk add --no-cache libstdc++
```

如果使用基于 Debian 的 Java Docker 镜像，在 Dockerfile 中加入：

```docker
RUN apt-get install libstdc++6
```

<a id="allow-access-to-kernel-perf-events"></a>

### 允许访问内核 perf-events

如果无法访问 perf-events，async-profiler 会自动改用 “itimer” 模式采样。大多数 Docker 运行环境默认限制了这些事件的访问，因此通常会遇到这种情况。

对于绝大多数用户，这完全够用。不过，如果需要记录原生代码的性能信息，就必须在启动容器时设置以下参数，让 async-profiler 获得访问权限。

```bash
docker run --cap-add SYS_ADMIN ...
```

<a id="install-hotspot-debug-symbols"></a>

### 安装 Hotspot 调试符号

内存分配采样模式需要安装 Hotspot 调试符号。在较新的 JVM（Java 11+）上，通常默认就有。

如果没有，可以使用操作系统的包管理器安装以下软件包：

- `openjdk-8-dbg`，或
- `openjdk-11-dbg`

例如，在 Debian/Ubuntu 上：

```bash
apt install openjdk-11-dbg
```

其他发行版的安装说明见[此处](https://github.com/jvm-profiling-tools/async-profiler#installing-debug-symbols)。
