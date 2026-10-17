---
title: 物品附加指令
---

# 物品附加指令

物品附加指令支持**特殊指令**机制，详见[**这里**](specialized.md)。

多条命令可用 **`;;`** 分隔。例如，要治疗玩家并恢复其饥饿值，可以使用 `/cmi attachcommand cmi heal [playerName];;cmi feed [playerName]`。

任何物品都可以附加一条或多条命令，使用物品时就会执行这些命令。

可以指定物品的使用次数，即物品使用多少次后会被移除。目前只能通过 **`/cmi attachcommand`** 命令设置。

`/cmi attachcommand cmi launch [interactedPlayer] a:45` 会将你手持该物品时交互的玩家发射出去。

`[interactedBlock]`：此变量可插入交互方块的类型。

`[interactedEntity]`：此变量可插入交互实体的类型。

## !cc!

从控制台执行命令，需要 `cmi.command.attachcommand.cc` 权限。请注意，只有创建物品时才需要此权限，使用物品时不需要。

## !right!

若只想在玩家右键点击时执行命令，添加 `!right!` 变量。例如，`/cmi attachcommand !right!cmi heal` 会在右键点击时执行治疗命令，左键点击时没有效果。

## !left!

若只想在玩家左键点击时执行命令，添加 `!left!` 变量。例如，`/cmi` **`attachcommand !left!cmi heal`** 会在左键点击时执行治疗命令，右键点击时没有效果。

可以在同一件物品上组合两种点击方式，例如 `/cmi attachcommand !left!cmi heal;;!right!cmi feed`：左键治疗玩家，右键恢复其饥饿值。与 `!silent!` 变量搭配的用法：`/cmi attachcommand !left!!silent!cmi heal;;!right!!silent!cmi feed`

## !ignore!

使用此变量后，物品本身的动作和附加命令都会执行。

## !cooldown:[seconds]!

`/cmi attachcommand !cooldown:60!;;!cc!cmi heal [playerName]` 允许玩家每 60 秒使用一次该物品来治疗自己。请注意，复制出来的物品会共用同一个冷却时间；新创建的物品即使附加的命令完全相同，也会有独立的冷却时间。

## !limiteduse:[amount]!

例如，`/cmi attachcommand !limiteduse:5!` 会将物品的使用次数设为 `5`。剩余次数会显示在物品描述中，使用物品时也会显示在动作栏中。  
也可以从控制台执行命令，例如 `/cmi attachcommand !cc!cmi fly [playerName]`。这里同样可以使用变量插入玩家名称。  
以下是一些示例：  
`/cmi attachcommand !limiteduse:3!;;!cc!cmi fly [playerName] true` 会将玩家的飞行模式设为 true。  
`/cmi attachcommand !limiteduse:3!;;!cc!cmi tfly [playerName] 60` 会为玩家开启 60 秒飞行模式，共可使用 3 次。  
`/cmi attachcommand !limiteduse:3!;;!cc!cmi heal [playerName]` 可治疗玩家 3 次，之后物品会消失。

如果物品堆叠在一起，每件物品都会在次数用尽后依次消耗。因此，5 件各有 3 次使用机会的物品，总共可使用 15 次。

## !safelimiteduse:[amount]!

与 `!limiteduse:[amount]!` 不同，此变量在使用次数耗尽后**不会**移除物品。次数达到 0 时，会清除物品上的额外数据和物品描述中的附加提示，之后点击物品将不再执行任何命令。如果玩家持有一叠采用这种安全限次方式的物品，背包中会获得一个清除了附加数据的普通版本物品。

## !consume!

若只想在玩家吃下食物时执行命令，可以在开头使用 **!consume!** 变量。例如：

```text
/cmi attachcommand !consume!;;!cc!cmi me [playerName] says helo!;;!cc!cmi panimation circle;c:85,254,254;twist;part:5;r:0.5;pitch:90;move:0,0.33,0;offset:0,-0.2,0;target:[playerName];;cmi sound [playerName] ambient_cave
```

玩家吃下物品时，会在聊天栏中输出消息、播放粒子效果并播放音效。

请注意，使用此功能时**不可同时使用 !limiteduse:[amount]!**，因为必须消耗物品才会执行命令。

---

[查看原文](https://www.zrips.net/cmi/commands/attached-commands/)
