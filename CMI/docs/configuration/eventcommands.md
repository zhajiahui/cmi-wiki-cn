---
title: 事件命令（EventCommands.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/EventCommands.yml
---

# 事件命令（EventCommands.yml）

文件：`plugins/CMI/Settings/EventCommands.yml`

## `firstJoinServer` { #firstjoinserver }

```yaml title="EventCommands.yml · firstJoinServer"
# 发生指定事件时执行的命令
# 支持完整颜色代码及部分变量
# 以 msg! 开头并填写玩家名称时，向该在线玩家发送普通消息
# 以 broadcast! 开头时，向服务器所有人发送普通广播
# 以 actionbar! 开头时，向所有玩家发送后面的动作栏消息
# 以 title! 开头时，向所有玩家发送后面的标题
# 以 subtitle! 开头时，向所有玩家发送后面的副标题
# 以 kickall! 开头时，用指定原因踢出所有玩家，适合停服前使用
# 以 perm:[permissionNode]! 开头时，只在玩家拥有该权限时执行；无法确定目标玩家时不生效。例如 perm:cmi.announce.vip! broadcast! Hello vip guys
# [playerName] 插入目标玩家名称
# [playerDisplayName] 插入玩家显示名称
# [lvl] 插入玩家等级
# [exp] 插入玩家总经验
# [hp] 插入玩家生命值
# [maxHp] 插入玩家最大生命值
# [hunger] 插入玩家饥饿值
# [gameMode] 插入玩家游戏模式
# firstJoinServer 触发时，不执行 joinServer 下的命令

# 注意！
# 大量执行高开销命令会增加服务器负载，每个事件请尽量减少此类命令
# 尽可能用 "delay! 0.3" 等参数，将命令延迟分批执行
# 让服务器有时间处理运算，避免同一时刻执行全部命令
firstJoinServer:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `joinServer` { #joinserver }

```yaml title="EventCommands.yml · joinServer"
joinServer:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `quitServer` { #quitserver }

```yaml title="EventCommands.yml · quitServer"
quitServer:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `playerDeath` { #playerdeath }

```yaml title="EventCommands.yml · playerDeath"
playerDeath:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
  SourceCommands: []
```

## `playerKillPlayer` { #playerkillplayer }

```yaml title="EventCommands.yml · playerKillPlayer"
playerKillPlayer:
  # [sourceName] 插入来源玩家名称
  # [sourceDisplayName] 插入玩家显示名称
  # [sourceLvl] 插入玩家等级
  # [sourceExp] 插入玩家总经验
  # [sourceHp] 插入玩家生命值
  # [sourceMaxHp] 插入玩家最大生命值
  # [sourceHunger] 插入玩家饥饿值
  # [sourceGameMode] 插入玩家游戏模式
  # 使用特殊指令时，Commands 对死者执行，SourceCommands 对击杀者执行
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
  SourceCommands: []
```

## `playerRespawn` { #playerrespawn }

```yaml title="EventCommands.yml · playerRespawn"
playerRespawn:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `playerTeleport` { #playerteleport }

```yaml title="EventCommands.yml · playerTeleport"
playerTeleport:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `bedLeave` { #bedleave }

```yaml title="EventCommands.yml · bedLeave"
bedLeave:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `bedEnter` { #bedenter }

```yaml title="EventCommands.yml · bedEnter"
bedEnter:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `playerWorldChange` { #playerworldchange }

```yaml title="EventCommands.yml · playerWorldChange"
playerWorldChange:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `playerPreWorldChange` { #playerpreworldchange }

```yaml title="EventCommands.yml · playerPreWorldChange"
playerPreWorldChange:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `playerGameModeChange` { #playergamemodechange }

```yaml title="EventCommands.yml · playerGameModeChange"
playerGameModeChange:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `playerKick` { #playerkick }

```yaml title="EventCommands.yml · playerKick"
playerKick:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `playerBan` { #playerban }

```yaml title="EventCommands.yml · playerBan"
playerBan:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `playerLevelChange` { #playerlevelchange }

```yaml title="EventCommands.yml · playerLevelChange"
playerLevelChange:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `voidFall` { #voidfall }

```yaml title="EventCommands.yml · voidFall"
voidFall:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `elytraStartGlide` { #elytrastartglide }

```yaml title="EventCommands.yml · elytraStartGlide"
elytraStartGlide:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `advancementDone` { #advancementdone }

```yaml title="EventCommands.yml · advancementDone"
advancementDone:
  # [value] 插入进度标识，例如 husbandry/balanced_diet
  # [value2] 插入进度名称，例如 'A Balanced Diet'
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `elytraEndGlide` { #elytraendglide }

```yaml title="EventCommands.yml · elytraEndGlide"
elytraEndGlide:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `sneakingSwapHandItems` { #sneakingswaphanditems }

```yaml title="EventCommands.yml · sneakingSwapHandItems"
sneakingSwapHandItems:
  Enabled: false
  # 可按需取消物品交换事件；仅在启用事件监听时有效
  CancelEvent: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `swapHandItems` { #swaphanditems }

```yaml title="EventCommands.yml · swapHandItems"
swapHandItems:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `pvpstart` { #pvpstart }

```yaml title="EventCommands.yml · pvpstart"
pvpstart:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```

## `pvpend` { #pvpend }

```yaml title="EventCommands.yml · pvpend"
pvpend:
  Enabled: false
  Commands:
  - "cmi msg [playerName] !这是一条事件命令示例！"
  - "cmi msg [playerName] !来自 sneakingSwapHandItems 事件！"
```
