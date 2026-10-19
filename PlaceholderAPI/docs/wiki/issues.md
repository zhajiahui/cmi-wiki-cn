---
title: 常见问题排查
source_url: https://wiki.placeholderapi.com/issues/
source_kind: official-wiki
translation_review: reviewed
source_version: official-site-2026-10-19-15adfb5d4a300156
---

<a id="common-issues"></a>
# 常见问题排查

本页列出了使用 PlaceholderAPI 时可能遇到的常见问题及其解决方法。

如果还有其他问题，欢迎加入 [Discord 服务器](https://discord.gg/helpchat)。

<a id="ecloud-download-fails-blocked-connection"></a>
## eCloud 下载失败或连接被阻止

如果服务器托管商或网络阻止向 Expansion Cloud（eCloud）发起连接，PlaceholderAPI 就无法下载占位符扩展。

请参阅：[eCloud 连接被阻止](issues-ecloud-block.md)

<a id="javalangnoclassdeffounderror-comgooglegsongson"></a>
## `java.lang.NoClassDefFoundError: com/google/gson/Gson`

如果遇到如下错误：

```
org.bukkit.plugin.InvalidPluginException: java.lang.NoClassDefFoundError: com/google/gson/Gson
```

这说明运行 PlaceholderAPI 的服务器没有包含 Gson。  
运行 1.8 或更早版本的服务器经常会遇到这种情况。要解决此问题，请至少使用 1.8.8，因为该版本包含所需的依赖。

<a id="expansions-wont-work"></a>
## 占位符扩展不生效

如果一个或多个占位符扩展不生效，请检查以下内容：

- 下载占位符扩展后，已执行 `/papi reload`。
- 所有必需的插件均已安装并启用。
- 占位符扩展本身有效（见后续章节）。

<a id="failed-to-load-expansion-class-expansion"></a>
## `Failed to load expansion class <expansion> ...`

<a id="-one-of-its-properties-is-null-which-is-not-allowed"></a>
### `- One of its properties is null which is not allowed`

出现此错误，说明占位符扩展中的 `getAuthor()`、`getIdentifier()` 或 `getVersion()` 返回了 `null`，而这些方法不允许返回该值。  
遇到这种情况，请联系占位符扩展的开发者，告知问题并请其修复。

<a id="is-a-dependency-missing"></a>
### `(Is a dependency missing?)`

占位符扩展加载失败时就会出现此错误，常见原因是缺少依赖（必需的插件），或创建扩展实例失败。

此时你唯一能做的是提供完整的错误信息，以便我们判断问题出在 PlaceholderAPI（可能性较低）还是占位符扩展。

<a id="some-player-placeholders-arent-working-on-hytale"></a>
## 部分玩家占位符在 Hytale 上不生效

受 Hytale 的并发机制和 PlaceholderAPI 的设计影响，某些玩家占位符需要开发者采用特定的解析方式。如果你是插件用户，发现 %player\_health% 等占位符不生效，但使用 `/papi parse me %player_health%` 时可以正常显示，那么很可能是所用插件对 PlaceholderAPI 支持的实现有误。

要访问某些玩家数据，需要在该玩家所在世界的线程中解析占位符。

```
final World world = player.getWorld();
world.execute(() -> {
    PlaceholderAPI.setPlaceholders(/* set placeholders here */);
})
```
