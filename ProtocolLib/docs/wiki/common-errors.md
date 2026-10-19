---
title: "常见错误"
source_url: "https://github.com/dmulloy2/ProtocolLib/wiki/Common-Errors"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "ProtocolLib d89a5deb3eb625b16846da57fbbb04bfdd0d031d；官方 Wiki 与发布页 2026-10-19 快照"
---

# 常见错误

<a id="plugins"></a>

## 插件

许多看似由 ProtocolLib 引起的错误，实际来自使用它的插件。移除 ProtocolLib 后，错误看似消失，是因为那些插件也无法运行了。较快的排查方式是手动进行[二分查找](https://www.geeksforgeeks.org/binary-search/)。先执行 `/protocol dump`，查看输出底部，确认哪些插件使用了它。然后移除其中一半，观察问题是否仍然存在。如果仍在，就移除另一半；如果不再出现，就继续在刚才移除的那一半中二分排查，因为另一半很可能没有问题。不断缩小插件范围，直到找到原因。
***

## FieldAccessException

这个错误通常表示某个插件尚未适配新的 Minecraft 版本。请向该插件作者反馈。如果你是插件作者、无法确定原因，或堆栈中没有出现其他插件，欢迎提交 Issue。
***

<a id="illegalaccesserrornosuchmethoderror-for-protocollogger"></a>

## ProtocolLogger 的 IllegalAccessError/NoSuchMethodError

某个插件错误地把 ProtocolLib 的一部分包含在自己的 JAR 中。可以优先检查 plugins 文件夹中体积最大的 JAR，因为它会包含远多于应有数量的类。用 7-zip、WinRar 或 Vim 等工具，在 JAR 中查找 `com/comphenix/protocol` 文件夹。
***

<a id="noclassdeffounderror-for-basecomponent"></a>

## BaseComponent 的 NoClassDefFoundError

使用[最新开发构建](https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/)，或改用 Spigot。
***

## IllegalArgumentException: Unable to find findStatistic

更新到[最新正式版本](https://github.com/dmulloy2/ProtocolLib/releases)或[开发构建](https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/)。
