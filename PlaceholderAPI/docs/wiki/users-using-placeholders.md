---
title: 使用占位符
source_url: https://wiki.placeholderapi.com/users/using-placeholders/
source_kind: official-wiki
translation_review: reviewed
source_version: official-site-2026-10-19-15adfb5d4a300156
---

<a id="using-placeholders"></a>
# 使用占位符

本页面向希望了解如何在插件中使用占位符的服主或服务器管理人员。

如果你是开发者，想了解如何提供占位符，或在自己的插件中支持其他插件的占位符，请参阅[使用 PlaceholderAPI](https://wiki.placeholderapi.com/developers/using-placeholderapi/)。

<a id="prerequisites"></a>
## 前置条件

使用占位符前，请先检查以下事项。

<a id="plugin-supports-placeholderapi"></a>
### 插件支持 PlaceholderAPI

首先，也是最重要的一点，是确认要使用占位符的插件是否支持 PlaceholderAPI。  
EssentialsXChat 等聊天插件并不原生支持 PlaceholderAPI，而是需要借助单独的插件，将解析后的占位符“注入”最终的聊天消息。

可以通过[支持 PlaceholderAPI 的插件](users-plugins-using-placeholderapi.md)页面，检查插件是否支持 PlaceholderAPI。  
如果插件在列表中，且 `Supports placeholders` 文字前标有勾号，就说明它支持 PlaceholderAPI。

如果列表中没有该插件，通常可以查看插件页面，或 Wiki 等其他资料，确认是否支持 PlaceholderAPI。

<a id="proper-internet-connection"></a>
### 正常的网络连接

PlaceholderAPI 会连接位于 <https://api.extendedclip.com> 的 eCloud，获取占位符扩展的信息，并从中下载扩展。  
请确认服务器允许向上述 URL 发起外部连接。如果不允许，且你使用的是托管服务，请联系服务商的客服，要求将此 URL 加入白名单。

服务器托管商须知

PlaceholderAPI 提供并检查一个专用环境变量，用于阻止下载指定的占位符扩展。  
如果你是服务器托管商，希望阻止下载某些占位符扩展，请添加 `PAPI_BLOCKED_EXPANSIONS` 环境变量，将不允许 PlaceholderAPI 下载的扩展名称用逗号分隔，作为变量的值。

此功能从 PlaceholderAPI 2.11.4 起提供

<a id="downloadget-expansion"></a>
## 下载或获取占位符扩展

按照 PlaceholderAPI 的工作方式，占位符扩展及其提供的占位符既可以包含在插件中（如果占位符需要该插件），也可以作为独立的 jar 文件在 PlaceholderAPI 的 eCloud 上提供。  
根据扩展的类型，使用其中的占位符前，可能还需要完成额外的步骤。

要判断占位符扩展是内置的还是独立的，可以在[占位符列表](users-placeholder-list.md)页面中查找对应条目。  
如果找到了条目，请查看扩展标题下方的信息框，判断属于以下哪种情况：

- `papi ecloud download <expansion>`：扩展在 eCloud 上提供，需要使用 [`/papi ecloud download` 命令](users-commands.md#papi-ecloud-download)下载。
- `Built into Plugin`：扩展是其依赖插件的一部分，除非另有说明，否则无需额外安装。
- *一个 URL*：扩展需要从其他来源（例如 GitHub Release）下载。你需要手动下载 jar 文件，并将其移入 expansions 文件夹。

执行 `/papi list`，可以查看已加载的占位符扩展。

<a id="use-expansion"></a>
## 使用占位符扩展

使用扩展提供的占位符很简单。  
只需将格式正确的占位符（例如 `%player_name%`）填入支持占位符的配置项即可。哪些配置项支持占位符，请查阅该插件提供的手册或 Wiki。
