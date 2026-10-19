---
title: "嵌入依赖的问题"
source_url: "https://docs.packetevents.com/introduction/the-problem-of-bundling/"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "packetevents-docs a2a91c32fe7ff913413072ab0e51fe95a36f4028（2026-10-19 快照）"
---

<a id="the-problem-of-bundling"></a>

# 嵌入依赖的问题

开始开发前，需要先做出一些重要决定。它们可能影响项目是否成功、是否容易推广，尤其会影响文件体积。

这里要讨论的是嵌入依赖（bundling，通常也称 shading）：把项目依赖一同放进发布文件。向论坛发布模组或插件时，可以选择将 PacketEvents 嵌入项目的发布文件或输出文件。好处很直接：最终用户无需另行安装 PacketEvents 这个前置，安装过程更简单。

这种方式对许多最终用户很有吸引力，因为项目更容易安装。但它也有明显缺点，因此官方不推荐嵌入依赖。嵌入后，保持 PacketEvents 为最新版本的责任就落在项目开发者身上。如果用户遇到问题，或更新了 Minecraft，可能会需要更新版 PacketEvents。他们无法自行更新，只能等待开发者发布包含新版库的项目版本。根据匿名数据，作者推测，部分用户一直使用过时 PacketEvents 的一个原因，就是插件开发者将它嵌入插件，无意中延迟了用户获得改进的时间。此外，嵌入还会使软件故障的责任归属变得复杂。常见情况如下：

!!! note "责任归属问题"

    **Bob** 安装了程序员 **frap** 开发的 **Vulcan** 插件，**Vulcan** 内含 PacketEvents。安装 **Vulcan** 后，**Bob** 的服务器报错。他认为问题出在 **Vulcan**，于是向 **frap** 报告。最后，**frap** 才发现问题实际来自 PacketEvents，并转交给 PacketEvents 团队。

这种情况下，PacketEvents 团队往往会延迟很久才收到错误报告。如果问题来自 PacketEvents，用户本可直接向团队反馈。这条间接反馈链使沟通更加复杂：团队可能需要后续信息，而开发者又得重新联系用户，把双方接起来。

总体而言，是否嵌入 PacketEvents，取决于你更重视什么。如果更看重项目的推广，可能更愿意将它一同打包，因为这能简化大多数用户的安装。如果更看重用户体验，则应避免嵌入。设想 Minecraft 发布了新版，而你正在休假，无法更新插件。如果 PacketEvents 与项目分开运行，用户就可以自行更新它，而且在许多情况下，插件仍能运行，无需你立即发布更新。虽然团队无法保证完全向后兼容，但会尽力减少库中的破坏性变更。
