---
title: 事件命令（EventCommands.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/EventCommands.yml
---

# 事件命令（EventCommands.yml）

文件：`plugins/CMI/Settings/EventCommands.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `firstJoinServer`

发生指定事件时执行的命令<br>
支持完整颜色代码及部分变量<br>
以 msg! 开头并填写玩家名称时，向该在线玩家发送普通消息<br>
以 broadcast! 开头时，向服务器所有人发送普通广播<br>
以 actionbar! 开头时，向所有玩家发送后面的动作栏消息<br>
以 title! 开头时，向所有玩家发送后面的标题<br>
以 subtitle! 开头时，向所有玩家发送后面的副标题<br>
以 kickall! 开头时，用指定原因踢出所有玩家，适合停服前使用<br>
以 perm:\[permissionNode\]! 开头时，只在玩家拥有该权限时执行；无法确定目标玩家时不生效。例如 perm:cmi.announce.vip! broadcast! Hello vip guys<br>
\[playerName\] 插入目标玩家名称<br>
\[playerDisplayName\] 插入玩家显示名称<br>
\[lvl\] 插入玩家等级<br>
\[exp\] 插入玩家总经验<br>
\[hp\] 插入玩家生命值<br>
\[maxHp\] 插入玩家最大生命值<br>
\[hunger\] 插入玩家饥饿值<br>
\[gameMode\] 插入玩家游戏模式<br>
firstJoinServer 触发时，不执行 joinServer 下的命令

注意！<br>
大量执行高开销命令会增加服务器负载，每个事件请尽量减少此类命令<br>
尽可能用 "delay! 0.3" 等参数，将命令延迟分批执行<br>
让服务器有时间处理运算，避免同一时刻执行全部命令

## `playerKillPlayer`

### `playerKillPlayer.Enabled`

\[sourceName\] 插入来源玩家名称<br>
\[sourceDisplayName\] 插入玩家显示名称<br>
\[sourceLvl\] 插入玩家等级<br>
\[sourceExp\] 插入玩家总经验<br>
\[sourceHp\] 插入玩家生命值<br>
\[sourceMaxHp\] 插入玩家最大生命值<br>
\[sourceHunger\] 插入玩家饥饿值<br>
\[sourceGameMode\] 插入玩家游戏模式<br>
使用特殊指令时，Commands 对死者执行，SourceCommands 对击杀者执行

## `advancementDone`

### `advancementDone.Enabled`

\[value\] 插入进度标识，例如 husbandry/balanced\_diet<br>
\[value2\] 插入进度名称，例如 'A Balanced Diet'

## `sneakingSwapHandItems`

### `sneakingSwapHandItems.CancelEvent`

可按需取消物品交换事件；仅在启用事件监听时有效
