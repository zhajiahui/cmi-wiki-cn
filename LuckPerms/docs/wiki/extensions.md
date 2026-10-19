---
title: "扩展"
source_url: https://luckperms.net/wiki/Extensions
source_kind: official-wiki
translation_review: reviewed
source_version: "fc2919c3d5e6bfba82af31f9930273b00f08ddbf"
---

扩展可以为插件附加额外功能。扩展的工作方式不受 LuckPerms 所运行平台（如 Bukkit、Sponge 等）的影响，因此在所有平台上都可以使用相同方式安装。扩展使用插件提供的原生 API。

扩展本质上就是“插件的插件”——听起来有点绕，也许有些小题大做，不过我觉得这是个不错的解决办法！

___

<a id="installing-extensions"></a>
### 安装扩展

扩展以 `.jar` 文件的形式提供。安装步骤如下：

1. 进入 `/LuckPerms/` 主文件夹（也就是 `config.yml` 所在的文件夹）。
2. 创建一个名为 `extensions` 的子文件夹
3. 将扩展的 `.jar` 文件放入 extensions 文件夹。
4. 重启服务器。

___

<a id="official-extensions"></a>
## 官方扩展

<a id="rest-api"></a>
### REST API

详情见[此处](standalone-and-rest-api.md)。:)

<a id="deprecated-extensions"></a>
### 已弃用的扩展

以下扩展大约发布于 6 年前（以 2025 年 6 月为准），用于减轻从 LuckPerms v4 升级到 LuckPerms v5 的负担。我们认为用户已有足够时间完成更新，因此这些扩展现已弃用，不再提供支持。

* [extension-legacy-api](https://github.com/LuckPerms/extension-legacy-api)
* [extension-default-assignments](https://github.com/LuckPerms/extension-default-assignments)
