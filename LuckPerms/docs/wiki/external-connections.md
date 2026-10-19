---
title: 外部连接
source_url: https://luckperms.net/wiki/External-connections
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

<a id="summary"></a>
### 简要说明
简而言之……

* LuckPerms 首次启动时，会通过互联网连接下载所需的库和翻译包，并采取安全校验措施
* LuckPerms 会将数据发送到外部服务，以提供某些功能（例如 `/lp editor`）
* LuckPerms 不会向指标统计或分析服务上报数据

下文详细说明这些交互和用途。

___

<a id="downloading-libraries"></a>
### 下载依赖库

LuckPerms 使用了许多库，完整列表见[此处](credits.md#open-source)。

插件支持多种配置和使用方式。例如，它支持多种存储方式，每种方式都需要各自的一组驱动。大多数插件会直接将这些库打包（或称为 "shade"）到插件 jar 文件中。但 LuckPerms 使用的库很多，这样做会使最终的 jar 文件过大，并不合适。解决办法是根据所用配置，在运行时下载*实际需要*的库。

<a id="the-download-process"></a>
##### 下载过程

* 只会尝试下载实际需要的库
* 首次下载后，二进制文件会缓存到 `/LuckPerms/libs/` 文件夹。如果库已存在于此处，就不会尝试连接下载服务器。
* 库的 URL 和版本硬编码在插件中，绝不会自动更新。

所有库均从 [https://libraries.luckperms.net/](https://libraries.luckperms.net/) 或 [https://repo1.maven.org/maven2/](https://repo1.maven.org/maven2/) 下载。
后者是通常称为 "Central Repository" 或 "Maven Central" 的公共软件仓库；前者是由 LuckPerms 项目拥有和管理的仓库，提供 Maven Central 的镜像。

Maven Central 是可信的软件来源，大多数 Java 开发者和开源项目都在使用它。

为防范任一网站遭到入侵，插件会在下载过程中执行额外校验，确保库文件完整且符合预期。

<a id="the-verification-process"></a>
##### 校验过程

LuckPerms 的[这个源代码文件](https://github.com/LuckPerms/LuckPerms/blob/master/common/src/main/java/me/lucko/luckperms/common/dependencies/Dependency.java)定义了每个可在运行时下载的依赖，以及它的版本和在 Maven Central 中的位置。

每个条目还包含该版本首次被 LuckPerms 纳入时，依赖文件的 SHA-256 哈希值。此哈希值用作下载文件的校验和。

从仓库下载依赖后，会对下载的数据执行相同的哈希计算，再将得到的哈希值与该依赖的校验和比较。

如果两个哈希值相同，就可以认为下载文件的完整性没有问题。如果不同，则很可能发生了以下两种情况之一：

* 只下载了文件的一部分，下载过程出现了问题
* 依赖文件遭到某种篡改，不应信任

无论哪种情况，LuckPerms 都会丢弃下载的二进制数据，并取消插件启动。

这些检查旨在尽量降低下载服务器遭到入侵后执行恶意代码的风险。它们有效排除了发生[任意代码执行](https://en.wikipedia.org/wiki/Arbitrary_code_execution)的可能性，使这套系统与直接将依赖打包进 jar 一样安全。

___

<a id="downloading-translation-bundles"></a>
### 下载翻译包

LuckPerms 命令中使用的消息已由[社区成员协助翻译](locale-and-translations.md)。

这些译文会自动导出，编译成“翻译包”文件，再通过 API 端点提供。这样就可以持续添加或改进翻译，而无需重新编译插件。

插件会自动更新翻译包，大约每 24 小时一次。这个过程相对安全，因为译文本身不会影响插件的工作方式。

可以在 LuckPerms 配置中禁用此功能。

___

<a id="web-apps-lp-editor-etc"></a>
### 网页应用（例如 `/lp editor`）

LuckPerms 提供了若干集中托管、供所有人使用的网页应用。

* **网页编辑器** - 用于编辑权限数据
* **详细记录查看器** - 用于查看详细记录的日志
* **权限树查看器** - 用于以可视化方式查看树状权限结构



各应用的客户端位于以下地址：

* [https://luckperms.net/editor/](https://luckperms.net/editor/)
* [https://luckperms.net/verbose/](https://luckperms.net/verbose/)
* [https://luckperms.net/treeview/](https://luckperms.net/treeview/)

以上地址依次对应前面列出的应用。

这些网站的源代码可在此处免费获取：[https://github.com/LuckPerms/LuckPermsWeb](https://github.com/LuckPerms/LuckPermsWeb)

编辑器或查看器与插件（运行在你的 Minecraft 服务器上）之间，使用独立的数据包进行通信。编辑器或查看器与服务器之间绝不会直接通信。

可以放心分享编辑器会话的链接。任何更改始终都需要通过在 Minecraft 服务器上执行命令，或明确将该编辑器会话设为信任，才会应用。

数据会提交到 https://usercontent.luckperms.net 并从中读取；它实际上是一个非常简单的内容存储系统，由 Luck 编写并托管。

同样，其源代码可在此处免费获取：https://github.com/lucko/bytebin

更多技术细节见[此处](web-editor-technical-details.md)。

___

<a id="metrics-and-auto-updaters"></a>
### 指标统计与自动更新程序

* LuckPerms **不会**向分析或监控服务上报数据，今后也绝不会这样做。
* LuckPerms **不会**自动检查更新（更不会自动安装更新 😠），今后也绝不会这样做。
