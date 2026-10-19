---
title: 2.0 之前的更新记录
source_url: https://wiki.mythiccraft.io/mythicmobs/changelogs/pre-2.0_changelogs
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 2.0 之前的更新记录 {#pre-20-changelogs}

## 2.0 之前的更新记录 {#pre-20-changelogs}

### v1.1.8 {#v118}

#### 通用设置 {#general}

更新 MythicMobs，支持 1.8。

#### 命令 {#commands}

添加 **/mm spawners cut [search_string]**、**/mm spawners paste** 和 **/mm spawners undo** 命令。

这些命令可以一次移动大量刷怪点，同时保留它们的相对位置，甚至可以移到其他世界。（剪切和粘贴方式与 WorldGuard 相同。）

[search_string] 接受多种输入，示例如下：

- **/mm spawners cut g:BoneCastle**——剪切 BoneCastle 组的所有刷怪点。
- **/mm spawners cut r:200**——剪切半径 200 个方块内的所有刷怪点。
- **/mm spawners cut Elementals_***——剪切名称以 *Elementals_* 开头的所有刷怪点。
- **/mm spawners cut ***——剪切世界内的全部刷怪点。

**/mm spawners paste** 会移动刷怪点。可以多次执行，但同一次剪切的后续粘贴会覆盖此前粘贴，因为刷怪点仍须保留唯一名称。

**/mm spawners undo** 会撤销上次剪切，将刷怪点放回剪切时的原位置，前提是仍选中同一批刷怪点。

#### 生物 {#mobs}

为 1.8 服务器添加新的 1.8 生物！请使用最新的 1.8 Spigot 构建，否则无法使用。

##### ARMOR_STAND {#armor_stand}

创建一个 Mythic Armor_Stand，可以自行使用它。

ARMOR_STAND 选项：

- Options.HasArms: (true/false)
- Options.HasGravity: (true/false)
- Options.Small: (true/false)
- Options.Invisible: (true/false)
- Options.ItemHead: [MythicItem Name]
- Options.ItemBody: [MythicItem Name]
- Options.ItemLegs: [MythicItem Name]
- Options.ItemFeet: [MythicItem Name]
- Options.ItemHand: [MythicItem Name]

##### GUARDIAN {#guardian}

##### ELDER_GUARDIAN {#elder_guardian}

##### ENDERMITE {#endermite}

##### RABBIT {#rabbit}

#### 问题修复与其他改动 {#bug-fixesother}

- 在 1.8 上，现在可以从更远处看到粒子效果。
- 修复部分 Bukkit 版本上 AI 的一些错误。
- 修复多个不同的 NPE 错误。
- 修复其他多项小错误。

### v1.1.4 {#v114}

**注意：v1.1.x 对生物生成代码进行了大幅重写。大多数生物配置仍可正常使用，但名称中包含“angry”或“baby”的大多数生物将不再生效。“Angry”和“Baby”已拆分为选项（分别为 Angry，以及 Age 和 AgeLock），因为它们实际上不是生物类型。BABY_ZOMBIE 等真正的生物变种仍可使用。**

#### AI 控制 {#ai-controls}

- AI 控制现在向后兼容所有受支持的 Bukkit 版本。
- 自定义 AI 现在应可在 Spigot 1.8 兼容构建上使用。

#### 技能 {#skills}

- 添加 **title** 技能，仅适用于 1.8 Spigot 兼容构建。

```
Skills:
- title [radius]:[fadeInTicks]:[displayTicks]:[fadeOutTicks]:"Title":"Subtitle"
```

#### API {#api}

- 为 Spawn 事件添加一些新的 API 方法。

#### 问题修复与其他改动 {#bug-fixesother-2}

- 修复多个不同的 NPE 错误。
- 修复目标进入其他世界时的 ThreatTable 错误。
- 修复其他多项小错误。

### v1.1.2 {#v112}

**<<color red>>注意：v1.1.x 对生物生成代码进行了大幅重写。大多数生物配置仍可正常使用，但名称中包含“angry”或“baby”的大多数生物将不再生效。“Angry”和“Baby”已拆分为选项（分别为 Angry，以及 Age 和 AgeLock），因为它们实际上不是生物类型。BABY_ZOMBIE 等真正的生物变种仍可使用。<</color>>**

#### 问题修复与其他改动 {#bug-fixesother-3}

- 修复生物死亡或消失后，计时能力有时仍继续触发的严重错误。
- 修复没有装备的生物导致的控制台错误。
- 修复生物未定义某些选项时抛出的控制台错误。
- 修复没有 Skills 的生物生成时发生的 NPE。
- 修复没有 DamageModifiers 的生物受到伤害时发生的 NPE。

### v1.1.1 {#v111}

**<<color red>>注意：v1.1.x 对生物生成代码进行了大幅重写。大多数生物配置仍可正常使用，但名称中包含“angry”或“baby”的大多数生物将不再生效。“Angry”和“Baby”已拆分为选项（分别为 Angry，以及 Age 和 AgeLock），因为它们实际上不是生物类型。BABY_ZOMBIE 等真正的生物变种仍可使用。<</color>>**

#### 刷怪点 {#spawners}

- 为刷怪点添加 RadiusY 选项。

#### 问题修复与其他改动 {#bug-fixesother-4}

- 改进生物和刷怪点的错误检查，防止部分启动错误。
- 修复苦力怕专用选项未应用的问题。
- 修复以刷怪点为目标的效果，使其定位到方块中心。
- 修复苦力怕的 preventSuicide 选项在大多数情况下不生效的问题。
- 修复 MagmaCube 的一个别名无法正常使用的问题。
- 修复 Slime 和 MagmaCube 选项无法应用的问题。
- 修复适用于死亡后事件的选项无法生效的问题。
- 修复（希望如此）生物自定义 AI 无法在区块重新加载后保留的问题。

### v1.1.0 {#v110}

**<<color red>>注意：v1.1.x 对生物生成代码进行了大幅重写。大多数生物配置仍可正常使用，但名称中包含“angry”或“baby”的大多数生物将不再生效。“Angry”和“Baby”已拆分为选项（分别为 Angry，以及 Age 和 AgeLock），因为它们实际上不是生物类型。BABY_ZOMBIE 等真正的生物变种仍可使用。<</color>>**

#### 新增功能 {#new-features}

##### AI 控制 {#ai-controls_1}

- 可以清空、添加和修改生物的 AI Pathfinder 目标。
- 可以清空、添加和修改生物的 AI TargetSelector 目标。
- 可用 AI 目标见[此处](http://xikage.elseland.net/mythicmobs/doku.php/databases/mobs/aigoals)。
- **教程见[此处](http://xikage.elseland.net/mythicmobs/doku.php/databases/mobs/customai)。**

##### 生物阵营 {#mob-factions}

- 现在可以用 **Faction** 属性为生物标记阵营。
- 生物 AI 控制新增自定义寻路目标，让生物攻击不同阵营的其他生物。
- 同一阵营的生物绝不会相互攻击。

##### 仇恨表 {#threat-tables}

- 添加威胁表。
- 添加生物选项 **UseThreatTable**，默认为 **false**。
- 在 config.yml 中添加完全禁用威胁表的选项。
- 为启用威胁表的生物添加 onEnterCombat、onDropCombat 和 onTargetChange 触发器。

启用威胁表后，生物的行为更像 RPG 游戏中的怪物。每名与其战斗的玩家都会根据造成的伤害获得威胁值，生物会攻击对它造成伤害最多的玩家（从而实现“坦克”等职责）。

玩家离开生物视线或范围过久后，威胁值会降低。

API 将包含“嘲讽”和修改玩家威胁值的方法。

#### 生物选项 {#mob-options}

添加许多新选项……

##### 动物 {#animals}

- **Options.Age: [integer]**——*设置生物年龄。*
- **Options.AgeLock: [true/false]**——*锁定生物年龄。*

##### 苦力怕 {#creeper}

- **Options.SuperCharged: [true/false]**——*设置苦力怕是否为高压状态。*

##### 豹猫 {#ocelots}

- **Options.Tameable: [true/false]**——*决定生物是否可以被驯服。*

##### 猪 {#pig}

- **Options.Saddled: [true/false]**——*设置猪是否装有鞍。*

##### 僵尸猪人与变种 {#pig-zombies-variants}

- **Options.Angry: [true/false]**——*决定生物初始是否处于愤怒状态。*

##### 蠹虫 {#silverfish}

- **Options.PreventBlockInfection: [true/false]**——*防止方块被侵染，现在应该确实生效了……*

##### 雪傀儡 {#snowman}

- **Options.PreventSnowFormation: [true/false]**——*阻止生物生成积雪。*

##### 狼 {#wolf}

- **Options.Angry: [true/false]**——*决定生物初始是否处于愤怒状态。*
- **Options.Tameable: [true/false]**——*决定生物是否可以被驯服。*

##### 僵尸与变种 {#zombies-variants}

- **Options.ReinforcementsChance**：取值为 0 到 1.0，1 表示受到伤害时有 100% 概率生成增援。

#### 效果 {#effects}

- 为效果目标添加 **EntitiesInRadius:radius:radiusY** 选项。
- 为效果目标添加 **ThreatTargets** 选项。

#### 技能 {#skills-2}

##### 新增触发器 {#new-triggers}

- 添加 **~onInteract**——玩家右键单击生物时触发。
- 添加 **~onEnterCombat**——生物进入战斗时触发。*（需要启用 ThreatTables。）*
- 添加 **~onDropCombat**——生物脱离战斗时触发。*（需要启用 ThreatTables。）*
- 添加 **~onTargetChange**——生物更换目标时触发。*（需要启用 ThreatTables。）*

##### 新增技能 {#new-skills}

- 添加 **AIRunGoalSelector** 技能——使用给定字符串修改生物的 AI Goal Selector。

- airungoalselector 'AI STRING'

- 添加 **AIRunTargetSelector** 技能——使用给定字符串修改生物的 AI Target Selector。

- airuntargetselector 'AI STRING'

- 添加 **Disguise** 技能——更改生物伪装，格式与 Disguise 选项相同。

- disguise [disguise_string]

- 添加 **Jump** 技能——让生物跳跃。

- jump [vertical_strength]:<horizontal_strength>

- 添加 **Leap** 技能——让生物从空中跃向目标。

- leap

- 添加 **Volley** 技能——发射一轮箭矢。

- volley
[#_of_arrows]:[arrow_speed]:[arrow_spread]:<fire_ticks>

##### 技能改动 {#skill-changes}

- 如果生物当前目标是非玩家实体，Damage 技能现在也会以该实体为目标。
- 半径为 0 时，DamageAll 现在会按预期工作。

#### 刷怪点 {#spawners-2}

- 添加 **/mm s resettimers [name]** 命令，用于重置冷却和预热计时器。

#### API {#api-2}

- 添加 MythicMobSpawnEvent。

#### 问题修复与其他改动 {#bug-fixesother-5}

- 修复 MythicMobs 攻击其他 MythicMobs 时，不一定激活技能的问题。
- 修复 ~onAttack 技能使用造成伤害的能力时导致递归的问题。
- 修复 onExplode 触发器不一定生效的问题。
- 修复 preventSuicide 选项阻止生物死亡后未保留生物数据的部分错误。
- 修复 projectile 技能生成的弹射物不一定造成所配置伤害的问题。
- 修复几个 NullPointerException。

### v1.0.0 正式版 {#v100-release}

#### 伪装 {#disguises}

- 添加 zombievillager、babyzombievillager 伪装。
- 伪装现在会遵循生物配置中的显示相关选项。
- 不包括涉及生物强度或功能的选项（马铠除外）。
- 包括 Horse、Ocelot、Sheep 和 Villager 伪装。

#### 马 {#horses}

- 为马添加 HorseCarryingChest 选项。

#### 问题修复与其他改动 {#bugsother}

- ShootPotion 现在使用刻而不是秒，以便与其他类似技能保持一致。
- 修复 ActivateSpawner 技能无法用于刷怪点组的问题。
- 修复新的 SafeSpawnLocation 算法中的错误。

### v1.0.0-RC3 {#v100-rc3}

#### 技能 {#skills-3}

- 添加 RemoveSelf 技能。

#### 刷怪点 {#spawners-3}

大多数刷怪点命令现在支持在刷怪点名称中使用通配符：

- ? 表示*单个字符*的通配符，* 表示*任意数量*字符的通配符。
- 例如，执行 **/mm s set T* leashrange 32**，会将所有名称以 T 开头的刷怪点的牵引范围设为 32。
- 例如，执行 **/mm s set ?at leashrange 32**，会作用于名称为 Cat、Rat、Fat 的刷怪点，但不会作用于 Matt。
- 如果在刷怪点命令中将名称设为 *，就会对全部刷怪点执行。

#### 问题修复与其他改动 {#bugsother-2}

- 进一步优化性能。
- 为几个系统添加错误检查。
- 改进对多种 Forge 整合包及模组化 Bukkit 服务器的兼容性。
- 修复计时技能偶尔在控制台抛出 ConcurrentModificationException 的问题。
- 修复 RandomSpawns 偶尔在控制台抛出 NullPointerException 的问题。
- 修复 RemoveMobs 技能，使其在移除生物前先从插件中注销。
- 修复 MovementSpeed 生物选项的一个罕见错误。
- 修复刷怪点，使其在目标方块中心生成生物。
- 修复刷怪点：现在会测量生物高度，选择合适的生成位置，不再将生物生成在过矮、无法生存的空间中。
- 修复负值 Damage Modifiers 未按预期治疗生物的问题。
- 修复 Damage 能力，使其正确归属于使用它的生物。
- 修复技能生命值范围将较小生命值写在前面时不生效的问题。
- 修复某些情况下刷怪点将生物生成到地下的问题。
- 修复玩家伪装，允许名称中使用颜色代码。
- 修复无视护甲的伤害技能可能对刚死亡的玩家再次“击杀”的问题，这会导致即使 DeathControl 等插件本应阻止掉落，玩家仍掉落物品。

### v1.0.0-RC2 {#v100-rc2}

#### 通用设置 {#general-2}

- 进一步优化性能！
- 更新以支持 Bukkit 1.7.10。
- 添加调试模式，使用 **/mm debugmode true** 启用。目前调试模式会禁用随机生成、生物刷怪点及其他一些“随机”功能，避免控制台刷屏妨碍高等级调试。
- 添加 TestEffect 和 TestSkill 实用命令，让你以自身作为“生物”、以看向的方块作为默认目标，在游戏内运行效果和技能字符串。（例如，**/mm u testeffect *target lightning*** 会在你的目标处执行闪电效果。）

#### 伪装 {#disguises-2}

- 玩家伪装现在可以通过 **Disguise: player:playername:skinname** 语法，分别指定皮肤和玩家名称。需要 LibsDisguises 构建 314 或更高版本。
- 添加 **Enderman:<held_item_name>** 伪装。
- 添加 **Skeleton** 伪装。

#### 技能 {#skills-4}

- ActivateSpawner 技能现在接受 **g:groupname** 格式的刷怪点组作为激活对象。

#### 效果 {#effects-2}

添加新的效果目标：

- Location：效果作用于世界中的指定位置。

**- effect location:[x],[y],[z] (effect)**

- Spawner：效果作用于刷怪点。

**- effect spawner:[spawner_name] (effect)**

也可以使用 **spawner:g:[group_name]** 格式选取刷怪点组。

#### API {#api-3}

- 为 MythicMobDeathEvent 添加 getMobLevel() 和 getNumberOfPlayerKills() 方法。

#### 问题修复与其他改动 {#bug-fixesother-6}

- 修复半径为 0 的刷怪点的严重错误。
- 修复生成半径逻辑中的错误。
- 修复以下刷怪点命令，使其可从控制台或命令方块执行：activate、info 和 set。
- 修复通过 **/mm m kill** 和 **/mm m killall** 命令移除生物后，仍触发死亡事件并给予玩家经验的问题。
- 修复生物死亡后仍短暂注册为活动状态的问题。
- 修复被动生物通过命令移除后，未从刷怪点注销的问题。
- 修复 dropped_item 伪装，用法示例为 Disguise: item:diamond。
- 修复将 Despawn 设为 true 后，部分生物在服务器重启后仍不消失的多个错误。
- 修复兼容模式导致生成多个坐骑的问题。

### v1.0.0-RC1 {#v100-rc1}

#### 新增生物选项 {#new-mob-options}

- **PreventMobKillDrops: (true/false)**——*阻止被此 MythicMob 杀死的生物掉落战利品。*

#### 新增伪装 {#new-disguises}

- 添加 **slime:[size]** 和 **magmacube:[size]** 伪装。

#### 问题修复与其他改动 {#bug-fixesother-7}

- 修复玩家传送到其他世界后导致 Target 距离条件出错的问题。
- 修复半径设为 0 时，刷怪点未按预期在自身上方生成生物的问题。
- 修复多处可能导致生物丢失伪装的潜在缺陷。
- 更新 CachedMobs 文件，保存生物等级，使使用生物等级时服务器重启前后更一致。
- 修复生物名称含问号时发生的错误。
- 修复凋灵骷髅伪装。
- 修复新建刷怪点时生成半径设置不正确并抛出错误的问题。

### Beta 版 v0.12.0 {#beta-release-v0120}

#### 性能大幅提升 {#massive-performance-boost}

v0.12.0 优化了许多组件以提高速度。大多数使用复杂生物的大型服务器应能看到明显的 TPS 提升。

#### 新增功能 {#new-features-2}

##### 掉落条件 {#drop-conditions}

现在可以在掉落表中使用所有条件，格式如下： <`>
SandSkeletonDrops:
Conditions:

- biome BEACH
Drops:
- WaterloggedArmor 1 0.01
  <`>

##### 物品描述改进 {#item-lore-improvements}

- 现在可以在物品描述中指定数值范围，例如 **{5-10}**，生成物品时会取该范围内的随机数。

#### 新增配置 {#new-configs}

在 **config.yml** 中添加以下配置，以改善与部分插件的兼容性：<`> compatibility: heroes-show-xp-message: true heroes-xp-message-format: You receive $xp experience for slaying $mobname mcmmo-show-xp-message: true mcmmo-xp-message-format: You receive $xp experience for slaying $mobname skillapi-show-xp-message: true skillapi-xp-message-format: You receive $xp experience for slaying $mobname vault-show-money-message: true vault-money-message-format: You receive $money for slaying $mobname <`>

#### 插件兼容性 {#plugin-compatibility}

##### Lib's Disguises {#libs-disguises}

将 Lib’s Disguises + ProtocolLib 与 MythicMobs 一起使用，可启用生物选项 **Disguise**。它能将任意生物伪装成其他实体，包括**玩家**、**下落方块**、**物品**和**矿车**。因此可以创建玩家外观的生物或敌对动物（例如将僵尸伪装成牛，就会得到一头攻击其他目标的牛）。

<`> AngryPig: Mobtype: pigzombie Display: 'Angry Pig' Health: 30 Damage: 5 Options: Disguise: pig <`>

##### EffectsLib {#effectslib}

添加多个需要安装 EffectsLib 才能使用的新效果。

##### McMMO {#mcmmo}

现在支持 McMMO！

生物可以在掉落表中使用 **mcmmo-exp [amount]** 格式，给予 McMMO 经验。

#### 新增技能 {#new-skills}

- CommandRing——*为生物周围“环形”范围内的所有玩家执行命令。*

- cmdring min_radius:max_radius:'command'

#### 新增技能触发器 {#new-skill-triggers}

- **~onPlayerKill**——*生物杀死玩家时触发。*

#### 新增生物选项 {#new-mob-options-2}

- HorseSaddled: (true/false)
- HorseArmor: (iron/gold/diamond)

#### 新增刷怪点选项 {#new-spawner-options}

- HealOnLeash (true/false)——*设为 true 时，生物被刷怪点拉回后会恢复全部生命值。*
- SpawnRadius——*此选项原本就已存在，但现在应该确实生效了！*

#### 新增效果 {#new-effects}

- ParticleRing——*在目标周围创建半径为 **ring_radius**、由 **ring_points** 个点组成的粒子圆环。*

- effect boss particlering
particle_name:ring_radius:ring_points:horizontalspread:verticalspread:count:<speed>:<y-offset>

- ParticleSquare——*在目标周围创建半径为 **square_radius** 的粒子正方形。*

- effect boss particlesquare
particle_name:square_radius:horizontalspread:verticalspread:count:<speed>:<y-offset>

#### 新增条件 {#new-conditions}

- haspotioneffect [potion_effect]:<level_number_range>
- holding [material]
- inblock [material]
- lightlevel [number_range]
- lightlevelabove [integer]
- lightlevelbelow [integer]
- mobtype [list,of,bukkit,mob,types]
- playerkills [number_range]——*匹配生物已杀死的玩家数量。*

#### 问题修复与其他改动 {#bug-fixesother-8}

- MobType 现在不区分大小写。
- 创建刷怪点时，现在可以使用 **mobname:level** 写法。
- 重写物品和掉落表系统的大部分内容，以提高性能并添加新功能。
- 添加支持，可根据 Heroes 队伍系统分配 Heroes 经验。
- 修复消息技能中 $mobname 内的变量未处理的问题。
- 修复生物追踪器，使其在服务器重启后正确追踪显示名称中包含等级的生物。
- 修复刷怪点未保存 moblevel 属性的问题。
- 修复部分 Timer 技能抛出 ConcurrentModificationException 的问题。
- 修复生物没有合适目标时 Rally 技能出错的问题。
- 修复部分物品的 null 物品描述错误。
- 修复坐骑与兼容模式相关的递归错误，该错误会生成多个坐骑。
- 修复 Summon 技能的位置逻辑错误。
- 修复 Mythic 刷怪点的 Warmup 计时器无法在重载后保留的问题。
- 修复 height 条件。
- 修复 level 条件。
- 修复 **/mm mob spawn command** 中未指定生物类型时抛出的错误。
- 修复 ChunkUnloadEvent 中抛出的 null 指针错误。
- 修复 EntityDeathEvents 中抛出的 null 指针错误。
- 修复生物字符串中连字符的显示。
- 修复某些情况下无法通过命令在指定位置生成生物的问题。
- 如果使用 ~onDeath 触发器，延迟技能现在会在生物死亡后执行。**这意味着，如果让 ~onDeath 技能调用自身，可能形成无限循环并增加服务器负担，因此不建议这样做。**

### Beta 版 v0.11.1 {#beta-release-v0111}

简化字符串解析，使所有生物变量都可用于所有技能，以及大多数使用变量的位置，包括生物名称。

#### 新增变量 {#new-variables}

- 为生物名称和消息添加 $mobuuid 变量。

#### 新增条件 {#new-conditions-2}

- mobsinchunk [number_range]
- mobsinworld [number_range]
- targetdistance [number_range]

#### 问题修复与其他改动 {#bug-fixesother-9}

- RandomSpawning 现在应遵循 WorldGuard 的 mob-spawning 旗标。
- 修复名称和消息中的 $level 变量。
- 修复掉落物重复掉落的问题。
- 修复 DropsPerLevel 不生效的问题。
- 修复随机生成中生物等级抛出的错误。
- 修复发射器射出的弹射物命中生物时抛出错误的问题。
- 修复 GCD 和 SetStance 技能。
- 修复 Equip 技能。
- 修复 biome 和 world 条件错误匹配名称相近但不同的生物群系及世界的问题。
- 显著降低更新检查的开销。

### Alpha 版 v0.11.0 {#alpha-release-v0110}

#### 新增功能 {#new-features-3}

##### 技能条件 {#skill-conditions}

- 现在可以为元技能指定条件。只有所有条件都为 true 时，才会使用该技能。技能可以使用与刷怪点及随机生成相同的全部条件（但某些对技能不太有意义的条件，效果可能不理想）。
- 条件写在元技能的 Conditions 标签下，如下所示：

<`>
SmashAttack:
Cooldown: 8
Conditions:

- targetwithin 25
Skills:
- msg 50:'$boss; &4Diiiie!' >0 0.2
...
  <`>

##### 生物等级 {#mob-levels}

- 添加**生物等级**。现在可以生成带等级的生物，并使用 **LevelModifiers** 选项，按可配置的设置进行缩放。掉落物也可通过 DropsPerLevel 标签随等级缩放；之后还可能添加一种方式，让部分掉落只在生物达到指定等级以上时出现。

设置刷怪点的 **moblevel** 属性，可以生成不同等级的生物。使用命令生成时，也可以在生物名称后加上 :level，例如 **/mm mob spawn SkeletalKnight:5**。

随机生成也支持通过 Level 选项设置生物等级。 <`>
SkeletalKnight:
Mobtype: witherskeleton
Display: '&2Skeletal Knight'
Health: 40
Damage: 8
Drops:

- GOLD_NUGGET 2 0.5
DropsPerLevel:
- GOLD_NUGGET 1 0.5
LevelModifiers:
Health: 5
Damage: 0.5
  <`>
- **重要：**使用生物缩放时，**必须**设置 **LevelModifiers.Health** 属性。其他修正项均为可选。

##### 特殊字符 {#special-characters}

Message 技能、SetName 技能和显示名称现在支持更多特殊字符：

- : 生成冒号 **:**
- ' 生成撇号 **'**
- ‐ 生成连字符 **-**

还有一些其他 HTML 字符有待发现……

#### 新增生物类型 {#new-mob-types}

- **pigzombievillager**
- **babypigzombievillager**
- **angrypigzombievillager**
- **angrybabypigzombievillager**

#### 新增技能 {#new-skills-2}

- **GCD** *将生物的**全局冷却**变量设为 # 刻，可与 **offgcd** 技能条件配合使用。*

- gcd [ticks]

- **SetName** *更改生物显示名称，可以使用与消息技能相同的全部变量。*

- setname '$mobname ($level) $mobhp/$mobmaxhp'

- **SetStance** *设置生物的 **stance** 变量，可与 **stance** 技能条件配合使用。*

- setstance [string]

- **Rally** *让附近所有指定类型的实体攻击生物当前的目标。类型也可以是 MythicMob 名称。*

- rally [horizontal_radius]:[vertical_radius]
<mobtype1>,<mobtype2>

#### 新增条件 {#new-conditions-3}

- biome [biome1],<biome2>,<biome3>, ...
- offgcd *检查生物的全局冷却变量是否已结束，该冷却可用 **gcd** 技能触发。*
- height [number_range]
- heightabove [integer]
- heightbelow [integer]
- level [number_range]
- onblock [material_type] *必须使用 Bukkit 定义的材料名称。*
- stance [string] *可与 **setstance** 技能配合使用的变量，默认姿态为 **default**。*
- targetinlineofsight
- targetnotinlineofsight
- targetwithin [integer]
- targetnotwithin [integer]
- world [world1],<world2>,<world3>, ...
- worldtime [number_range]

*[number_range] 可以是 =10、>10、<15 之类的数值，也可以是 1-20 之类的范围。*

#### 效果 {#effects-3}

##### 新增效果位置 {#new-effect-position}

- **playersinradius:#**——*对 # 个方块范围内的所有玩家施加效果。*

##### 新增效果 {#new-effects_1}

- **particleline**——*根据给定参数，在 Boss 与目标位置之间创建粒子线。如果目标位置设为 boss，实际上不会有什么效果，因为 Boss 以自身为目标，无法形成明显的线。*

- effect target particleline
particleName:horizontalSpread:verticalSpread:amount:<speed>:<y-offset>:<particleSpacing>
=HP <chance>

#### 问题修复 {#bug-fixes}

- 修复能力早于预期触发的问题。
- 修复 1.7.9 中僵尸有时生成为幼年僵尸的问题。

### Beta 版 v0.10.8 {#beta-release-v0108}

- 添加对 1.7.9 的支持。
- 修复多项小错误。

### Beta 版 v0.10.5 {#beta-release-v0105}

**注意：此构建引入了许多性能相关的更改和调整。建议先测试，再放到正式服务器。**

#### 性能改动 {#performance-changes}

此更新包含许多性能调整和一些新选项，帮助解决部分服务器自 v0.10 发布后出现的卡顿。最近加入的计时技能，以及用于防止生物丢失技能和掉落物的新生物扫描器，增加了大量开销，因此我进行了一些较大改动来提高性能。

我在 config.yml 中添加了以下两个选项：

- **general.clock-interval**——*控制 MythicMobs 内部时钟的间隔，单位为刻。默认为 1（每刻）。更改后需要重启插件。建议每次增加 5。*
- **general.scanner-interval**——*控制 MythicMobs 扫描世界、重新识别或移除丢失自身身份的 Mythic 生物的频率，单位为秒。默认为 20 秒。*

**clock-interval** 不会影响计时器、刷怪点等的触发频率，这与我先前可能在注释中所说的不同，因为现在已经修复。但如果将 clock-interval 设得较高，某些预定触发间隔比内部时钟更短的计时器，就无法达到预期频率，因为时钟精度不够。不建议将 clock-interval 设为超过 20 刻，不过这样做也不会真正损坏什么，只是某些行为可能稍显奇怪。

提醒一下，config.yml 中还有以下选项可用于调整性能：

- **general.spawns-interval**——*控制 MythicMobs 刷怪点的更新间隔，单位为秒。更改它会影响刷怪点 Cooldown 和 Warmup 属性的计时速度。*
- **general.save-interval**——*控制 MythicMobs 的保存间隔，单位为分钟。默认为 5。*

#### 新增生物类型 {#new-mob-type}

- 添加 **chickenjockey** 生物类型。鸡骑士的鸡单独存在时没有特殊行为，但如果僵尸骑上它，就会攻击玩家。

#### 新增生物选项 {#new-mob-options-3}

- 添加 FuseTicks 选项——仅限苦力怕，设置苦力怕爆炸前所需的刻数。
- 添加 ExplosionRadius 选项——仅限苦力怕，设置爆炸半径／威力。

#### 问题修复与其他改动 {#bug-fixes-other}

- 修复 Heroes EXP、SkillAPI Exp 和 Vault 货币不一定正确发放的问题。
- 修复计时技能的一条罕见错误消息。
- 修复 MythicMobs 生物扫描器实际运行频率远高于预期的问题。
- 进行其他多项性能调整。

### Beta 版 v0.10.2 {#beta-release-v0102}

- 修复生物未装备护甲的问题。

### Beta 版 v0.10.1 {#beta-release-v0101}

#### 问题修复与其他改动 {#bug-fixes-other-2}

- 将基于计时器的技能改为使用生物当前目标作为技能目标。
- 修复数量和概率，使其对掉落表内所有掉落类型生效。
- 修改掉落表数量，允许所有掉落类型使用 #-# 范围。
- 修复启动时调试功能不生效的问题。
- 修复作用于生物目标的效果错误。
- 修复物品属性在启动时产生无关错误的问题。
- 修复生物未放弃已被杀死目标的仇恨的问题。
- 修复苦力怕爆炸伤害未正确更改的问题。
- 修复苦力怕未遵循方块爆炸保护的问题。

### Beta 版 v0.10.0 {#beta-release-v0100}

**注意：此版本修复部分物品属性错误，并将应用方式改得更合理。这可能影响你的服务器，如有顾虑请先测试！例如，将 MovementSpeed 设为 0.1，现在会增加 +10% 移动速度，而不是增加较为随意的固定 +0.1 移动速度。**

#### 新增功能 {#new-features-4}

- 添加对 1.7.5 的支持。
- 添加对 1.6.4 的支持。
- 添加**技能触发器**。现在可以在技能生命值修正前写入 **~eventname**，或用它替代生命值修正，以指定事件触发器。某些触发器会在合理情况下忽略生命值修正（主要为 onSpawn、onDeath），这些触发器不要求指定生命值修正。如果不指定事件，技能仍按此前方式工作，*即像目前一样在 onSpawn、onDeath、onAttack 和 onDamaged 时触发*。当前触发器包括：

* onSpawn——*生物生成时调用* * onDeath——*生物死亡时调用* * onAttack——*生物造成伤害时调用* * onDamaged

- *生物受到伤害时调用* * onExplode——*生物爆炸时调用（仅苦力怕）* * onTeleport——*生物传送时调用（仅末影人）* * onTimer:#——*每 # 刻调用一次（**不**适用于元技能）*

例如，以下苦力怕只会在爆炸时用闪电击中附近所有目标： <`>
LightningCreeper:
Mobtype: poweredcreeper
Display: '&2Lightning Creeper'
Health: 40
Damage: 8
Options:
PreventSuicide: true
Skills:

- lightningall 6:5 ~onExplode >0 1
- lightningall 10:1 ~onTimer:40 >0 1
  <`>
- 为 RandomSpawns 添加 **SpawnMethod** 属性，可设为 **add** 或 **replace**，默认为 **add**。Add 与目前随机生成的方式相同，向世界添加新生物；“replace”则让生成的生物有机会替换其他生物。
- 添加 SkillAPI 支持。安装 SkillAPI 后，可以使用 **skillapi-exp [amount]** 作为掉落。
- 添加 MythicDrops 支持。现在可以使用 **mythicdrop
  <tier>** 作为掉落，前提是安装了 MythicDrops。

#### 新增生物选项 {#new-mob-options-4}

- 添加 PreventSuicide 选项（默认 false）——防止苦力怕生物在爆炸时死亡。

#### 新增生成条件 {#new-spawning-conditions}

- dawn
- day
- dusk
- night

#### 问题修复与其他改动 {#bug-fixes-other-3}

- 修复物品属性的一些错误。
- 在适当情况下，某些物品属性现在会以百分比修正应用，而不是固定值。
- 添加额外检查，防止生物丢失掉落物和技能。
- 可能修复了 Despawn 设为 true 时，被动生物仍不消失的问题。
- 如果定义了苦力怕的 Damage 值，其爆炸破坏量现在会以该值为依据。
- 修复部分类型生物无法通过随机生成产生的问题。
- 修复通过命令方块生成生物的问题。
- 希望修复了随机生成数量高于预期的问题（我自己无法验证）。
- 修复冷却未考虑小数的问题。
- 修复小于 1 的技能冷却完全未被识别的问题。
- 修复掉落表内部分物品在每次击杀生物后成倍增加的问题。
- 修复其他多项错误。

### Beta 版 v0.9.0 {#beta-release-v090}

#### 新增功能 {#new-features-5}

- 生物堆叠——如果一个坐骑还不够，现在可以创建生物堆叠：

<`> SheepStack: MobStack: StaticallyChargedSheep,StaticallyChargedSheep,StaticallyChargedSheep,StaticallyChargedSheep <`>

- 刷怪点组命令——大多数刷怪点命令现在接受 **g:groupname** 替代刷怪点名称，并修改该组关联的全部刷怪点。
- 技能现在可以使用百分比生命值修正，例如 **=50%** 或 **<25%** 等。
- 生命值修正现在会随生物最大生命值缩放，包括装备提供的生命值，以及生物等级缩放增加的生命值（将在后续构建加入）。也就是说，生物最大生命值为 200、技能设为在 =100 触发时，如果装备或缩放使生物拥有 400 生命值，该技能就会在 200 生命值时触发。这是未来生物等级和缩放所必需的。
- 现在可以为每个技能使用多个生命值修正，以逗号分隔。因此以下技能字符串有效：

<`>

- skill dosomething =75%,=50%,<200
  <`>
- 添加 WorldGuard 支持。
- 为所有生物添加 **ShowHealth** 选项，并在 config.yml 中添加 **show-health-radius** 和 **show-health-format** 两个配置值。

ShowHealth 设为 true 时，生物每变化 10% 生命值，就会向半径内所有玩家显示一条消息。格式支持颜色代码，以及 $mobname、$mobhp、$mobmaxhp 和 $percent 变量。

#### 新增刷怪点属性 {#new-spawner-attributes}

- 现在可以通过设置 **mobtype** 属性，更改刷怪点的生物类型。

#### 新增生成条件 {#new-spawning-conditions-2}

WorldGuard 条件，其中 region 可以是用逗号分隔的区域名称列表：

- inregion [region]
- notinregion [region]

also:

- inside [true/false]

#### 新增与更新的技能 {#newupdated-skills}

- 添加 Mount 技能。
- 添加 Dismount 技能。
- 添加 SpawnPassenger 技能。
- 添加 EjectPassenger 技能。
- 添加 MountPlayer 技能。
- 添加 TeleportLocation 技能。
- 添加 RemoveMobs 技能。
- 添加 ToggleLever 技能。
- 添加 SetHealth 技能。
- 添加 SetMaxHealth 技能。

#### 问题修复与其他改动 {#bug-fixes-other-4}

- 生物现在应会在达到预定生命值时立即使用能力，而不是再受一次攻击后才使用。
- 修复 spawners/listnear 命令涉及多世界的错误。
- 修复 Message 技能无法正确显示生物生命值的问题。
- RepeatAllSkills 选项现在应按预期工作。
- 修复生命值修正中的范围，使其正确生效。
- 进行一些重构和优化。

### Beta 版 v0.8.2 {#beta-release-v082}

#### 问题修复 {#bug-fixes-2}

- 修复 Vault 支持中的错误。

### Beta 版 v0.8.1 {#beta-release-v081}

#### 问题修复 {#bug-fixes-3}

- 修复死亡时显示名称丢失颜色代码的问题。
- 修复 Heroes 经验相关错误。
- 修复未安装 Vault 的服务器上的错误。

### Beta 版 v0.8.0 {#beta-release-v080}

#### 新增功能 {#new-features-6}

- 生物现在可以拥有坐骑（目前限制为 1 个）！使用 Riding: 属性，值为另一个 MythicMob 的名称，例如：

<`> Herobrine: Mobtype: witherskeleton Display: '&4Herobrine' Health: 50 Riding: MrEd <`>

添加大量其他插件兼容支持！

- 添加 BarAPI 支持。
- 添加 Heroes 支持。
- 添加 LanguageAPI 支持。
- 添加 PhatLoots 支持。
- 添加 Vault 支持。

#### 新增技能 {#new-skills-3}

- **BarTimer** *创建显示指定消息的进度条，持续 # 秒。**需要 BarAPI。***

- bartimer [radius]:[seconds]:'Message' <health>
<chance>

#### 新增掉落类型 {#new-drop-types}

- 添加 **heroesexp #**——给予击杀者 # 点 Heroes 经验。需要 Heroes。
- 添加 **phatloot [phatloot_name]**——Boss 会从指定 PhatLoot 生成战利品并掉落物品。需要 PhatLoots。
- 添加 **money #**——通过 Vault 给予金钱。需要 Vault 及相应经济插件。

#### 新增生物选项 {#new-mob-options-5}

- 添加 AlwaysShowName 选项（默认 false）——决定始终显示生物名称，还是只在被看向时显示。
- 添加 PreventItemPickup 选项（默认 true）——阻止僵尸等生物拾取玩家掉落的物品。
- 添加 PreventBlockInfection 选项（默认 true）——阻止蠹虫侵染石头方块。
- 添加 HorseTamed 选项（默认 true）——决定马是否已驯服。

#### 物品改进 {#item-improvements}

- 物品描述现在可以使用 $player 和 $boss，在物品掉落时显示生物名称和击杀者名称。

#### 问题修复 {#bug-fixes-4}

- 修复 Damage 技能的一两个错误。
- 修复 Firework 和 RadiusFirework 效果。
- 修复许多其他错误。

### Beta 版 v0.7.0 {#beta-release-v070}

**重要：至少请阅读下文关于物品和掉落表更改的说明。**

#### API {#api-4}

- 添加 MythicMobSkillEvent()，每当生物执行 Mythic Mob 技能时触发。即使该技能并不存在于 Mythic Mobs 中，也会调用此事件，因此可以用它创建自定义技能。

#### 新增功能 {#new-features-7}

- Mythic 刷怪点现在可以像随机生成一样使用生成条件。
- 通过几个新的游戏内命令添加和移除刷怪点条件，并可在 **/mm s info** 下查看。

#### 新增命令 {#new-commands}

- **/mm spawner addcondition [spawner_name] [condition]
[value]**
- **/mm spawner removecondition [spawner_name] [condition]**

#### 新增生成条件 {#new-spawning-conditions-3}

这些应该都很容易理解……我想是这样。很快会将它们加入插件手册。

- lunarphase [phase] *（[phase] 可以是对应月相的游戏内天数列表，以逗号分隔，范围为 0 到 7。）*
- outside [true/false]
- playerwithin [distance]
- playernotwithin [distance]
- raining [true/false]
- sunny [true/false]
- thundering [true/false]

#### 掉落表改动 {#drop-table-changes}

我原本尝试沿用 EpicBoss 的掉落表和物品掉落格式，但实际使用起来不够合理，也造成了不少困惑，所以最后改了一些地方。**这会破坏现有物品配置，请见谅，目前毕竟还是测试版！**

- 装备使用的格式基本相同：**- MythicItem:slot
  <amount> <chance>**
- MythicItem 掉落改用略有不同的格式：**- MythicItem
  <amount> <chance>**
- 使用物品的掉落表现在采用以下格式：**- [item_id]:<data_value> <amount> <chance>**
- 经验现在使用 **- exp <amount>** 格式。

Chance 是 0 到 1 之间的整数，1 表示 100% 概率。Amount 可以是单个数值，也可以是 1-20、30-100 等范围。

因此，以下示例会掉落 100 经验及 32 到 64 个金粒：
<`>
SkeletonKingDrops:
Drops:

- 371:0 32-64 1
- exp 100
  <`>

#### 问题修复 {#bug-fixes-5}

- 修复 0.6.5 中导致无法创建刷怪点的错误……（哎呀）
- 修复复制的刷怪点共用生物表，以及不生成新生物的问题。
- 修复另一个经验掉落错误。
- 修复物品数量范围未随机取值的问题。
- 修复 outside 条件不一定生效的问题。

### Beta 版 v0.6.5 {#beta-release-v065}

#### API {#api-5}

- 添加 MythicMobDeathEvent()，供希望接入以实现兼容的开发者使用。
- 未来还会添加更多 API 内容；这部分已经完成，因此先与错误修复一起发布。

#### 新增功能 {#new-features-8}

- 现在可以直接在 Drops 下使用 **exp #** 为生物添加经验，无需掉落表。

#### 问题修复 {#bug-fixes-6}

- 希望修复了 MythicMob 物品与其他插件配合不佳的问题，即使物品“Options”下没有添加任何属性，也可能出现该问题。
- 给物品添加属性仍可能导致奇怪行为，因为 Bukkit 还没有用于这些功能的 API。
- 修复战利品掉落的一些错误。
- 修复生物未掉落所配置经验数量的问题。
- 修复效果不一定正确触发的一些错误。
- 修复使用多个世界并重新加载其中一个世界时，刷怪点失效的问题。
- 修复其他多项错误。

#### 已知问题 {#known-issues}

- 掉落表中的数量范围未按预期工作。
- 世界卸载并重新加载后，刷怪点有时可能多生成一个生物。

### Beta 版 v0.6.0 {#beta-release-v060}

#### 新增功能 {#new-features-9}

- Mythic 生物刷怪蛋（通过 **/mm eggs** 或 **/mm e** 访问）。
- 实用命令（通过 **/mm utilities** 或 **/mm u** 访问）。

目前唯一的实用命令可以方便地查找所看方块的坐标，供 pushbutton 技能使用。

#### 新增技能 {#new-skills-4}

- **PushButton** *按下指定坐标处的按钮，激活红石。*

- pushbutton x:y:z

#### 新增刷怪点属性 {#new-spawner-attributes-2}

- LeashRange——为生物刷怪点设置牵引范围。生物离刷怪点超过该范围时，会被传送回刷怪点。

#### 问题修复与其他改动 {#bug-fixes-other-5}

- 生物现在会对狼等其他生物使用更多技能。
- 修复生物刷怪点和未加载区块引起的更多生物复制问题。
- 改用更好的缓存格式。**你可能需要删除并重新生成 SavedData/CachedMobs.yml。**
- 技能冷却和延迟现在应能更平滑、更可预测地衔接。\
- 修复其他多项错误并进行优化。

### Beta 版 v0.5.3 {#beta-release-v053}

#### 问题修复 {#bug-fixes-7}

- 大多数情况下现在可以按名称引用物品，为未来物品 ID 不再存在的情况做准备。
- 修复物品 Data 值不生效的问题（修复玩家头颅相关问题）。
- 修复区块卸载时可能导致生物刷怪点失效的几个问题。
- 修复生物用弓攻击时不使用能力的问题。
- 修复与刷怪点和未加载区块有关的其他错误。
- 可能修复了史莱姆在不应分裂时分裂的问题？（需要更多测试）

### Beta 版 v0.5.0 {#beta-release-v050}

#### 主要功能 {#major-features}

- Mythic 生物刷怪点（通过 **/mm spawners** 或 **/mm s** 访问）。

Mythic 生物刷怪点可以创建根据特定条件在某个位置生成生物的“刷怪点”。它既可以像普通刷怪笼一样工作，也可以设置较长冷却来生成 Boss。可以通过计时器生成；关闭计时器后，也可以只通过命令，或由其他 Mythic 生物使用新的 spawner 技能来生成。

输入 **/mm spawners**（或 **/mm s**）会显示全部刷怪点命令。创建刷怪点后，可以用 **/mm s set [spawner_name] [attribute] [value]** 设置属性。只输入 **/mm s set** 会显示属性列表及其作用。

我很快会发布刷怪点教程。不过，熟悉服务器管理的服主应该可以仅根据游戏内命令及其提供的信息弄清用法。

#### 新增技能 {#new-skills-5}

- **Spawner** *激活一个 Mythic 生物刷怪点。*

- spawner [name] =HP <chance>

#### 新增生物设置 {#new-mob-setting}

- 为所有生物添加 Despawn 设置。

#### 问题修复 {#bug-fixes-8}

- 为命令添加许多异常捕获，以防止错误。
- 进行多项修复，防止铁傀儡等不会自然消失的生物丢失 Mythic Mobs 技能。
- 修复多项错误。

### Beta 版 v0.4.0 {#beta-release-v040}

** 删除示例文件，即可在本次更新中获取更新后的文件！ **

#### 主要功能 {#major-features-2}

*随附示例配置展示了这些功能的用法。文档会在之后提供。*

- 伤害修正——允许调整生物从特定来源受到的伤害，将该来源的伤害乘以指定数值。
- 物品命令（**/mm items**）。

以下绵羊不会受到火焰伤害，只会受到 20% 的熔岩伤害： <`> FireResistantSheep: Mobtype: sheep DamageModifiers: - LAVA 0.2 - FIRE 0 - FIRE_TICK 0 <`>

使用内置伤害原因，可以在此处找到：
<http://jd.bukkit.org/rb/doxygen/de/d62/enumorg_1_1bukkit_1_1event_1_1entity_1_1EntityDamageEvent_1_1DamageCause.html>

#### 命令 {#commands-2}

现在可以使用 mobs spawn 命令，在指定 x,y,z 位置生成生物：

- **/mythicmobs mobs spawn [amount] [world],[x],[y],[z]**

#### 新增选项 {#new-options}

为生物添加许多新选项，见随附示例……

- **PreventOtherDrops**——*True/False，默认为 False。阻止掉落未在 Mythic Mobs 中配置的物品。*
- **PreventLeashing**——*True/False，默认为 True。阻止为 Mythic 生物拴上拴绳。*
- **PreventRenaming**——*True/False，默认为 True。阻止使用命名牌更改 Mythic 生物名称。*
- **RepeatAllSkills**——*True/False，默认为 False。设为 True 后，使用 =HEALTH 技能时，如果生物恢复到高于该生命值，再次达到条件时会重复施放技能。*
- **PreventSlimeSplit**——*True/False，默认为 False。防止 Mythic 生物中的 Slime 和 MagmaCube 死亡时分裂。*
- **PreventTeleporting**——*True/False，默认为 False。阻止 Mythic 生物传送，主要用于末影人。*

很快会随文档添加完整的生物选项列表。

#### 新增技能 {#new-skills-6}

添加 5 个新的特殊技能。在这些技能名称末尾加上“all”，除了玩家之外，它们还会命中附近其他生物；其余行为完全相同。

- **damageall**
- **igniteall**
- **pullall**
- **throwall**
- **lightningall**

#### 新增效果 {#new-effects-2}

- **particles** - *按指定参数在目标位置创建粒子效果。*

- effect boss particles
particleName:horizontalSpread:verticalSpread:amount:<speed>:<y-offset>
=HP <chance>

文档完成前，可在这里查看可用粒子列表（使用其中的“coding name”）：
<http://minecraft.gamepedia.com/Particles>

#### 问题修复 {#bug-fixes-9}

- 修复未设置显示名称的生物生成时报错的问题
- 修复物品显示名称的问题
- 修复物品的“amount”默认值不是 1 的问题
- 修复史莱姆生命值设置不正确的问题
- 纠正一个有误的物品示例……
- 修复其他多项错误。

### Beta 版 v0.3.0 {#beta-release-v030}

#### 主要功能 {#major-features-3}

*随附示例配置展示了这些功能的用法。文档会在之后提供。*

- 自定义物品
- 生物装备
- 生物掉落物
- 掉落表

**关于装备：**物品功能大体与 EpicBoss Gold Edition 相同，但 MythicMobs 不强制使用掉落表配置装备。可以直接在“Equipment”下，按 **ItemName:slot** 格式填写 items 文件夹中定义的物品名称。也可以继续使用掉落表；如果掉落表与物品同名，会优先使用掉落表。接下来的几个构建中，计划允许直接在生物配置中填写基础物品，无须先创建自定义物品。

#### 新增技能 {#new-skills-7}

*技能在大多数情况下与 EpicBoss Gold Edition 中的技能用法相同，相关文档见这里：*
<http://www.epicboss.empirehostings.net/Support/showthread.php?tid=4551>

- **Ignite** *使半径范围内的玩家着火，持续指定的游戏刻数。如果 radius = 0，则只作用于正在攻击的玩家。*

- ignite radius:ticks

- **Equip** *让 Boss 装备 items 文件夹中定义的物品。*

- equip itemname:slot

- **Explosion** *在半径范围内的玩家处产生爆炸，并使其着火，持续指定的游戏刻数。如果 radius = 0，则只作用于正在攻击的玩家。*

- explosion
radius:power:<fire(true/balse)>:<destroyblocks(true/false)>

- **Weather** *更改天气，可设为 rain、thunder 或 sunny。*

- weather type:duration

#### 问题修复 {#bug-fixes-10}

- 修复发布前最后发现的随机生成条件问题

#### 从 EBGE 转换 {#converting-from-ebge}

要让 EBGE 的 Items 和 Loots 配置适用于 MythicMobs，只需进行以下修改：

- 将 Tags 改为 Options
- 将 Loots 改为 Drops
- 将 Lores 改为 Lore
- 将 Enchants 改为 Enchantments

### Beta 版 v0.2.0 {#beta-release-v020}

#### 主要功能 {#major-features-4}

- 随机生成系统
- 随机生成条件（目前仅添加了“outside”条件，示例文件中已有演示）

#### 新增技能 {#new-skills-8}

*技能在大多数情况下与 EpicBoss Gold Edition 中的技能用法相同，相关文档见这里：*
<http://www.epicboss.empirehostings.net/Support/showthread.php?tid=4551>

- ForcePull
- ForcePullNear
- NewTarget
- Potion
- PotionBoss
- PotionMobs
- Pull
- RandomSkill
- ShootFireball
- ShootPotion
- Projectile
- ShootSkull

#### 新增效果 {#new-effects-3}

- endersignal

- effect boss endersignal =HP <chance>

- firework

- effect boss firework
<type>:<colors>:<fadecolors>:<flicker>:<trail>:<flightduration>
=HP <chance>

- flames

- effect boss flames =HP <chance>

- lightning

- effect boss lightning =HP <chance>

- smoke

- effect boss endersignal =HP <chance>

- radiusfirework

- effect boss radiusfirework
<type>:<colors>:<fadecolors>:<flicker>:<trail>:<flightduration>
=HP <chance>

#### 其他改动 {#other-stuff}

- 添加 Metrics 统计

### Beta 版 v0.1.0 {#beta-release-v010}

首次公开开发版本！

#### 主要功能 {#major-features-5}

- 创建生物
- 生物技能与创建“元”技能
- 效果系统的初步实现

#### 即将推出 {#coming-soon}

- 自定义生物刷怪点
- 物品或装备
- 位置
- 随机生成
- 生物生成蛋
- 定时器

技能在大多数情况下与 EpicBoss Gold Edition 中的技能用法相同，相关文档见这里：
<http://www.epicboss.empirehostings.net/Support/showthread.php?tid=4551>

MythicMobs 与 EBGE 的区别包括：

- 技能中的 health 和 chance 字段为可选项；省略时，技能触发概率为 100%
- Boss 属性称为“options”，不再称为“tags”

#### 技能 {#skills-5}

- command（或 cmd）
- consume
- damage
- damageself
- effect
- healself（或 heal）
- lightning
- message（或 msg）
- radiuscommand
- skill（即“pack”或元技能）
- suicide
- summon（即 swarm）
- teleport
- teleportnear
- throw

#### 效果 {#effects-4}

- sound
- explosion

#### 生物选项 {#mob-options-2}

EBGE 的所有 options/tags 都应可用，如有遗漏请告知。完整列表见这里：
<http://www.epicboss.empirehostings.net/Support/showthread.php?tid=4548>

#### 欢迎反馈！ {#feedback-is-appreciated}

请通过工单反馈所有漏洞相关问题，通过论坛提交建议。
