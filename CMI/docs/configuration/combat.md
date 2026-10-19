---
title: 战斗状态（Combat.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/Combat.yml
---

# 战斗状态（Combat.yml）

文件：`plugins/CMI/Settings/Combat.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `Combat`

### `Combat.Timer`

各项功能使用的战斗判定时长

### `Combat.safeZoneDamage`

启用后，已被标记为 PvP 状态的玩家，即使进入安全区也可受伤

### `Combat.Player.DisableFlight`

设为 true，玩家进入战斗状态时关闭飞行<br>
会让玩家掉落，并阻止重新开启飞行<br>
若战斗中未禁用命令，且玩家有权执行 fly，仍可手动开启飞行<br>
可通过 cmi.pvp.PFlyBypass 绕过

### `Combat.Player.IncludeVictim`

设为 true，被攻击的玩家即使不还手，也会进入战斗状态<br>
设为 false，只将攻击者标记为 PvP 状态

### `Combat.Player.DisableFallDamage`

设为 true，因关闭飞行而落下的玩家获得一次摔落伤害豁免

### `Combat.Player.ShowBossBar`

设为 true，通过 Boss 栏显示距离战斗状态结束的时间<br>
仅影响 PvP 战斗

### `Combat.Player.ShowDamageNumbers`

启用后，攻击玩家时通过全息图显示伤害数字

### `Combat.Player.noGodDamage`

阻止上帝模式玩家造成伤害<br>
可通过 cmi.pvp.godBypass 绕过

### `Combat.Player.noGodDamageInform`

提示玩家无法在上帝模式下伤害其他玩家

### `Combat.Player.BlockCommands`

设为 true，战斗中只能执行列表中的命令<br>
仅影响 PvP 战斗

### `Combat.Player.MakeBlackList`

设为 true，AllowedCommands 改为黑名单，用于指定战斗中禁止的命令

### `Combat.Mob.DisableFlight`

设为 true，玩家进入战斗状态时关闭飞行<br>
可通过 cmi.pvp.MFlyBypass 绕过

### `Combat.Mob.IncludeVictim`

设为 true，被攻击的玩家即使不还手，也会进入战斗状态

### `Combat.Mob.DisableFallDamage`

设为 true，因关闭飞行而落下的玩家获得一次摔落伤害豁免

### `Combat.Mob.ShowBossBar`

设为 true，通过 Boss 栏显示距离战斗状态结束的时间<br>
仅影响 PvE 战斗

### `Combat.Mob.IncludeEnvironment`

启用后，环境伤害也会触发生物战斗计时<br>
包括仙人掌、岩浆块、窒息、燃烧和摔落等伤害

### `Combat.Mob.ShowDamageNumbers`

启用后，攻击生物时通过全息图显示伤害数字

### `Combat.Mob.noGodDamage`

阻止上帝模式玩家造成伤害<br>
可通过 cmi.pve.godBypass 绕过

### `Combat.Mob.noGodDamageInform`

提示玩家无法在上帝模式下伤害生物

### `Combat.Mob.BlockCommands`

设为 true，战斗中只能执行列表中的命令<br>
仅影响 PvE 战斗

### `Combat.Mob.MakeBlackList`

设为 true，AllowedCommands 改为黑名单，用于指定战斗中禁止的命令
