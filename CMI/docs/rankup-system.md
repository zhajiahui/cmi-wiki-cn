---
title: 自动晋级
---

# 自动晋级

打开服务器主目录中的 **spigot.yml**，确认禁止保存统计数据的选项已设为 false，即 **stats->disable-saving: false**。  
玩家会根据拥有的 **cmi.rank.[rankName]** 权限，获得对应的默认等级组。

未启用的等级会被忽略。

可用的等级命令见[此处](commands.md)。

## 基础选项

**DisplayName** 为可选项，用于设置等级在游戏中的显示名称。它不决定所需权限节点；晋升到该等级时，仍需使用该等级的节点名称。

**DefaultRank** 决定玩家尚未拥有等级时，是否可以被分配到该等级。可以设置多个默认等级；需要分配等级时，会根据玩家的权限，将第一个符合条件的等级分配给玩家。

**AutoRankup** 决定玩家满足条件后，是否自动晋升到该等级。如果有多个符合条件的晋升选项，玩家必须确认要晋升到哪个等级。

**RankupConfirmation** 决定此次晋升是否需要额外确认，可以避免意外晋升。注意，启用此项后，即使只有一个符合条件的晋升选项，**autorankup** 在晋升到该等级时也会要求确认。

**NextRanks** 是从当前等级可以晋升到的后续等级列表，可以只有一个，也可以有几十个。每个等级的要求都会在聊天栏显示，如果一次列出很多等级，消息可能会很杂乱。

**MoneyCost** 定义玩家晋升到该等级需要支付的金钱。

**ExpCost** 定义玩家晋升到该等级需要消耗的经验值。

**Votes** 定义玩家需要拥有的投票次数，取自 CMI 基于 Votifier 插件记录的投票数据。

**Commands** 是晋级时执行的命令列表，可以执行广播消息等额外操作，也可以执行其他操作。

**CommandsOnRankDown** 是降级时执行的命令列表，在玩家**从这个等级**降级时执行。

## **StatsRequirements**

**StatsRequirements** 是主要的要求配置部分，可以填写多种不同的值。  
一般格式为 `[mainStat]( : optionalSubStat):amount`。  
例如，**MonsterKills:100** 要求玩家击杀 100 只怪物，**MonsterKills:Zombie:100** 则要求击杀 **100 只僵尸**。需要时可以同时使用这两项。

可用的要求及简要说明如下：

距离，单位为方块：

- **Travel** — 总移动距离
- **Walk** — 步行距离
- **Sneak** — 潜行距离
- **Sprint** — 疾跑距离
- **Swim** — 游泳距离
- **Fall** — 下落距离
- **Climb** — 攀爬距离
- **Fly** — 飞行距离
- **WalkUnderWater** — 水下行走距离
- **WalkOnWater** — 水面行走距离
- **MinecartTravel** — 乘坐矿车的距离
- **BoatTravel** — 乘船距离
- **PigTravel** — 骑猪的距离
- **HorseTravel** — 骑马的距离
- **ElytraTravel** — 使用鞘翅飞行的距离
- **GhastTravel** — 乘坐恶魂的距离
- **NautilusTravel** — 乘坐鹦鹉螺的距离
- **Strider travel** — 乘坐炽足兽的距离

时间，单位为秒：

- **PlayTime** — 累计在线时长
- **AccountAge** — 自玩家首次登录服务器以来经过的时间
- **FromLastDeath** — 自上次死亡以来经过的时间
- **SneakTime** — 潜行时长
- **TotalWorldTime**

数值与次数：

- **GameQuit** — 玩家退出游戏的次数
- **Jump** — 跳跃次数
- **DamageDealt** — 造成的总伤害
- **DamageTaken** — 受到的总伤害
- **Deaths** — 死亡次数
- **MobKills** — 玩家击杀的生物总数
- **PlayerKills** — 击杀玩家的总数，不计间接击杀
- **ItemEnchanted** — 附魔的物品数量
- **AnimalsBred** — 繁殖动物的数量
- **FishCaught** — 钓到的鱼的数量
- **TalkedToVillager** — 与村民交谈的次数
- **TradedWithVillager** — 与村民交易的次数
- **CakeSlicesEaten** — 吃掉的蛋糕片数
- **CauldronFilled** — 装满炼药锅的次数
- **CouldronUsed** — 使用炼药锅的次数
- **ArmorCleaned** — 清洗盔甲的次数（皮革盔甲）
- **BannerCleaned** — 清洗旗帜的次数
- **BrewingstandInteractions** — 与酿造台交互的次数
- **BeaconInteractions** — 与信标交互的次数
- **CraftingTableInteractions** — 与工作台交互的次数
- **FurnaceInteractions** — 与熔炉交互的次数
- **DispenserInspected** — 查看发射器的次数
- **DropperInspected** — 查看投掷器的次数
- **HopperInspected** — 查看漏斗的次数
- **ChestOpen** — 打开箱子的次数
- **TrappedChestTriggered** — 触发陷阱箱的次数
- **EnderchestOpened** — 打开末影箱的次数
- **NoteblockPlayed** — 播放音符盒的次数
- **NoteblockTuned** — 调整音符盒音调的次数
- **FlowerPotted** — 在花盆中种花的次数
- **RecordPlayed** — 播放唱片的次数
- **SleeptInBed** — 上床睡觉的次数
- **ShulkerBoxOpened** — 打开潜影盒的次数
- **ShulkerBoxCleaned** — 清洗潜影盒的次数
- **ItemDropped** — 丢出的物品数量；未指定具体物品时，使用总数
- **ItemPickups** — 拾取的物品数量；未指定具体物品时，使用总数
- **BlocksMined** — 挖掘的方块数量；未指定具体方块时，使用总数
- **ItemBreaks** — 损坏的物品数量；未指定具体物品时，使用总数
- **ItemCrafts** — 合成的物品数量；未指定具体物品时，使用总数
- **ItemsUsed** — 物品使用次数，例如用镐挖掘；未指定具体物品时，使用总数
- **MonsterKills** — 击杀怪物的数量；未指定具体怪物时，使用总数
- **KilledBy** — 被怪物杀死的次数；未指定具体怪物时，使用总数
- **InteractionWithBlastFurnace**
- **InteractionWithSmoker**
- **InteractionWithLectern**
- **InteractionWithCampfire**
- **InteractionWithCartographyTable**
- **InteractionWithLoom**
- **InteractionWithStonecutter**
- **InteractionWithAnvil**
- **InteractionWithGrindstone**
- **InteractionWithSmithingTable**
- **BellRing**
- **RaidTrigger**
- **RaidWin**
- **TargetHit**
- **OpenBarrel**
- **DropCount**

```text
  StatsRequirements:
  - "PlayTime:3600"
  - "travel:1000"
  - "MonsterKills:zombie:10"
  - "MonsterKills:slime:5"
  - "MonsterKills:wolf:5"
  - "AccountAge:1209600"
```

## ItemRequirement

玩家背包中必须拥有的物品列表，格式为物品材质后接数量。

```text
  ItemRequirement:
  - "stone:10"
  - "stone:1:20"
  - "book:20"
```

## JobsRequirement

玩家必须从事的职业及其最低等级列表。还可以使用 **totallevel**，要求玩家所有当前职业的等级总和达到指定数值。

```text
  JobsRequirement:
  - "miner:10"
  - "totallevel:20"
```

## McMMORequirement

mcMMO 技能及其最低等级列表。还可以使用 **power**，要求技能总等级达到指定数值。

```text
  McMMORequirement:
  - "woodcutting:10"
  - "power:20"
```

## PermissionRequirement

权限要求列表。每项需要填写实际权限节点，后接一个简短的显示名称，用于在游戏中显示等级信息。

```text
  PermissionRequirement:
  - "cmi.command.fly:Fly"
```

## PlaceholderRequirements

占位符要求列表，可以检查数值型或文本型占位符。对于数值型占位符，使用 **>=** 或 **==**，分别检查是否大于等于指定值，或是否与指定值完全相等。对于文本型占位符，始终使用 **==** 检查是否完全匹配，但不区分大小写。每项还需要包含一段简短描述，用作游戏内等级信息中的显示名称。

```text
  PlaceholderRequirements:
  - '%cmi_user_level%>=10;Get to level 10'
  - '%cmi_user_homeamount%>=3;Get 3 homes'
  - '%cmi_user_weather%==rainy;We like rain'
```

## 默认文件示例

```text
Newbie:
  Enabled: true
  DisplayName: "&2Newbie"
  DefaultRank: true
  AutoRankup: true
  NextRanks:
  - Branch1
  - Branch2
Branch1:
  Enabled: true
  DisplayName: "&2Branch1"
  AutoRankup: true
  RankupConfirmation: true
  Votes: 5
  PermissionRequirement:
  - "cmi.command.fly:Fly"
  McMMORequirement:
  - "woodcutting:10"
  - "power:20"
  JobsRequirement:
  - "miner:10"
  - "totallevel:20"
  ItemRequirement:
  - "stone:10"
  - "stone:1:20"
  - "book:20"
  NextRanks:
  - Branch1Rank1
  MoneyCost: 100
  Commands:
  - "broadcast! &6[playerDisplayName] &eleveled up to Branch1 rank!"
  StatsRequirements:
  - "PlayTime:3600"
  - "travel:1000"
  - "MonsterKills:zombie:10"
  - "MonsterKills:slime:5"
  - "MonsterKills:wolf:5"
  - "AccountAge:1209600"
  PlaceholderRequirements:
  - '%cmi_user_level%>=10;Get to level 10'
  - '%cmi_user_homeamount%>=3;Get 3 homes'
  - '%cmi_user_weather%==rainy;We like rain'
Branch1Rank1:
  Enabled: true
  DisplayName: "&2Branch1Rank1"
  DefaultRank: false
  AutoRankup: true
  RankupConfirmation: false
  PermissionRequirement:
  - "cmi.command.heal:Heal"
  NextRanks:
  - Last
  MoneyCost: 300
  ExpCost: 350
  Commands:
  - "broadcast! &6[playerDisplayName] &eleveled up to Branch1Rank1 rank!"
  StatsRequirements:
  - "travel:10000"
  - "blocksmined:3000"
  - "blocksmined:diamond_ore:30"
  - "MonsterKills:1000"
  - "AccountAge:1209600"
  McMMORequirement:
  - "taming:10"
  - "unarmed:30"
Branch2:
  Enabled: true
  DisplayName: "&2Branch2"
  AutoRankup: true
  RankupConfirmation: true
  MoneyCost: 150
  NextRanks:
  - Branch2Rank1
  Commands:
  - "broadcast! &6[playerDisplayName] &eleveled up to Branch2 rank!"
  PermissionRequirement:
  - "cmi.command.tp:Teleport"
  StatsRequirements:
  - "PlayTime:3600"
  - "travel:2000"
  - "MonsterKills:zombie:15"
  - "MonsterKills:slime:10"
Branch2Rank1:
  Enabled: true
  DisplayName: "&2Branch2Rank1"
  AutoRankup: true
  RankupConfirmation: false
  MoneyCost: 100
  ExpCost: 150
  NextRanks:
  - Branch2Rank2
  Commands:
  - "broadcast! &6[playerDisplayName] &eleveled up to Branch1Rank1 rank!"
  StatsRequirements:
  - "PlayTime:4600"
  - "Swim:1000"
  - "SneakTime:180"
  - "MonsterKills:100"
Branch2Rank2:
  Enabled: true
  DisplayName: "&2Branch2Rank2"
  AutoRankup: true
  RankupConfirmation: false
  MoneyCost: 100
  ExpCost: 150
  NextRanks:
  - Last
  Commands:
  - "broadcast! &6[playerDisplayName] &eleveled up to Branch2Rank2 rank!"
  StatsRequirements:
  - "walk:15000"
  - "HorseTravel:1000"
  - "ItemsUsed:10000"
  - "PlayerKills:10"
Last:
  Enabled: true
  DisplayName: "&2Last"
  AutoRankup: true
  StatsRequirements:
  - "PlayTime:21600"
  - "walk:30000"
  - "MonsterKills:1000"
  - "blocksmined:30000"
  Commands:
  - "broadcast! &6[playerDisplayName] &eleveled up to Last rank!"
  - "cmi heal [playerName]"
  - "money give [playerName] 100"
```

---

[查看原文](https://www.zrips.net/cmi/rankup-system/)
