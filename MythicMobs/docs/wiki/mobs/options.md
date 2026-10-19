---
title: 生物选项
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/Options
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 生物选项

创建生物时可用的所有选项。大多数选项都位于 `Options` 部分下，如下所示：

```yml
Dummy:
  Type: skeleton
  Options:
    MovementSpeed: 0.3
    PreventSunburn: true
```

##  {#section}

- [通用选项](options.md#universal-options)
- [组特定选项](options.md#group-specific-options)
- [特定生物选项](options.md#mob-specific-options)

##  {#section-2}

# 通用选项 {#universal-options}

这些选项是通用的，无论生物类型如何，都将起作用。

#### AlwaysShowName {#alwaysshowname}

名称标签是否始终显示。相当于NBT-标签`CustomNameVisible`。默认为`false`。

```yml
  Options:
    AlwaysShowName: false
```

#### AttackSpeed {#attackspeed}

生物的攻击速度，默认为该生物的原版攻击速度。

```yaml
  Options:
    AttackSpeed: 1
```

#### VisibleByDefault {#visiblebydefault}

设置当生物生成或加载生物时默认情况下生物是否可见。默认为`true`。

```yml
  Options:
    VisibleByDefault: true
```

#### Invisible {#invisible}

为生物设置永久隐身效果，无需通过 `~onSpawn` 触发器施加隐身药水效果。默认为 `false`。

```yml
  Options:
    Invisible: true
```

#### Collidable {#collidable}

生物是否具有碰撞。Minecraft 的碰撞是双向的，双方实体都需要设为 `false` 才能完全消除碰撞；这样也会阻止玩家推动生物。默认为 `true`。

```yml
  Options:
    Collidable: true
```

#### DigOutOfGround {#digoutofground}

如果生物受到 `SUFFOCATION` 伤害，则将其传送到上方两格。默认为`false`。

```yml
  Options:
    DigOutOfGround: false
```

#### Despawn {#despawn}

决定生物如何消失。使用大量刷怪点时应开启此项，避免实体过多压垮服务器；制作 NPC、Boss 等需要特殊消失策略的实体时也应设置。默认为 `true`。

| 模式 | 别名 | 说明 |
| --- | --- | --- |
| NORMAL | TRUE, YES | - 附近没有玩家时消失 - 服务器重启时消失 - 区块卸载时消失 - 会被普通的 mythicmobs 击杀命令杀死 |
| CHUNK |  | - 服务器重启时消失 - 区块卸载时消失 - 会被普通的 mythicmobs 击杀命令杀死 |
| NEVER | FALSE, NO | - 会被普通的 mythicmobs 击杀命令杀死 |
| PERSISTENT |  | - 区块卸载时，将生物保存到世界文件中。- 服务器重启后仍然保留。- 持久化生物不会在未加载的区块中触发技能。 |
| NPC |  | - 服务器重启时消失 - 区块卸载时消失 |

> 对于PERSISTENT消失模式：要删除持久性生物，你必须使用kill命令（`/mm m kill <type>`）或将`-p`标志附加到killall命令（`/mm m killall -p`）。有关该主题的更多信息可以在[此处](../commands-and-permissions.md#mob-commands)找到。

```yml
  Options:
    Despawn: true
```

#### FollowRange {#followrange}

生物选择攻击目标或追踪实体的范围，单位为格。默认为原版跟随范围 `32`。

```yml
  Options:
    FollowRange: 32
```

#### Glowing {#glowing}

设置生物是否永久发光。默认为`false`。

```yml
  Options:
    Glowing: false
```

#### HealOnReload {#healonreload}

允许不会自然消失的生物在所在区块重新加载时恢复生命值。默认为 `false`。

```yml
  Options:
    HealOnReload: false
```

#### 隐藏 {#hidden}

如果  true  ，该生物将被排除在命令建议和生物浏览器菜单之外，这对于模板生物和内部实用生物很有用。默认为`false`。

该生物通过其内部名称保持完全可用，并且`/mm mobs list`仍然列出它。 `/mm mobs list` 是一个显示所有加载的生物（无论是否隐藏）的地方。

**这是生物定义最外层的键，不是 `Options:` 下的键。**放在 `Options:` 下不会生效。

```yml
example_mob:
  Type: ZOMBIE
  Hidden: true
```

#### Invincible {#invincible}

使生物对所有类型的伤害完全无敌。该选项无法通过命令技能更改。默认为`false`。

```yml
  Options:
    Invincible: false
```

#### Interactable {#interactable}

设置生物是否可以与之交互。如果生物是盔甲架，它将拒绝与设备进行任何交互。默认为`false`。

```yml
  Options:
    Interactable: false
```

#### LockPitch {#lockpitch}

防止生物的头部向上/向下看。默认为`false`。

```yml
  Options:
    LockPitch: false
```

#### KnockbackResistance {#knockbackresistance}

抵抗攻击击退的比例，取值为 `0` 到 `1`。即使具有 100% 击退抗性，仍可能被弓的 `ARROW_KNOCKBACK`（冲击）附魔击退。要实现真正的（  true  ）击退抗性，请参阅 [velocity](../skills/mechanics/velocity.md) 机制。默认为 `0`。

```yml
  Options:
    KnockbackResistance: 0.5
```

#### MaxCombatDistance {#maxcombatdistance}

阻止距离超过指定格数的玩家伤害此生物。将其设为小于该生物技能或攻击距离的数值，可以让生物仍能伤害玩家，减少玩家利用距离无伤攻击的情况。默认为 `256`。

```yml
  Options:
    MaxCombatDistance: 256 
```

#### MovementSpeed {#movementspeed}

生物的移动速度。大多数生物的默认移动速度为`0.2`，任何高于`1`的值往往会使生物难以或无法战斗。

```yml
  Options:
    MovementSpeed: 0.2
```

#### NoAI {#noai}

控制生物是否具有 AI。此选项会覆盖 [AIGoalSelectors](mobs.md#aigoalselectors) 中指定的 AI 行为。与 AIGoalSelectors 不同，它也适用于具有硬编码 AI 的实体。设为 `true` 时，生物永远不会施放技能。默认为 `false`。

```yml
  Options:
    NoAI: false
```

#### NoDamageTicks {#nodamageticks}

生物受伤后的无敌时间，单位为游戏刻。启用[免疫表](immunitytables.md)时，`NoDamageTicks` 按玩家分别计算，而非统一计算。默认为 `10`。

```yml
  Options:
    NoDamageTicks: 20
```

#### NoGravity {#nogravity}

生物是否不受重力影响。设为 `true` 后，生物**无法**使用 [velocity](../skills/mechanics/velocity.md) 机制。默认为 `false`。

```yml
  Options:
    NoGravity: false
```

#### PassthroughDamage {#passthroughdamage}

将生物受到的全部伤害转移给其父实体（如果存在）。父实体是最初召唤它的实体。默认为 `false`。

```yml
  Options:
    PassthroughDamage: false
```

#### PreventItemPickup {#preventitempickup}

防止生物拾取物品；默认为`true`。

```yml
  Options:
    PreventItemPickup: false
```

#### PreventLeashing {#preventleashing}

是否阻止给生物拴上拴绳。默认为 `true`。

```yml
  Options:
    PreventLeashing: false
```

#### PreventMobKillDrops {#preventmobkilldrops}

防止MythicMob的目标掉落战利品。默认为`false`。

```yml
  Options:
    PreventMobKillDrops: false
```

#### PreventOtherDrops {#preventotherdrops}

防止生物掉落其原版战利品表。默认为`false`。

```yml
  Options:
    PreventOtherDrops: false
```

#### PreventRandomEquipment {#preventrandomequipment}

防止怪物生成随机装备。默认为`false`。

```yml
  Options:
    PreventRandomEquipment: false
```

#### PreventRenaming {#preventrenaming}

防止使用名称标签对生物进行重命名。默认为`true`。

```yml
  Options:
    PreventRenaming: false
```

#### PreventSunburn {#preventsunburn}

防止生物在阳光下燃烧。默认为`false`。

```yml
  Options:
    PreventSunburn: true
```

#### PreventTransformation {#preventtransformation}

设置是否应防止生物变成其他实体。

```yaml
  Options:
    PreventTransformation: false
```

#### PreventVanillaDamage {#preventvanilladamage}

取消此生物造成的每一次“普通”原版伤害。

```yml
  Options:
    PreventVanillaDamage: true
```

#### RepeatAllSkills {#repeatallskills}

生物生命值恢复到某个阈值以上时，是否再次执行按生命值触发的技能。默认为 `false`。

```yml
  Options:
    RepeatAllSkills: false
```

#### ReviveHealth {#revivehealth}

当生物的死亡事件被取消时（通过 [Cancelevent](../skills/mechanics/cancelevent.md) 机制 [~onDeath](../skills/triggers/ondeath.md)），指定的就是生物将被设置的生命值。如果该值为`-1`，生物将恢复到其自身的最大生命值。

```yaml
#This mob will always return to 50 health every time the death event is cancelled
ExampleMob:
  Type: COW
  Health: 100
  Options:
    ReviveHealth: 50
  Skills:
  - cancelevent{sync=true} @self ~onDeath
```

```yaml
#This mob will always return to its maximum health (100) every time the death event is cancelled
ExampleMob:
  Type: COW
  Health: 100  
  Options:
    ReviveHealth: -1
  Skills:
  - cancelevent{sync=true} @self ~onDeath
```

#### Scale {#scale}

生物的缩放比例。

```yaml
  Options:
    Scale: 2
```

#### ShowHealth {#showhealth}

在指定半径内广播生物生命值。半径和消息格式分别由 `/plugins/MythicMobs/config.yml` 中的 `Mobs.ShowHealth.Radius`、`Mobs.ShowHealth.Formatting` 决定。默认为 `false`。

```yml
  Options:
    ShowHealth: false
```

#### Silent {#silent}

生物是否应该使用原版音效。默认为`false`。

```yml
  Options:
    Silent: false
```

#### UseThreatTable {#usethreattable}

生物是否应启用[仇恨表](https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/Mobs/ThreatTables)

```yaml
  Options:
    UseThreatTable: true
```

#### RandomizeProperties {#randomizeproperties}

RandomizeProperties 是生成时赋予生物不同特征的原版功能，例如装备、僵尸首领状态、动物变种、僵尸或蜘蛛骑士、体型、生成幼年个体的概率等。

```yaml
  Options:
    RandomizeProperties: false
```

# 特定类别选项 {#group-specific-options}

## Boat 与 BoatChest {#boat-boatchest}

#### 类型 {#type}

[船实体的类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Boat.Type.html)。

```yaml
  Options:
    BoatType: MANGROVE
```

## 可繁殖生物 {#breedable-mobs}

#### Age {#age}

生物年龄。幼年使用 `-1`，成年使用 `1`。适用于所有具有年龄的生物，例如绵羊、猪、牛等。大于 0 时，表示距离下次可繁殖还需等待的游戏刻数。相当于 `Age` NBT。极小的负数可使生物模型出现异常变化，但这种用法不受支持，某些情况下可能无法正常工作。默认为 `1`。

```yml
  Options:
    Age: -1
```

#### AgeLock {#agelock}

是否锁定生物年龄，可防止幼年生物随时间长大。若要让 Age 选项长期生效，必须设置此项。默认为 `false`。

```yml
  Options:
    AgeLock: true
```

#### Adult {#adult}

设置生物的成人状态。如果 `Age` 不起作用，请使用。

```yml
  Options:
    Adult: true
```

#### Baby {#baby}

设置生物的婴儿/成人状态。如果 `Age` 不起作用，请使用。

```yml
  Options:
    Baby: true
```

## 可染色生物 {#colorable-mobs}

用于马、羊驼、行商羊驼、鹦鹉、绵羊、潜影贝、热带鱼和狼。

### Color {#color}

设置生物的颜色（绵羊的羊毛颜色或狼的项圈颜色） 该值可以是此[颜色](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/DyeColor.html)中的任何一个，默认为`WHITE`。

```yml
  Options:
    Color: RED
```

## 中立实体 {#neutral-entities}

例如，用于狼和僵尸猪人。

#### Angry {#angry}

生物是否以愤怒状态生成。

> 注意：由于 Bukkit/Spigot 的一个问题，使用此选项无法让狼在生成时处于愤怒状态。
> 如果你想生成愤怒的狼，请使用AIGoalSelectors和AITargetSelectors。
> 默认为`false`。

```yaml
  Options:
    Angry: true
```

## 史莱姆与岩浆怪 {#slimes-magma-cubes}

#### PreventSlimeSplit {#preventslimesplit}

阻止史莱姆和岩浆怪分裂。默认为 `false`。

```yaml
  Options:
    PreventSlimeSplit: true
```

## 大小可变的实体 {#entities-with-variable-size}

#### Size {#size}

设置史莱姆、岩浆怪和幻翼的大小。体型可以非常大，且每次增大会呈指数增长。极大的体型会导致服务器卡顿，甚至崩溃。默认为 `1to8`，幻翼默认为 `1`。

```yaml
  Options:
    Size: 10
```

## 袭击生物 {#raiders}

#### CanJoinRaid {#canjoinraid}

该实体是否可以加入袭击。默认为`true`。

```yaml
  Options:
    CanJoinRaid: false
```

#### PatrolLeader {#patrolleader}

该实体是否是巡逻队的领导者。默认为`false`。

```yaml
  Options:
    PatrolLeader: true
```

#### PatrolSpawnPoint {#patrolspawnpoint}

默认为`false`。

```yaml
  Options:
    PatrolSpawnPoint: true
```

## 可驯服生物 {#tameable-mobs}

#### Tameable {#tameable}

玩家是否能够驯服生物。用于狼、猫和马。默认为`false`。

```yaml
  Options:
    Tameable: true
```

## 僵尸（所有变种） {#zombies-all-variants}

#### PreventJockeyMounts {#preventjockeymounts}

设置是否阻止僵尸作为骑师生成。   仅适用于僵尸。默认为`false`。

```yaml
  Options:
    PreventJockeyMounts: true
```

#### PreventConversion {#preventconversion}

防止僵尸转化为其他类型的僵尸。   默认为`false`。

```yaml
  Options:
    PreventConversion: true
```

#### ReinforcementsChance {#reinforcementschance}

僵尸在受到伤害时有机会生成增援部队。   应该是 0 和 1 之间的数字（0% 和 100% 几率）。仅适用于僵尸。默认为`0`。

```yaml
  Options:
    ReinforcementsChance: 0.38
```

# 特定生物选项 {#mob-specific-options}

这些是特定的生物选项，当用于不同的生物类型时不会产生任何效果。

## 盔甲架 {#armor-stand}

#### CanMove {#canmove}

设置盔甲架是否可以移动。默认为 `true` 并需要 PaperSpigot

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    CanMove: true
```

#### CanTick {#cantick}

设置盔甲架是否参与游戏刻更新。默认为 `true`，需要 PaperSpigot。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    CanTick: true
```

#### HasArms {#hasarms}

设置盔甲架是否有手臂。默认为`false`。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasArms: true
```

#### HasBasePlate {#hasbaseplate}

设置盔甲架是否有底板。默认为`true`

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasBasePlate: false
```

#### HasGravity {#hasgravity}

设置盔甲架是否受重力影响。默认为`true`。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasGravity: true
```

#### Invisible {#invisible-2}

设置盔甲架是否隐形。默认为`false`。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Invisible: true
```

#### ItemBody {#itembody}

指定应放入盔甲架的身体/胸部插槽中的[Mythic 物品](../items/items.md)。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemBody: AN_EXAMPLE_CHESTPLATE
```

#### ItemFeet {#itemfeet}

指定应放入盔甲架脚槽中的[Mythic 物品](../items/items.md)。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemFeet: AN_EXAMPLE_BOOTS
```

#### ItemHand {#itemhand}

指定应放入盔甲架主手槽的[Mythic 物品](../items/items.md)。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemHand: AN_EXAMPLE_SWORD
```

#### ItemOffhand {#itemoffhand}

指定应放入盔甲架副手插槽中的[Mythic 物品](../items/items.md)。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemOffhand: AN_EXAMPLE_STICK
```

#### ItemHead {#itemhead}

指定应放入盔甲架头盔槽中的[Mythic 物品](../items/items.md)。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemHead: AN_EXAMPLE_HELMET
```

#### ItemLegs {#itemlegs}

指定应放入盔甲架护腿槽中的[Mythic 物品](../items/items.md)。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemLegs: AN_EXAMPLE_PANTS
```

#### Marker {#marker}

将盔甲架设置为标记。此选项可防止盔甲架在游戏中被破坏，使其完全不可交互。默认为`false`。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Marker: false
```

#### Small {#small}

将盔甲架设置为小型版本。默认为`false`。

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Small: true
```

#### Pose {#pose}

设置身体部位的当前姿势。   默认值为 `0,0,0` 并接受类似 `#to#` 的范围。这些将位于 `Pose` 部分而不是 `Options` 部分。

###### Head {#head}

```yml
Mob:
  Type: armor_stand
  Pose:
    Head: 0,50,0
```

###### Body {#body}

```yml
Mob:
  Type: armor_stand
  Pose:
    Body: 0,10,10
```

###### LeftArm {#leftarm}

```yml
Mob:
  Type: armor_stand
  Pose:
    LeftArm: 0to360,0,0
```

###### RightArm {#rightarm}

```yml
Mob:
  Type: armor_stand
  Pose:
    RightArm: 0to90,0,0
```

###### LeftLeg {#leftleg}

```yml
Mob:
  Type: armor_stand
  Pose:
    LegLeg: 0,0to80,0
```

###### RightLeg {#rightleg}

```yml
Mob:
  Type: armor_stand
  Pose:
    RightLeg: 20,25,0
```

## 蜜蜂 {#bee}

#### Anger {#anger}

蜜蜂愤怒状态结束前的剩余时间，单位为游戏刻。设为 0 时不会愤怒。默认为 `0`。

```yaml
  Options:
    Anger: 200
```

#### HasNectar {#hasnectar}

蜜蜂是否携带花粉。   默认为`false`。

```yaml
  Options:
    HasNectar: true
```

#### HasStung {#hasstung}

蜜蜂是否蜇过实体。   默认为`false`。

```yaml
  Options:
    HasStung: true
```

#### PreventStingerLoss {#preventstingerloss}

是否防止蜜蜂在击中实体后失去毒刺。   默认为`false`。

```yaml
  Options:
    PreventStingerLoss: true
```

## 骆驼 {#camel}

#### Saddled {#saddled}

实体是否有鞍。   默认为`false`。

```yaml
  Options:
    Saddled: true
```

#### Tamed {#tamed}

该实体是否被驯服。   默认为`false`。

```yaml
  Options:
    Tamed: true
```

## 猫 {#cat}

#### CatType {#cattype}

设置猫的类型。   类型可以是 ALL_BLACK、BLACK、BRITISH_SHORTHAIR、CALICO、PERSIAN、JELLIE、RAGDOLL、RED、SIAMESE、TABBY 或WHITE。

```yaml
  Options:
    CatType: BLACK
```

#### CollarColor {#collarcolor}

设置猫项圈的颜色。   可用颜色有：BLACK、BLUE、BROWN、CYAN、GRAY、GREEN、LIGHT_BLUE、LIGHT_GRAY、LIME、MAGENTA、ORANGE、 PINK、PURPLE、RED、WHITE 或 YELLOW。

```yaml
  Options:
    CollarColor: GREEN
```

#### Tamed {#tamed-2}

该实体是否被驯服。   默认为`false`。

```yaml
  Options:
    Tamed: true
```

## 牛 {#cow}

#### Variant {#variant}

用于牛实体的变体。如果有添加更多变体的数据包，则接受命名空间。在 Minecraft Wiki 上阅读有关该主题的更多信息 [此处](https://minecraft.wiki/w/Cow#Variants) 和 [此处](https://minecraft.wiki/w/Mob_variant_definitions#Cow)

```yaml
  Options:
    Variant: WARM
```

## 鸡 {#chicken}

#### Jockey {#jockey}

鸡的 `IsChickenJockey` NBT 是否设为 1。设为   true   时，鸡可以自然消失，死亡掉落 10 点经验而非 1-3 点，而且不会下蛋。默认为 `false`。

```yaml
  Options:
    Jockey: true
```

#### Variant {#variant-2}

用于鸡实体的变体。如果有添加更多变体的数据包，则接受命名空间。在 Minecraft Wiki 上阅读有关该主题的更多信息 [此处](https://minecraft.wiki/w/Chicken#Variants) 和 [此处](https://minecraft.wiki/w/Mob_variant_definitions#Chicken)

```yaml
  Options:
    Variant: WARM
```

## 苦力怕 {#creepers}

#### ExplosionRadius {#explosionradius}

设置苦力怕爆炸的半径/功率。   负值将被忽略，爆炸半径仍然是苦力怕的默认半径。默认为`-1`。

```yaml
  Options:
    ExplosionRadius: 5
```

#### FuseTicks {#fuseticks}

苦力怕爆炸前的等待游戏刻数。负值会被忽略，改用苦力怕的默认引爆时间。默认为 `-1`。

```yaml
  Options:
    FuseTicks: 60
```

#### SuperCharged {#supercharged}

苦力怕是否以闪电苦力怕形态生成。默认为 `false`。

```yaml
  Options:
    SuperCharged: true
```

#### PreventSuicide {#preventsuicide}

防止苦力怕在爆炸时死亡。要使此选项生效，需要将游戏规则 `mobGriefing` 设为   true  。默认为 `false`。

```yaml
  Options:
    PreventSuicide: true
```

## Copper_Golem {#copper-golem}

#### WeatheringState {#weatheringstate}

傀儡的风化状态。可以是[这些值](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/CopperGolem.CopperWeatherState.html)中的任何一个

```yaml
  Options:
    WeatheringState: OXIDIZED
```

#### Waxed {#waxed}

铜傀儡是否打蜡。   默认为 `true`。

```yaml
  Options:
    Waxed: false
```

## 末影人 {#enderman}

#### PreventTeleport {#preventteleport}

适用于末影人，但//可能//适用于其他生物。可能会破坏瞬移技能！   默认为 `false`。

```yaml
  Options:
    PreventTeleport: true
```

#### HeldBlock {#heldblock}

设置末影人携带的方块。   默认为`AIR`。

```yaml
  Options:
    HeldBlock: STONE
```

## Experience_orb {#experience-orb}

#### Experience {#experience}

设置经验球生物提供的经验量。   默认为 `1`。

```yaml
  Options:
    Experience: 10
```

## 下落方块 {#falling-blocks}

#### Block {#block}

指定[方块类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)。默认为 `STONE`。

```yaml
  Options:
    Block: BIRCH_WOOD
```

#### BlockData {#blockdata}

用于输入块数据的附加字段。   默认为`0`。

#### DropsItem {#dropsitem}

是否可以掉落该下落方块对应的物品。默认为 `true`。

```yaml
  Options:
    DropsItem: false
```

#### HurtsEntities {#hurtsentities}

撞击时是否对实体造成伤害。默认为 `true`。

```yaml
  Options:
    HurtsEntities: false
```

#### ReplaceSpawnLocationBlock {#replacespawnlocationblock}

实体是否应在其生成位置替换方块。   默认为`false`。

```yaml
  Options:
    ReplaceSpawnLocationBlock: true
```

#### UseSpawnLocationType {#usespawnlocationtype}

下落方块是否采用生成位置原有的方块类型。默认为 `false`。

```yaml
  Options:
    UseSpawnLocationType: true
```

## 狐狸 {#fox}

#### FoxType {#foxtype}

确定狐狸的类型。   可以是`RED`或`SNOW`。默认为`RED`。

```yaml
  Options:
    FoxType: SNOW
```

## 青蛙 {#frog}

#### 类型 {#type-2}

确定青蛙的类型。   别名是`Variant`。可以是 `WARM`、`COLD` 或 `TEMPERATE`。默认为`WARM`。

```yaml
  Options:
    Type: COLD
```

## 山羊 {#goat}

#### Screaming {#screaming}

是否为尖叫山羊。尖叫山羊会更频繁地尖叫和冲撞。默认为 `false`。

```yaml
  Options:
    Screaming: true
```

## 疣猪兽 {#hoglin}

#### ImmuneToZombification {#immunetozombification}

疣猪兽是否免疫僵尸化。   默认为`false`。

```yaml
  Options:
    ImmuneToZombification: true
```

#### Huntable {#huntable}

疣猪兽是否能够被猪灵猎杀。   默认为`true`。

```yaml
  Options:
    Huntable: true
```

## 马、驴和骡 {#horses-donkeys-and-mules}

#### HorseArmor {#horsearmor}

用于马设置其所穿盔甲的类型。   可以是 `iron`、`gold` 或 `diamond` [armor_type] 必须为小写

```yaml
  Options:
    HorseArmor: gold
```

#### CarryingChest {#carryingchest}

用于驴子设置是否携带箱子。   默认为`false`。

```yaml
  Options:
    CarryingChest: true
```

#### HorseColor {#horsecolor}

设置马的颜色。   颜色必须大写，可以是任何一种[Spigot Horse颜色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Horse.Color.html)。

```yaml
  Options:
    HorseColor: CREAMY
```

#### Saddled {#saddled-2}

用于马匹设置是否上鞍。   如果设置了 [HorseArmor](options.md#horsearmor)，则默认为 `true`，否则默认为 `false`

```yaml
  Options:
    Saddled: true
```

#### HorseStyle {#horsestyle}

设置马的花纹，可使用任意 [Spigot Horse 花纹](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Horse.Style.html)。

```yaml
  Options:
    HorseStyle: WHITE_DOTS
```

#### Tamed {#tamed-3}

用于设置马匹是否被驯服。   默认为`false`。

```yaml
  Options:
    Tamed: true
```

#### HorseType {#horsetype}

指定马的类型，可使用任意 [Spigot Horse 变种](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Horse.Variant.html)。默认为 `HORSE`。**MC 1.11+ 已移除此项，请改用 [Type](mobs.md#type)。**

## 交互实体 {#interaction}

#### Height {#height}

交互实体的高度。   默认为 `1`。

```yaml
  Options:
    Height: 2
```

#### 宽度 {#width}

交互实体的宽度。   默认为 `Height` 选项的值。

```yaml
  Options:
    Width: 3
```

#### Responsive {#responsive}

交互实体是否有响应。   默认为`true`。

```yaml
  Options:
    Responsive: false
```

## IronGolem {#irongolem}

#### PlayerCreated {#playercreated}

是否视为由玩家建造的生物。默认为 `false`。

```yaml
  Options:
    PlayerCreated: true
```

## Item {#item}

#### Item {#item-2}

物品实体的材质。默认为 `STONE`。

```yaml
  Options:
    Item: BRICK
```

#### 数量 {#amount}

物品堆叠中的数量。默认为 `1`。

```yaml
  Options:
    Amount: 10
```

#### CanPickup {#canpickup}

该物品堆是否可以被拾取。默认为 `true`。

```yaml
  Options:
    CanPickup: false
```

## 羊驼 {#llama}

#### CarryingChest {#carryingchest-2}

设置实体是否携带箱子。   默认为`false`。

```yaml
  Options:
    CarryingChest: true
```

#### Tamed {#tamed-4}

设置实体是否被驯服。   默认为`false`。

```yaml
  Options:
    Tamed: true
```

#### Color {#color-2}

设置羊驼颜色。颜色必须大写，可以使用任意 [Spigot Llama 颜色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Llama.Color.html)。

```yaml
  Options:
    Color: CREAMY
```

## MinecartChest {#minecartchest}

#### ChestContents {#chestcontents}

将放置在箱子内的[droptable](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#drop-tables)。

```yaml
  Options:
    ChestContents: example_droptable
```

## 熊猫 {#panda}

#### MainGene {#maingene}

设置熊猫可以遗传给后代的主要[基因](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Panda.Gene.html)。   可以是 NORMAL、AGGRESSIVE、LAZY、WORRIED、PLAYFUL、WEAK、BROWN。默认为`NORMAL`。

```yaml
  Options:
    MainGene: LAZY
```

#### HiddenGene {#hiddengene}

设置熊猫可以遗传给后代的隐藏[基因](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Panda.Gene.html)。   可以是 NORMAL、AGGRESSIVE、LAZY、WORRIED、PLAYFUL、WEAK、BROWN。默认为`NORMAL`。

```yaml
  Options:
    HiddenGene: WORRIED
```

## 鹦鹉 {#parrot}

#### Variant {#variant-3}

鹦鹉的[变体](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Parrot.Variant.html)。

```yaml
  Options:
    Variant: GRAY
```

#### FlyingSpeed {#flyingspeed}

鹦鹉的飞行速度。   默认为`-1`（该选项不适用）

```yml
  Options:
    FlyingSpeed: 0.2
```

## 猪 {#pig}

#### Saddled {#saddled-3}

若猪已备鞍。   默认为`false`。

```yaml
  Options:
    Saddled: true
```

#### Variant {#variant-4}

用于猪实体的变体。如果有添加更多变体的数据包，则接受命名空间。在 Minecraft Wiki 上阅读有关该主题的更多信息 [此处](https://minecraft.wiki/w/Pig#Variants) 和 [此处](https://minecraft.wiki/w/Mob_variant_definitions#Pig)

```yaml
  Options:
    Variant: WARM
```

## 猪灵 {#piglin}

#### AbleToHunt {#abletohunt}

猪灵是否能够狩猎。   默认为`true`。

```yaml
  Options:
    AbleToHunt: false
```

#### ImmuneToZombification {#immunetozombification-2}

猪灵是否免疫僵尸化。   默认为`true`。

```yaml
  Options:
    ImmuneToZombification: false
```

## 猪灵蛮兵 {#piglin-brute}

#### ImmuneToZombification {#immunetozombification-3}

猪灵是否免疫僵尸化。   默认为`true`。

```yaml
  Options:
    ImmuneToZombification: false
```

## 兔子 {#rabbit}

#### IsKillerBunny {#iskillerbunny}

别名：`Angry`。
将兔子设为杀手兔。
默认为 `false`。

```yaml
  Options:
    IsKillerBunny: true
```

#### RabbitType {#rabbittype}

设置兔子的[类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Rabbit.Type.html)。   类型可以是 BLACK、BLACK_AND_WHITE、BROWN、GOLD、SALT_AND_PEPPER、THE_KILLER_BUNNY 或 WHITE

```yaml
  Options:
    RabbitType: SALT_AND_PEPPER
```

## 绵羊 {#sheep}

#### Sheared {#sheared}

羊是否已经剪毛。   默认为`false`。

```yaml
  Options:
    Sheared: true
```

## 蠹虫 {#silverfish}

#### PreventBlockInfection {#preventblockinfection}

防止蠹鱼感染方块。   默认为 `false`。

```yaml
  Options:
    PreventBlockInfection: true
```

## 骷髅 {#skeleton}

#### PreventConversion {#preventconversion-2}

防止骷髅转化为其他类型的骷髅。   默认为`false`。

```yaml
  Options:
    PreventConversion: true
```

## 雪傀儡 {#snow-golem}

#### Derp {#derp}

雪傀儡的南瓜是否已经被剪掉了。   默认为`false`。

```yaml
  Options:
    Derp: true
```

#### PreventSnowFormation {#preventsnowformation}

防止雪傀儡制造雪。   默认为`false`。

```yaml
  Options:
    PreventSnowFormation: true
```

## TNT {#tnt}

#### FuseTicks {#fuseticks-2}

TNT 爆炸需要多长时间。   默认为 `-1`（即时）。

```yaml
  Options:
    FuseTicks: 100
```

#### ExplosionYield {#explosionyield}

决定爆炸的强度。   默认为`-1`（使用正常的TNT爆炸当量）。

```yaml
  Options:
    ExplosionYield: 2
```

#### Incendiary {#incendiary}

爆炸是否能够引发火灾。   默认为`false`。

```yaml
  Options:
    Incendiary: true
```

## 热带鱼 {#tropical-fish}

#### Pattern {#pattern}

设置鱼的[形状/图案](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/TropicalFish.Pattern.html)。

```yaml
  Options:
    Pattern: GLITTER
```

#### BodyColor {#bodycolor}

设置鱼的[主颜色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html)。

```yaml
  Options:
    BodyColor: GRAY
```

## PatternColor {#patterncolor}

设置鱼的[次颜色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html)。

```yaml
  Options:
    BodyColor: LIME
```

## Villagers {#villagers}

#### HasTrades {#hastrades}

村民是否可以进行交易。   默认为`false`。

> 查看[交易](mobs.md#trades)

```yaml
  Options:
    HasTrades: true
```

#### Profession {#profession}

指定村民的[职业](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Villager.Profession.html)。   没有此选项的村民将在最初生成时随机选择一个职业。

```yaml
  Options:
    Profession: MASON
```

#### 类型 {#type-3}

代表[村民类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Villager.Type.html)，通常对应于他们生成的生物群落。默认为PLAINS。

```yaml
  Options:
    Type: DESERT
```

#### Level {#level}

村民职业等级，范围为 1 - 5。等级 1 的村民可以更换职业；要让它保持职业，需设为 2 或更高。设置村民职业时，此项必填。

```yaml
  Options:
    Level: 3
```

## 狼 {#wolfs}

#### Variant {#variant-5}

设置[狼变体](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Wolf.Variant.html)

```yaml
  Options:
    Variant: black
```

#### Color {#color-3}

设置狼项圈的[颜色](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html)

```yaml
  Options:
    Color: RED
```

## 僵尸村民 {#zombie-villagers}

#### Profession {#profession-2}

指定僵尸村民的[职业](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Villager.Profession.html)。   此选项还将使僵尸在使用药水治愈时变成相应的村民类型。默认为`FARMER`。

```yaml
  Options:
    Profession: MASON
```
