---
title: "配置"
source_url: "https://spark.lucko.me/docs/Configuration"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "spark-docs 07dc48b059e25731294c9ca6f713c358dfabb8fc（2026-10-19 快照）"
---

<a id="configuration"></a>

# 配置

spark 的配置选项不多，用途也比较特定，大多数用户无需修改默认值。

要覆盖默认配置值，可以使用以下任一种方式：

* 在 spark 插件或模组文件夹中创建配置**文件** `config.json`（配置文件不会自动生成）
* 设置**环境变量**
* 设置 Java **系统属性**


<a id="options"></a>

## 配置选项

以下列出了可用的配置项。

---

### `backgroundProfiler`
是否启用后台性能采样。

设为 true 时，spark 会在服务端、客户端或代理端启动时自动开始后台采样。可以用常规命令上传性能报告。默认值为 `true`。

<a id="example-config-file"></a>

#### 示例（配置文件）
```json
{
    "backgroundProfiler": true
}
```

<a id="example-environment-variable"></a>

#### 示例（环境变量）
```shell
export SPARK_BACKGROUNDPROFILER=true
```

<a id="example-system-property"></a>

#### 示例（系统属性）
```shell
java -Dspark.backgroundProfiler=true
```
---

### `backgroundProfilerInterval`
后台性能采样器的采样间隔。默认值为 `10`（毫秒）。

<a id="example-config-file-1"></a>

#### 示例（配置文件）
```json
{
    "backgroundProfilerInterval": 10
}
```

<a id="example-environment-variable-1"></a>

#### 示例（环境变量）
```shell
export SPARK_BACKGROUNDPROFILERINTERVAL=10
```

<a id="example-system-property-1"></a>

#### 示例（系统属性）
```shell
java -Dspark.backgroundProfilerInterval=10
```
---

### `backgroundProfilerEngine`
后台性能采样器使用的引擎。

默认值为 `"async"`，也支持 `"java"`。

<a id="example-config-file-2"></a>

#### 示例（配置文件）
```json
{
    "backgroundProfilerEngine": "async"
}
```

<a id="example-environment-variable-2"></a>

#### 示例（环境变量）
```shell
export SPARK_BACKGROUNDPROFILERENGINE=async
```

<a id="example-system-property-2"></a>

#### 示例（系统属性）
```shell
java -Dspark.backgroundProfilerEngine=async
```
---

### `viewerUrl`
命令输出中提供查看器链接时使用的 URL。

数据的“代码”会追加在 URL 后，因此 URL 必须以 `/` 结尾。

默认值为 [`"https://spark.lucko.me/"`](project-home.md)。

<a id="example-config-file-3"></a>

#### 示例（配置文件）
```json
{
    "viewerUrl": "https://spark.lucko.me/"
}
```

<a id="example-environment-variable-3"></a>

#### 示例（环境变量）
```shell
export SPARK_VIEWERURL=https://spark.lucko.me/
```

<a id="example-system-property-3"></a>

#### 示例（系统属性）
```shell
java -Dspark.viewerUrl=https://spark.lucko.me/
```
---

### `bytebinUrl`
接收性能报告和堆转储摘要上传的 bytebin 实例 URL。URL 应以 `/` 结尾。

默认值为 `"https://spark-usercontent.lucko.me/"`。

<a id="example-config-file-4"></a>

#### 示例（配置文件）
```json
{
    "bytebinUrl": "https://spark-usercontent.lucko.me/"
}
```

<a id="example-environment-variable-4"></a>

#### 示例（环境变量）
```shell
export SPARK_BYTEBINURL=https://spark-usercontent.lucko.me/
```

<a id="example-system-property-4"></a>

#### 示例（系统属性）
```shell
java -Dspark.bytebinUrl=https://spark-usercontent.lucko.me/
```
---

### `bytesocksHost`
用于与 spark 查看器通信的 bytesocks 实例主机名。

默认值为 `"spark-usersockets.lucko.me"`。

<a id="example-config-file-5"></a>

#### 示例（配置文件）
```json
{
    "bytesocksHost": "spark-usersockets.lucko.me"
}
```

<a id="example-environment-variable-5"></a>

#### 示例（环境变量）
```shell
export SPARK_BYTESOCKSHOST=spark-usersockets.lucko.me
```

<a id="example-system-property-5"></a>

#### 示例（系统属性）
```shell
java -Dspark.bytesocksHost=spark-usersockets.lucko.me
```
---

### `overrideTpsCommand`
是否用 spark 的 TPS 命令替换默认 TPS 命令。只有在 Bukkit 服务器上运行 spark 时才会读取此项。

默认值为 `true`。

<a id="example-config-file-6"></a>

#### 示例（配置文件）
```json
{
    "overrideTpsCommand": true
}
```

<a id="example-environment-variable-6"></a>

#### 示例（环境变量）
```shell
export SPARK_OVERRIDETPSCOMMAND=true
```

<a id="example-system-property-6"></a>

#### 示例（系统属性）
```shell
java -Dspark.overrideTpsCommand=true
```
---

### `disableResponseBroadcast`
是否禁止 spark 向所有在线管理员（具有使用 spark 所需权限的玩家）广播命令输出。

默认值为 `false`。

<a id="example-config-file-7"></a>

#### 示例（配置文件）
```json
{
    "disableResponseBroadcast": false
}
```

<a id="example-environment-variable-7"></a>

#### 示例（环境变量）
```shell
export SPARK_DISABLERESPONSEBROADCAST=false
```

<a id="example-system-property-7"></a>

#### 示例（系统属性）
```shell
java -Dspark.disableResponseBroadcast=false
```
---

### `maxStackDepth`
采样器记录的最大栈帧深度。超过此深度的栈帧会被丢弃或忽略。

设为适中的数值，可以避免记录不必要的过量数据，并防止后续处理通过递归方法调用读取数据时发生栈溢出。

默认值为 `300`。

!!! note "注意"

    此项只能通过系统属性配置。

<a id="example-system-property-8"></a>

#### 示例（系统属性）
```shell
java -Dspark.maxStackDepth=300
```
---

### `continuousProfilingHistorySize`
持续采样时，在丢弃数据前保留的窗口数量。每个窗口约为 1 分钟。

默认值为 `60`。

spark 官方查看器不接受超过 10MB 的上传。将此值设为大于 60，更容易超过限制。如果遇到 HTTP 413 错误，可以尝试调低此值。

!!! note "注意"

    此项只能通过系统属性配置。

<a id="example-system-property-9"></a>

#### 示例（系统属性）
```shell
java -Dspark.continuousProfilingHistorySize=60
```
---

### `useOsTmpDir`
是否使用操作系统自带的临时目录存放 spark 临时文件。

默认值为 `false`。

| `useOsTmpDir` 设置 | 操作系统 | 可能的路径 |
|-----------------------|---------|-------------------------------------------|
| `true`                | Windows | `C:\Users\<username>\AppData\Local\Temp\` |
| `true`                | macOS   | `/var/folders/.../T/`                     |
| `true`                | Linux   | `/tmp/`                                   |
| `false`               | n/a     | `plugins/spark/tmp`（或类似路径）          |

!!! note "注意"

    此项只能通过系统属性配置。

<a id="example-system-property-10"></a>

#### 示例（系统属性）
```shell
java -Dspark.useOsTmpDir=true
```
---
