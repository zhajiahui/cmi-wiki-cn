---
title: 箱子保护
source_url: https://worldguard.enginehub.org/en/latest/chest-protection/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 箱子保护 { #chest-protection }

WorldGuard 提供基础的玩家自助箱子保护：在箱子下方放置写有特定格式文字的告示牌即可使用。对于新配置的服务器，我们通常建议**不要**使用此功能，因为它并非 WorldGuard 中持续更新的部分。此外，更推荐用[区域](regions/index.md)来定义所有权，因为区域保护不会遇到漏斗等方块带来的这类问题。

!!! warning "警告"

    WorldGuard 的箱子保护不支持 UUID，因此玩家改名后将无法再访问原来的箱子。它也独立于区域和其他保护功能运行。

    **强烈建议不要使用 WorldGuard 的此项功能。此功能将在未来版本中移除。**

    如果需要保护单个方块，请使用 [LWC Extended](https://github.com/pop4959/LWCX) 等专门的插件。

## 开始使用 { #getting-started }

必须先在[配置](config.md)中启用箱子保护。禁用时，箱子保护不会生效，但仍无法制作“锁定告示牌”（不过，现代 WorldGuard 版本已在配置中禁用这种行为）。

只要在箱子下方放置*特殊告示牌*，告示牌就会受到保护。该告示牌：

- 必须是立式告示牌

- 必须位于箱子或其他容器下方；双箱只需在其中一侧下方放置

- 第一行必须写 `[Lock]`

- 第二行必须写玩家的用户名

- 接下来的两行最多再填写两名其他玩家的名字

无法在第二行填写其他玩家的名字。
