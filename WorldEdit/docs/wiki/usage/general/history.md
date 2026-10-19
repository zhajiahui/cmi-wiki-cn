---
title: 操作历史
source_url: https://worldedit.enginehub.org/en/latest/usage/general/history/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 操作历史 { #history }

开始深入使用 WorldEdit 前，应先了解如何通过历史记录撤销操作中的失误。历史记录保存在会话中，详情见[此处](sessions.md)。

## 撤销与重做 { #undo-and-redo }

通过命令或工具执行的每一次 WorldEdit 操作，都会保存在会话的历史记录中。默认保留最近 15 次操作（可在[配置](../../config.md)中更改）。

如果要撤销操作，可以使用 `//undo` 命令。这会撤销最近一次操作。要重做该操作，使用 `//redo`。

!!! warning "警告"

    WorldEdit 只记录直接更改。液体开始流动、附着方块（门、告示牌、高草等）脱落之类的间接更改，不会保存在历史记录中。处理这些内容时要小心。

如[快速入门](../../quickstart.md)所示，历史记录命令可以一次处理多次操作。例如，使用 `//undo 5` 撤销最近 5 次操作。

在多人游戏中，拥有相应权限的玩家还可以使用历史记录命令撤销或重做其他玩家的操作。由于有会话机制，只要对方仍在线就可以撤销；即使对方已退出，之后 10 分钟内仍可撤销。操作方式为 `//undo <number> <player name>`。

可以使用 `/clearhistory` 命令清空保存的历史记录。
