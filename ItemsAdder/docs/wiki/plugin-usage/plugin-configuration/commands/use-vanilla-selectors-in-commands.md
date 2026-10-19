---
title: "在命令中使用原版选择器"
source_url: "https://wiki.itemsadder.com/plugin-usage/plugin-configuration/commands/use-vanilla-selectors-in-commands"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 在命令中使用原版选择器

说实话，我怀疑其他插件是否实现了此功能。这意味着我必须以某种方式识别出你正在使用 Minecraft 原版命令 `execute as`，并正确替换占位符。

要在 ItemsAdder 命令中使用原版选择器，必须安装 [PsudoCommands](https://www.spigotmc.org/resources/psudocommands-perform-plugin-commands-after-execute-and-use-selectors-fork.83535/)。

例如：

`/execute at (player) run psudo iaentity summon (entity) ~ ~ ~ world`
