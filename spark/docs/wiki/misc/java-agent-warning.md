---
title: "Java agent 警告"
source_url: "https://spark.lucko.me/docs/misc/Java-agent-warning"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "spark-docs 07dc48b059e25731294c9ca6f713c358dfabb8fc（2026-10-19 快照）"
---

<a id="java-agent-warning"></a>

# Java agent 警告

从 Java 21 开始，使用 spark 时可能会在控制台或日志中看到以下警告：

> WARNING: A Java agent has been loaded dynamically (/tmp/byteBuddyAgentxxxxxxxxxxxxxxxxxxx.jar)   
> WARNING: If a serviceability tool is in use, please run with -XX:+EnableDynamicAgentLoading to hide this warning   
> WARNING: If a serviceability tool is not in use, please run with -Djdk.instrument.traceUsage for more information   
> WARNING: Dynamic loading of agents will be disallowed by default in a future release   

<a id="why-does-spark-use-a-java-agent"></a>

### spark 为什么使用 Java agent？

spark 使用 Java Instrumentation API 查找 JVM 中已加载 Java 类的元数据，见 [`ClassFinder.java`](https://github.com/lucko/spark/blob/master/spark-common/src/main/java/me/lucko/spark/common/util/ClassFinder.java)。

为了访问 Instrumentation API，spark 使用 [byte-buddy-agent](https://github.com/raphw/byte-buddy) 库。这个库会动态加载 Java Agent，从而获得 Instrumentation API 的访问能力。

<a id="i-am-using-java-21-what-should-i-do"></a>

### 使用 Java 21 时该怎么做？

如果 instrumentation agent 不可用或加载失败，spark 会自动改用另一种方式查找类，只是效率略低。

因此，建议 Java 21 用户忽略该错误，或按照下面的说明明确启用动态 agent 加载。

<a id="i-am-using-java-22-what-should-i-do"></a>

### 使用 Java 22 时该怎么做？

有两种选择：

<a id="1-re-enable-dynamic-agent-loading"></a>

#### 1. 重新启用动态 agent 加载

这会恢复 JVM 之前的行为，让 spark 正常工作。

在 Java 启动参数中加入：

```
-XX:+EnableDynamicAgentLoading
```

<a id="2-do-nothing"></a>

#### 2. 不做处理

如上所述，即使 agent 安装失败，spark 仍然可以工作。
