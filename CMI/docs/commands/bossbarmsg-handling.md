---
title: Boss 栏消息
---

# Boss 栏消息

![](../assets/images/17d4a93f6f-2018-03-22_13-20-48-1.gif)

###### /cmi bossbarmsg all Server shutting down in [autoTimeLeft]! -cmd:"stop" -sec:-60 -c:red

![](../assets/images/25d75f5f2d-2024-01-24_17-52-02.gif)

###### /cmi bossbarmsg all -cw:0.05,10,yellow,red !!!Warning!!!

![](../assets/images/1b92693155-2024-01-24_17-58-50.gif)

###### /cmi bossbarmsg all -p:100 -a:1 -s:1 -t:30 -cw:0.05,10,green,pink,662266 Event starts soon!

这会向 **Zrips** 显示内容为“**Hey you**”的 Boss 栏消息，并在 3 秒后消失。

`cmi bossbarmsg Zrips &2Hey you! -t:5`  
向 Zrips 显示内容为“Hey you”的 Boss 栏消息，并在 5 秒后消失。

`cmi bossbarmsg Zrips &2Hey you! -c:red`  
向 Zrips 显示内容为“Hey you”的红色 Boss 栏消息（默认为绿色）。

`cmi bossbarmsg Zrips &2Hey you! -s:1`  
设置 Boss 栏样式。可选值为 **1, 6, 10, 12, 20**，会将进度条分为相应数量的区段。使用 1 时显示完整进度条，使用 20 时分成 20 段。

`cmi bossbarmsg Zrips &2Hey you! -n:bossBarName`  
指定 Boss 栏名称，可以任意命名。名称用于识别同一条 Boss 栏，并在需要时更新信息。例如，先执行 `cmi bossbarmsg Zrips &2Hey you! -n:myBar`，再执行 `cmi bossbarmsg Zrips &2Whats up? -n:myBar`，会更新同一条 Boss 栏的文本，而不是新建一条。如果不指定名称，每次执行命令都会创建新的 Boss 栏。

`cmi bossbarmsg Zrips &2Hey you! -p:100/23`  
指定 Boss 栏进度，本例会填充到 23%。可以使用一些 **PlaceHolderAPI** 变量，例如 **-p:%server_max_players%/%server_online%**。  
也可以设置自动变化的进度，例如：  
`cmi bossbarmsg Zrips &2Hey you! -p:+1`  
表示每次额外增加一个百分点。如果未设置初始值，则从 0 开始。使用  
`cmi bossbarmsg Zrips &2Hey you! -p:-1`  
时，Boss 栏会从 100 开始递减。  
自动变化的进度达到 0 或 100% 时（取决于进度变化方向），Boss 栏会在 –**t** 预设的时间后消失。可用于各种计数器。

`cmi bossbarmsg Zrips &2Hey you! -cmd:"cmi broadcast !{#red}Timer run out;;cmi broadcast !{#cancan}Better luck next time"`

指定计时结束后执行的命令。可以使用 [playerName] 等全局变量，**但**只有对特定玩家使用此命令时才有效。如果目标玩家为 **all**，即向全服玩家显示 Boss 栏，**-cmd:** 定义的命令会有不同的行为：命令只触发一次，即使有 50 位玩家在线也是如此；[playerName] 等与玩家有关的全局变量也**不会**被解析。

`cmi bossbarmsg all &2Hey you! -pcmd:"msg [playerName] hey;;cmi heal [playerName]"`  
指定自动变化的进度达到 0 或 100 时执行的命令。多条命令可用 ;; 分隔，也支持特殊指令格式，详见[**这里**](specialized.md)。玩家需要 **cmi.command.bossbarmsg.admin** 权限节点才能在其中加入命令。  
与 **-cmd:** 不同，无论目标是单个玩家还是 **all**，这里的命令都会对每位收到 Boss 栏消息的玩家分别执行，并解析对应的全局变量或占位符。  
-cmd: 和 -pcmd: 都可用于单个目标（命令会合并），也可与 **all** 变量一起使用。

`cmi bossbarmsg Zrips &2Hey you! -a:20`  
设置 Boss 栏自动更新的间隔，可以每隔 x 刻自动更新其中的信息。请注意，20 刻等于 1 秒。

`cmi bossbarmsg Zrips -cancel:testbar`

除了文本本身，所有变量都是可选的，可以组合使用来获得所需效果。  
`cmi bossbarmsg all -a:1 Healing incomming in [autoTimeLeft]! -t:2 -p:1 -pcmd:"msg [playerName] &2Some dude healed you!;;cmi heal [playerName] -s" -n:test -c:red` 会显示自动计数的 Boss 栏消息，每刻增加 1（每秒 20 次），从 0 增加到 100，标题为 **Healing incoming in 5sec!**（时间会自动更新）。达到 100 后，所有在线玩家都会收到 **Some dude healed you!** 消息并被治疗。Boss 栏会在 2 秒后消失。

如需精确计时，使用 **-sec:[amount]** 变量。正数表示从 0 计数到目标值，负数表示从指定数值倒计时到 0。因此，前者的进度条会逐渐填满、计时增加，后者的进度条会逐渐减少到 0。页面顶部提供了关闭服务器的基本示例。

将计时设为 **-1** 后，Boss 栏会一直显示，直到玩家重新登录。

---

[查看原文](https://www.zrips.net/cmi/commands/bossbarmsg-handling/)
