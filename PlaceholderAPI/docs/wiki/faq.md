---
title: 常见问题
source_url: https://wiki.placeholderapi.com/faq/
source_kind: official-wiki
translation_review: reviewed
source_version: official-site-2026-10-19-15adfb5d4a300156
---

<a id="faq"></a>
# 常见问题

这里汇总了有关 PlaceholderAPI 的常见问题。

<a id="what-is-an-expansion"></a>
## 什么是占位符扩展？

占位符扩展（或 PlaceholderExpansion）指的是一个 jar 文件，或插件中为 PlaceholderAPI 提供占位符的部分。  
扩展是独立的 jar 文件，还是插件的一部分，取决于扩展本身及其主要用途。

独立 jar 文件形式的占位符扩展可以在 eCloud 上找到；通过审核的扩展可以使用 [`/papi ecloud download <expansion>`](users-commands.md#papi-ecloud-download) 下载。

<a id="it-only-shows-placeholder-and-not-the-variable"></a>
## 只显示 `%placeholder%`，而没有显示对应的值

如果插件或 [`/papi parse me %placeholder%`](users-commands.md#papi-parse) 只返回占位符本身，没有返回对应的值，请检查以下内容：

<a id="the-expansion-is-actually-installed"></a>
- ### 确认已安装占位符扩展

  有些占位符扩展没有集成在插件中，甚至没有依赖的插件。这意味着它们可能是独立的 jar 文件，需要单独下载。  
  这类扩展通常可以在 PlaceholderAPI 的 eCloud 上找到，并使用 [`/papi ecloud download <expansion>`](users-commands.md#papi-ecloud-download) 命令下载。

  可以通过[占位符列表](users-placeholder-list.md)判断扩展是否在 eCloud 上提供：凡是显示了 papi 命令的扩展，都可以下载。
<a id="plugin-actually-supports-placeholderapi"></a>
- ### 确认插件支持 PlaceholderAPI

  用于显示占位符的插件可能不支持 PlaceholderAPI。遇到这种情况，请检查 parse 命令能否返回占位符的实际值。  
  如果 parse 命令能返回实际值，但插件仍然原样显示占位符，就可能说明该插件不支持 PlaceholderAPI。

  可以在[这里](users-plugins-using-placeholderapi.md)查看支持 PlaceholderAPI 的插件列表。  
  请确认“支持占位符”前标有勾号。
<a id="no-typo-in-the-placeholder"></a>
- ### 确认占位符拼写无误

  仔细检查填写的占位符是否有拼写错误。可以使用 [`/papi ecloud placeholders <expansion>`](users-commands.md#papi-ecloud-placeholders)（将 `<expansion>` 替换为扩展名称）获取该扩展可能提供的全部占位符列表。  
  注意，这只适用于 eCloud 上的独立占位符扩展，不适用于由插件加载的扩展。

  此外，eCloud 上的占位符列表可能已经过时。建议查看[占位符列表](users-placeholder-list.md)，或查找所需占位符的相关文档。
<a id="plugin-is-enabled"></a>
- ### 确认插件已启用

  如果占位符扩展依赖某个插件，请确认已安装并启用该插件（在 `/pl` 中显示为绿色）。

<a id="i-cant-download-the-expansion"></a>
## 无法下载占位符扩展

请检查以下内容：

1. 防火墙或服务器托管商没有阻止服务器连接 eCloud（地址为 <https://api.extendedclip.com>）。
2. 所需的占位符扩展确实在 eCloud 上提供。部分扩展直接包含在插件中。
3. 占位符扩展已通过审核。只有通过审核的扩展才能使用 PlaceholderAPI 的下载命令下载。这是一项防止恶意软件传播的安全措施。

如果以上检查均无问题，但仍然无法通过下载命令获取占位符扩展，可以考虑手动下载。  
打开该扩展的 eCloud 页面，下载 jar 文件并放入 `/plugins/PlaceholderAPI/expansions/`，然后执行 [`/papi reload`](users-commands.md#papi-reload)。

<a id="how-can-other-plugins-use-my-placeholders-with-placeholderapi"></a>
## 如何让其他插件通过 PlaceholderAPI 使用我提供的占位符？

请参阅[使用 PlaceholderAPI](https://wiki.placeholderapi.com/developers/using-placeholderapi/)页面。

<a id="can-i-help-on-this-wiki"></a>
## 我可以参与完善这个 Wiki 吗？

当然可以！  
欢迎所有人为 Wiki 做贡献。如果发现错别字，或想以其他方式改进 Wiki，请阅读 [Wiki 的 readme 文件](https://github.com/PlaceholderAPI/PlaceholderAPI/blob/wiki/README.md)，了解如何参与。

<a id="placeholderapi-is-posting-an-error-about-an-outdated-expansion"></a>
## PlaceholderAPI 报错，提示占位符扩展已过时？

```
[00:00:01 ERROR]: [PlaceholderAPI] Failed to load Expansion class <expansion> (Is a dependency missing?)
[00:00:01 ERROR]: [PlaceholderAPI] Cause: NoClassDefFoundError <path>
```

如果出现上述错误，请尝试以下步骤：

- 确认已安装报错所指扩展的全部必需依赖（例如某个插件）。
- 确认使用的是当前服务器版本所支持的最新版本。
- 如果 jar 文件是从 eCloud 下载的，请确认文件格式正确且未损坏。

如果完成这些检查后问题仍然存在，请向占位符扩展的作者报告。  
大多数情况下，问题是缺少依赖，或占位符扩展尝试调用 PlaceholderAPI 中已过时的方法。
