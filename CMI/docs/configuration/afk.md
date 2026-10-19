---
title: 暂离与闲置（Afk.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/Afk.yml
---

# 暂离与闲置（Afk.yml）

文件：`plugins/CMI/Settings/Afk.yml`

## `Afk` { #afk }

```yaml title="Afk.yml · Afk"
Afk:
  # 开启或关闭自动 AFK 系统
  Enabled: false
  # 启用后，通过标题提示玩家已进入 AFK 状态
  TitleMessage: true
  # 启用后，随机显示副标题消息
  SubTitleMessage: true
  # 防止玩家通过原地跳跃避开 AFK 判定
  PreventJumping: true
  # 防止 AFK 玩家受到伤害
  PreventDamage: true
  # 防止 AFK 玩家对生物造成伤害
  PreventMobDamage: true
  # 检查玩家 AFK 状态的间隔，单位为秒
  CheckInterval: 10
  # 设为 true，停止累计玩家在线时长
  # 受实现方式影响，查看在线时长时可能出现约 1 秒的上下波动
  StopPlayTime: false
  # 玩家停止移动多久后，标记为 AFK
  # 玩家需要 cmi.command.afk.auto 权限
  # 设为 0 关闭此限制
  AutoAfkIn: 300
  # 玩家因长时间无操作而自动进入 AFK 时执行的命令
  # 支持特殊指令
  AutoAfkCmds:
  - "cmi broadcast !&6[playerDisplayName] &e进入了暂离状态"
  # 玩家执行 /cmi afk 时执行的命令
  # 支持特殊指令
  ManualAfkCmds:
  - "cmi broadcast !&6[playerDisplayName] &e进入了暂离状态"
  LeaveCmds:
    # 玩家手动进入 AFK 后，退出 AFK 时执行的命令
    Manual:
    - "cmi broadcast !&6[playerDisplayName] &e结束了暂离状态"
    # 玩家自动进入 AFK 后，退出 AFK 时执行的命令
    Auto:
    - "cmi broadcast !&6[playerDisplayName] &e结束了暂离状态"
  AutoKickTimes:
    # 玩家停止移动多久后踢出
    # 此计时叠加在 AutoAfkIn 之后。手动进入 AFK 时，也会在 AutoAfkIn+AutoKickIn 秒后被踢出
    # 也可不踢出玩家，而是每隔 X 秒重复执行指定操作
    # 设为 -1 关闭自动踢出
    # 可通过 cmi.command.afk.kickbypass 权限绕过
    # 也可用 cmi.command.afk.kickOutIn.[seconds] 指定踢出时间，有多个值时取较大值
    Default: -1
    # 在线人数达到多少时，才开始自动踢出
    # 设为 0 时，无论在线人数多少都生效
    # 建议值：15
    FromPlayerCount: 0
    # 按在线人数设置自动踢出时间，格式为 [playerCount]-[seconds]
    # 仅在默认踢出时间大于 -1 时生效
    # 向下选择最接近当前人数的条目。例如有 30-400、40-350，当前在线 35 人时使用 400 秒
    # 进入 AFK 时选定踢出时间；AFK 期间即使在线人数变化，也不会重新计算
    # 找不到合适条目时，使用默认值
    ByPlayerCount:
    - 10-600
    - 20-500
    - 30-400
    - 40-350
    - 50-300
  # 再次执行踢出命令前的等待时间
  RepeatingAutoKickInterval: 300
  # 设为 true，每隔 RepeatingAutoKickInterval 秒重复执行踢出命令
  RepeatKickCommand: false
  # 玩家达到可踢出条件时执行的命令
  # 若玩家未被踢出，每隔 RepeatingAutoKickInterval 秒重复执行
  AutoKickCmds:
  - "cmi kick [playerName] &e你因闲置超过 [time] 被踢出服务器"
  # 这些世界中，玩家即使长时间无操作也不会自动进入 AFK
  DisabledWorlds:
  - oneTestWorld
  - secondTestWorld
  # 交互时退出 AFK
  DisableOnInteract: true
  # 防止玩家对特定物品或方块持续按住某个按键，以绕过 AFK
  SmartInteractCheck: true
  # 防止通过挂机装置持续移动来绕过 AFK
  AntiAfkMachines: true
  # 防止 AFK 玩家被拉走
  PreventHook: true
  # 实验性功能！防止 AFK 玩家被推动
  # 玩家仍可能在当前所在的同一个方块内移动
  PreventPushing: false
  # 点击物品栏时退出 AFK
  DisableOnInventoryClick: true
  # 丢弃物品时退出 AFK
  DisableOnitemDrop: true
  # 执行命令时退出 AFK
  DisableOnCommand: true
  # 发送公共聊天消息时退出 AFK
  DisableOnPublicChat: true
  # 发送私聊消息时退出 AFK
  DisableOnPrivateChat: true
  # 移动时退出 AFK
  DisableOnMove: true
  # 转动视角时退出 AFK
  DisableOnLookAround: false
  # 钓到鱼时退出 AFK
  DisableOnFishing: false
  # AFK 时禁止拾取物品
  DisableItemPickup: false
  PreventMobSpawning:
    # 启用后，可阻止在 AFK 玩家附近生成生物
    Enabled: false
    # 阻止自然生成生物
    # 可能增加服务器负载，因为服务端仍会持续尝试在 AFK 玩家附近生成怪物
    Natural: false
    # 阻止刷怪笼生成生物
    Spawners: true
    # 通常影响铁傀儡生成
    VillageDefence: true
  # AFK 时禁止拾取经验
  # 注意！由于 Minecraft 经验球的处理方式，较合适的做法是将经验球设为 0 经验后允许吸收
  # 因此启用后，AFK 玩家吸收经验球不会获得经验
  DisableExpPickup: false
  Disable:
    # 禁止潜影贝将 AFK 玩家选为目标
    ShulkerTargeting: true
```
