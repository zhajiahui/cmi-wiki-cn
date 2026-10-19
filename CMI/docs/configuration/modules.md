---
title: 功能模块（Modules.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/Modules.yml
---

# 功能模块（Modules.yml）

文件：`plugins/CMI/Settings/Modules.yml`

## `silentChest` { #silentchest }

```yaml title="Modules.yml · silentChest"
# 可关闭不使用的模块，以节省服务器资源
# 这会完全关闭相应功能
# 需要完整重启服务器才生效
# 部分模块关闭时也会禁用对应命令，例如 cuffed 禁用 cuff，silentChest 禁用 silentChest
# 被禁用的命令不出现在 Tab 补全中，执行时提示命令不存在

#
# 静默打开箱子
# 适用于 1.7.x 及以上服务器
silentChest: true
```

## `versionCheck` { #versioncheck }

```yaml title="Modules.yml · versionCheck"
#
# 玩家登录时检查版本
# 适用于 1.7.x 及以上服务器
versionCheck: true
```

## `worldLimits` { #worldlimits }

```yaml title="Modules.yml · worldLimits"
#
# 世界限制：飞行、游戏模式和上帝模式
# 适用于 1.7.x 及以上服务器
worldLimits: true
```

## `worldLimitsElytra` { #worldlimitselytra }

```yaml title="Modules.yml · worldLimitsElytra"
#
# 世界限制：鞘翅飞行
# 适用于 1.9.x 及以上服务器
worldLimitsElytra: true
```

## `customMessages` { #custommessages }

```yaml title="Modules.yml · customMessages"
#
# 加入、退出和死亡消息
# 适用于 1.7.x 及以上服务器
customMessages: true
```

## `firstJoinMessages` { #firstjoinmessages }

```yaml title="Modules.yml · firstJoinMessages"
#
# 首次加入消息
# 适用于 1.7.x 及以上服务器
firstJoinMessages: true
```

## `cuffed` { #cuffed }

```yaml title="Modules.yml · cuffed"
#
# 被铐玩家的行为处理
# 适用于 1.7.x 及以上服务器
cuffed: true
```

## `elevator` { #elevator }

```yaml title="Modules.yml · elevator"
#
# 电梯处理
# 适用于 1.7.x 及以上服务器
elevator: true
```

## `nightSpeedup` { #nightspeedup }

```yaml title="Modules.yml · nightSpeedup"
#
# 玩家睡觉时加速夜晚
# 适用于 1.7.x 及以上服务器
nightSpeedup: true
```

## `damageControl` { #damagecontrol }

```yaml title="Modules.yml · damageControl"
#
# 伤害控制
# 适用于 1.7.x 及以上服务器
damageControl: true
```

## `portalCreation` { #portalcreation }

```yaml title="Modules.yml · portalCreation"
#
# 传送门创建
# 适用于 1.7.x 及以上服务器
portalCreation: true
```

## `teleportWith` { #teleportwith }

```yaml title="Modules.yml · teleportWith"
#
# 传送门创建
# 适用于 1.7.x 及以上服务器
teleportWith: true
```

## `durabilityLoss` { #durabilityloss }

```yaml title="Modules.yml · durabilityLoss"
#
# 物品耐久度过低的提示
# 适用于 1.7.x 及以上服务器
durabilityLoss: true
```

## `mirror` { #mirror }

```yaml title="Modules.yml · mirror"
#
# 镜像功能，监听方块放置和破坏
# 适用于 1.7.x 及以上服务器
mirror: true
```

## `spawners` { #spawners }

```yaml title="Modules.yml · spawners"
#
# 刷怪笼掉落、放置和刷怪蛋交互等处理
# 适用于 1.7.x 及以上服务器
spawners: true
```

## `spawnerProximity` { #spawnerproximity }

```yaml title="Modules.yml · spawnerProximity"
#
# 检查刷怪笼放置间距
# 适用于 1.7.x 及以上服务器
spawnerProximity: true
```

## `spawnerCharge` { #spawnercharge }

```yaml title="Modules.yml · spawnerCharge"
#
# 检查刷怪笼挖掘次数
# 适用于 1.7.x 及以上服务器
spawnerCharge: true
```

## `warmup` { #warmup }

```yaml title="Modules.yml · warmup"
#
# 命令预热
# 适用于 1.7.x 及以上服务器
warmup: true
```

## `cooldown` { #cooldown }

```yaml title="Modules.yml · cooldown"
#
# 命令冷却
# 适用于 1.7.x 及以上服务器
cooldown: true
```

## `interactiveCommands` { #interactivecommands }

```yaml title="Modules.yml · interactiveCommands"
#
# 交互指令
# 适用于 1.8.x 及以上服务器
interactiveCommands: true
```

## `attachedCommands` { #attachedcommands }

```yaml title="Modules.yml · attachedCommands"
#
# 物品附加指令
# 适用于 1.8.x 及以上服务器
attachedCommands: true
```

## `armorEffects` { #armoreffects }

```yaml title="Modules.yml · armorEffects"
#
# 盔甲效果
# 适用于 1.7.x 及以上服务器
armorEffects: true
```

## `playerChatTag` { #playerchattag }

```yaml title="Modules.yml · playerChatTag"
#
# 聊天中的玩家提及，以及 @ 的 Tab 补全
# 适用于 1.7.x 至 1.14.x 服务器
playerChatTag: true
```

## `chatBubble` { #chatbubble }

```yaml title="Modules.yml · chatBubble"
#
# 聊天气泡
# 适用于 1.20.x 及以上服务器
chatBubble: true
```

## `tablist` { #tablist }

```yaml title="Modules.yml · tablist"
#
# Tab 列表
# 适用于 1.7.x 及以上服务器
tablist: false
```

## `paintingEditor` { #paintingeditor }

```yaml title="Modules.yml · paintingEditor"
#
# 潜行右键编辑画
# 适用于 1.7.x 及以上服务器
paintingEditor: true
```

## `vanish` { #vanish }

```yaml title="Modules.yml · vanish"
#
# 玩家隐身模式
# 适用于 1.21.x 及以上服务器
vanish: true
```

## `moneyCheque` { #moneycheque }

```yaml title="Modules.yml · moneyCheque"
#
# 金额支票
# 适用于 1.7.x 及以上服务器
moneyCheque: true
```

## `armorstand` { #armorstand }

```yaml title="Modules.yml · armorstand"
#
# 盔甲架编辑器
# 适用于 1.8.x 及以上服务器
armorstand: true
```

## `cmiPlaytime` { #cmiplaytime }

```yaml title="Modules.yml · cmiPlaytime"
#
# CMI 独立在线时长记录
# 适用于 1.7.x 及以上服务器
cmiPlaytime: true
```

## `holograms` { #holograms }

```yaml title="Modules.yml · holograms"
#
# 全息图更新
# 适用于 1.7.x 及以上服务器
holograms: true
```

## `portals` { #portals }

```yaml title="Modules.yml · portals"
#
# 传送区域
# 适用于 1.7.x 及以上服务器
portals: true
```

## `homeInteractions` { #homeinteractions }

```yaml title="Modules.yml · homeInteractions"
#
# 家与床的交互和床破坏事件。关闭后，家功能仍可使用
# 适用于 1.7.x 及以上服务器
homeInteractions: true
```

## `dynamicSigns` { #dynamicsigns }

```yaml title="Modules.yml · dynamicSigns"
#
# 动态告示牌
# 适用于 1.7.x 及以上服务器
dynamicSigns: true
```

## `signEdit` { #signedit }

```yaml title="Modules.yml · signEdit"
#
# 告示牌编辑
# 适用于 1.20.x 及以上服务器
signEdit: true
```

## `coloredArmor` { #coloredarmor }

```yaml title="Modules.yml · coloredArmor"
#
# 动态颜色皮革盔甲
# 适用于 1.7.x 及以上服务器
coloredArmor: true
```

## `noTarget` { #notarget }

```yaml title="Modules.yml · noTarget"
#
# 阻止实体选中玩家为目标，/cmi notarget
# 适用于 1.7.x 及以上服务器
noTarget: true
```

## `ranks` { #ranks }

```yaml title="Modules.yml · ranks"
#
# 晋级系统
# 适用于 1.7.x 及以上服务器
ranks: true
```

## `votifier` { #votifier }

```yaml title="Modules.yml · votifier"
#
# Votifier 投票系统
# 适用于 1.7.x 及以上服务器
votifier: true
```

## `playerCombat` { #playercombat }

```yaml title="Modules.yml · playerCombat"
#
# 玩家战斗系统
# 适用于 1.7.x 及以上服务器
playerCombat: true
```

## `headDrop` { #headdrop }

```yaml title="Modules.yml · headDrop"
#
# 头颅掉落系统
# 适用于 1.16.x 及以上服务器
headDrop: true
```

## `kits` { #kits }

```yaml title="Modules.yml · kits"
#
# 礼包事件监听，主要用于发放新手礼包
# 适用于 1.7.x 及以上服务器
kits: true
```

## `schedule` { #schedule }

```yaml title="Modules.yml · schedule"
#
# 定时任务系统
# 适用于 1.7.x 及以上服务器
schedule: true
```

## `namePlates` { #nameplates }

```yaml title="Modules.yml · namePlates"
#
# 玩家名称标签
# 适用于 1.7.x 及以上服务器
namePlates: true
```

## `jail` { #jail }

```yaml title="Modules.yml · jail"
#
# 监狱系统
# 适用于 1.7.x 及以上服务器
jail: true
```

## `flightCharge` { #flightcharge }

```yaml title="Modules.yml · flightCharge"
#
# CMI 飞行能量系统
# 适用于 1.7.x 及以上服务器
flightCharge: true
```

## `shulkerBackpack` { #shulkerbackpack }

```yaml title="Modules.yml · shulkerBackpack"
#
# 将潜影盒用作背包
# 适用于 1.11.x 及以上服务器
shulkerBackpack: true
```

## `decoratedpot` { #decoratedpot }

```yaml title="Modules.yml · decoratedpot"
#
# 显示饰纹陶罐内容
# 适用于 1.20.x 及以上服务器
decoratedpot: true
```

## `skin` { #skin }

```yaml title="Modules.yml · skin"
#
# 玩家皮肤
# 适用于 1.8.x 及以上服务器
skin: true
```

## `selection` { #selection }

```yaml title="Modules.yml · selection"
#
# 选区处理。关闭后，选择命令仍可使用
# 适用于 1.7.x 及以上服务器
selection: true
```

## `hpBossBar` { #hpbossbar }

```yaml title="Modules.yml · hpBossBar"
#
# 通过 Boss 栏显示生物和玩家生命值
# 适用于 1.9.x 及以上服务器
hpBossBar: true
```

## `afk` { #afk }

```yaml title="Modules.yml · afk"
#
# AFK 功能。关闭后停止全部相关检查，玩家不会再进入 AFK 状态
# 适用于 1.9.x 及以上服务器
afk: true
```

## `timedCommands` { #timedcommands }

```yaml title="Modules.yml · timedCommands"
#
# tfly、tgod 等限时命令
# 适用于 1.7.x 及以上服务器
timedCommands: true
```

## `eventCommands` { #eventcommands }

```yaml title="Modules.yml · eventCommands"
#
# eventCommands.yml 功能
# 适用于 1.12.x 及以上服务器
eventCommands: true
```

## `disabledEnchants` { #disabledenchants }

```yaml title="Modules.yml · disabledEnchants"
#
# 物品栏中的禁用附魔处理
# 适用于 1.7.x 及以上服务器
disabledEnchants: true
```

## `sitAnimation` { #sitanimation }

```yaml title="Modules.yml · sitAnimation"
#
# 坐在方块上
# 适用于 1.8.x 及以上服务器
sitAnimation: true
```

## `rideAnimation` { #rideanimation }

```yaml title="Modules.yml · rideAnimation"
#
# 骑乘时的窒息检测
# 适用于 1.7.x 及以上服务器
rideAnimation: true
```

## `bossBarCompass` { #bossbarcompass }

```yaml title="Modules.yml · bossBarCompass"
#
# Boss 栏指南针
# 适用于 1.9.x 及以上服务器
bossBarCompass: true
```

## `elytraBoost` { #elytraboost }

```yaml title="Modules.yml · elytraBoost"
#
# 鞘翅加速
# 适用于 1.9.x 及以上服务器
elytraBoost: true
```

## `elytraLaunch` { #elytralaunch }

```yaml title="Modules.yml · elytraLaunch"
#
# 鞘翅起飞
# 适用于 1.9.x 及以上服务器
elytraLaunch: true
```

## `elytraExploit` { #elytraexploit }

```yaml title="Modules.yml · elytraExploit"
#
# 防止利用三叉戟无限飞行、用箭伤害自身加速等行为
# 适用于 1.15.x 及以上服务器
elytraExploit: true
```

## `totemBehavior` { #totembehavior }

```yaml title="Modules.yml · totemBehavior"
#
# 自定义不死图腾行为
# 适用于 1.11.x 及以上服务器
totemBehavior: true
```

## `anvilColor` { #anvilcolor }

```yaml title="Modules.yml · anvilColor"
#
# 铁砧物品名称着色
# 适用于 1.9.x 及以上服务器
anvilColor: true
```

## `anvilRename` { #anvilrename }

```yaml title="Modules.yml · anvilRename"
#
# 铁砧物品改名
# 适用于 1.9.x 及以上服务器
anvilRename: true
```

## `launchPad` { #launchpad }

```yaml title="Modules.yml · launchPad"
#
# launch 命令的摔落伤害处理
# 适用于 1.9.x 及以上服务器
launchPad: true
```

## `deathMessages` { #deathmessages }

```yaml title="Modules.yml · deathMessages"
#
# 自定义死亡消息
# 适用于 1.7.x 及以上服务器
deathMessages: true
```

## `serverLinks` { #serverlinks }

```yaml title="Modules.yml · serverLinks"
#
# 服务器链接
# 适用于 1.7.x 及以上服务器
serverLinks: true
```

## `hat` { #hat }

```yaml title="Modules.yml · hat"
#
# 帽子功能
# 适用于 1.7.x 及以上服务器
hat: true
```

## `dialogs` { #dialogs }

```yaml title="Modules.yml · dialogs"
#
# 部分对话框界面处理
# 适用于 1.21.x 及以上服务器
dialogs: true
```

## `speedtracking` { #speedtracking }

```yaml title="Modules.yml · speedtracking"
#
# 速度记录
# 适用于 1.9.x 及以上服务器
speedtracking: true
```

## `viewdistance` { #viewdistance }

```yaml title="Modules.yml · viewdistance"
#
# 视距监听
# 适用于 1.20.x 及以上服务器
viewdistance: true
```
