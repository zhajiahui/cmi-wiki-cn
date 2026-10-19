---
title: 从 v4 升级到 v5
source_url: https://luckperms.net/wiki/Upgrading-from-v4-to-v5
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

从 LuckPerms v4 升级到 LuckPerms v5 是一次较大的更新，最主要的变化包括：

* 实现了新的开发者 API。
* 推出了全新版本的网页编辑器。
* 在内部重写了多项功能，使其今后更易于理解和维护。

这次更新后续还会带来更多内容。不过，为了让用户尽早用上这些新功能，我们决定现在就发布。

___

<a id="before-updating"></a>
### 更新之前……
**请务必、务必、务必备份数据。**

<a id="api-compatibility"></a>
### API 兼容性

如果有插件使用旧版 LuckPerms API，它们很可能会在更新后停止工作。

可以通过以下两种方式解决：

1. 请插件作者更新插件，以支持新版 API。（推荐）
2. 安装 `extension-legacy-api` 扩展。

<a id="installing-the-extension"></a>
#### 安装扩展
1. 打开主 `/LuckPerms/` 文件夹。（通常位于 `/plugins/LuckPerms`。）
2. 在此目录中创建名为 `extensions` 的文件夹。
3. 下载 [`extension-legacy-api.jar`](https://ci.lucko.me/job/extension-legacy-api/lastSuccessfulBuild/artifact/build/libs/extension-legacy-api-1.0.0.jar)，并放入 extensions 文件夹。
4. 重启服务器。

<a id="other"></a>
### 其他

如果之前使用了“默认分配”（default assignments，位于配置文件的最后一节），需要[安装 `extension-default-assignments` 扩展](extensions.md)，并考虑迁移到不再依赖此功能的方案。
