## 随机传送简介

CMI 的**随机传送**功能允许服主将玩家强制传送到某个世界中的随机位置。

这个功能适用于某些活动、自定义别名，最常见的用途是 **/rtp** 命令。

## 配置 /rtp 命令

/cmi rt 命令有几种配置方式，许多服务器习惯将其称为 /rtp。
**通过 Alias.yml 配置：**
打开 Alias.yml 文件，找到 /rt 和 /rtp 命令，将各自的 enabled: 设为 true，然后保存文件。

```text
  # /cmi rt $1-
  /rt:
    Enabled: true
    Tab: true
  /rtp:
    Enabled: true
    Tab: true
```

保存文件后执行 /cmi reload，即可立即使用这些命令。不过，在较新的 Minecraft 版本中，这些命令会显示为红色，直到执行 /stop 并重新启动服务器。
**通过 AliasEditor 配置：**
在游戏中执行 /cmi aliaseditor 命令，创建新的 /rtp 命令。执行后，点击绿色 + 图标，将命令命名为 rtp，再点击下一个绿色 + 图标，即可添加一条或多条命令。可以添加显示粒子、延迟、发送自定义 msg 或 actionmsg 等命令，也可以以控制台身份执行完整的 cmi rt 命令，将随机传送限定到某个世界等。
下面是 cmi-rtp-cmd.yml 文件的示例，可以将其放入 plugins/CMI/CustomAlias/ 文件夹，然后执行 /cmi reload 或重启服务器。

```text
CustomAlias:
  rtp:
    Cmds:
    - asConsole! cmi sound block_conduit_deactivate [playerName]
    - asConsole! cmi titlemsg [playerName] &6⸭ ⸭ ⸭\n&fCharging teleporter
    - delay! 3
    - asConsole! cmi titlemsg [playerName] &6⸭ ⸭ ⸭\n&fTeleporter is ready!
    - asConsole! cmi rt [playerName]
    - delay! 0.2
    - asConsole! cmi sound entity_generic_explode [playerName]
```

这个示例展示了如何播放音效、添加延迟、显示自定义标题消息、执行 cmi rt 命令，以及播放结束音效。用 aliaseditor 创建的自定义 /rtp 命令也可以按需要执行其他操作，命令名称也可以改为 /random、/rt 或 /teleporter。

## 配置（命令 / config.yml）

可以通过几种方式配置或自动配置 /cmi rt 的行为，包括 config.yml 中的多项设置和一些游戏内命令。请正确配置全局设置和各世界的独立设置，避免出现非预期结果。

**命令：**（完整语法见本页下方）  
`/cmi setrt world center:0,0 min:250 max:5000 square enabled`

**Config.yml：**

```text
RandomTeleportation:
  # If this set to true we will generate random teleport default settings for all detected worlds
  # Setting to false will not longer generate world setups, but you can add them manually if needed
  AutoGenerateWorlds: true
  Worlds:
    # World name to use this feature. Add annother one with appropriate name to enable random teleportation
    world:
      Enabled: true
      # Max coordinate to teleport, setting to 1000, player can be teleported between -1000 and 1000 blocks between defined center location
      # For example having centerX at 2000 and centerZ at 3000 while MaxRange is set to 1500 we will teleport player between x:500;z:1500 and x:3500;z:4500 coordinates
      MaxRange: 1000
      # If maxcord set to 1000 and mincord to 500, then player can be teleported between -1000 to -500 and 1000 to 500 coordinates
      MinRange: 500
      CenterX: 0
      CenterZ: 0
      Circle: false
      IgnoreWater: true
      IgnoreLava: true
      ignorePowderSnow: false
      minY: -50
      maxY: 300
    world_nether:
      Enabled: true
      MaxRange: 25000
      MinRange: 100
      CenterX: 25
      CenterZ: -50
      Circle: true
      IgnoreWater: false
      IgnoreLava: true
      ignorePowderSnow: false
      minY: 0
      maxY: 128
    world_the_end:
      Enabled: true
      MaxRange: 1000
      MinRange: 500
      CenterX: 0
      CenterZ: 0
      Circle: false
      IgnoreWater: true
      IgnoreLava: true
      ignorePowderSnow: true
      minY: 0
      maxY: 256
  # How long force player to wait before using command again.
  Cooldown: 5
  # How many times to try find correct location for teleportation.
  # Keep it at low number, as player always can try again after delay
  MaxTries: 20
  # List of biomes to exclude from random teleportation
  ExcludedBiomes:
  - Ocean
  - Deep ocean
```

## 执行前等待、冷却时间与命令费用

CMI 可以设置命令的冷却时间、执行前等待时间，以及执行命令的费用。这些设置可以在 config.yml 文件中配置。

注意，CMI 的 RT 功能有一项 Cooldown: 设置，见上方配置。

Config.yml 中有一个 WarmUps: 部分，可以在其中添加 cmi rt 命令。使用时要将该功能设为 enabled: true。

要管理 CMI 中执行命令的费用，请查看 commandCost.yml 文件。

## 重定向随机传送

可以使用 CMI 的专用命令功能修改 /rtp 命令：例如，识别玩家是否在 /lobby 或 /spawn 世界中输入 /rtp，并让玩家实际随机传送到另一个世界，也就是重定向随机传送。

目前，这种方式只适用于通过 aliaseditor 创建的自定义 /rt 或 /rtp 命令，创建方法见本页上方。

编辑自定义 /rtp 命令，在现有所有命令之前添加类似内容：

```text
ifinworld:spawn! asConsole! cmi rt [playerName] world_survival
ifinworld:lobby! asConsole! cmi rt [playerName] world_games
```

## 限制随机传送的使用次数

有些服主希望玩家只能使用一次或几次 /rtp 命令。下面的示例展示了一种实现方式。

目前，这种方式只适用于通过 aliaseditor 创建的自定义 /rt 或 /rtp 命令，创建方法见本页上方。

编辑自定义 /rtp 命令，将其调整为：

```text
perm:cmi.onetimertp! msg! [playerName] Sorry, you could only use /rtp once.
perm:cmi.onetimertp@! asConsole! cmi rt [playerName] %cmi_player_world%
perm:cmi.onetimertp@! asConsole! lp user [playerName] permission set cmi.onetimertp true
```

如果要将 /rtp 的使用次数限制为 3 次或 5 次，可能需要调整命令，读取并设置或递增 /cmi usermeta 中的数据。
[需要补充更多信息] [需要为 usermeta 创建别名并进行测试]

## 命令、权限与占位符

**命令：**（传送相关命令列表见[此处](https://www.zrips.net/cmi/commands/)）

```text
> cmi checkcommand rt
 --------------------------------------------------
/cmi setrt (worldName) (center:[x]:[z]) (min:[range]) (max:[range]) (square/circle) (enabled/disabled)
/cmi rt (playerName) (worldName) (-s)
>
```

**权限：**

```text
> cmi checkperm rt
 --------------------------------------------------
 cmi.command.rt - Teleports to random location
 cmi.safeteleport.bypass.[lava/void/suffocation/unknown/plugin/unsafeteleportation/noperm] - Allows to teleport into unsafe location without confirmation
 cmi.command.setrt - Set random teleport bounds
 cmi.teleport.with.[entitytype] - Allows teleportation with defined mount
 cmi.command.tpbypass - Bypass teleportation to unsafe location
 cmi.warmupbypass.[commandname] - Allows to bypass particular CMI command warmup
 cmi.randomteleport.cooldownbypass - Allows to bypass random teleport cooldown
 cmi.teleport.bypassblacklist - Allows to bypass protection from teleporting with blacklisted items
 cmi.command.rt.others - Teleports to random location
 cmi.chorusteleport - Allows to use chorus to teleport around
 cmi.safeteleport - Prevents teleportation to unsafe locations
>
```

**占位符：**（没有 RT 专用占位符，但下面这些也很实用）

```text
%cmi_user_backloc%
%cmi_player_world%
%cmi_player_x%
%cmi_player_y%
%cmi_player_z%
%cmi_player_biome%
```
