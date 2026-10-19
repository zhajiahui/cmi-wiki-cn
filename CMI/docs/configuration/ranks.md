---
title: 自动晋级（Ranks.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/Ranks.yml
---

# 自动晋级（Ranks.yml）

文件：`plugins/CMI/Settings/Ranks.yml`

## `Newbie` { #newbie }

```yaml title="Ranks.yml · Newbie"
# 检查服务器根目录的 spigot.yml，确认未关闭统计保存，即 stats->disable-saving: false
# 按 cmi.rank.[groupName] 权限给玩家分配默认等级组
# 未启用的等级会被忽略
# DisplayName 为可选显示名称，只用于游戏内显示；不会改变权限节点，晋级仍使用节点名称
# DefaultRank 决定玩家无等级时能否分配到此等级。可设置多个默认等级，按权限分配第一个符合条件的等级
# PermissionRequirement 是晋级所需权限列表。可在节点后用 : 添加显示名称，供 /cmi rankinfo 显示，例如 cmi.command.fly:Fly
# McMMORequirement 是晋级所需的 McMMO 技能与等级
# AureliumRequirement 是晋级所需的 Aurelium 技能与等级
# AuraSkillsRequirement 是晋级所需的 Aura 技能与等级
# McMMO 和 Aurelium 中，可用技能名称 Power 表示全部技能等级总和
# JobsRequirement 是晋级所需的职业及等级
# ItemRequirement 是晋级所需物品，成功晋级后从玩家物品栏扣除
# AutoRankup 决定满足条件时是否自动晋级。若有多个可选等级，玩家仍需确认要晋升到哪一个
# RankupConfirmation 增加一次确认，避免误晋级。开启后，即使只有一个有效选项，自动晋级也需要确认
# NextRanks 为当前等级的后续等级列表，可有一个或多个。各等级要求都会显示在聊天中，数量过多可能刷屏
# MoneyCost：晋级所需金钱
# ExpCost：晋级所需经验
# Votes：晋级所需投票数
# Commands：晋级时执行的命令，可用于广播或其他操作
# 主要要求位于 StatsRequirements，可填写多种统计值：
#   通常格式为 [mainStat](:optionalSubStat):amount
#   也可组合多个子项，但 mainStat 必须相同，格式为 [mainStat](:optionalSubStat)(;SecondaryOptionalSubStat):amount
#   例如 MonsterKills:100 要求击杀 100 只怪物，MonsterKills:Zombie:100 要求击杀 100 只僵尸，需要时可同时使用
#     可用要求及基本说明：
#       距离，单位为方块：
#         Travel - 总移动距离
#         Walk - 步行距离
#         Sneak - 潜行距离
#         Sprint - 疾跑距离
#         Swim - 游泳距离
#         Fall - 下落距离
#         Climb - 攀爬距离
#         Fly - 飞行距离
#         Dive - 水下游泳距离
#         WalkOn Water - 水面行走距离
#         WalkUnderWater - 水下行走距离
#         MinecartTravel - 矿车行驶距离
#         BoatTravel - 乘船距离
#         PigTravel - 骑猪距离
#         HorseTravel - 骑马距离
#         ElytraTravel - 鞘翅飞行距离
#         GhastTravel - 乘坐恶魂的距离
#         StriderTravel - 乘坐炽足兽的距离
#       时间，单位为秒：
#         PlayTime - 总在线时长
#         FromLastDeath - 距离上次死亡的时间
#         SneakTime - 潜行时间
#         TotalWorldTime - 世界总时间
#       数量或次数：
#         LeaveGame - 退出游戏次数
#         Jump - 跳跃次数
#         DamageDealt - 造成的总伤害
#         DamageTaken - 受到的总伤害
#         DamageDealtAbsorbed - 总伤害吸收量
#         DamageDealtResisted - 总伤害抵抗量
#         DamageBlockedByShield - 盾牌格挡的总伤害
#         DamageAbsorbed - 总伤害吸收量
#         DamageResisted - 总伤害抵抗量
#         Deaths - 死亡次数
#         KilledBy - 被怪物击杀次数；不指定怪物时，使用总次数
#         MobKills - 玩家击杀生物总数
#         PlayerKills - 玩家击杀其他玩家的总数，不含间接击杀
#         ItemEnchanted - 附魔物品数量
#         AnimalsBred - 繁殖动物数量
#         FishCaught - 钓鱼数量
#         TalkedToVillager - 与村民交谈次数
#         TradedWithVillager - 与村民交易次数
#         CakeSlicesEaten - 吃掉的蛋糕片数
#         CauldronFilled - 炼药锅装填次数
#         CouldronUsed - 炼药锅使用次数
#         ArmorCleaned - 清洗皮革盔甲次数
#         BannerCleaned - 清洗旗帜次数
#         BrewingStandInteraction - 与酿造台交互次数
#         BeaconInteraction - 与信标交互次数
#         CraftingTableInteraction - 与工作台交互次数
#         FurnaceInteraction - 与熔炉交互次数
#         DispenserInspected - 查看发射器次数
#         DropperInspected - 查看投掷器次数
#         HopperInspected - 查看漏斗次数
#         ChestOpened - 打开箱子次数
#         TrappedChestTriggered - 触发陷阱箱次数
#         EnderchestOpened - 打开末影箱次数
#         NoteblockPlayed - 播放音符盒次数
#         NoteblockTuned - 调整音符盒音调次数
#         FlowerPotted - 花盆种植次数
#         RecordPlayed - 播放唱片次数
#         SleeptInBed - 上床睡觉次数
#         ShulkerBoxOpened - 打开潜影盒次数
#         CleanShulkerBox - 清洗潜影盒次数
#         Drop - 丢弃物品数量，不指定物品时使用总数
#         MineBlock - 挖掘方块数量，不指定方块时使用总数
#         PlaceBlock - 放置方块数量，不指定方块时使用总数
#         BreakItem - 损坏物品数量，不指定物品时使用总数
#         CraftItem - 合成物品数量，不指定物品时使用总数
#         UseItem - 使用物品次数，例如用镐挖掘；不指定物品时使用总数
#         Pickup - 拾取物品数量，不指定物品时使用总数
#         KillEntity - 击杀怪物数量，不指定怪物时使用总数
#         InteractWithBlastFurnace - 与高炉交互次数
#         InteractWithSmoker - 与烟熏炉交互次数
#         InteractWithLectern - 与讲台交互次数
#         InteractWithCampfire - 与营火交互次数
#         InteractWithCartographyTable - 与制图台交互次数
#         InteractWithLoom - 与织布机交互次数
#         InteractWithStonecutter - 与切石机交互次数
#         InteractWithAnvil - 与铁砧交互次数
#         InteractWithGrindstone - 与砂轮交互次数
#         InteractWithSmithingTable - 与锻造台交互次数
#         BellRing - 与钟交互次数
#         RaidTrigger - 触发袭击次数
#         RaidWin - 袭击胜利次数
#         TargetHit - 命中标靶次数
#         OpenBarrel - 打开木桶次数
#         DropCount - 丢弃物品次数

Newbie:
  Enabled: true
  DisplayName: "&2新手"
  DefaultRank: true
  AutoRankup: true
  NextRanks:
  - Branch1
  - Branch2
```

## `Branch1` { #branch1 }

```yaml title="Ranks.yml · Branch1"
Branch1:
  Enabled: true
  DisplayName: "&2分支1"
  AutoRankup: true
  RankupConfirmation: true
  Votes: 5
  PermissionRequirement:
  - cmi.command.fly:Fly
  McMMORequirement:
  - woodcutting:10
  - power:20
  JobsRequirement:
  - miner:10
  - totallevel:20
  AuraSkillsRequirement:
  - miner:10
  - power:20
  AureliumRequirement:
  - fishing:10
  - power:30
  ItemRequirement:
  - stone:10
  - stone:1:20
  - book:20
  NextRanks:
  - Branch1Rank1
  MoneyCost: 100
  Commands:
  - "broadcast! &6[playerDisplayName] &e晋升到了分支1等级！"
  StatsRequirements:
  - PlayTime:3600
  - travel:1000
  - MonsterKills:zombie:10
  - MonsterKills:slime:5
  - MonsterKills:wolf:5
  - AccountAge:1209600
```

## `Branch1Rank1` { #branch1rank1 }

```yaml title="Ranks.yml · Branch1Rank1"
Branch1Rank1:
  Enabled: true
  DisplayName: "&2分支1等级1"
  DefaultRank: false
  AutoRankup: true
  RankupConfirmation: false
  PermissionRequirement:
  - cmi.command.heal:Heal
  NextRanks:
  - Last
  MoneyCost: 300
  ExpCost: 350
  Commands:
  - "broadcast! &6[playerDisplayName] &e晋升到了分支1等级1！"
  StatsRequirements:
  - travel:10000
  - blocksmined:3000
  - blocksmined:diamond_ore:30
  - MonsterKills:1000
  - AccountAge:1209600
  McMMORequirement:
  - taming:10
  - unarmed:30
```

## `Branch2` { #branch2 }

```yaml title="Ranks.yml · Branch2"
Branch2:
  Enabled: true
  DisplayName: "&2分支2"
  AutoRankup: true
  RankupConfirmation: true
  MoneyCost: 150
  NextRanks:
  - Branch2Rank1
  Commands:
  - "broadcast! &6[playerDisplayName] &e晋升到了分支2等级！"
  PermissionRequirement:
  - cmi.command.tp:Teleport
  StatsRequirements:
  - PlayTime:3600
  - travel:2000
  - MonsterKills:zombie:15
  - MonsterKills:slime:10
```

## `Branch2Rank1` { #branch2rank1 }

```yaml title="Ranks.yml · Branch2Rank1"
Branch2Rank1:
  Enabled: true
  DisplayName: "&2分支2等级1"
  AutoRankup: true
  RankupConfirmation: false
  MoneyCost: 100
  ExpCost: 150
  NextRanks:
  - Branch2Rank2
  Commands:
  - "broadcast! &6[playerDisplayName] &e晋升到了分支1等级1！"
  StatsRequirements:
  - PlayTime:4600
  - Swim:1000
  - SneakTime:180
  - MonsterKills:100
```

## `Branch2Rank2` { #branch2rank2 }

```yaml title="Ranks.yml · Branch2Rank2"
Branch2Rank2:
  Enabled: true
  DisplayName: "&2分支2等级2"
  AutoRankup: true
  RankupConfirmation: false
  MoneyCost: 100
  ExpCost: 150
  NextRanks:
  - Last
  Commands:
  - "broadcast! &6[playerDisplayName] &e晋升到了分支2等级2！"
  StatsRequirements:
  - walk:15000
  - HorseTravel:1000
  - ItemsUsed:10000
  - PlayerKills:10
```

## `Last` { #last }

```yaml title="Ranks.yml · Last"
Last:
  Enabled: true
  DisplayName: "&2最终等级"
  AutoRankup: true
  StatsRequirements:
  - PlayTime:21600
  - walk:30000
  - MonsterKills:1000
  - blocksmined:30000
  Commands:
  - "broadcast! &6[playerDisplayName] &e晋升到了最终等级！"
  - cmi heal [playerName]
  - money give [playerName] 100
```
