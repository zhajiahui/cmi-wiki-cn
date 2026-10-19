---
title: 战斗状态（Combat.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/Combat.yml
---

# 战斗状态（Combat.yml）

文件：`plugins/CMI/Settings/Combat.yml`

## `Combat` { #combat }

```yaml title="Combat.yml · Combat"
Combat:
  # 各项功能使用的战斗判定时长
  Timer: 15
  # 启用后，已被标记为 PvP 状态的玩家，即使进入安全区也可受伤
  safeZoneDamage: false
  Player:
    # 设为 true，玩家进入战斗状态时关闭飞行
    # 会让玩家掉落，并阻止重新开启飞行
    # 若战斗中未禁用命令，且玩家有权执行 fly，仍可手动开启飞行
    # 可通过 cmi.pvp.PFlyBypass 绕过
    DisableFlight: false
    # 设为 true，被攻击的玩家即使不还手，也会进入战斗状态
    # 设为 false，只将攻击者标记为 PvP 状态
    IncludeVictim: true
    # 设为 true，因关闭飞行而落下的玩家获得一次摔落伤害豁免
    DisableFallDamage: false
    # 设为 true，通过 Boss 栏显示距离战斗状态结束的时间
    # 仅影响 PvP 战斗
    ShowBossBar: false
    # 启用后，攻击玩家时通过全息图显示伤害数字
    ShowDamageNumbers: true
    DamageNumbersFormat: '&c⚔[damage]'
    # 阻止上帝模式玩家造成伤害
    # 可通过 cmi.pvp.godBypass 绕过
    noGodDamage: false
    # 提示玩家无法在上帝模式下伤害其他玩家
    noGodDamageInform: false
    # 设为 true，战斗中只能执行列表中的命令
    # 仅影响 PvP 战斗
    BlockCommands: false
    AllowedCommands:
    - cmi msg
    - cmi reply
    # 设为 true，AllowedCommands 改为黑名单，用于指定战斗中禁止的命令
    MakeBlackList: false
  Mob:
    # 设为 true，玩家进入战斗状态时关闭飞行
    # 可通过 cmi.pvp.MFlyBypass 绕过
    DisableFlight: false
    # 设为 true，被攻击的玩家即使不还手，也会进入战斗状态
    IncludeVictim: false
    # 设为 true，因关闭飞行而落下的玩家获得一次摔落伤害豁免
    DisableFallDamage: false
    # 设为 true，通过 Boss 栏显示距离战斗状态结束的时间
    # 仅影响 PvE 战斗
    ShowBossBar: false
    # 启用后，环境伤害也会触发生物战斗计时
    # 包括仙人掌、岩浆块、窒息、燃烧和摔落等伤害
    IncludeEnvironment: true
    # 启用后，攻击生物时通过全息图显示伤害数字
    ShowDamageNumbers: true
    DamageNumbersFormat: '&c❤[damage]'
    # 阻止上帝模式玩家造成伤害
    # 可通过 cmi.pve.godBypass 绕过
    noGodDamage: false
    # 提示玩家无法在上帝模式下伤害生物
    noGodDamageInform: false
    # 设为 true，战斗中只能执行列表中的命令
    # 仅影响 PvE 战斗
    BlockCommands: false
    AllowedCommands:
    - cmi msg
    - cmi reply
    # 设为 true，AllowedCommands 改为黑名单，用于指定战斗中禁止的命令
    MakeBlackList: false
```
