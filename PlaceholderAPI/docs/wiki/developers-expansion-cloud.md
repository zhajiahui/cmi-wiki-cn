---
title: Expansion Cloud
source_url: https://wiki.placeholderapi.com/developers/expansion-cloud/
source_kind: official-wiki
translation_review: reviewed
source_version: official-site-2026-10-19-15adfb5d4a300156
---

<a id="ecloud"></a>
# eCloud

<a id="about"></a>
## 简介

PlaceholderAPI 通过 Expansion Cloud（存放各类占位符扩展的网站）下载 jar 文件，这些文件包含可供 PlaceholderAPI 使用的占位符。

Expansion Cloud 的地址为 <https://ecloud.placeholderapi.com>

<a id="how-it-works"></a>
## 工作原理

服务器启动时，PlaceholderAPI 会连接 eCloud，检查其是否可用，以及上面有多少个可用的占位符扩展。  
执行 [`/papi ecloud download <expansion>`](users-commands.md#papi-ecloud-download) 时，PlaceholderAPI 会连接网站，先检查指定的占位符扩展是否存在，存在则下载。

说明

PlaceholderAPI 只能下载 eCloud 上已通过审核的占位符扩展。未通过审核的扩展都需要手动下载。

将 config.yml 中的 `cloud_enabled` 设为 false，即可禁用与云端的连接。

<a id="adding-your-own-expansion"></a>
## 添加自己的占位符扩展

可以将自己制作的占位符扩展添加到 Expansion Cloud，供其他人使用。  
具体步骤如下：

1. 确认已按照[创建 PlaceholderExpansion](https://wiki.placeholderapi.com/developers/creating-a-placeholderexpansion/)页面的说明，制作独立的 jar 文件。
2. 在网站上注册账号；如果已有账号，直接登录。
3. 点击 `Expansions`，再点击 [`Upload New`](https://ecloud.placeholderapi.com/expansions/new/)。
4. 填写必需的信息。`Source URL` 和 `Dependency URL` 为可选项，分别填写占位符扩展的源代码链接和依赖（插件）链接。
5. 点击 `Choose an file...` 按钮，选择占位符扩展的 jar 文件。

   **重要！**  
   确认 jar 文件名中包含的版本号与版本字段中填写的一致。
6. 点击 `Submit Expansion`

占位符扩展现已上传，接下来将由审核人员审核。  
如果一切正常，占位符扩展就会通过审核，并可由 PlaceholderAPI 从 eCloud 获取\*。

服务器托管商须知

可以使用 `PAPI_BLOCKED_EXPANSIONS` 环境变量阻止下载指定的占位符扩展。  
将不允许通过 PlaceholderAPI 下载的扩展名称用逗号分隔，作为该环境变量的值即可。

此功能从 PlaceholderAPI 2.11.4 起提供。

<a id="updating-your-expansion"></a>
## 更新占位符扩展

更新前，请注意以下事项：  
更新占位符扩展后，其状态会自动变为未审核，需要网站审核人员重新审核。这是为了防止恶意软件被上传和传播。

要更新占位符扩展，先打开[自己的扩展列表](https://ecloud.placeholderapi.com/expansions/manage/)。  
点击 `Expansions`，再选择 `Your Expansions` 即可打开。  
然后按以下步骤操作：

1. 点击要更新的占位符扩展名称。
2. 点击 `Version` 按钮
3. 点击 `Add Version`
4. 填写各个字段，并上传新的 jar 文件。

   **重要！**  
   确认 jar 文件名中包含的版本号与版本字段中填写的一致。
5. 点击 `Save Changes`

现在，新版本应已上传到 eCloud。可以在 [HelpChat Discord](https://discord.gg/helpchat) 中请负责的工作人员审核占位符扩展，以便重新通过审核。提出请求时，请保持耐心和礼貌。

<a id="downloading-a-specific-expansion-version"></a>
## 下载占位符扩展的指定版本

有时可能需要使用占位符扩展的某个旧版本。例如，服务器版本较旧，而扩展的最新版本调用了该服务器版本中不存在的方法，导致兼容性问题。  
遇到这种情况，可以下载占位符扩展的指定版本。既可以手动下载，也可以通过 PlaceholderAPI 下载。  
下面分别说明这两种方法。

<a id="download-with-placeholderapi"></a>
### 通过 PlaceholderAPI 下载

这是两种方法中较简单的一种，所需操作最少。  
在游戏内或控制台中执行以下命令，即可下载指定版本：  
[`/papi ecloud download <expansion> [version]`](users-commands.md#papi-ecloud-download)

执行 [`/papi ecloud info <expansion>`](users-commands.md#papi-ecloud-info)，可以查看该占位符扩展有哪些可用版本。

下载指定版本后，执行 [`/papi reload`](users-commands.md#papi-reload)，刷新已安装的占位符扩展。

<a id="download-manually"></a>
### 手动下载

要手动下载占位符扩展，先访问网站，打开所需扩展的页面。  
点击 `Version` 按钮，再点击所需版本旁的下载图标。

最后，关闭服务器，将 jar 文件上传到 `/plugins/PlaceholderAPI/expansions` 文件夹（如果已有旧的 jar 文件，请先将其删除），然后重新启动服务器。
