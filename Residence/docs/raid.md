---
title: 领地战争（Raid）
---

# 领地战争（Raid）

领地战争（Raid）默认关闭。保持关闭时，不会影响插件现有功能；开启后才会启用下面的规则。

## 基本规则

- 只有领地主人在线，且不处于战争冷却期时，才可以向其领地发起攻击。
- 防守方有一段战前准备时间，可以布置防御、赶回领地，或邀请其他人协防。其他玩家也可以申请协防，但需要领地主人确认。
- 宣布该领地进入战争时，除防守者外，领地内的所有玩家都会被踢出。
- 进攻者可以邀请其他人参战。其他玩家也可以自行加入进攻方，无需最初发起者确认。
- 战争期间，防守方无法使用容器，防止将物品转移到其他领地。
- 进攻方会获得 `move` 权限，但没有 `tp` 权限。因此，进攻者死亡后，必须从领地外重新赶回。
- 配置文件允许时，防守方可以传送进入领地。默认情况下，只有领地主人可以传送进入，其他协防玩家和进攻方一样，需要从领地边界外步行返回。
- 进攻方可以放置和破坏方块。原文计划在后续版本中限制可进行的操作和时机，以平衡玩法。
- 正式交战期间，进攻方可以打开任何容器并取走其中的物品。原文计划在后续版本中限制一次战争可打开的箱子数量，或可取走的物品数量。
- 战争结束后，除领地主人外，所有玩家都会被踢出领地，领地恢复正常状态。
- 战争后，玩家会进入冷却期。在指定时间内，其他人无法再次攻击该玩家，包括其拥有的其他领地。
- 领地本身也有独立的冷却期，可以与玩家冷却时间不同。例如，领地冷却为 7 天，玩家冷却为 24 小时，那么该玩家的另一块领地在第二天就可能遭到攻击，而刚被攻击的领地在接下来一周内仍受保护。

## 命令

### `/res attack [residenceName]`

满足条件时，向指定领地发起攻击。其他玩家对同一领地执行此命令，会作为进攻方加入战争。

### `/res defend [residenceName]`

申请加入领地防守方。请求会发送给领地主人，获得确认后才能参战。

如果由领地主人执行类似 `/res defend Zrips` 的命令，则会向玩家 Zrips 发送协防邀请，需要对方接受。

### `/res leaveraid`

退出进攻方或防守方。正在遭受攻击的领地主人无法使用此命令退出。

### `/res raid [start/stop/kick/immunity]`

供服务器管理人员控制战争。可以强制开始、停止战争，或将玩家踢出战争。

`immunity` 用于让领地在指定时间内免受攻击。它还包含 `add/take/clear/set` 等子命令，用于调整剩余免战时间。

### `/res raidstatus (playername/residence)`

显示当前战争的基本信息，包括进攻方和防守方名单。

## 配置文件

```yaml
Raid:
  # Determines if you want to enable raid feature for your server
  # When residence is under raid, attackers can move inside residence even if residence has move false flag
  Enabled: false
  # Time in seconds before raid starts
  # This will allow defenders to get back to residence and prepare for attack
  PreTimer: 120
  # Time in seconds raid should be
  # During this time attackers can steal and kill defenders
  Timer: 120
  # Time in seconds residence is immune for next raid
  # Default is 79200 seconds which results into 22 hours, this might reset if you have server restart
  Cooldown: 120
  # Time in seconds player is immune for next raid
  # In case player has more than one residence, this can prevent player from being attacked again
  # Default is 79200 seconds which results into 22 hours, this might reset if you have server restart
  PlayerCooldown: 120
  Allow:
    Attacker:
      # Allows to break blocks inside raided residence even if it has destroy false
      # This only applies for attackers and for raid time
      blockBreak: true
      # Allows to place blocks inside raided residence even if it has place false
      # This only applies for attackers and for raid time
      blockPlace: true
    Defender:
      # Allows to break blocks inside raided residence even if it has destroy false
      # This only applies for defenders and for raid time
      blockBreak: true
      # Allows to place blocks inside raided residence even if it has place false
      # This only applies for defenders and for raid time
      blockPlace: true
      # Allows to teleport into raided residence, includes /res tp and other 3rd party teleport commands
      # This only applies for defenders and for raid time
      # keep in mind that attackers will not have this option and will be prevented from teleporting inside raided residence
      Teleport: false
      # Allows to use containers, such as chests, during raid time
      # This only applies for defenders and for raid time
      # Keeping this at false might prevent from players moving their items to another residence which is not in raid
      # Attackers will have access to any container in your residence during raid
      containerUsage: false
  # When set to false players in same teams (attackers or defenders) will not cause each other damage
  FriendlyFire: true
```

---

[查看原文](https://www.zrips.net/residence/raid/)
