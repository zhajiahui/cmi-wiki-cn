---
title: "常见问题"
source_url: "https://www.zrips.net/cmilib/faq/"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "官方站点 2026-10-19 快照；当前下载 1.6.0.1"
---

# 常见问题

<a id="what-is-cmi-library-cmilib"></a>

## CMI Library（CMILib）是什么？

这个插件辅助库可以统一处理常用文本、十六进制颜色等功能。各个插件无需分别编写这些功能的代码，而是共用同一份代码。这样可以减小插件的总体积，也让更新和维护更简单、更一致。

<a id="how-do-i-get-it"></a>

## 从哪里获取？

最新版本可从 <https://www.spigotmc.org/resources/87610/> 或 <https://www.zrips.net/cmilib/> 获取。

<a id="which-plugins-use-this"></a>

## 哪些插件使用它？

截至 2023 年 6 月的完整列表：

- **CMI**：9.x.x.x 及以上版本
- **Selection Visualizer**：3.x.x.x 及以上版本
- **TryMe**：7.x.x.x 及以上版本
- **Mob Farm Manager**：2.x.x.x 及以上版本
- **Residence**：5.x.x.x 及以上版本
- **Jobs-Reborn**：5.x.x.x 及以上版本
- **BottledExp**：3.x.x.x 及以上版本
- **Recount**：3.x.x 及以上版本
- **TradeMe**：6.x.x.x 及以上版本

这些插件当时都支持 Spigot 和 Paper 1.20.x 及更早的服务端版本，并且需要最新的 CMILib 才能正常运行。

<a id="i-have-updated-locale-but-it-did-not-update"></a>

## 更新了语言文件，为什么没有生效？

CMILib 本身是独立的库，需要执行 **/cmil reload** 命令重新加载它的配置文件，修改才会生效。

<a id="do-i-have-to-restart"></a>

## 需要重启吗？

如果服务器启动时用的就是最新版本，则无需重启；即使存在多个版本，也应当会选用最新版本。但如果 CMILib 在服务器运行期间下载了新版，就需要重启服务器，新版本才会生效。

<a id="backing-up-and-testing"></a>

## 需要备份和测试吗？

需要。作者强烈建议在修改服务器前完整备份，包括插件更新，即使只是小版本更新也要备份，养成定期保留备份的习惯。先测试 CMILib 的升级；如果失败，至少可以从备份恢复到修改前的状态。

<a id="i-have-multiple-versions-what-to-do"></a>

## 有多个版本怎么办？

插件应当会自动移除旧版本。如果自动处理失败，也可以手动删除，但要确认删除的不是当前已加载的版本，否则会产生错误。最稳妥的方式是先关闭服务器，再删除旧版本。

<a id="omg-i-had-cmi-with-lib-1002-then-tryme-with-lib-1010-and-now-residence-with-lib-1023"></a>

## CMI 用 Lib 1.0.0.2，TryMe 用 Lib 1.0.1.0，现在 Residence 又用 Lib 1.0.2.3，怎么办？

无需慌张。实际只会使用一个版本，所有受支持的插件应当共用最新版本。无论使用哪些插件，始终使用最新的库文件。

<a id="i-keep-deleting-this-cmilib-jar-and-it-keeps-coming-back"></a>

## 为什么删掉 CMILib JAR 后，它又出现了？

相关插件需要 CMILib 才能正常工作，因此无法在没有它的情况下使用这些插件。只有更早的版本支持独立运行，但这些旧版本已经不再维护。

<a id="can-i-see-the-cmilib-source-code"></a>

## 能查看 CMILib 源码吗？

源码位于这个 Github 仓库：<https://github.com/Zrips/CMILib>。
