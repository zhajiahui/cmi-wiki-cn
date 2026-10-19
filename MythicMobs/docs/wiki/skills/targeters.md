---
title: 目标选择器
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/targeters
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 目标选择器

目标选择器用于决定技能触发时会作用于哪些目标。

目标选择器可以省略，默认通常为 @trigger，但忘记设置目标选择器可能是 MythicMobs 新手最常犯的错误之一。

在 Skill 机制上设置目标选择器后，元技能中的所有技能都会继承这个初始目标选择器。也可以为元技能中的单个机制单独指定目标选择器，覆盖继承的目标。

如果实体目标被传递给基于位置的机制，它将使用实体的位置。

1. [扩展目标选择器](targeters.md#additional-targeters)
2. [目标选择器](targeters.md#targeters)
   1. [实体目标选择器](targeters.md#entity-targeters)
      1. [单实体目标选择器](targeters.md#single-entity-targeters)
      2. [多实体目标选择器](targeters.md#multi-entity-targeters)
      3. [仇恨表目标选择器](targeters.md#threattable-targeters)
   2. [位置目标选择器](targeters.md#location-targeters)
      1. [单位置目标选择器](targeters.md#single-location-targeters)
      2. [多位置目标选择器](targeters.md#multi-location-targeters)
   3. [元目标](targeters.md#meta-targeters)
      1. [元实体目标选择器](targeters.md#meta-entity-targeters)
      2. [元位置目标选择器](targeters.md#meta-location-targeters)
   4. [特殊目标选择器](targeters.md#special-targeters)
3. [通用属性](targeters.md#common-attributes)
   1. [所有目标选择器](targeters.md#all-targeters)
      1. [Sudo 属性](targeters.md#sudo-attributes)
   2. [实体目标选择器通用属性](targeters.md#common-entity-targeters-attributes)
   3. [位置目标选择器通用属性](targeters.md#common-location-targeters-attributes)
4. [目标选择器选项](targeters.md#targeter-options)
   1. [目标过滤器](targeters.md#target-filters)
      1. [特定过滤器](targeters.md#specific-filters)
   2. [目标限制](targeters.md#target-limits)

# 额外目标选择器 {#additional-targeters}

以下链接列出了扩展插件提供的目标选择器。只有安装对应插件后，这些目标选择器才能使用。

- [ModelEngine 4](https://git.mythiccraft.io/mythiccraft/model-engine-4/-/wikis/Skills/Targeters)
- [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Targeters)
- [MythicEnchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Skills/Targeters)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#targeters)

# 目标选择器 {#targeters}

## 实体目标选择器 {#entity-targeters}

### 单实体目标选择器 {#single-entity-targeters}

| 目标选择器 | 简写 | 说明 |
| --- | --- | --- |
| @[Self](targeters/self.md) | @Caster @Boss @Mob | 以此机制的施法者为目标。 |
| @[Target](targeters/target.md) | @T | 以施法者的目标为目标。 |
| @[Trigger](targeters/trigger.md) |  | 以触发技能的实体为目标。 |
| @[NearestPlayer](targeters/nearestplayer.md) |  | 以半径内最近的玩家为目标。 |
| @[WolfOwner](targeters/wolfowner.md) |  | 以狼的所有者为目标。 |
| @[Owner](targeters/owner.md) |  | 以生物的[所有者](mechanics/setowner.md)为目标。 |
| @[Parent](targeters/parent.md) | @summoner | 以生物的[父实体](mechanics/setparent.md)为目标。 |
| @[Mount](targeters/mount.md) |  | 以施法者最初的[坐骑](../mobs/mobs.md#mount)为目标。 |
| @[Father](targeters/father.md) | @dad @daddy | 以施法生物的父亲为目标。 |
| @[Mother](targeters/mother.md) | @mom @mommy | 以施法生物的母亲为目标。 |
| @[Passenger](targeters/passenger.md) |  | 以施法生物的骑乘者为目标。 |
| @[PlayerByName](targeters/playerbyname.md) | @specificplayer | 按名称选择特定玩家为目标，支持占位符。 |
| @[UniqueIdentifier](targeters/uniqueidentifier.md) | @UUID | 按 UUID 选择特定实体为目标，支持占位符。 |
| @[Vehicle](targeters/vehicle.md) |  | 以施法者的载具为目标。 |
| @[InteractionLastAttacker](targeters/interactionlastattacker.md) | @lastAttacker | 以最后攻击施法 `INTERACTION` 实体的实体为目标。 |
| @[InteractionLastInteract](targeters/interactionlastinteract.md) | @lastInteract | 以最后与施法 `INTERACTION` 实体交互的实体为目标。 |
| @[OwnerLocation](targeters/ownerlocation.md) |  | 以生物所有者的位置为目标。 |
| @[ParentLocation](targeters/parentlocation.md) | @summonerlocation | 以生物父实体的位置为目标。 |

### 多实体目标选择器 {#multi-entity-targeters}

| 目标选择器 | 简写 | 说明 |
| --- | --- | --- |
| @[LivingInCone](targeters/livingincone.md) | @entitiesInCone @livingEntitiesInCone @LEIC @EIC | 以相对于朝向具有指定角度、长度和旋转角度的锥形范围内所有活体实体为目标。 |
| @[LivingInWorld](targeters/livinginworld.md) | @EIW | 以施法者所在世界中的所有活体实体为目标。 |
| @[NotLivingNearOrigin](targeters/notlivingnearorigin.md) | @nonLivingNearOrigin @NLNO | 以原点附近指定半径内的所有非活体实体为目标。 |
| @[PlayersInRadius](targeters/playersinradius.md) | @PIR | 以给定半径内的所有玩家为目标。 |
| @[MobsInRadius](targeters/mobsinradius.md) | @MIR | 以指定半径内所有给定类型的 MythicMobs 生物或原版覆盖生物为目标。 |
| @[EntitiesInRadius](targeters/entitiesinradius.md) | @livingEntitiesInRadius @livingInRadius @allInRadius @EIR | 以给定半径内的所有实体为目标。 |
| @[EntitiesInRing](targeters/entitiesinring.md) | @EIRR | 以给定环形范围内的所有实体为目标。 |
| @[EntitiesInRingNearOrigin](targeters/entitiesinringnearorigin.md) | @ERNO | 以原点周围给定环形范围内的所有实体为目标。 |
| @[PlayersInWorld](targeters/playersinworld.md) | @World | 以当前世界的所有玩家为目标。 |
| @[PlayersOnServer](targeters/playersonserver.md) | @Server @Everyone | 以服务器中的所有玩家为目标。 |
| @[PlayersInRing](targeters/playersinring.md) |  | 以距中心指定最小半径和最大半径之间的所有玩家为目标。 |
| @[PlayersNearOrigin](targeters/playersnearorigin.md) | @PNO | 以元技能[原点](targeters/origin.md)附近的玩家为目标。 |
| @[TrackedPlayers](targeters/trackedplayers.md) | @tracked | 以位于施法者渲染距离内的玩家为目标。 |
| @[MobsNearOrigin](targeters/mobsnearorigin.md) |  | 以原点周围指定半径内所有给定类型的 MythicMobs 生物或原版覆盖生物为目标。 |
| @[EntitiesNearOrigin](targeters/entitiesnearorigin.md) | @ENO | 以元技能[原点](targeters/origin.md)附近的所有实体为目标。 |
| @[Children](targeters/children.md) | @child @summons | 以施法者召唤的任意子实体为目标。 |
| @[Siblings](targeters/siblings.md) | @sibling @brothers @sisters | 以与施法者具有相同父实体的任意生物为目标。 |
| @[ItemsNearOrigin](targeters/itemsnearorigin.md) |  | 以元技能[原点](targeters/origin.md)附近的掉落物为目标。 |
| @[ItemsInRadius](targeters/itemsinradius.md) | @IIR | 以给定半径内的所有掉落物为目标。 |
| @[Bound](targeters/bound.md) | @bounds | 以长方体、球体或圆柱体内的所有活体实体为目标。 |

### 仇恨表目标选择器 {#threattable-targeters}

这些目标选择器仅在生物启用[仇恨表](../mobs/threattables.md)时可用。

| 目标选择器 | 简写 | 说明 |
| --- | --- | --- |
| @[ThreatTable](targeters/threattable.md) | @TT | 以施法生物仇恨表中的每个实体为目标。 |
| @[ThreatTablePlayers](targeters/threattableplayers.md) |  | 以施法生物仇恨表中的所有玩家为目标。 |
| @[RandomThreatTarget](targeters/randomthreattarget.md) | @RTT | 以施法生物仇恨表中的随机实体为目标。 |
| @[RandomThreatTargetLocation](targeters/randomthreattargetlocation.md) | @RTTL | 以施法生物仇恨表中随机实体的位置为目标。 |

## 位置目标选择器 {#location-targeters}

### 单位置目标选择器 {#single-location-targeters}

| 目标选择器 | 简写 | 说明 |
| --- | --- | --- |
| @[SelfLocation](targeters/selflocation.md) | @casterLocation @bossLocation @mobLocation | 以施法者的位置为目标。 |
| @[SelfEyeLocation](targeters/selfeyelocation.md) | @eyeDirection @casterEyeLocation @bossEyeLocation @mobEyeLocation | 以施法者眼睛的位置为目标。 |
| @[Forward](targeters/forward.md) |  | 以施法者朝向前方的某个位置为目标。 |
| @[ProjectileForward](targeters/projectileforward.md) |  | 以施法弹射物沿其方向前方的某个位置为目标。 |
| @[TargetLocation](targeters/targetlocation.md) | @targetloc @TL | 以施法者目标的位置为目标。 |
| @[TargetPredictedLocation](targeters/targetpredictedlocation.md) | @targetPredictedLoc @TPL @PredictedTargetLocation | 根据施法者首要目标当前的移动速度，预测其经过指定刻数后的位置，并以该位置为目标。 |
| @[TriggerLocation](targeters/triggerlocation.md) |  | 以触发技能的实体所在位置为目标。 |
| @[SpawnLocation](targeters/spawnlocation.md) |  | 以世界出生位置为目标。 |
| @[CasterSpawnLocation](targeters/casterspawnlocation.md) |  | 以施法者的出生位置为目标。 |
| @[Location](targeters/location.md) |  | 以施法者所在世界的指定坐标为目标。 |
| @[Origin](targeters/origin.md) | @source | 以元技能“原点”或“来源”的位置为目标。通常是施法生物的位置，但在特殊情况下这一点并不成立，例如 Projectile 技能的“原点”就是弹射物所在位置。 |
| @[ObstructingBlock](targeters/obstructingblock.md) |  | 尝试以施法者前方阻挡它的方块为目标。 |
| @[TargetBlock](targeters/targetblock.md) |  | 以施法玩家正在看的方块为目标。 |
| @[TrackedLocation](targeters/trackedlocation.md) |  | 以生物追踪的位置为目标。 |
| @[NearestStructure](targeters/neareststructure.md) |  | 以施法者所在世界指定半径内最近的指定类型结构为目标。 |
| @[VariableLocation](targeters/variablelocation.md) | @varLocation | 以指定变量中保存的位置为目标。 |
| @[HighestBlock](targeters/highestblock.md) |  | 以技能原点处最高的方块为目标。 |
| @[PlayerLocationByName](targeters/playerlocationbyname.md) |  | 按名称选择特定玩家的位置为目标。 |
| @[EscapeLocation](targeters/escapelocation.md) |  | 以附近安全的逃离位置为目标，选择方式类似于末影人选择传送目的地。 |

### 多位置目标选择器 {#multi-location-targeters}

| 目标选择器 | 简写 | 说明 |
| --- | --- | --- |
| @[ForwardWall](targeters/forwardwall.md) |  | 以施法者前方的一个平面为目标。 |
| @[PlayerLocationsInRadius](targeters/playerlocationsinradius.md) | @PLIR | 以给定半径内所有玩家的位置为目标。 |
| @[Pin](targeters/pin.md) |  | 以某个[定位点](../pins.md)的位置为目标。 |
| @[Ring](targeters/ring.md) |  | 选择一组位置点为目标，使其形成圆环。 |
| @[RandomRingPoint](targeters/randomringpoint.md) |  | 以施法者周围环形范围内的随机点为目标。 |
| @[Cone](targeters/cone.md) |  | 返回组成锥体的指定数量目标位置点。注意：锥体固定在 y 轴上，无法向上或向下旋转。 |
| @[Sphere](targeters/sphere.md) |  | 以施法者周围球体内的点为目标。 |
| @[Rectangle](targeters/rectangle.md) | @cube @cuboid | 返回组成矩形的指定数量目标位置点。 |
| @[RandomLocationsNearCaster](targeters/randomlocationsnearcaster.md) | @randomLocations @RLNC | 以施法者附近的随机位置为目标。 |
| @[RandomLocationsNearOrigin](targeters/randomlocationsnearorigin.md) | @RLO @randomLocationsOrigin @RLNO | 以技能原点附近的随机位置为目标。 |
| @[BlocksNearOrigin](targeters/blocksnearorigin.md) | @BNO | 以元技能原点周围指定半径内的所有方块为目标。 |
| @[RingAroundOrigin](targeters/ringaroundorigin.md) | @ringOrigin @RAO | 以原点周围指定环形范围内的位置为目标。 |
| @[Spawners](targeters/spawners.md) |  | 以指定刷怪器的位置为目标。 |
| @[BlocksInPinRegion](targeters/blocksinpinregion.md) |  | 以两个定位点界定的区域内的方块为目标。 |
| @[ChunksInWERegion](targeters/chunksinweregion.md) | @chunksInWGRegion | 以指定 WorldGuard 区域内各区块的 0,0 角点为目标。 |

## 元目标选择器 {#meta-targeters}

元目标选择器会相对于[继承目标](metaskills.md#inheritance)选取目标。例如：

```yaml
# Mob file
Laser:
  Type: CREEPER
  Display: 'Laser'
  Health: 12
  AITargetSelectors:
  - 0 clear
  - 1 players
  Skills:
  - skill{s=Laser} @target
```

```yaml
# Skill file
Laser:
  Skills:
  - ignite @EntitiesInLine{r=1}
```

在上面的技能示例中，ignite 机制会选中施法者与 `- skill{s=Laser} @target` 所指定目标之间的实体，也就是施法者与其目标之间直线上的实体。

一些元目标选择器还支持以 "fromOrigin" 方式施放技能机制。这会将元目标选择器的起始位置从施法者改为 @Origin，可以实现一些复杂效果，尤其适合与弹射物配合使用。

### 元实体目标选择器 {#meta-entity-targeters}

| 目标选择器 | 简写 | 说明 |
| --- | --- | --- |
| @[LivingInLine](targeters/livinginline.md) | @entitiesInLine @livingEntitiesInLine @LEIL @EIL | 以继承目标与施法生物之间直线上的任意实体为目标。 |
| @[LivingNearTargetLocation](targeters/livingneartargetlocation.md) | @LNTL @ENTL @ENT | 以继承目标附近的所有活体实体为目标。 |
| @[PlayersNearTargetLocations](targeters/playersneartargetlocations.md) | @playersNearTargetLocation @PNTL | 以继承目标附近的所有玩家为目标。 |
| @[TargetedTarget](targeters/targetedtarget.md) | @Targeted | 以继承的实体目标为目标。 |

### 元位置目标选择器 {#meta-location-targeters}

| 目标选择器 | 简写 | 说明 |
| --- | --- | --- |
| @[Line](targeters/line.md) |  | 以生物与继承目标之间的位置为目标。 |
| @[RandomLocationsNearTargets](targeters/randomlocationsneartargets.md) | @randomLocationsNearTarget @randomLocationsNearTargetEntities @randomLocationsNearTargetLocations @RLNT @RLNTE @RLNTL | 以继承目标周围的随机位置为目标。 |
| @[FloorOfTargets](targeters/flooroftargets.md) | @FOT @floorsOfTarget | 以继承目标下方的方块为目标。 |
| @[LocationsOfTargets](targeters/locationsoftargets.md) | @locationOfTarget @LOT | 以继承实体目标的位置为目标。 |
| @[TargetedLocation](targeters/targetedlocation.md) | @targetedLocations @targetedLoc | 以继承位置目标的位置为目标。 |
| @[BlocksInRadius](targeters/blocksinradius.md) | @BIR | 以继承目标周围指定半径内的所有方块为目标。 |
| @[BlocksInChunk](targeters/blocksinchunk.md) | @BIC | 以相对于继承目标的某个区块内的所有方块为目标。 |
| @[BlockVein](targeters/blockvein.md) | @vein @bv | 从技能原点开始，选择所有相邻且符合 blocktype 的方块为目标。 |

## 特殊目标选择器 {#special-targeters}

| 目标选择器 | 简写 | 说明 |
| --- | --- | --- |
| @[None](targeters/none.md) |  | 不提供目标，适合无需目标输入的机制。 |
| @[Region](targeters/region.md) |  | 用于选择区域的特殊目标选择器，仅适用于特定机制。 |

# 常用属性 {#common-attributes}

大多数目标选择器支持一些通用属性，可用属性取决于该目标选择器的返回值

## 全部目标选择器 {#all-targeters}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| targetconditions | conditions, cond, c | [内联目标条件](inline-conditions.md#targetconditions) |  |
| fallback | fb | 此目标选择器未返回目标时使用的备用目标选择器。 |  |

### Sudo 属性 {#sudo-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| sudoparent | fromparent, ofparent, asparent, parent, ofparent | 设为 `true` 时，会像执行此机制的是施法实体的[父实体](targeters/parent.md)一样解析目标选择器。 |  |
| sudoowner | fromowner, ofowner, asowner, owner, ofowner | 设为 `true` 时，会像执行此机制的是施法实体的[所有者](targeters/owner.md)一样解析目标选择器。 |  |
| sudotrigger | fromtrigger, oftrigger, astrigger, trigger, oftrigger | 设为 `true` 时，会像执行此机制的是技能树的[触发实体](targeters/trigger.md)一样解析目标选择器。 |  |

在此示例中，[生物会不断传送到其主人前方](https://cdn.discordapp.com/attachments/523443579574681600/1101186712174088253/a.gif)。这是因为 `Forward` 目标选择器使用了 `sudoowner` 属性，解析时会将该生物的主人视为技能机制的执行者

```yaml
TestOwner:
  Type: Wolf
  Skills:
  - setOwner @NearestPlayer{r=99} ~onSpawn
  - tp @Forward{f=5;y=1;sudoowner=true} ~onTimer:1
```

## 实体目标选择器通用属性 {#common-entity-targeters-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| useboundingbox | bb | 目标选择器进行距离检查时，此选项允许其针对目标的边界框而非碰撞箱中心进行检查。 |  |
| unique | u | 同一实体可被选为目标的最大次数，默认为 1，设为 0 可禁用限制。主要用于具有多个碰撞箱的 meg 模型。 |  |
| nomegbb | nmb | 是否过滤掉 MEG 子碰撞箱。 |  |

## 位置目标选择器通用属性 {#common-location-targeters-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| xoffset | xo, x | 将 x 轴偏移居中。 |  |
| yoffset | yo, y | 将 y 轴偏移居中。 |  |
| zoffset | zo, z | 将 z 轴偏移居中。 |  |
| forwardOffset | foffset, fo | 根据施法者的视角，将前后偏移居中。 | 0 |
| sideOffset | soffset, so | 根据施法者的视角，将左右偏移居中。 | 0 |
| upoffset | uoffset, uo | 根据施法者的视角，将上下偏移居中。 | 0 |
| rotatex | rotx | 绕 x 轴旋转。 |  |
| rotatey | roty | 绕 y 轴旋转。 |  |
| rotatez | rotz | 绕 z 轴旋转。 |  |
| coordinatex | cx | 设置 x 轴坐标。 |  |
| coordinatey | cy | 设置 y 轴坐标。 |  |
| coordinatez | cz | 设置 z 轴坐标。 |  |
| length |  | 将方向向量乘以指定值。 |  |
| blocktypes | blocktype, bt | 仅以选定的方块类型为目标。可用 `,` 分隔多个方块。在类型前加 `#` 表示只需匹配类型名称的一部分，加 `@` 表示只需匹配类型名称的开头。在类型前加 `*` 表示指定的是[方块标签](https://minecraft.wiki/w/Tag#Block_tags_2)，而不是方块类型，例如 `blocktype=*sculk_replaceable`。 |  |
| blockignores | blockignore, bi | 从目标选择器中排除选定的方块类型。可用 `,` 分隔多个方块，也可使用 `blocktype` 中说明的特殊语法。 |  |
| coordinateyaw | cyaw | 设置偏航角。 |  |
| coordinatepitch | cpitch | 设置俯仰角。 |  |
| blockcentered | centered | 布尔值。设为 true 时，以目标位置所在方块的中心为目标，而不是以目标位置本身为目标。 |  |
| faulty |  | 是否使用旧版向量计算公式。 | false |
| blockSurface | surface | 插件是否尝试将位置调整到表面上。 | false |
| blockSurfaceTolerance | surfaceTolerance | `blockSurface` 设为 `true` 时，搜索表面所用的容差。 | 5 |

# 目标选择器选项 {#targeter-options}

## 目标过滤器 {#target-filters}

目标过滤器用于过滤掉特定目标，让目标选择器的用法更加灵活。

通过以下两个属性设置，**所有**实体目标选择器都可使用：

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| target |  | 要选择为目标的实体类型。 |  |
| ignore |  | 不选择为目标的实体类型。 |  |

例如，要让目标选择器忽略所有玩家和非敌对生物，可以这样写：

```yaml
  - damage{a=20} @EntitiesInRadius{r=10;ignore=players,animals}
```

要让目标选择器**仅**选中玩家，可以这样写：

```yaml
  - skill{s=ASkill} @EntitiesInRadius{r=5;target=players}
```

> 你可以在 MythicMobs/config/config-skills.yml 中设置默认目标过滤器

可用的筛选器包括：

#### Target 属性 {#target-attribute}

| 目标过滤器 | 别名 | 说明 |
| --- | --- | --- |
| ground |  | 是否以地面实体为目标。使用时会忽略飞行实体和水生实体。 |
| water |  | 是否以水生实体为目标。使用时会忽略飞行实体和地面实体。 |
| flying |  | 是否以飞行实体为目标。使用时会忽略地面实体和水生实体。 |
| self | caster | 是否可以选择此机制的施法者为目标。 |
| player |  | 是否可以选择玩家为目标。 |
| creative |  | 是否可以选择创造模式玩家为目标。 |
| spectator |  | 是否可以选择旁观模式玩家为目标。 |
| armorstand | armor_stand | 是否可以选择盔甲架为目标。 |
| marker |  | 是否可以选择标记实体为目标。 |
| textdisplay | text_display | 是否可以选择文本展示实体为目标。 |
| itemdisplay | item_display | 是否可以选择物品展示实体为目标。 |
| blockdisplay | block_display | 是否可以选择方块展示实体为目标。 |
| interaction |  | 是否可以选择交互实体为目标。 |
| npc |  | 是否可以选择 Citizens NPC 为目标。 |
| animal |  | 是否可以选择动物为目标。 |
| creature |  | 是否可以选择生物为目标。 |
| monster |  | 是否可以选择怪物为目标。 |
| villager |  | 是否可以选择村民为目标。 |
| vanilla |  | 是否仅以非 Mythic 实体为目标。使用时会忽略 Mythic 生物。 |
| mythic |  | 是否仅以 Mythic 生物为目标。使用时会忽略非 Mythic 实体。 |

> 如果`ground`、`water`和`flying`均未使用，并且默认过滤器不包含其中任何一个，则`Players`、`ArmorStands`、`Markers`、`TextDisplays`、`ItemDisplays`、`BlockDisplays`、 `Interactions`、`Creative`、`Spectator`、`CitizensNPCs`、`Animals`、`Creatures`、`Monsters` 和 `Villagers` 也将被忽略

#### Ignore 属性 {#ignore-attribute}

| 忽略过滤器 | 别名 | 说明 |
| --- | --- | --- |
| player |  | 是否排除玩家，不将其选为目标。 |
| creative |  | 是否排除创造模式玩家，不将其选为目标。 |
| spectator |  | 是否排除旁观模式玩家，不将其选为目标。 |
| armorstand | armor_stand | 是否排除盔甲架，不将其选为目标。 |
| marker |  | 是否排除标记实体，不将其选为目标。 |
| textdisplay | text_display | 是否排除文本展示实体，不将其选为目标。 |
| itemdisplay | item_display | 是否排除物品展示实体，不将其选为目标。 |
| blockdisplay | block_display | 是否排除方块展示实体，不将其选为目标。 |
| interaction |  | 是否排除交互实体，不将其选为目标。 |
| npc |  | 是否排除 Citizens NPC，不将其选为目标。 |
| animal |  | 是否排除动物，不将其选为目标。 |
| creature |  | 是否排除生物，不将其选为目标。 |
| monster |  | 是否排除怪物，不将其选为目标。 |
| villager |  | 是否排除村民，不将其选为目标。 |
| faction |  | 是否排除同一阵营的实体，不将其选为目标。 |
| owner |  | 是否排除施法者的所有者，不将其选为目标。 |
| vanilla | nonmythic | 是否排除原版实体，即非 Mythic 实体，不将其选为目标。 |
| mythic |  | 是否排除 Mythic 实体，不将其选为目标。 |

### 特定筛选器 {#specific-filters}

也可以使用以下属性，单独设置是否选中特定类型的实体。这些属性会针对其对应的实体类型，覆盖通用 target/ignore 属性的效果

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| targetself |  | 是否以此机制的施法者为目标。 |  |
| targetplayers |  | 是否以玩家为目标。 |  |
| targetcreative |  | 是否以创造模式玩家为目标。 |  |
| targetspectator |  | 是否以旁观模式玩家为目标。 |  |
| targetinvulnerable |  | 是否以无敌实体为目标。 |  |
| targetarmorstands |  | 是否以盔甲架为目标。 |  |
| targetmarkers |  | 是否以标记实体为目标。 |  |
| targettextdisplays | targettextdisplay | 是否以文本展示实体为目标。 |  |
| targetitemdisplays | targetitemdisplay | 是否以物品展示实体为目标。 |  |
| targetblockdisplays | targetblockdisplay | 是否以方块展示实体为目标。 |  |
| targetinteractions | targetinteraction | 是否以交互实体为目标。 |  |
| targetnpcs |  | 是否以 Citizens NPC 为目标。 |  |
| targetanimals |  | 是否以动物为目标。 |  |
| targetcreatures |  | 是否以生物为目标。 |  |
| targetsamefaction |  | 是否以同一阵营的实体为目标。 |  |
| targetowner |  | 是否以施法者的所有者为目标。 |  |
| targetvanilla | targetnonmythic | 是否以非 Mythic 实体为目标。 |  |
| targetvillagers |  | 是否以村民为目标。 |  |
| targetall |  | 是否选择所有对象为目标。为 true 时，忽略所有筛选条件。 | false |

```yaml
  - damage{a=20} @EntitiesInRadius{r=10;targetplayers=true;targetsamefaction=true;targetowner=false}
```

> 使用此项可明确选中玩家、同阵营实体及其他有效目标，同时排除施法者的主人

## 目标数量限制 {#target-limits}

从 v5.0.4 起，所有实体和位置目标选择器都支持目标数量限制，也可以设置选取顺序。

这是通过属性完成的：

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| sort | sortby | 目标实体或位置的排序方式。基于距离的排序以机制原点为参照。 |  |
| skipTargetsUpToIndex | stuti | 大于 0 时，在排序后跳过目标选择器的前 `n` 个目标。 | 0 |
| limit |  | 大于 0 时，限制跳过目标后可选择的实体或位置数量。 | 0 |

假设技能只需选中 30 格内最近的 2 名玩家，只需将 limit 设为 2，并按最近距离排序：

```yaml
  - mechanic @PlayersInRadius{r=30;limit=2;sort=NEAREST}
```

目前，sort 支持以下值：

**通用排序方式：**

- NONE *（通常按实体已存在的时间排序）*
- RANDOM
- NEAREST *（距技能机制原点最近）*
- FURTHEST *（距技能机制原点最远）*

**仅限实体的排序方式**

- HIGHEST_HEALTH
- LOWEST_HEALTH
- HIGHEST_THREAT
- LOWEST_THREAT

目标选择器会按以下顺序处理：

- 如果指定了 sort 属性，且 limit 与 skipTargetsUpToIndex 均 >0，则根据 sort 属性对目标排序
- 如果 skipTargetsUpToIndex >0，则按其值跳过前 n 个目标
- 如果 limit > 0，则按其值返回前 n 个目标

因此，结合使用 limit 和 skipTargetsUpToIndex，就能获取特定索引处的目标

```yaml
GiveRewards:
  Skills:
  - message{m="You are first!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;limit=1} #targets the player that has the highest threat
  - message{m="You are second!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;limit=1;stuti=1} #targets the player that has the second highest threat
  - message{m="You are third!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;limit=1;stuti=2} #targets the player that has the third highest threat
  - message{m="You aren't on the podium!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;stuti=3} #targets everyone else
```
