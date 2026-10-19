---
title: "玩家使用了不同的协议版本"
source_url: "https://wiki.itemsadder.com/faq/player-is-using-a-different-protocol-version"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 玩家使用了不同的协议版本

`'Player' is using a different protocol version of the game (x) than the server (x).`

此消息只是一个警告，你可以忽略它。

## 为什么？

一般不建议使用 ViaVersion 及类似插件，除非你想创建大厅服务器（[来源](https://github.com/PluginBugs/Issues-ItemsAdder/issues/3683)）。

ViaVersion 一旦使用不当，就会成为毒瘤。ViaVersion 的用途原本是让客户端连接到支持多版本的大厅，玩家可以在其中选择要加入的服务器。

每个服务器有各自的版本，例如生存服为 1.20.5，PVP 服为 1.8。这样，玩家便能连接到同一个大厅服务器，作为整个服务器社区的主枢纽。

服务器管理员滥用这种能力，允许玩家通过 1.8、1.9、1.13、1.18、1.20 客户端加入 1.20.x 生存服游玩。这会造成多种不兼容、不稳定、漏洞和显示故障。这是因为不同版本之间的客户端（和服务器）发生了大量变化，其中大部分变化都至关重要。

不同版本之间引入了大量变化，因此无法保证毫无问题的游戏体验。

[OriginRealms](https://originrealms.com/) 就是一个成功且只允许单一版本加入的明确例子。它是自定义程度最高的 Minecraft 多人生存体验之一，这一点毋庸置疑。

一边允许过旧的游戏版本加入服务器，一边期待游戏体验稳定，或更进一步保留旧服务端、允许新版客户端加入，作者认为继续这样做没有道理。

ItemsAdder 编写了大量变通代码，用于检查客户端和服务器版本，再启用特殊修复，避免例如 1.18 客户端加入 1.20 服务器时发生崩溃/显示故障。我希望停止维护这类技巧，因为它们并不稳定，只会给我和用户带来压力。我想专注于提供完善、现代的功能，而不必继续支持非常旧的客户端。

因此，请考虑停止允许多个版本加入你的生存服/游戏模式服务器。
