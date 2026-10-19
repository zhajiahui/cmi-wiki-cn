---
title: 备份快照
source_url: https://worldedit.enginehub.org/en/latest/usage/snapshots/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 备份快照 { #snapshots }

WorldEdit 可以从备份中加载并恢复世界的一部分，范围由[选区](regions/selections.md)决定，无需关闭服务器或使用离线地图编辑器。通过这种方式可以处理许多问题，例如撤销恶意破坏、修复世界存档错误，甚至回退做到一半后放弃的工程。

<a id="contents"></a>

- [配置备份快照](#configuring-snapshots)



  - [支持的归档格式](#supported-archive-formats)

- [使用备份快照](#using-snapshots)

## 配置备份快照 { #configuring-snapshots }

要让 WorldEdit 读取备份，必须选择一个目录来存放备份。路径可以在[配置](../config.md)中设置，相对于服务器或 `.minecraft` 根文件夹（不是 WorldEdit 文件夹！）。如果备份存放在服务器文件夹以外，也可以使用绝对路径（例如另一块磁盘，建议这样做，以防硬件故障）。

设置后，将世界文件夹的副本或其 ZIP 压缩包放入备份文件夹即可。下面给出一种备份文件夹布局示例。

示例：备份存储的可用结构

**![f](../assets/ac4862224dfa-folder.png) `backups/`（配置中的文件夹名称）**

**![f](../assets/ac4862224dfa-folder.png) `world/`（世界名称）**

**![z](../assets/19f16f6bd87c-zip.png) `2019-06-15-03-00-00.zip`（只包含此世界的备份）**

**![f](../assets/ac4862224dfa-folder.png) `world/`（必须与上面的世界名称一致）**

![f](../assets/ac4862224dfa-folder.png) `region/`（包含此世界的 `.mca` 文件）

**![f](../assets/ac4862224dfa-folder.png) `2019-05-15-03-00-00`（备份不必压缩成 ZIP）**

![f](../assets/ac4862224dfa-folder.png) `world/`

**![f](../assets/ac4862224dfa-folder.png) `world_nether/`（另一个世界名称）**

![z](../assets/19f16f6bd87c-zip.png) `2019-06-15-03-00-00.zip`

**![z](../assets/19f16f6bd87c-zip.png) `2019-06-01-03-00-00.zip`（一个包含多个世界的备份）**

**![f](../assets/ac4862224dfa-folder.png) `world/`**

![f](../assets/ac4862224dfa-folder.png) `region/`（所有 `.mca` 文件都在这里）

![f](../assets/ac4862224dfa-folder.png) `world_nether/`

![z](../assets/19f16f6bd87c-zip.png) `2019-05-01-03-00-00.zip`（一个月前的另一份备份）

你可能已经注意到，每份备份都必须带有时间戳，WorldEdit 依靠这些时间戳判断哪份备份最新。备份内必须包含世界文件夹，世界文件夹内必须包含 region 文件夹。可以在顶层放置包含多个世界文件夹的备份，也可以先按世界建文件夹，再在各世界文件夹内放入该世界的备份。

!!! tip "提示"

    在类 Linux 系统上，可以使用以下命令创建文件名符合要求的世界备份 ZIP：``zip -v backups/`date "+%Y-%m-%d-%H-%M-%S"`.zip -r world``。

### 支持的归档格式 { #supported-archive-formats }

WorldEdit 使用 Java 的 ZIP 库，原生支持 ZIP 文件。但 Java 的 ZIP 支持仅限基本 ZIP 文件。如果使用 ZIP 时遇到难以理解的错误，可以安装 TrueZip。如果要使用 tarball 等其他归档格式，TrueZip 也支持它们。

要安装 TrueZip，从 [Maven 仓库下载 JAR 文件](https://repo.maven.apache.org/maven2/de/schlichtherle/truezip/6.8.1/truezip-6.8.1.jar)，保存为 `truezip.jar`。Bukkit 上应放在 `plugins` 或 `plugins/WorldEdit` 文件夹，其他平台则放在 `mods` 文件夹。

!!! tip "提示"

    使用备份归档文件（例如 ZIP）可以节省磁盘空间，但会增加实际恢复时的 CPU 开销。如何取舍由你决定。

## 使用备份快照 { #using-snapshots }

配置好备份快照后，使用起来很简单：[选择一个区域](regions/selections.md)，然后执行 `//restore`。

默认情况下，WorldEdit 会查找当前世界最新的备份，并从中恢复所选区域。

如果不想使用最新快照（例如破坏在此之前就已发生，需要更早的备份），还有其他命令可以选择使用哪份快照。

先使用 `/snap list`，列出当前世界的所有可用快照。

可以使用 `/snap use latest` 选择最新快照，或用 `/snap use [name]` 按名称选择。也可以使用 `/snap sel <number>` 选择列表中对应编号的快照。

如果知道需要某个时间点之前或之后的备份，可以使用 `/snap before <time>` 或 `/snap after <time>` 查找离该时间最近的前一份或后一份快照。这些命令接受与文件名相同格式的时间戳，甚至支持自然语言时间，例如 `/snap before "last friday"`。
