---
title: 暂离与闲置（Afk.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/Afk.yml
---

# 暂离与闲置（Afk.yml）

文件：`plugins/CMI/Settings/Afk.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `Afk`

### `Afk.Enabled`

开启或关闭自动 AFK 系统

### `Afk.TitleMessage`

启用后，通过标题提示玩家已进入 AFK 状态

### `Afk.SubTitleMessage`

启用后，随机显示副标题消息

### `Afk.PreventJumping`

防止玩家通过原地跳跃避开 AFK 判定

### `Afk.PreventDamage`

防止 AFK 玩家受到伤害

### `Afk.PreventMobDamage`

防止 AFK 玩家对生物造成伤害

### `Afk.CheckInterval`

检查玩家 AFK 状态的间隔，单位为秒

### `Afk.StopPlayTime`

设为 true，停止累计玩家在线时长<br>
受实现方式影响，查看在线时长时可能出现约 1 秒的上下波动

### `Afk.AutoAfkIn`

玩家停止移动多久后，标记为 AFK<br>
玩家需要 cmi.command.afk.auto 权限<br>
设为 0 关闭此限制

### `Afk.AutoAfkCmds`

玩家因长时间无操作而自动进入 AFK 时执行的命令<br>
支持特殊指令

### `Afk.ManualAfkCmds`

玩家执行 /cmi afk 时执行的命令<br>
支持特殊指令

### `Afk.LeaveCmds.Manual`

玩家手动进入 AFK 后，退出 AFK 时执行的命令

### `Afk.LeaveCmds.Auto`

玩家自动进入 AFK 后，退出 AFK 时执行的命令

### `Afk.AutoKickTimes.Default`

玩家停止移动多久后踢出<br>
此计时叠加在 AutoAfkIn 之后。手动进入 AFK 时，也会在 AutoAfkIn+AutoKickIn 秒后被踢出<br>
也可不踢出玩家，而是每隔 X 秒重复执行指定操作<br>
设为 -1 关闭自动踢出<br>
可通过 cmi.command.afk.kickbypass 权限绕过<br>
也可用 cmi.command.afk.kickOutIn.\[seconds\] 指定踢出时间，有多个值时取较大值

### `Afk.AutoKickTimes.FromPlayerCount`

在线人数达到多少时，才开始自动踢出<br>
设为 0 时，无论在线人数多少都生效<br>
建议值：15

### `Afk.AutoKickTimes.ByPlayerCount`

按在线人数设置自动踢出时间，格式为 \[playerCount\]-\[seconds\]<br>
仅在默认踢出时间大于 -1 时生效<br>
向下选择最接近当前人数的条目。例如有 30-400、40-350，当前在线 35 人时使用 400 秒<br>
进入 AFK 时选定踢出时间；AFK 期间即使在线人数变化，也不会重新计算<br>
找不到合适条目时，使用默认值

### `Afk.RepeatingAutoKickInterval`

再次执行踢出命令前的等待时间

### `Afk.RepeatKickCommand`

设为 true，每隔 RepeatingAutoKickInterval 秒重复执行踢出命令

### `Afk.AutoKickCmds`

玩家达到可踢出条件时执行的命令<br>
若玩家未被踢出，每隔 RepeatingAutoKickInterval 秒重复执行

### `Afk.DisabledWorlds`

这些世界中，玩家即使长时间无操作也不会自动进入 AFK

### `Afk.DisableOnInteract`

交互时退出 AFK

### `Afk.SmartInteractCheck`

防止玩家对特定物品或方块持续按住某个按键，以绕过 AFK

### `Afk.AntiAfkMachines`

防止通过挂机装置持续移动来绕过 AFK

### `Afk.PreventHook`

防止 AFK 玩家被拉走

### `Afk.PreventPushing`

实验性功能！防止 AFK 玩家被推动<br>
玩家仍可能在当前所在的同一个方块内移动

### `Afk.DisableOnInventoryClick`

点击物品栏时退出 AFK

### `Afk.DisableOnitemDrop`

丢弃物品时退出 AFK

### `Afk.DisableOnCommand`

执行命令时退出 AFK

### `Afk.DisableOnPublicChat`

发送公共聊天消息时退出 AFK

### `Afk.DisableOnPrivateChat`

发送私聊消息时退出 AFK

### `Afk.DisableOnMove`

移动时退出 AFK

### `Afk.DisableOnLookAround`

转动视角时退出 AFK

### `Afk.DisableOnFishing`

钓到鱼时退出 AFK

### `Afk.DisableItemPickup`

AFK 时禁止拾取物品

### `Afk.PreventMobSpawning.Enabled`

启用后，可阻止在 AFK 玩家附近生成生物

### `Afk.PreventMobSpawning.Natural`

阻止自然生成生物<br>
可能增加服务器负载，因为服务端仍会持续尝试在 AFK 玩家附近生成怪物

### `Afk.PreventMobSpawning.Spawners`

阻止刷怪笼生成生物

### `Afk.PreventMobSpawning.VillageDefence`

通常影响铁傀儡生成

### `Afk.DisableExpPickup`

AFK 时禁止拾取经验<br>
注意！由于 Minecraft 经验球的处理方式，较合适的做法是将经验球设为 0 经验后允许吸收<br>
因此启用后，AFK 玩家吸收经验球不会获得经验

### `Afk.Disable.ShulkerTargeting`

禁止潜影贝将 AFK 玩家选为目标
