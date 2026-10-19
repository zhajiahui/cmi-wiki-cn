---
title: 条件
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 条件

1. [附加条件](conditions.md#additional-conditions)
2. [条件](conditions.md#conditions-2)
   1. [更多示例](conditions.md#more-examples)

## 介绍 {#introduction}

条件用于确定是否可以执行某个操作。

条件可以用于以下位置 [1]：

- [技能机制](mechanics/skill.md)
- [掉落表](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#drop-tables)
- [刷怪点](../spawners.md)
- [随机生成](../random-spawns.md)

当应用多个条件时，必须满足所有条件才能执行该技能。某些条件允许数组可以用逗号分隔。此类条件仅需要数组中的字符串之一匹配。

要了解如何使用内联条件，[点击此处！](inline-conditions.md)

## 类型 {#types}

条件可以分为四种类型：

1. 实体条件：这些检查实体的条件。
2. 位置条件：检查位置上的条件。对实体使用时，检查实体所在的位置。
3. 比较条件：这些检查两个不同“事物”之间的某些条件。例如，如果目标位于角为两个坐标的立方体内，“Cuboid”将返回   true  
4. 元条件：不一定检查施法者或目标自身的属性。例如 StringEquals 会根据两个字符串是否相同，返回   true   或   false  。字符串*可以*使用取得施法者或目标数据的占位符，但这只是其中一种用法。

## 用法 {#usage}

条件还可以用在元技能中的三个不同位置：

#### 条件 {#conditions}

此处的条件针对施法者或其所在位置检查。

```yaml
  Conditions:
  - health{h=>10}
```

> 检查施法者的生命值是否超过10

```yaml
  Conditions:
  - globalscore{objective=Test;v=>10}
```

> 在上面的示例中，全局分数条件将检查施法者的全局分数。

---

#### TargetConditions {#targetconditions}

本节中的条件根据元技能的[继承目标](metaskills.md#inheritance)进行检查

```yaml
  TargetConditions:
  - health{h=>10}
```

> 检查继承目标实体的生命值是否大于 10，只有满足条件的实体才会继续作为元技能的继承目标。默认情况下，若没有任何实体满足条件，元技能就不会执行。

```yaml
  TargetConditions:
  - globalscore{objective=Test;v=>10}
```

> 上面的全局分数条件示例将检查继承目标的全局分数。由于 globalscore 是一个实体条件，因此只有当实体成为目标时它才会起作用。

---

#### TriggerConditions {#triggerconditions}

此处的条件针对元技能的触发实体检查。

```yaml
  TriggerConditions:
  - health{h=>10}
```

> 检查元技能触发实体的生命值是否大于 10。

## 范围值 {#ranged-values}

范围值使用 **#to#** 或 **#-#** 格式。范围包含负数时，必须使用 to，不能使用 -。例如：

```yaml
YourMagnificentSkill:
  Conditions:
    - altitude{a=1-5}
  TargetConditions:
    - distance{d=1to10} true
  TriggerConditions:
    - distance{d=1to10} true
```

## 条件动作 {#condition-actions}

条件操作允许你根据条件执行其他操作。默认条件动作是**  true  **

| 操作 | 说明 |
| --- | --- |
| `true` | 满足此条件时，技能会执行。 |
| `false` | 满足此条件时，技能*不会*执行。 |
| `power` [multiplier] | 将技能威力乘以 `multiplier` 的值，例如 power 2.0 会将技能威力翻倍。 |
| `cast` [skill] | 满足条件时，额外施放一个技能，不影响原技能的执行。 |
| `castinstead` [skill] | 满足条件时，改为施放另一个技能。 |
| `orElseCast` [skill] | 不满足条件时，改为施放另一个技能。 |

```yaml
  Conditions:
  - day true
  Skills:
  - message{m="It's day!"} @self
```

> 仅当施法者的世界是白天时才会运行

```yaml
  Conditions:
  - day false
  Skills:
  - message{m="It's *not* day!"} @self
```

> 仅在施法者所在世界不是白天时运行。
> 与`true`相反的行为

```yaml
ExampleSkill:
  Conditions:
  - day true
  - sunny orElseCast OtherSkill
  Skills:
  - message{m="It's day and sunny!"} @self

OtherSkill:
  Skills:
  - message{m="It's day and not sunny!"} @self
```

> 条件行不成立时（*条件满足但条件动作为   false  ，或反之*），[不再检查后续条件](https://en.wikipedia.org/wiki/Short-circuit_evaluation)。
> 因此，即使 `sunny` 条件使 OtherSkill 执行，也可以确定 `day` 条件已经满足；否则根本不会执行任何技能，因为
> `day true`  
> 会先进行检查。
> `sunny orElseCast OtherSkill`

```yaml
YourAwesomeSkill:
  Conditions:
  - day true
  TargetConditions:
  - stance{s=defensive} power 0.5
  TriggerConditions:
  - stance{stance=defensive} power 0.5
  - score{objective=test;value=>20} false
  - haspotioneffect{type=POISON;level=>0;duration=0to100} true
```

## 复合条件 {#composite-conditions}

条件还可以用括号分组，并通过**与（AND）** (`&&`) 和**或（OR）** (`||`) 布尔运算符求值。这样使用的条件仍可以附带条件操作。

```yaml
  Conditions:
  - ((day false || raining true) && onBlock{material=LIME_CONCRETE}) true
```

> 当下雨或非白天时满足该条件，除此之外，仅当施法者位于 LIME_CONCRETE 方块上时才满足

> day 和 raining 明确声明了条件动作，onBlock 则使用默认的 `true`。

## 通用属性 {#universal-attributes}

每个条件共享并可以使用以下属性

# 附加条件 {#additional-conditions}

由附加插件添加的条件的链接。如果没有安装该插件，这些链接中的任何条件都将不起作用。

- [ModelEngine 4](https://git.mythiccraft.io/mythiccraft/model-engine-4/-/wikis/Skills/Conditions)
- [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Conditions)
- [MythicEnchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Skills/Conditions)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#conditions)

# 条件 {#conditions-2}

| 条件 | 类型 | 说明 |
| --- | --- | --- |
| [Altitude](conditions/altitude.md) | Entity | 检测目标实体距离地面的高度。 |
| [Biome](conditions/biome.md) | Location | 检测目标是否位于给定生物群系列表中的某个生物群系。 |
| [BiomeType](conditions/biometype.md) | Location | 检测某个位置的生物群系类别。 |
| [BlockType](conditions/blocktype.md) | Location | 检测目标位置的材质类型。 |
| [BlockTypeInRadius](conditions/blocktypeinradius.md) | Location | 检查目标位置周围指定半径内的指定方块数量。 |
| [Blocking](conditions/blocking.md) | Entity | 检测目标玩家是否正在使用盾牌格挡。 |
| [BoundingBoxesOverlap](conditions/boundingboxesoverlap.md) | Compare | 检查施法者的 BoundingBox 是否与目标的 BoundingBox 重叠。 |
| [BowTension](conditions/bowtension.md) | Meta | 检查实体用弓射击时的拉弓力度。 |
| [Burning](conditions/burning.md) | Entity | 目标实体是否着火。 |
| [Chance](conditions/chance.md) | Meta | 元技能的执行概率。 |
| [Charged](conditions/charged.md) | Entity | 检查目标苦力怕是否为闪电苦力怕。 |
| [Children](conditions/children.md) | Entity | 检测施法者拥有的子实体数量。 |
| [Color](conditions/color.md) | Entity | 检测实体的颜色。 |
| [CompareValues](conditions/comparevalues.md) | Meta | 根据指定运算比较两个值。 |
| [Crouching](conditions/crouching.md) | Entity | 目标实体是否正在潜行。 |
| [Cuboid](conditions/cuboid.md) | Compare | 目标是否位于 location1 x location2 所确定的长方体范围内。 |
| [DamageAmount](conditions/damageamount.md) | Meta | 检查受到的伤害是否在指定范围内。 |
| [DamageCause](conditions/damagecause.md) | Meta | 检查伤害来源的类型。 |
| [DamageTag](conditions/damagetag.md) | Meta | 检查伤害来源的标签。 |
| [Dawn](conditions/dawn.md) | Location | 时间是否为黎明，即游戏时间 22000 到 2000。 |
| [Day](conditions/day.md) | Location | 时间是否为白天，即游戏时间 2000 到 10000。 |
| [Dimension](conditions/dimension.md) | Location | 目标位置是否位于指定维度。 |
| [DirectionalVelocity](conditions/directionalvelocity.md) | Entity | 目标的速度是否与给定参数匹配。 |
| [Distance](conditions/distance.md) | Compare | 施法者与目标之间的距离是否在给定范围内。 |
| [DistanceFromLocation](conditions/distancefromlocation.md) | Entity | 目标与指定位置之间的距离是否在指定范围内。 |
| [DistanceFromPin](conditions/distancefrompin.md) | Location | 检查目标是否位于指定定位点的一定距离内。 |
| [DistanceFromSpawn](conditions/distancefromspawn.md) | Location | 世界出生点与目标之间的距离是否在给定范围内。 |
| [DistanceFromTrackedLocation](conditions/distancefromtrackedlocation.md) | Location | 追踪的位置与施法者之间的距离是否在给定范围内。 |
| [Dusk](conditions/dusk.md) | Location | 时间是否为黄昏，即游戏时间 14000 到 18000。 |
| [EnchantingExperience](conditions/enchantingexperience.md) | Entity | 检查目标玩家的经验点数。 |
| [EnchantingLevel](conditions/enchantinglevel.md) | Entity | 检查目标玩家的经验等级。 |
| [EnderDragonAlive](conditions/enderdragonalive.md) | Location | 检查目标位置所在世界中是否至少有一只存活的 EnderDragon。 |
| [EnderDragonPhase](conditions/enderdragonphase.md) | Entity | 检查末影龙是否处于指定的一个或多个阶段。 |
| [EntityItemIsSimilar](conditions/entityitemissimilar.md) | Entity | 检测目标物品实体是否与另一个物品相似。 |
| [EntityItemType](conditions/entityitemtype.md) | Entity | 检测目标物品实体的类型。 |
| [EntityMaterialType](conditions/entitymaterialtype.md) | Entity | 检测目标物品实体的材质。 |
| [EntityType](conditions/entitytype.md) | Entity | 检测目标的实体类型。 |
| [Faction](conditions/faction.md) | Entity | 检测目标的阵营。 |
| [FallSpeed](conditions/fallspeed.md) | Entity | 目标的下落速度是否在给定范围内。 |
| [FieldOfView](conditions/fieldofview.md) | Compare | 检测目标是否位于施法者朝向的给定角度范围内。 |
| [FoodLevel](conditions/foodlevel.md) | Entity | 检查目标的饥饿值是否在指定范围内。 |
| [FoodSaturation](conditions/foodsaturation.md) | Entity | 检查目标的饥饿值是否在指定范围内。 |
| [Gamemode](conditions/gamemode.md) | Entity | 检查目标玩家的游戏模式是否为指定模式。 |
| [Gliding](conditions/gliding.md) | Entity | 目标是否正在滑翔。 |
| [GlobalScore](conditions/globalscore.md) | Entity | 检查全局记分板数值。 |
| [HasAI](conditions/hasai.md) | Entity | 检查目标实体是否启用了 AI。 |
| [HasAura](conditions/hasaura.md) | Entity | 检查目标实体是否具有给定光环。 |
| [HasAuraStacks](conditions/hasaurastacks.md) | Entity | 检测目标所具有的指定光环层数是否在给定范围内。 |
| [HasAuraType](conditions/hasauratype.md) | Entity | 检查目标实体是否具有给定的光环类型。 |
| [HasCurrency](conditions/hascurrency.md) | Entity | 目标是否拥有给定数量的 Vault 货币。 |
| [HasDialogOpen](conditions/hasdialogopen.md) | Entity | 检查目标玩家是否打开了对话框。 |
| [HasEnchantment](conditions/hasenchantment.md) | Entity | 检查目标实体装备的物品是否具有附魔。 |
| [HasFreeInventorySlot](conditions/hasfreeinventoryslot.md) | Entity | 检查被检测的实体是否有空闲的物品栏槽位。 |
| [HasGravity](conditions/hasgravity.md) | Entity | 检测目标生物是否受重力影响。 |
| [HasItem](conditions/hasitem.md) | Entity | 检测目标玩家是否拥有给定数量的指定材质。 |
| [HasOffhand](conditions/hasoffhand.md) | Entity | 检查目标实体的副手是否持有物品。 |
| [HasOwner](conditions/hasowner.md) | Entity | 检测目标生物是否有所有者。 |
| [HasParent](conditions/hasparent.md) | Entity | 检测目标生物是否有父实体。 |
| [HasPassenger](conditions/haspassenger.md) | Entity | 检查目标实体是否有乘客。 |
| [HasPermission](conditions/haspermission.md) | Entity | 检测目标玩家是否具有某项权限。 |
| [HasPotionEffect](conditions/haspotioneffect.md) | Entity | 检测目标实体是否具有药水效果。 |
| [HasTag](conditions/hastag.md) | Entity | 检测目标是否具有记分板标签。 |
| [Health](conditions/health.md) | Entity | 匹配目标的生命值。 |
| [HealthPercent](conditions/healthpercent.md) | Entity | 匹配目标的生命值百分比或倍率。 |
| [Height](conditions/height.md) | Location | 检查目标的 Y 坐标是否在指定范围内。 |
| [HeightAbove](conditions/heightabove.md) | Location | 检查目标的 Y 坐标是否高于指定值。 |
| [HeightBelow](conditions/heightbelow.md) | Location | 检查目标的 Y 坐标是否低于给定值。 |
| [Holding](conditions/holding.md) | Entity | 检查目标是否手持给定材质，支持 MythicMobs 和原版物品。 |
| [inBounds](conditions/inbounds.md) | Compare | 检测目标是否位于长方体、球体或圆柱体内。 |
| [inClaim](conditions/inclaim.md) | Location | 检查目标位置是否位于领地内。 |
| [InCombat](conditions/incombat.md) | Entity | 检查目标生物是否被视为处于战斗中。 |
| [InPinRegion](conditions/inpinregion.md) | Location | 检查目标位置是否位于两个定位点界定的区域内。 |
| [IsInvulnerable](conditions/isinvulnerable.md) | Entity | 检查目标实体是否无敌。 |
| [IsInSurvivalMode](conditions/isinsurvivalmode.md) | Entity | 检查目标玩家是否处于生存模式。 |
| [Inside](conditions/inside.md) | Location | 检查目标头顶是否有方块。 |
| [isBaby](conditions/isbaby.md) | Entity | 检查目标实体是否为幼年形态。 |
| [isCancelled](conditions/iscancelled.md) | Meta | 检查触发技能的事件是否已取消。 |
| [isCaster](conditions/iscaster.md) | Entity | 检查目标是否为施法者。 |
| [isChild](conditions/ischild.md) | Entity | 检查目标是否为施法者的子实体。 |
| [isClimbing](conditions/isclimbing.md) | Entity | 检查目标实体是否正在攀爬。 |
| [IsCreeperPrimed](conditions/iscreeperprimed.md) | Entity | 检查目标苦力怕是否已进入准备爆炸的状态。 |
| [isFlying](conditions/isflying.md) | Entity | 检查目标玩家是否正在飞行。 |
| [isFrozen](conditions/isfrozen.md) | Entity | 检查目标实体是否被冻结。 |
| [isInCinematic](conditions/isincinematic.md) | Entity | 检查目标玩家是否正在播放过场动画。 |
| [isLeashed](conditions/isleashed.md) | Entity | 检查目标是否被拴绳拴住。 |
| [isLiving](conditions/isliving.md) | Entity | 检查目标是否为活体实体。 |
| [isMonster](conditions/ismonster.md) | Entity | 检查目标是否为怪物。 |
| [isMythicMob](conditions/ismythicmob.md) | Entity | 检查目标是否为 MythicMob。 |
| [IsParentAlive](conditions/isparentalive.md) | Entity | 检查目标实体的父实体是否仍然存活。 |
| [IsParent](conditions/isparent.md) | Compare | 检查目标实体是否为施法者的父实体。 |
| [isPlayer](conditions/isplayer.md) | Entity | 检查目标是否为玩家。 |
| [isRaiderPatrolLeader](conditions/israiderpatrolleader.md) | Entity | 检查目标实体是否为掠夺者小队的队长。 |
| [isSaddled](conditions/issaddled.md) | Entity | 检查目标实体是否装有鞍。 |
| [IsSibling](conditions/issibling.md) | Compare | 目标实体是否为施法者的兄弟实体。 |
| [isSkill](conditions/isskill.md) | Meta | 检查指定的元技能是否存在。 |
| [isTamed](conditions/istamed.md) | Entity | 检查目标实体是否已被驯服。 |
| [IsUsingSpyglass](conditions/isusingspyglass.md) | Entity | 检查目标玩家是否正在使用望远镜。 |
| [ItemGroupOnCooldown](conditions/itemgrouponcooldown.md) | Entity | 检查目标玩家的指定物品组是否正在冷却。 |
| [ItemIsSimilar](conditions/itemissimilar.md) | Entity | 检查目标玩家物品栏槽位中的物品是否与指定物品相似。 |
| [ItemRecharging](conditions/itemrecharging.md) | Entity | 检查目标的武器是否正在恢复攻击冷却。 |
| [ItemType](conditions/itemtype.md) | Meta | 检查触发此技能的物品材质。 |
| [LastDamageCause](conditions/lastdamagecause.md) | Entity | 检查目标上一次受到伤害的原因。 |
| [LastSignal](conditions/lastsignal.md) | Entity | 匹配目标生物最后收到的信号。 |
| [Level](conditions/level.md) | Entity | 检查目标 MythicMob 的等级。 |
| [LightLevel](conditions/lightlevel.md) | Location | 检测目标位置的亮度。 |
| [LightLevelFromBlocks](conditions/lightlevelfromblocks.md) | Location | 检测目标位置由发光方块产生的方块光照等级。 |
| [SkyLightLevel](conditions/skylightlevel.md) | Location | 检测目标位置的天空光照等级。 |
| [LineOfSight](conditions/lineofsight.md) | Compare | 检测目标是否在施法者的视线内。 |
| [LineOfSightFromOrigin](conditions/lineofsightfromorigin.md) | Compare | 检测目标是否在施法者的视线内。 |
| [LivingInRadius](conditions/livinginradius.md) | Location | 将给定半径内的活体实体数量与指定范围匹配。 |
| [LocalDifficulty](conditions/localdifficulty.md) | Location | 检测目标位置的难度系数。 |
| [LookingAt](conditions/lookingat.md) | Entity | 检查玩家是否正看着某个对象。 |
| [LunarPhase](conditions/lunarphase.md) | Location | 检查目标世界的月相。 |
| [MaterialisOnCooldown](conditions/materialisoncooldown.md) | Entity | 检查目标玩家的指定材质是否正在冷却。 |
| [MetaskillCondition](conditions/metaskillcondition.md) | Meta | 施放一个元技能，以确定此条件是否成立。 |
| [MobsInChunk](conditions/mobsinchunk.md) | Location | 将目标位置所在区块中的生物数量与指定范围匹配。 |
| [MobsInRadius](conditions/mobsinradius.md) | Location | 检查给定半径内的生物数量。 |
| [MobsInWorld](conditions/mobsinworld.md) | Location | 将目标世界中的生物数量与指定范围匹配。 |
| [MobsNearOrigin](conditions/mobsnearorigin.md) | Meta | 将原点周围给定半径内的生物数量与指定范围匹配。 |
| [MobSize](conditions/mobsize.md) | Entity | 检查可改变大小的实体的大小。 |
| [Moist](conditions/moist.md) | Location | 检查目标耕地方块是否湿润。 |
| [MoistureLevel](conditions/moisturelevel.md) | Location | 检查目标耕地方块是否具有指定的湿润程度。 |
| [MotionX](conditions/motionx.md) | Entity | 检查目标实体在 X 轴方向的运动速度是否在指定范围内。 |
| [MotionY](conditions/motiony.md) | Entity | 检查目标实体在 Y 轴方向的运动速度是否在指定范围内。 |
| [MotionZ](conditions/motionz.md) | Entity | 检查目标实体在 Z 轴方向的运动速度是否在指定范围内。 |
| [Mounted](conditions/mounted.md) | Entity | 目标实体是否正在骑乘坐骑或载具。 |
| [Moving](conditions/moving.md) | Entity | 目标的速度是否大于零。 |
| [MythicMobType](conditions/mythicmobtype.md) | Entity | 检查目标生物的 MythicMob 类型。 |
| [MythicPack](conditions/mythicpack.md) | Meta | 检查某个包是否存在。 |
| [MythicPackVersion](conditions/mythicpackversion.md) | Meta | 检查某个包是否为指定版本。 |
| [MythicPackVersionGreater](conditions/mythicpackversiongreater.md) | Meta | 检查某个包的版本是否大于或等于指定版本。 |
| [Name](conditions/name.md) | Entity | 检查实体的名称。 |
| [NearClaim](conditions/nearclaim.md) | Location | 目标位置是否靠近任意 GriefPrevention 领地。 |
| [Night](conditions/night.md) | Location | 时间是否为夜晚，即游戏时间 14000 到 22000。 |
| [NotInRegion](conditions/notinregion.md) | Location | 目标位置是否不在给定的 WorldGuard 区域内。 |
| [OffGCD](conditions/offgcd.md) | Entity | 检查目标生物是否处于全局冷却中。 |
| [OnBlock](conditions/onblock.md) | Location | 匹配目标实体脚下的方块。 |
| [OnGround](conditions/onground.md) | Entity | 目标实体是否站在实心地面上。 |
| [OriginDistanceFromPin](conditions/origindistancefrompin.md) | Location | 检查原点是否位于指定定位点的一定距离内。 |
| [OriginLocation](conditions/originlocation.md) | Meta | 检查原点是否位于给定位置。 |
| [Outside](conditions/outside.md) | Location | 目标上方是否无遮挡、直通天空。 |
| [Owner](conditions/owner.md) | Compare | 检查目标实体是否为施法者的所有者。 |
| [OwnerIsOnline](conditions/ownerisonline.md) | Entity | 目标生物的所有者为玩家时，检查其所有者是否在线。 |
| [Pitch](conditions/pitch.md) | Entity | 检查目标实体的俯仰角是否在指定范围内。 |
| [PlayerKills](conditions/playerkills.md) | Entity | 匹配目标生物击杀的玩家数量。 |
| [PlayerNotWithin](conditions/playernotwithin.md) | Location | 检查目标周围指定半径内是否有玩家。 |
| [PlayerWithin](conditions/playerwithin.md) | Location | 检查目标周围指定半径内是否有玩家。 |
| [PlayersInRadius](conditions/playersinradius.md) | Entity | 检查指定半径内的玩家数量。 |
| [PlayersInWorld](conditions/playersinworld.md) | Meta | 匹配施法者所在世界的玩家数量。 |
| [PlayersOnline](conditions/playersonline.md) | Meta | 匹配在线玩家数量。 |
| [Plugin](conditions/plugin.md) | Meta | 检查服务器是否正在运行指定插件。 |
| [Premium](conditions/premium.md) | Meta | 检查服务器是否正在运行 MythicMobs Premium。 |
| [ProjectileHasEnded](conditions/projectilehasended.md) | Meta | 检查发起调用的弹射物是否已结束。 |
| [Raining](conditions/raining.md) | Location | 目标世界是否正在下雨。 |
| [Region](conditions/region.md) | Location | 目标是否位于给定的 WorldGuard 区域内。 |
| [SameFaction](conditions/samefaction.md) | Entity | 检测施法者和目标是否属于同一阵营。 |
| [Score](conditions/score.md) | Entity | 检查目标实体的记分板数值。 |
| [ServerIsPaper](conditions/serverispaper.md) | Meta | 检查服务器是否运行 Paper 的分支版本。 |
| [ServerNmsVersion](conditions/servernmsversion.md) | Meta | 检查服务器是否正在运行指定的 Minecraft NMS 版本。 |
| [ServerVersion](conditions/serverversion.md) | Meta | 检查服务器是否正在运行指定的 Minecraft 版本。 |
| [ServerVersionAfterOrEqual](conditions/serverversionafterorequal.md) | Meta | 检查服务器版本是否大于或等于指定版本。 |
| [ServerVersionBefore](conditions/serverversionbefore.md) | Meta | 检查服务器版本是否早于指定版本。 |
| [Size](conditions/size.md) | Entity | 检查目标实体的大小。 |
| [SkillOnCooldown](conditions/skilloncooldown.md) | Entity | 检查给定技能是否正在对目标冷却。 |
| [SpawnReason](conditions/spawnreason.md) | Entity | 检查目标的生成原因。 |
| [Sprinting](conditions/sprinting.md) | Entity | 检查目标**玩家**是否正在疾跑。 |
| [Stance](conditions/stance.md) | Entity | 检查目标生物的姿态。 |
| [StatDamageModifier](conditions/statdamagemodifier.md) | Meta | 用于属性触发器中，检查增加的伤害（以倍率表示）。 |
| [StringEmpty](conditions/stringempty.md) | Meta | 检查提供的字符串是否为空。 |
| [StringNotEmpty](conditions/stringnotempty.md) | Meta | 检查提供的字符串是否非空。 |
| [StringEquals](conditions/stringequals.md) | Meta | 检查 value1 是否等于 value2。两个值都可以使用变量和占位符。 |
| [Structure](conditions/structure.md) | Location | 匹配目标位置是否处于某个结构内部。 |
| [Sunny](conditions/sunny.md) | Location | 目标世界是否为晴天。 |
| [TargetInLineOfSight](conditions/targetinlineofsight.md) | Entity | 检测目标是否能看见其自身的目标。 |
| [TargetNotInLineOfSight](conditions/targetnotinlineofsight.md) | Entity | 检测目标是否无法看见其自身的目标。 |
| [TargetWithin](conditions/targetwithin.md) | Entity | 检测目标的目标是否在指定距离内。 |
| [TargetNotWithin](conditions/targetnotwithin.md) | Entity | 检测目标的目标是否不在指定距离内。 |
| [Targets](conditions/targets.md) | Meta | 检测从父 skilltree 继承的目标数量是否与给定范围匹配。 |
| [TemplateType](conditions/templatetype.md) | Entity | 检查目标生物是否继承了指定的 Template。 |
| [Thundering](conditions/thundering.md) | Location | 目标世界是否正在打雷。 |
| [TriggerBlockType](conditions/triggerblocktype.md) | Meta | 检查触发技能的材质类型。 |
| [TriggerItemType](conditions/triggeritemtype.md) | Meta | 检查触发技能的物品材质类型。 |
| [VariableContains](conditions/variablecontains.md) | Meta | 检查给定变量是否包含指定值。 |
| [VariableEquals](conditions/variableequals.md) | Meta | 检查给定变量是否具有指定值。 |
| [VariableInRange](conditions/variableinrange.md) | Meta | 检查给定数值变量是否在指定范围内。 |
| [VariableIsSet](conditions/variableisset.md) | Meta | 检查给定变量是否已设置。 |
| [VehicleIsDead](conditions/vehicleisdead.md) | Entity | 检查施法者乘坐的载具是否已死亡。 |
| [Velocity](conditions/velocity.md) | Entity | 检查目标实体的速度是否在指定范围内。 |
| [Wearing](conditions/wearing.md) | Entity | 检测目标实体的装备。 |
| [World](conditions/world.md) | Location | 检查目标世界的名称。 |
| [WorldTime](conditions/worldtime.md) | Location | 将目标位置所在世界的时间与指定范围匹配。 |
| [Yaw](conditions/yaw.md) | Entity | 检查目标实体的偏航角是否在指定范围内。 |
| [xDiff](conditions/xdiff.md) | Entity | 检查目标实体与施法者之间的 X 坐标差。 |
| [yDiff](conditions/ydiff.md) | Entity | 检查目标实体与施法者之间的 Y 坐标差。 |
| [zDiff](conditions/zdiff.md) | Entity | 检查目标实体与施法者之间的 Z 坐标差。 |

## 更多示例 {#more-examples}

```yaml
FlameShock:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - incombat
  - stance aggressive
  - onblock GRASS
  - offgcd
  Skills:
  - gcd{t=60}
  - message{m="<mob.name> begins casting a spell"}
  - potion{t=SLOW;d=60;l=7}
  - delay 60
  - message{m="<target.name> &ecombusts"}
  - effect:particles{p=flame;a=20;hS=3;vS=1;s=0;y=2}
  - potion{t=HARM;d=1;l=1}
```

[1] 并非所有条件都适用于所有地方。
