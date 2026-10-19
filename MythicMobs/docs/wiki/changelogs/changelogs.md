---
title: 更新记录
source_url: https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 更新记录

1. [5.13.1](changelogs.md#5131)
   1. [常规](changelogs.md#general)
   2. [条件](changelogs.md#conditions)
   3. [目标选择器](changelogs.md#targeters)
      1. [新增：bound](changelogs.md#new-bound)
   4. [触发器](changelogs.md#triggers)
      1. [新增：onPlayerEnter / onPlayerExit](changelogs.md#new-onplayerenter-onplayerexit)
      2. [边界形状](changelogs.md#bounds-shapes)
   5. [对话框](changelogs.md#dialogs)
2. [5.13.0](changelogs.md#5130)
   1. [常规](changelogs.md#general-2)
   2. [属性](changelogs.md#stats)
   3. [机制](changelogs.md#mechanics)
      1. [新增：过场动画系统](changelogs.md#new-cinematics-system)
      2. [新增：clearpath](changelogs.md#new-clearpath)
      3. [坐骑模式](changelogs.md#mount-mode)
      4. [OnDeath 光环组件](changelogs.md#ondeath-aura-component)
      5. [光环组件 cancelOn* 选项](changelogs.md#aura-component-cancelon-flags)
      6. [杂项](changelogs.md#misc)
   4. [条件](changelogs.md#conditions-2)
      1. [新增：isCancelled](changelogs.md#new-iscancelled)
      2. [新增：skyLightLevel](changelogs.md#new-skylightlevel)
      3. [entityType 条件：嵌套变种匹配](changelogs.md#entitytype-condition-nested-variant-matching)
      4. [杂项](changelogs.md#misc-2)
   5. [目标选择器](changelogs.md#targeters-2)
      1. [新增：targetinvulnerable](changelogs.md#new-targetinvulnerable)
      2. [mythic / vanilla 过滤器](changelogs.md#mythic-vanilla-filters)
      3. [新增：展示实体／交互实体目标过滤器](changelogs.md#new-displayinteraction-target-filters)
      4. [杂项](changelogs.md#misc-3)
   6. [生物](changelogs.md#mobs)
      1. [新增：默认等级](changelogs.md#new-default-level)
      2. [杂项](changelogs.md#misc-4)
   7. [触发器](changelogs.md#triggers-2)
      1. [新增：onEnterBounds / onExitBounds](changelogs.md#new-onenterbounds-onexitbounds)
   8. [占位符](changelogs.md#placeholders)
      1. [新增：min / max / clamp](changelogs.md#new-min-max-clamp)
      2. [杂项](changelogs.md#misc-5)
   9. [物品](changelogs.md#items)
   10. [API](changelogs.md#api)
   11. [兼容性](changelogs.md#compatibility)
   12. [错误修复／其他](changelogs.md#bug-fixes-other)
3. [5.12.1](changelogs.md#5121)
   1. [常规](changelogs.md#general-3)
   2. [属性](changelogs.md#stats-2)
      1. [新增：MUTATOR 属性](changelogs.md#new-mutator-stats)
   3. [命令技能](changelogs.md#command-skills)
      1. [命令父级](changelogs.md#command-parent)
   4. [机制](changelogs.md#mechanics-2)
      1. [OnAttack 光环组件](changelogs.md#onattack-aura-component)
      2. [ToggleSitting](changelogs.md#togglesitting)
   5. [条件](changelogs.md#conditions-3)
      1. [新增：canBeHitByProjectile](changelogs.md#new-canbehitbyprojectile)
      2. [新增：petsitting](changelogs.md#new-petsitting)
   6. [触发器](changelogs.md#triggers-3)
      1. [新增：onEffectRemove](changelogs.md#new-oneffectremove)
   7. [物品](changelogs.md#items-2)
      1. [CustomModelData 组件](changelogs.md#custommodeldata-component)
   8. [API](changelogs.md#api-2)
   9. [错误修复／其他](changelogs.md#bug-fixes-other-2)
4. [5.12.0](changelogs.md#5120)
   1. [常规](changelogs.md#general-4)
   2. [属性系统](changelogs.md#stats-system)
   3. [机制](changelogs.md#mechanics-3)
      1. [新增：光环组件](changelogs.md#new-aura-components)
      2. [新增：removeTaggedAuras](changelogs.md#new-removetaggedauras)
      3. [新增：Charges / CooldownMode](changelogs.md#new-charges-cooldownmode)
      4. [新增：addSkillCharges](changelogs.md#new-addskillcharges)
      5. [新增：showDialog](changelogs.md#new-showdialog)
      6. [新增：closeDialog](changelogs.md#new-closedialog)
      7. [新增：hide](changelogs.md#new-hide)
      8. [新增：enchantItem](changelogs.md#new-enchantitem)
      9. [新增：SetCustomMenuTitle](changelogs.md#new-setcustommenutitle)
      10. [Wait](changelogs.md#wait)
      11. [Sudo](changelogs.md#sudo)
      12. [Heal](changelogs.md#heal)
      13. [DropItem](changelogs.md#dropitem)
      14. [Sound](changelogs.md#sound)
      15. [Projectile](changelogs.md#projectile)
      16. [Throw](changelogs.md#throw)
      17. [自定义菜单](changelogs.md#custom-menus)
   4. [条件](changelogs.md#conditions-4)
      1. [新增：input](changelogs.md#new-input)
      2. [新增：skillIsRecharging](changelogs.md#new-skillisrecharging)
      3. [新增：statDamageModifier](changelogs.md#new-statdamagemodifier)
      4. [新增：inLiquid](changelogs.md#new-inliquid)
      5. [新增：isFrozen](changelogs.md#new-isfrozen)
      6. [新增：uuid](changelogs.md#new-uuid)
      7. [新增：goatHorn](changelogs.md#new-goathorn)
      8. [新增：isSheared](changelogs.md#new-issheared)
      9. [新增：trim](changelogs.md#new-trim)
      10. [新增：blockAbove](changelogs.md#new-blockabove)
      11. [新增：isTarget](changelogs.md#new-istarget)
      12. [inClaim](changelogs.md#inclaim)
      13. [复合条件](changelogs.md#composite-conditions)
      14. [物品过滤器](changelogs.md#item-filters)
   5. [目标选择器](changelogs.md#targeters-3)
      1. [useBoundingBox](changelogs.md#useboundingbox)
      2. [sort](changelogs.md#sort)
      3. [EntitiesInLine](changelogs.md#entitiesinline)
      4. [RandomLocations](changelogs.md#randomlocations)
   6. [生物](changelogs.md#mobs-2)
      1. [新增：1.21.11 实体类型](changelogs.md#new-12111-entity-types)
      2. [新增：美西螈变种](changelogs.md#new-axolotl-variant)
      3. [ThreatTable](changelogs.md#threattable)
      4. [鞍](changelogs.md#saddles)
   7. [触发器](changelogs.md#triggers-4)
      1. [新增：输入触发器](changelogs.md#new-input-triggers)
      2. [新增：onHealed](changelogs.md#new-onhealed)
      3. [新增：onSheared](changelogs.md#new-onsheared)
      4. [新增：onEffectApply](changelogs.md#new-oneffectapply)
      5. [新增：onThrownByMechanic](changelogs.md#new-onthrownbymechanic)
      6. [新增：onMount](changelogs.md#new-onmount)
   8. [占位符](changelogs.md#placeholders-2)
      1. [占位符引擎](changelogs.md#placeholder-engine)
      2. [新增：输入占位符](changelogs.md#new-input-placeholder)
      3. [新增：光环层数占位符](changelogs.md#new-aura-stacks-placeholder)
      4. [新增：<skill.power>](changelogs.md#new-skillpower)
      5. [新增：技能充能占位符](changelogs.md#new-skill-charge-placeholders)
      6. [新增：damage-amount-post](changelogs.md#new-damage-amount-post)
      7. [新增：对话框占位符](changelogs.md#new-dialog-placeholders)
      8. [新增：itemcount](changelogs.md#new-itemcount)
      9. [新增：<char.*>](changelogs.md#new-char)
      10. [新增：随机 UUID](changelogs.md#new-random-uuid)
      11. [杂项](changelogs.md#misc-6)
   9. [物品](changelogs.md#items-3)
      1. [常规](changelogs.md#general-5)
      2. [新增组件支持](changelogs.md#new-component-support)
   10. [API](changelogs.md#api-3)
   11. [兼容性](changelogs.md#compatibility-2)
   12. [错误修复与优化](changelogs.md#bug-fixes-optimizations)
5. [5.11.0](changelogs.md#5110)
   1. [常规](changelogs.md#general-6)
   2. [优化](changelogs.md#optimiations)
   3. [兼容性](changelogs.md#compatibility-3)
   4. [机制](changelogs.md#mechanics-4)
      1. [新增：fear](changelogs.md#new-fear)
      2. [新增：TRAIL 粒子](changelogs.md#new-trail-particle)
      3. [新增：forEachPin](changelogs.md#new-foreachpin)
      4. [新增：VariableMove](changelogs.md#new-variablemove)
      5. [新增：determineCondition](changelogs.md#new-determinecondition)
      6. [Velocity](changelogs.md#velocity)
      7. [杂项](changelogs.md#misc-7)
   5. [条件](changelogs.md#conditions-5)
      1. [新增：MetaskillCondition](changelogs.md#new-metaskillcondition)
      2. [新增：isSibling](changelogs.md#new-issibling)
      3. [Targets 条件](changelogs.md#targets-condition)
      4. [改进](changelogs.md#enhancements)
   6. [目标选择器](changelogs.md#targeters-4)
      1. [新增：@EscapeLocation](changelogs.md#new-at-escapelocation)
      2. [新增：@EntitiesNearPin](changelogs.md#new-at-entitiesnearpin)
      3. [位置目标选择器](changelogs.md#location-targeters)
   7. [生物](changelogs.md#mobs-3)
      1. [新增：铜傀儡（1.21.10）](changelogs.md#new-copper-golem-12110)
      2. [新增：假人（1.21.10）](changelogs.md#new-mannequin-12110)
      3. [其他生物新增内容](changelogs.md#other-mob-additions)
   8. [触发器](changelogs.md#triggers-5)
      1. [新增：onDismounted](changelogs.md#new-ondismounted)
   9. [占位符](changelogs.md#placeholders-3)
      1. [数值占位符改进](changelogs.md#numeric-placeholder-improvements)
      2. [静态占位符优化](changelogs.md#static-placeholder-optimization)
      3. [杂项](changelogs.md#misc-8)
   10. [物品](changelogs.md#items-4)
   11. [API](changelogs.md#api-4)
   12. [错误修复与优化](changelogs.md#bug-fixes-optimizations-2)
6. [5.10.0（正式版）](changelogs.md#5100-release)
   1. [常规](changelogs.md#general-7)
   2. [API 与事件](changelogs.md#api-events)
   3. [占位符](changelogs.md#placeholders-4)
   4. [变量](changelogs.md#variables)
   5. [机制](changelogs.md#mechanics-5)
   6. [Teleport（仅限 Paper）](changelogs.md#teleport-paper-only)
   7. [目标选择器与触发器](changelogs.md#targeters-triggers)
   8. [条件](changelogs.md#conditions-6)
   9. [物品与装备](changelogs.md#items-equipment)
   10. [生物与生成](changelogs.md#mobs-spawning)
   11. [全息文字与展示实体](changelogs.md#holograms-displays)
   12. [兼容性与杂项](changelogs.md#compatibility-misc)
   13. [错误修复与其他](changelogs.md#bug-fixes-other-3)
7. [较早的更新记录](changelogs.md#older-changelogs)

# 5.13.1 {#5131}

## 通用设置 {#general}

- 为 `packinfo.yml` 添加 `PackOverrides` 和 `FileOverrides`，作用与 `PackDependencies` 和 `FileDependencies` 相反：列出的包或插件存在时，跳过该包或其中部分文件。现在这四个键都接受用 `&&`、`||`、`!` 和括号组合的条件，名称可以是插件名、其他包的文件夹名，或 `MythicMobsPremium`。

```yaml
PackDependencies:
- ((MythicCrucible && MythicMobsPremium) || Nexo)
PackOverrides:
- TheRealPack
FileDependencies:
- armors/** MythicArmors
FileOverrides:
- items/armors_vanilla.yml MythicArmors
```

- 修复 `FileDependencies` 在真实服务器上始终无法排除文件的问题。

## 条件 {#conditions}

- `inBounds` 支持“触发器”下列出的新形状、位置目标选择器和角点覆盖设置。
- 修复目标为位置时，`heightAbove`/`heightBelow` 不解析 `height` 中施法者和技能占位符的问题。

## 目标选择器 {#targeters}

### 新增：bound {#new-bound}

- 添加 `@bound` 目标选择器（别名 `@bounds`），选取长方体、球体或圆柱体内的存活实体，选项与 `inBounds` 相同。

```yaml
- ignite @bound{shape=sphere;l=@selfLocation;r=8}
```

## 触发器 {#triggers}

### 新增：onPlayerEnter / onPlayerExit {#new-onplayerenter-onplayerexit}

- 添加生物触发器：按生物计时器周期检查，每名玩家移入或移出区域时各触发一次；`@trigger` 为该玩家。因退出、死亡或切换世界离开时，不会触发 `onPlayerExit`。

```yaml
Skills:
- message{m=Turn back while you can} @trigger ~onPlayerEnter{shape=sphere;location=@selfLocation;radius=20}
```

### 边界形状 {#bounds-shapes}

- 除了默认的双角点长方体，`onEnterBounds`、`onExitBounds`、`onPlayerEnter`、`onPlayerExit`、`inBounds` 和 `@bound` 还支持 `shape=sphere`（使用 `location` 和 `radius`）以及 `shape=cylinder`（还需 `height`）。
- 角点和位置支持 `@selfLocation` 或 `@CasterSpawnLocation` 等位置目标选择器，每次检查都会重新解析。
- 添加 `x1`/`y1`/`z1` 和 `x2`/`y2`/`z2`，用于替换已解析角点的单个坐标，例如设置两个标记点之间任意高度的区域。
- 边界触发器的配置错误现在会指出具体问题，例如圆柱体缺少 `height`。

```yaml
Skills:
- teleport @CasterSpawnLocation ~onExitBounds{shape=sphere;location=@CasterSpawnLocation;radius=20}
- message{m=Welcome to the arena} @trigger ~onPlayerEnter{c1=arena_a;c2=arena_b;y1=-64;y2=320}
```

## 对话框 {#dialogs}

- 为正文元素和按钮添加 `ForEach` 与 `PageSize`：为每个目标或值各生成一份，并分页显示（`<dialog.page>`、`<dialog.pages>`）。
- 为按钮添加 `Skills`（内联机制）。
- 添加可点击文本：正文中的 `<skill:Name:key=value>` 会在点击时运行技能。
- `Initial` 对所有输入类型生效。输入项初始值会沿用前一个对话框传来的值。
- 选项标签支持 MiniMessage 和占位符。
- 物品元素接受 Mythic 物品、`DIAMOND{amount=3}` 等原版物品行、掉落表和占位符。
- 正文元素、输入项和按钮上的 `Conditions` 可以读取 `dialog.*` 值。
- 添加 `MythicDialogOpenEvent`、`MythicDialogClickEvent` 和 `DialogManager#open`。
- `/mm dialogs show` 接受 `key=value` 参数对。
- 所有 MythicMobs 文本中 MiniMessage 标签内部的占位符都会解析，例如 `<head:<target.name>>`。
- `<char>` 接受超过 FFFF 的编码，例如 `<char.1F600>`。
- 修复点击未运行任何技能时，`WAIT_FOR_RESPONSE` 对话框停留在等待界面的问题（1.21.8+）。
- 修复玩家离开或使用 `ExitButton` 后，`hasDialogOpen` 仍为 true 的问题。
- 修复点击按钮会将按钮值写入打开对话框的技能变量的问题。
- 修复 `closeDialog` 在 1.21.6 和 1.21.7 上导致错误的问题。
- 在文本输入项中输入的 MiniMessage 标签会显示为纯文本。
- 不再显示的对话框收到的点击会被忽略。

```yaml
Buttons:
- ForEach: "@PlayersOnServer{targetself=true}"
  PageSize: 6
  Label: "<skill.value>"
  Skills:
  - message{m="<gold>You picked <skill.value>"}
```

# 5.13.0 {#5130}

## 通用设置 {#general-2}

- 为 `packinfo.yml` 添加 `PackDependencies` 和 `FileDependencies`，让包声明所需插件／文件。当依赖缺失时，Mythic 会跳过依赖这些内容的部分，而不是继续解析并报错。

```yaml
PackDependencies:
- MythicCrucible
FileDependencies:
- enchantments/* MythicEnchants
```

- 刷怪点新增 `Chance`、`RandomRotation` 和 `UseWorldScaling` 选项；大多数刷怪点字段（`Cooldown`、`Warmup`、`MobsPerSpawn`、`MobLevel`、`Radius`、`RadiusY`、`ActivationRange`、`ScalingRange`、`LeashRange`）现在支持占位符和范围值，不再只接受固定数值。

```yaml
Chance: 0.5
RandomRotation: true
Cooldown: 5to10
MobsPerSpawn: 1to3
```

- 40 多种机制中的数值属性现在支持占位符，不再只接受静态数值，包括 `missile`、`projectile`、`beam`、`summon`、`orbital`、`lightning`、`shootfireball`、`volley`、`raytrace`、粒子效果机制等。
- 为菜单配置添加 `Hide`、`HideFlags`、`Glint` 和 `Enchantments` 图标选项；修复条件覆盖图标显示不应出现的物品标志的问题（#2232）。

## 属性 {#stats}

- 将 `CRITICAL_STRIKE_DAMAGE` 改回对最终伤害复合相乘的倍率，而不再并入 `modifyDamage{}` 等机制的同一加算池。
- 修复属性重算中的更新丢失竞争问题，该问题可能丢弃并发属性变更（例如异步光环造成的变更）；生命恢复现在每刻读取实时属性值，不再使用可能不同步的缓存。

## 技能机制 {#mechanics}

### 新增：过场动画系统 {#new-cinematics-system}

- 添加脚本化镜头系统，用于过场动画、Boss 出场及脚本化揭示场景：关键帧镜头路径在 `cutscenes/` 下定义（也可内联），通过 `cinematicCamera` 机制（别名 `cinecam`、`camerapath`）向玩家播放。支持循环、逐段缓动曲线、仅通过数据包实现的 `DISPLAY` 镜头或基于 `TELEPORT` 的回退方式，以及可选的 `onStart`/`onEnd` 技能。
- 添加 `cinematicCancel` 机制（别名 `cinecancel`、`stopcinematic`），提前停止正在播放的过场动画。
- 添加 `isInCinematic` 条件（别名 `incinematic`、`incine`、`cinematicactive`）和 `cinematic.active`、`cinematic.frame`、`cinematic.progress` 占位符。
- 添加 `/mm camera <pathId> add|remove` 命令，用于在游戏内创建镜头路径。
- 为附加插件添加 `MythicCinematicStartEvent`（可取消）和 `MythicCinematicEndEvent` API 事件。
- 修复 `DISPLAY` 镜头模式未加载镜头路径沿途区块的问题。

```yaml
my_path_id:
  duration: 100
  easing: EASE_IN_OUT_CUBIC
  points:
  - "world,100,70,100,90,10"
  - "~,0,5,-10,0,30,40"

- cinematicCamera{path=my_path_id} @target
```

### 新增：clearpath {#new-clearpath}

- 添加 `clearpath` 机制（别名 `stoppath`、`clearnavigation`、`stopnavigation`），清除目标生物当前的导航路径。

```yaml
- clearpath @self
```

### 坐骑模式 {#mount-mode}

- 为 `mount` 和 `summonPassenger` 机制添加 `mode` 选项：`ADD`（添加为乘客）、`SET`（设置乘客，已有乘客时失败，即此前的默认行为）或 `REPLACE`（替换当前所有乘客）。

```yaml
- mount{type=Wolf;mode=ADD} @self
- summonPassenger{type=Horse;mode=REPLACE} @self
```

### OnDeath 光环组件 {#ondeath-aura-component}

- 为 `ondeath` 光环组件添加 `ce`/`cancelEvent` 选项：死亡技能成功执行时（仅限 Paper），现在会取消死亡事件并复活实体，而不是让它死亡。

```yaml
- aura{onDeathSkill=ReviveSkill;ce=true} @self
```

### 光环组件的 cancelOn* 标志 {#aura-component-cancelon-flags}

- `cancelOnDeath`、`cancelOnCasterDeath`、`cancelOnTeleport`、`cancelOnChangeWorld`、`cancelOnGiveDamage` 和 `cancelOnTakeDamage` 现在可以设在单个光环组件上，不再只能设在光环行上（#2254）。

```yaml
- aura{auraname=Shield;duration=200;components=[
    - ondamaged{cancelOnTakeDamage=true;ondamaged=BreakShield}
  ]} @self
```

### 其他 {#misc}

- `setProjectileDirection` 现在除了位置目标，也支持对实体目标派发操作（例如 `@target`）（#2229）。
- 为 `missile`、`projectile` 和 `slashProjectile` 添加 `hitBlockConditions`（别名 `hbcond`），根据命中方块检查条件，决定弹射物是否可以在那里停止。
- `forEach` 机制现在通过 `<skill.var.index>` 提供当前循环索引。
- `delay` 机制的 `ticks` 参数现在也支持占位符。
- 合并 `aura` 时，现在可以覆盖已运行实例的附着对象，不再总是保留原对象。
- 添加 `firefly` 粒子类型。

## 条件 {#conditions-2}

### 新增：isCancelled {#new-iscancelled}

- 添加 `isCancelled` 条件（别名 `isCanceled`、`cancelled`、`canceled`），检查触发事件当前是否已取消，例如同一技能链前面已执行 `cancelevent` 时。

```yaml
Skills:
- cancelevent{}
- message{m="blocked!"} ~onDamaged ?isCancelled
```

### 新增：skyLightLevel {#new-skylightlevel}

- 添加 `skyLightLevel` 条件，检查目标位置的天空光照等级（仅来自天空的光）。

```yaml
- skylightlevel{l=10}
```

### entityType 条件：嵌套变种匹配 {#entitytype-condition-nested-variant-matching}

- `entityType`/`mobtype` 现在接受各类型的限制条件（`variant`、`color`、`style`、`mainGene`、`hiddenGene`、`biome`、`profession`、`crack`、`bodyColor`、`patternColor`、`pattern`），用于匹配具体动物变种、村民职业／生物群系、绵羊／羊驼／潜影贝颜色、铁傀儡裂纹状态、热带鱼图案等。

```yaml
- entityType{type=[COW{variant=warm},SHEEP{color=rainbow}]}
- entityType{type=VILLAGER{profession=librarian;biome=taiga}}
```

### 其他 {#misc-2}

- 为 `mobsInRadius` 添加 `shape` 选项（默认 `SPHERE`，也可用 `CYLINDER`、`SQUARE`），与 `EntitiesInRadius`/`EntitiesNearOrigin` 目标选择器已有的形状选项一致。
- 添加用于蜜蜂、狼和恼鬼的 `angry` 条件（别名 `isAngry`）。
- 添加用于蜜蜂的 `pollinated` 条件（别名 `isPollinated`、`hasNectar`）。
- 扩展 `isSheared`，使其也检查沼骸和雪傀儡。
- 为 `variableContains` 添加 `EXACT_ENTRY`（别名 `EXACTENTRY`、`EE`）比较类型，匹配完整的逗号分隔项，而非子字符串。
- `heightAbove`/`heightBelow` 现在使用施放技能的元数据解析 `height` 值，因此支持技能变量和其他占位符。
- 添加 `inBounds` 条件（别名 `withinBounds`、`insideBounds`）；见下文 `onEnterBounds`。

## 目标选择器 {#targeters-2}

### 新增：targetinvulnerable {#new-targetinvulnerable}

- 添加 `targetinvulnerable` 目标选择器选项（默认 `true`）；设为 `false` 可跳过无敌实体（例如设有 `Options.Invincible` 的生物）。

```yaml
@EntitiesInRadius{r=10;targetinvulnerable=false}
```

### mythic / vanilla 过滤器 {#mythic-vanilla-filters}

- 添加 `mythic` 和 `vanilla` 作为 `target`/`ignore` 过滤值，将目标选择器限制为只选取 Mythic 实体或只选取非 Mythic（原版）实体。

```yaml
@EntitiesInRadius{r=10;target=mythic}
@EntitiesInRadius{r=10;ignore=vanilla}
```

### 新增：展示实体/交互实体目标过滤器 {#new-displayinteraction-target-filters}

- 添加 `targettextdisplays`、`targetitemdisplays`、`targetblockdisplays` 和 `targetinteractions` 过滤器（默认均为 `true`），让技能包含或排除文本／物品／方块展示实体及交互实体。

### 其他 {#misc-3}

- `uuid` 目标选择器现在接受逗号分隔的 UUID 列表，不再只接受一个 UUID。

## 生物 {#mobs}

### 新增：默认等级 {#new-default-level}

- 添加顶层生物选项 `Level`（别名 `MobLevel`、`Options.Level`），设置生物默认等级。在未明确指定等级时生成生物（刷怪点、`/mm mobs spawn`、图腾、生物弹体等）都会使用此值；接受固定值或每次生成时随机取值的 `minTOmax` 范围。
- 未设置 `MobLevel` 的刷怪点现在使用生物自身的 `Level`（或 1），不再生成等级为 0 的生物。
- 负值 `LevelModifiers` 现在会生效（此前会被静默忽略），因此属性可以随等级提升而降低。
- 生物等级现在绝不会被限制到低于 1，包括世界缩放产生的零散小数等级。
- 重新加载或重新加载区块时，现在会正确读取已保存的生物等级，不再根据生命值推测。

```yaml
MyBoss:
  Type: ZOMBIE
  Level: 5
  LevelModifiers:
    HEALTH: 50
    MOVEMENT_SPEED: -0.005
```

### 其他 {#misc-4}

- 在 `config-mobs.yml` 中添加全局默认值 `DefaultMobOptions.PreventJockeyMounts`、`PreventConversion`、`PreventLeashing`、`PreventItemPickup` 和 `NoDamageTicks`；修复从未读取 `DefaultMobOptions.PreventVanillaDamage` 的问题。

## 触发器 {#triggers-2}

### 新增：onEnterBounds / onExitBounds {#new-onenterbounds-onexitbounds}

- 添加生物触发器：当生物进入或离开由两个角点定义的轴对齐长方体时触发（按生物计时器周期检查；在内部生成的生物会在首次检查时触发 `onEnterBounds`）。角点接受标记点名称、`world,x,y,z` 或 `x,y,z`，并支持占位符和数学运算。

```yaml
Skills:
- message{m="Entered the arena"} @World ~onEnterBounds{corner1=world,100,64,100;corner2=world,120,80,120}
```

## 占位符 {#placeholders}

### 新增：min / max / clamp {#new-min-max-clamp}

- 添加 `.min{amount=X}`、`.max{amount=X}` 和 `.clamp{min=A;max=B}` 元占位符，可直接限制数值占位符或变量的范围，无需串联 `variableSet`+`variableInRange`。

```yaml
- setvariable{var=caster.spawn_chance;value=<caster.var.spawn_chance.clamp{min=0;max=100}>} @self
```

### 其他 {#misc-5}

- 添加 `location.temperature`（别名 `l.temp`、`temp`），返回位置处经过调整的生物群系温度。
- 添加 `absorption`（别名 `absorb`），返回指定作用域实体当前的伤害吸收（金色）生命值。
- 未设置元素时，`<skill.var.damage-type>` 现在回退为伤害标签（用逗号连接），而不是字面值 `SKILL`；添加 `<skill.var.damage-tags>`，返回原始标签列表。
- 添加 `slot.item`，返回实体装备／背包槽内的物品，作为支持继续访问子属性及物品元关键字的物品值。

## 物品 {#items}

- `BAG` 类型物品的默认堆叠数量现在为 1（仍可通过 `Options.StackSize` 覆盖）。

## API {#api}

- 添加 `MythicLoadedEvent`，在插件完全加载完毕后触发。
- 添加 `MythicCinematicStartEvent`/`MythicCinematicEndEvent`（见上文过场动画系统）。
- `MythicTriggerEvent` 现在实现 `Cancellable`。
- 为 `LootBag#give` 添加接受 `BiFunction` 的重载，让附加插件覆盖掉落物加入玩家背包的方式。
- 为 `LootBag#give` 添加接受 `BiConsumer` 的重载，自定义处理玩家背包装不下的物品。
- 修复 `MythicPlaceholdersLoadEvent` 在附加插件订阅之前触发，导致其注册的占位符丢失的问题（#2214）。
- 恢复已弃用的 `SkillCondition#evaluateLocation(AbstractLocation)` 重载，以兼容附加插件。

## 兼容性 {#compatibility}

- 添加对 Minecraft 26.2 的支持。
- 改进触发器、刷怪点、机制、弹射物和粒子批处理中的 Folia 处理方式（涉及 `altitude`、`DEATH`／死亡观察器、随机生成、刷怪点逐刻更新、机制实体状态、弹射物 `onHit` 的区域线程派发，以及调度器使用）。
- 修复 `~onMount`/`~onDismount` 在 1.20.1 上抛出 `NoClassDefFoundError` 的问题。
- 修复 `EntityKnockbackEvent` 在 1.20.4 上导致插件加载失败的问题。
- 修复查找雪傀儡实体类型时崩溃的问题，并为 1.21 之前版本的旋风人弹射物检测添加防护。

## 问题修复与其他改动 {#bug-fixes-other}

- 缓存占位符、条件和变量运算中已编译的数学表达式，计算速度最高约提升 20 倍。
- 减少技能延迟占位符、目标选择器及弹射物数据包派发每刻分配的对象。
- 优化数据包弹体旋转解析、实体传送数据包、范围条件的位置解析，以及 Boss 血条距离检查。
- 使用每名玩家独立的无锁位置容器优化玩家移动追踪，不再每次移动事件都克隆 `Location`。
- 减少频繁执行的 `SkillMetadata` 克隆中的目标列表复制。
- 在 `getEntitiesNearLocation` 中用直接 AABB 空间查询替代区块遍历，并防护 NaN／无限坐标，限定为有限的世界高度范围。
- 将 `VariableRegistry`/`PlayerVariableRegistry` 改为无锁，并避免批量写入时每项触发两次 `MythicPlayerVariableSetEvent`。
- 减少弹射物、数据包渲染和伤害触发高频路径中每刻分配的对象。
- Gson 反序列化后，`VariableRegistry` 的底层映射仍保持为 `ConcurrentHashMap`，不再重建为 Gson 的 `LinkedTreeMap`。
- 所有活动弹射物共用一个 `WorldUnloadEvent` 监听器，不再为每个弹射物单独创建。
- 除非确有需要，否则 `doDamage` 不再每次命中都分配抗击退 `AttributeModifier`/UUID。
- 优化数据包实体渲染器每刻遍历玩家的方式，并改用基本类型存储数据包的 yaw/pitch。
- 在 `ILocationSelector` 过滤中使用普通循环替代 Stream 流水线。
- 移除 `PacketEntityRenderer.sendPacket` 中一次性列表的分配。
- 降低弹射物每刻派发数据包的开销，并在评估目标时缓存实体 UUID。
- 通过缓存 JAR 注解扫描，并在未设置盾牌颜色时跳过每个物品的异常处理，使每次 `/mm reload` 约缩短一秒。
- 只使受影响配置节的查找缓存失效，进一步加快 `/mm reload`。
- 降低弹射物命中检测中每刻评估目标的开销。
- 减少弹射物碰撞检查中重复的方块状态查找。
- 减少弹射物目标缓冲中的对象分配。
- 优化异步战斗技能派发（约快 1.9x）。
- 优化 `CylinderShape`/`SquareShape` 目标选择器、`altitude` 条件和 `stun` 机制的位置查找；`onDamaged` 光环匹配不再每次命中都分配 `HashMap`。
- 优化 `pin` 目标选择器的随机选择，并将重复查找移到计时技能和生物时钟循环之外。
- 修复目标数量增加时，`targetinterval` 批处理和 `RandomRingPointTargeter` 选择出现 O(n²) 性能下降的问题。
- 修复 `particletornado` 的云粒子发送无效数据并在控制台刷出“particle data is void”的问题。
- 修复施法者实体为 null 时，技能冷却检查和机制派发中的 NullPointerException。
- 修复玩家丢出的物品忽略 `DropGlowColor`/`DropBeamColor` 的问题（#2264）。
- 修复 `chainmissile` 始终无法弹射至新目标的问题（#2287）。
- 修复 `PreventSnowFormation` 在雪傀儡死亡动画期间不生效的问题（#2149）。
- 修复禁用 PvP 时，以自身为目标的伤害机制被阻止的问题（#2285）。
- 修复 `hitbox`/`hitboxissubhitbox` 条件无法识别弹射物命中的 ModelEngine 子碰撞箱骨骼的问题。
- 修复只安装 MythicRPG 时命令技能执行器始终未初始化的问题。
- 修复 `blockmask` 默认只遮罩遮挡方块，而不是所有非空气方块的问题（#2277）。
- 修复全息文字过暗，以及全息渲染中的并发 NullPointerException（#2199）。
- 为 `rayTraceBlock` 防护无限、NaN 或极远坐标，避免服务器挂起。
- 修复 `attack_cooldown` 占位符和 `~onAttack` 触发器在 26.1+ 读取到重置后的冷却值的问题（#2257）。
- 修复弹射物记录使用实体元数据而非持久数据造成的内存泄漏，该泄漏会一直持续到服务器重启。
- 修复 `~onHear` 始终不响应弹射物声音（箭、投掷药水等）的问题。
- 修复 `bulletKillable` 弹射物在首次命中时便终止，而不是只在死亡或消失时终止的问题（#2272）。
- 修复 `stat` 光环组件在 `/mm reload` 后丢失已应用修正的问题（#2271）。
- 修复 `ARROW` 弹射物弹体除了预期技能伤害，还会造成无视盾牌的原版箭伤害的问题（#2274）。
- 修复延迟装备处理执行前区块已卸载时，生物保留原版随机装备的问题。
- 修复 `recoil` 的 `pitch`/`yaw` 选项未在每次施放时解析占位符和数学表达式的问题（#2265）。
- 修复已禁用属性未加载其显示／格式配置，导致 Crucible 生成物品描述时出现 NPE 的问题。
- 修复 Crucible 模拟的弹射物技能伤害不触发 `~onBowHit` 的问题（#2261）。
- 修复 `damage` 机制的重入防护即使设有 `triggerSkills`/`ts=true`，仍会丢弃 onAttack 触发伤害的问题（#2269）。
- 修复映射到原版属性的属性变更（例如异步光环逐刻更新产生的变更）在实体所属线程之外应用，导致属性追踪器损坏的问题（#2270）。
- 修复 `totem` 机制上的 `hugSurface`/`heightFromSurface` 实际上未调整模型位置的问题（#2267）。
- 修复轨道弹体 `bullet=DISPLAY` 因向前偏移而渲染在圆形轨迹之外的问题（#2237）。
- 修复 `DamageModifier` 属性的 `TriggerStats`/`ParentStats` 从错误属性的配置作用域读取的问题（#2213）。
- 修复 `dialog` 元素／按钮的条件以施法者而非查看者为对象进行检查、按钮忽略自身条件／冷却，以及 `/mm reload` 不重载对话框的问题（#2251）。
- 修复 `sound` 机制的 `volume` 不支持占位符的问题。
- 修复 `metaskill` 机制每次施放都检查两遍目标技能 Conditions 的问题（#2246）。
- 修复随机生成的 `maxHeight` 未限制在世界建造高度以内的问题（#2260）。
- 修复配置 `Model.Id` 后，生成时重复应用两次 Model Engine 模型的问题。
- 修复添加时长单位后，时长字段（例如 `Cooldown`、机制持续时间）无法再使用随机范围的问题。
- 修复 `speak{}` 机制的对话气泡全息文字渲染过暗的问题。
- 修复使用实体目标选择器施放 `tracklocation` 和其他位置目标机制时，机制静默不执行的问题。
- 修复 `onDeath` 光环组件在玩家死亡时不触发的问题。
- 修复启用 `cancelOnDeath` 时，`onDeath` 光环组件始终不触发的问题。
- 修复异步消失时钟在死亡事件到达前将一次击杀判为消失，导致刷怪点预热未启动的问题（#2204）。
- 为实体传送防护已卸载／null 世界，包括 `teleport` 机制，以及世界卸载时弹射物执行结束技能的情况。
- 修复 `recoil`/`fear` 强制旋转会以“Invalid move player packet received”踢出玩家的问题。
- 修复 `charged`/`creeperCharged` 条件因构造函数不匹配而无法加载的问题。
- 修复生成的 `tooltip_style` 组件键无法在 MythicCrucible 包命名空间下解析的问题。
- 修复将实体对实体伤害降至恰好 0 的伤害修正，必须同时启用 `CancelDamageIfZero` 才会应用的问题。
- 修复异步生物时钟与 `EntityDeathEvent` 之间的竞争：生物快速死亡时，可能跳过 `DEATH` 触发器，或漏掉击杀者的 `PreventMobKillDrops`。
- 修复 `shoot` 机制的 `ITEM` 和 `BLOCK` 弹射物类型不生效的问题。
- 修复 `blockwave` 抛出 `LIGHT` 方块的问题。

# 5.12.1 {#5121}

## 通用设置 {#general-3}

- 粒子效果现在会排队并打包发送，大幅减少数据包使用量；粒子效果将不遵循客户端粒子设置（可配置）。
- 技能冷却及大多数具有持续时间、间隔的机制，现在支持用后缀指定时长单位（例如 `5s` = 5 秒、`20t` = 20 刻）。

```yaml
Cooldown: 5t
Cooldown: 1m

- potion{type=POISON;duration=10s}
```

## 属性 {#stats-2}

### 新增：MUTATOR 属性 {#new-mutator-stats}

- 添加 `MUTATOR` 自定义属性类型，通过组件、公式和运算，将一个属性值应用到其他属性。

```yaml
AGILITY:
  Enabled: false
  Type: MUTATOR
  AlwaysActive: true
  Display: 'Agility'
  PlayerBaseValue: 0
  Components:
    - Stat: BONUS_DAMAGE
      Formula: 'v / 5'
      Operation: ADDITIVE
    - Stat: CRITICAL_STRIKE_CHANCE
      Formula: 'v / 1000'
      Operation: ADDITIVE
```

## 命令技能 {#command-skills}

### 命令父级 {#command-parent}

- 为命令技能添加 `Command.Parent`，用于创建子命令。

```yaml
ParentCommandSkill:
  Command:
    Id: parent

ChildCommandSkill:
  Command:
    Id: child
    Parent: ParentCommandSkill
```

## 技能机制 {#mechanics-2}

### OnAttack 光环组件 {#onattack-aura-component}

- 为 `onattack` 光环组件添加触发条件支持。

```yaml
- aura{auraname=Counter;duration=200;components=[ - onattack{onattack=CounterSkill} ]} @self ?targetwithin{d=5}
```

### ToggleSitting {#togglesitting}

- 添加 `togglesitting` 机制，用于控制宠物坐下。

```yaml
- togglesitting{state=toggle} @target
- sit{state=true} @target
```

## 条件 {#conditions-3}

### 新增：canBeHitByProjectile {#new-canbehitbyprojectile}

- 添加 `canBeHitByProjectile` 条件。
- 通过 API 跳过自定义 MEG 碰撞箱。

```yaml
- canBeHitByProjectile
- hitByProjectile
```

### 新增：petsitting {#new-petsitting}

- 添加 `petsitting` 条件，检查宠物是否坐下。

```yaml
- petsitting
- petsit
```

## 触发器 {#triggers-3}

### 新增：onEffectRemove {#new-oneffectremove}

- 添加 `onEffectRemove` 触发器。

```yaml
Skills:
  - skill{s=EffectRemovedSkill} ~onEffectRemove
```

## 物品 {#items-2}

### CustomModelData 组件 {#custommodeldata-component}

- 添加对带类型 `CustomModelData` 组件值的支持。
- 支持 `float`、`string`、`boolean` 和 `color` 数据。
- 支持标量、列表和映射列表格式。
- 需要 Paper 1.21.4+。

```yaml
CustomModelData:
  - float/1,2,3
  - string/example_model
  - boolean/true
  - color/#ff8800
```

## API {#api-2}

- 公开供附加插件使用的属性注册方法。
- 添加 `MythicStatsRegistrationEvent`。
- 添加 `PlaceholderDuration`。
- 添加用于数据包物品描述的实验性 API。

## 问题修复与其他改动 {#bug-fixes-other-2}

- `incombat` 现在可以检查由战斗标记追踪器追踪的玩家。
- 改进 `RandomSpawnGenerator` 的 Folia 处理。
- 改进 `SetTextDisplayMechanic` 写入实体数据时的 Folia 处理。
- 改进虚拟施法者的施法调度。
- 渲染 MythicMenu 时，静态占位符不再每次渲染都重新解析，以此优化渲染。
- 优化文本像素长度计算。
- 缓存正则表达式元关键字模式。
- 优化 Boss 血条更新。
- 优化单标记占位符解析。
- 优化随机位置目标选择。
- 优化最终伤害计算。
- 优化刷怪点时钟逐刻更新。
- 优化目标条件检查时的对象分配。
- 优化 `ChanceCondition` 中的随机生成。
- 优化掉落处理的高频执行路径。
- 优化 `EntitiesNearbyTargeter`。
- 优化 `PlaceholderInt` 解析。
- 优化 `IEntitySelector` 的玩家过滤。
- 优化变量字符串连接。
- 优化 `MapVariable`、`MapSerializer` 和 `AuraRegistry` 中的循环。
- 修复 `blockwave`，使其在未指定材料时使用现有 `BlockState`。
- 修复 `setDisplayEntityItem` 不支持方块展示实体的问题。
- 修复 `stats.yml` 中默认属性基础值的部分问题。
- 修复列表变量的 `sortNum` 占位符输出。
- 修复集合变量的 `sortNum` 占位符输出。
- 修复 `playersInRadius` 未采用文档所列默认值的问题。
- 修复自定义击杀消息中的 MiniMessage 标签未解析的问题。
- 修复默认闪光粒子未被设为白色的问题。
- 修复带持续时间的 `blockmask` 机制重叠时，旧蒙版到期影响新蒙版持续时间的问题，现在新蒙版会保留自身持续时间。
- 修复 Mythic 发起的生成操作导致 `RandomSpawner` 的 `REPLACE` 递归的问题。
- 修复 `hasitem` 将 amount 默认设为条件变量，而不是 `>0` 的问题。
- 修复名称牌亮度。
- 修复属性执行器加载顺序。
- 修复命令技能的父命令处理。
- 修复 `stats.yml` 提取时机，让附加插件能够及早注册属性。
- 修复 `particlelineequation` 忽略 `eqy` 和 `eqz` 的问题。
- 修复 `teleport` 在查找安全生成位置时丢失 `preservepitch` 和 `preserveyaw` 的问题。
- 修复 `particlesphere` 应用两次 `yoffset` 的问题。
- 修复 `trail` 粒子的位置键使用来源而非目标的问题。
- 修复 `aura{cancelOnDeath=false}` 在玩家重生后仍然保留的问题。
- 修复异步技能时钟竞争期间遗漏 `MythicMobDeathEvent` 和掉落物的问题。
- 修复 1.21.1 兼容性问题。
- 修复 `BukkitAttribute.values()` 过滤反转的问题。
- 修复 `onTick` 光环到期后仍继续运行的问题。
- 修复负持续时间的光环循环。
- 修复 `location=` 槽中的嵌套实体目标选择器未应用排序、条件或数量限制的问题。
- 修复 `onattack` 的 `damage-amount` 技能变量。
- 修复 `onattack` 的 `damage-type` 技能变量。
- 修复 `onattack` 的 `damage-cause` 技能变量。
- 修复 `MobsNearOrigin` 缺少 type 时抛出 NPE 的问题。
- 修复 `MobsNearOrigin`，使其在缺少 type 时记录配置错误。
- 修复 `pickupitem` 在拾取的物品上残留 fancy-drop PDC 的问题。
- 修复 `giveitem` 将物品装进饰纹陶罐，而不是掉落在旁边的问题。
- 修复召唤问题。
- 修复持续时间返回过高精度的问题。
- 修复数学公式返回过高精度的问题。
- 修复 `damage{}` 未遵循 `triggerSkills` 的问题。
- 修复 `stun` 允许玩家向上传送的问题。
- 修复 `stun`，恢复将 `g=` 用作光环组的选项。
- 修复药水持续时间 `-1` 无法表示无限的问题。

# 5.12.0 {#5120}

## 通用设置 {#general-4}

- 添加对 1.21.11 和 `26.1.x` 的支持（需要 Java 25）。
- 添加自动更新配置功能。
- 改进不区分大小写的配置加载。
- 添加新的 `files/` 包目录。
- 添加自动生成的 `.internal` 包，其中包含 Crucible 可自动生成的部分资源，以及其他可修改的实用内部内容。

## 属性系统 {#stats-system}

- 更新默认 `stats.yml`，采用更合适的基础值。
- 将缺少的属性添加到默认 `stats.yml`。
- 添加 `LOOT_BIAS` 属性，用于影响加权掉落表。

## 技能机制 {#mechanics-3}

### 新增：光环组件 {#new-aura-components}

- 将光环重写为基于组件的形式，使单个光环可以组合多种效果。
- 添加 `targetIsCaster=true`。
- 添加 `decayStackOnExpire=true`。
- 添加可持久保留的 `cancelOnQuit=false`。
- 添加 `ChunkLoadAuraComponent`。
- 添加 `projectilerebound`。

```yaml
- aura{auraname=MultiAura;duration=200;interval=10;targetIsCaster=true;decayStackOnExpire=true;components=[ - onattack{onattack=[ - particles{p=flame;a=50;s=1} @self ]}, - stat{stat=HEALTH;type=ADDITIVE;value=20} ]} @target
```

### 新增：removeTaggedAuras {#new-removetaggedauras}

- 添加 `removeTaggedAuras`，按标签清除光环实例。

```yaml
- removeTaggedAuras{tags=stun;limit=2} @target
```

### 新增：充能 / CooldownMode {#new-charges-cooldownmode}

- 为技能和元技能添加 `Charges`。
- 为技能和元技能添加 `CooldownMode`。

```yaml
Charges: 3
CooldownMode: PARALLEL
```

### 新增：addSkillCharges {#new-addskillcharges}

- 添加 `addSkillCharges`，恢复所追踪技能的充能次数。

```yaml
- addSkillCharges{skill=Dash;amount=1;order=LATEST;overflow=true} @self
```

### 新增：showDialog {#new-showdialog}

- 添加 `showDialog`，打开自定义 Paper 对话框。

```yaml
- showDialog{dialog=QuestOffer} @trigger
```

### 新增：closeDialog {#new-closedialog}

- 添加 `closeDialog`，强制关闭当前对话框。

```yaml
- closeDialog @trigger
```

### 新增：hide {#new-hide}

- 添加 `hide` / `hideFromPlayers`，对选定玩家隐藏施法者，可选择持久保留。

```yaml
- hide{permanent=true;save=true} @PlayersInRadius{r=30}
```

### 新增：enchantItem {#new-enchantitem}

- 添加 `enchantItem`，直接为目标槽位添加附魔。

```yaml
- enchantItem{enchant=SHARPNESS;level=1;slot=HAND} @self
```

### 新增：SetCustomMenuTitle {#new-setcustommenutitle}

- 添加 `SetCustomMenuTitle` / `setMenuTitle`，更新已打开的自定义菜单标题。

```yaml
- setMenuTitle{title="<gold>Boss Rewards"} @self
```

### Wait {#wait}

- 为 `wait` 添加 `onTimeoutSkill` / `ontimeout` / `ots`。

```yaml
- wait{cond=[ - onground ];tt=300;ontimeout=TimeoutSkill}
```

### Sudo {#sudo}

- 为 `sudo` 添加 `chained=true`。

```yaml
- sudoskill{chained=true;skill=Example} @EIR{limit=3;radius=10}
```

### Heal {#heal}

- 为治疗机制添加 `tags`。

```yaml
- heal{a=10;tags=holy,burst} @self
```

### DropItem {#dropitem}

- 为 `DropItem` 添加 `ForceDynamic`。

```yaml
- dropitem{item=MyDrop;ForceDynamic=true} @self
```

### Sound {#sound}

- 为声音机制添加 `emitter` 和 `seed` 选项。

```yaml
- sound{s=minecraft:entity.warden.heartbeat;emitter=caster;seed=42} @self
```

### Projectile {#projectile}

- 为 `volley` 添加 `spread`。
- 为弹射物机制添加 `bulletBrightness`。
- 为弹射物机制添加 `bulletALOD=false`。

```yaml
- volley{spread=4} @target
```

### Throw {#throw}

- 为 `throw` 添加占位符支持和 `triggers=false`。

```yaml
- throw{v="<caster.var.throw_speed>";vy=1.5;triggers=false} @target
```

### 自定义菜单 {#custom-menus}

- 为自定义菜单添加 `Shared: false`。
- 为自定义菜单添加 `UIElements`。

```yaml
CustomMenu:
  Shared: false
  UIElements:
  - myc_menu_hats{char=\ue832;path=ui/cosmetics_gui_hat;height=256;ascent=14}
```

## 条件 {#conditions-4}

### 新增：input {#new-input}

- 添加 `input`，检查玩家当前按下的移动按键。

```yaml
- input{key=forward,sprint}
```

### 新增：skillIsRecharging {#new-skillisrecharging}

- 添加 `skillIsRecharging`，检查技能充能恢复状态。

```yaml
- skillIsRecharging{skill=Dash}
```

### 新增：statDamageModifier {#new-statdamagemodifier}

- 添加 `statDamageModifier`，用于属性技能检查。

```yaml
- statDamageModifier{m=1.01} castInstead PositiveEffectSkill
```

### 新增：inLiquid {#new-inliquid}

- 添加 `inLiquid`，包含对含水方块的支持。

```yaml
- inLiquid
```

### 新增：isFrozen {#new-isfrozen}

- 添加 `isFrozen`。
- 添加 `freezing` / `isfreezing` 别名。

```yaml
- isFrozen
```

### 新增：uuid {#new-uuid}

- 添加 `uuid`，将实体与指定 UUID 值比较。

```yaml
- uuid{u="<trigger.uuid>"}
```

### 新增：goatHorn {#new-goathorn}

- 添加 `goatHorn`，检查山羊是否仍有角。

```yaml
- goatHorn
```

### 新增：isSheared {#new-issheared}

- 添加 `isSheared`，检查绵羊是否已被剪毛。

```yaml
- isSheared
```

### 新增：trim {#new-trim}

- 添加 `trim` / `armorTrim`，检查盔甲纹饰的图案和材料。

```yaml
- trim{slot=CHEST;pattern=sentry;material=gold}
```

### 新增：blockAbove {#new-blockabove}

- 添加 `blockAbove`，检查被检查位置上方指定偏移处的材料。

```yaml
- blockAbove{m=DIRT;y=2}
```

### 新增：isTarget {#new-istarget}

- 添加 `isTarget` / `target`，检查被检查实体是否是施法生物当前的目标。

```yaml
- isTarget
```

### inClaim {#inclaim}

- 扩展 `inClaim`，支持 PlotSquared。
- 扩展 `inClaim`，支持 Residence。

```yaml
- inClaim
```

### 复合条件 {#composite-conditions}

- 复合条件现在可以更可靠地包含空格。

```yaml
- ((day false || raining true) && onBlock{material=LIME_CONCRETE}) true
```

### 物品过滤器 {#item-filters}

- 为 `hasitem` 添加占位符支持。
- 为 `hasitem` 添加变量支持。
- 为 `haspermission` 添加占位符支持。
- 为 `haspermission` 添加变量支持。
- 为物品相关条件和机制添加运行时物品过滤器解析。

```yaml
- hasitem{i="<caster.var.required_item>"}
```

## 目标选择器 {#targeters-3}

### useBoundingBox {#useboundingbox}

- 为形状实体目标选择器添加 `useBoundingBox` / `bb=true`，并为 `@EIC` 添加圆锥碰撞箱检查。

```yaml
@EIC{a=45;r=12;bb=true}
```

### sort {#sort}

- 为实体目标过滤器添加 `sort=OLDEST` 和 `sort=NEWEST`。

```yaml
@EIR{r=20;sort=OLDEST}
```

### EntitiesInLine {#entitiesinline}

- 为 `EntitiesInLine` 半径添加占位符与数学运算支持。

```yaml
@EntitiesInLine{r="<skill.var.beam_radius>"}
```

### RandomLocations {#randomlocations}

- 为 `RandomLocations` 目标选择器添加占位符与数学运算支持。

```yaml
@RandomLocations{a=5;r="<caster.var.scatter_radius>"}
```

## 生物 {#mobs-2}

### 新增：1.21.11 实体类型 {#new-12111-entity-types}

- 添加对 `CAMEL_HUSK` 的支持。
- 添加对 `NAUTILUS` 的支持。
- 添加对 `PARCHED` 的支持。
- 添加对 `ZOMBIE_NAUTLIS` 的支持。

```yaml
Type: CAMEL_HUSK
```

### 新增：美西螈变种 {#new-axolotl-variant}

- 为美西螈添加 `Variant` 支持。

```yaml
Variant: blue
```

### ThreatTable {#threattable}

- 添加 `ThreatTable.DropUnreachableSeconds`。

```yaml
ThreatTable.DropUnreachableSeconds: 10
```

### 鞍 {#saddles}

- 为鞍相关逻辑添加较新生物的支持。
- 改进 `isSaddled` 对较新生物的支持。

```yaml
- isSaddled
```

## 触发器 {#triggers-4}

### 新增：输入触发器 {#new-input-triggers}

- 添加 `~onInputForward`。
- 添加 `~onInputBackward`。
- 添加 `~onInputLeft`。
- 添加 `~onInputRight`。
- 添加 `~onInputJump`。
- 添加 `~onInputSneak`。
- 添加 `~onInputSprint`。

```yaml
- message{m="Jump detected"} ~onInputJump
```

### 新增：onHealed {#new-onhealed}

- 添加 `~onHealed`。

```yaml
- skill{s=AfterHeal} ~onHealed
```

### 新增：onSheared {#new-onsheared}

- 添加 `~onSheared`。

```yaml
- skill{s=AfterShear} ~onSheared
```

### 新增：onEffectApply {#new-oneffectapply}

- 添加 `~onEffectApply`。

```yaml
- skill{s=OnPotionGain} ~onEffectApply
```

### 新增：onThrownByMechanic {#new-onthrownbymechanic}

- 添加 `~onThrownByMechanic`，别名为 `~onThrown`。

```yaml
- skill{s=AfterThrow} ~onThrown
```

### 新增：onMount {#new-onmount}

- 启用 `~onMount`。

```yaml
- skill{s=MountedSkill} ~onMount
```

## 占位符 {#placeholders-2}

### 占位符引擎 {#placeholder-engine}

- 将占位符重构为新的解析器／片段处理流水线。
- 添加通配符注册。
- 添加泛型返回类型。
- 为元关键字添加 `MythicLineConfig` 支持。
- 改进静态占位符解析。
- 为变量占位符添加 `{default=...}` 支持。

### 新增：输入占位符 {#new-input-placeholder}

- 添加反映玩家当前移动状态的实时输入占位符。

```text
<trigger.input.jump>
```

### 新增：光环层数占位符 {#new-aura-stacks-placeholder}

- 添加 `<caster.aura.ID.stacks>`。

```text
<caster.aura.FireShield.stacks>
```

### 新增：<skill.power> {#new-skillpower}

- 添加 `<skill.power>`。

```yaml
- message{m="Power: <skill.power>"} @self
```

### 新增：技能充能占位符 {#new-skill-charge-placeholders}

- 添加 `<[scope].skill.SkillName.charges>`。
- 添加 `<[scope].skill.SkillName.maxcharges>`。
- 添加 `<[scope].skill.SkillName.overflowcharges>`。

```yaml
- message{m="Dash: <caster.skill.Dash.charges>/<caster.skill.Dash.maxcharges> (+<caster.skill.Dash.overflowcharges>)"} @self
```

### 新增：damage-amount-post {#new-damage-amount-post}

- 添加 `damage-amount-post`。
- 添加 `<skill.var.damage-amount-post>`。

```yaml
- message{m="Final damage: <skill.var.damage-amount-post>"} @self
```

### 新增：对话框占位符 {#new-dialog-placeholders}

- 添加对话框输入占位符。

```yaml
- message{m="Class: <dialog.classChoice>"} @trigger
```

### 新增：itemcount {#new-itemcount}

- 添加 `itemcount`，统计玩家背包中的原版或 Mythic 物品数量。

```yaml
- message{m="Diamonds: <caster.itemcount.DIAMOND>"} @self
```

### 新增：<char.*> {#new-char}

- 添加 `<char.*>`，用于延迟插入 Unicode 字符。

```text
<char.007B>
```

### 新增：随机 UUID {#new-random-uuid}

- 添加 `<random.uuid>`。

```yaml
- message{m="<random.uuid>"} @self
```

### 其他 {#misc-6}

- 添加映射元关键字 `sortByValue`。
- 添加 `round` 数学运算支持。
- 将 `<item.level>` 重命名为 `<item.droplevel>`。

## 物品 {#items-3}

### 通用设置 {#general-5}

- 添加 `Options.Glint: false` 支持。

### 新增组件支持 {#new-component-support}

- 添加 `AttackRange`。
- 添加 `BlocksAttacks`。
- 添加 `Weapon`。
- 添加 `KineticWeapon`。
- 添加 `PiercingWeapon`。
- 添加 `JukeboxPlayable`。
- 添加 `NoteBlockSound`。
- 添加 `UseRemainder`。
- 添加 `BreakSound`。
- 添加 `Instrument`。
- 添加 `Enchantability`。
- 添加 `Repairable`。
- 添加 `OminousBottleAmplifier`。
- 添加 `PotDecorations`。
- 添加 `banner_patterns`。
- 添加 `LodestoneTracker`。

```yaml
AnItem:
  Material: DIAMOND
  AttackRange: 3.5
  Weapon:
    ItemDamagePerAttack: 2
    DisableBlockingForSeconds: 0.5
  JukeboxPlayable: "minecraft:thirteen"
  UseRemainder: ADifferentItem
  Repairable:
  - STICK
  PotDecorations:
    Back: brick
    Left: arms_up_pottery_sherd
    Right: skull_pottery_sherd
    Front: prize_pottery_sherd
```

## API {#api-3}

- 添加注册自定义命令函数的 API。
- 添加自定义可装备物品的 API。
- 添加 `MythicPlayerQuitEvent`。
- 添加 `MythicAuraStartEvent`。
- 添加 `MythicAuraStopEvent`。
- 添加 `MythicMobPreSpawnConfigureEvent`。
- 添加 `MythicTargetEvent`。
- 添加拦截最终攻击元伤害的 API。
- 公开光环剩余刻数。
- 添加菜单钩子。
- 添加图标钩子。
- 添加颜色选择器钩子。

## 兼容性 {#compatibility-2}

- 大幅改进 Folia 兼容性。
- 为 `inClaim` 添加 PlotSquared 支持。
- 为 `inClaim` 添加 Residence 支持。

## 问题修复与优化 {#bug-fixes-optimizations}

- 重构占位符引擎。
- 改进静态占位符处理。
- 减少弹射物高频执行路径中的对象分配。
- 减少目标选择器高频执行路径中的对象分配。
- 减少掉落处理高频执行路径中的对象分配。
- 减少冷却处理高频执行路径中的对象分配。
- 减少聚类高频执行路径中的对象分配。
- 减少注册表查找高频执行路径中的对象分配。
- 改进菜单重载性能。
- 改进自定义名称组件缓存。
- 优化不区分大小写的配置处理。
- 修复持久光环的保存和重新加入问题。
- 修复光环终止时的竞争问题。
- 修复 `removeAura` 的属性泄漏。
- 修复 `onDamaged` 光环的回归问题。
- 修复随机占位符输出的回归问题。
- 修复 MiniMessage 占位符的回归问题。
- 修复进度条占位符的回归问题。
- 修复姿态占位符的回归问题。
- 修复威胁表占位符的回归问题。
- 修复缓存属性占位符的回归问题。
- 修复静态占位符的回归问题。
- 修复非占位符 `<` 的解析问题。
- 修复递归占位符缓存的竞争问题。
- 修复占位符并发问题。
- 修复弹射物负重力。
- 修复弹射物命中所有者子碰撞箱的问题。
- 修复文本展示实体亮度问题。
- 修复速度为零的展示实体弹体。
- 修复弹射物反弹轴错误。
- 修复弹射物 NPE。
- 修复 `doEndSkillOnHit=false` 的处理。
- 修复随机生成逻辑。
- 修复刷怪点数据过期的问题。
- 修复各玩家独立的随机生成冷却。
- 修复重复生成。
- 修复自然消失时的注销。
- 修复区块加载时持久生物的恢复。
- 修复等级缩放问题。
- 修复 `BaseValue` 属性问题。
- 修复属性舍入问题。
- 修复百分比治疗问题。
- 修复加算伤害修正的行为。
- 修复 `modDamage{action=ADD}` 将伤害作为倍率应用的问题。
- 修复物品属性翻倍及重载后重置的问题。
- 修复 `OnCooldownSkill` 重定向忽略目标技能冷却的问题。
- 修复菜单生成问题。
- 修复条件菜单问题。
- 修复菜单重载性能问题。
- 修复隐藏物品处理。
- 修复在 Mythic 文件夹以外查找 FAWE 原理图的问题。
- 修复向上或向下看时 `EntitiesInCone` 的目标选择。
- 修复 `haspotion` 条件问题。
- 修复 `inLiquid` 条件问题。
- 修复召唤的 owner/parent 选项。
- 修复 `runaigoal` 优先级和叠加。
- 修复未安装 Nexo 时全息文字的十六进制颜色。
- 修复其他 `26.1.x` 后续问题。
- 修复 Folia 区块竞争问题。
- 修复 Folia 命令竞争问题。
- 修复 Folia 药水效果线程问题。
- 修复 Folia 可见性线程问题。
- 修复 Folia 治疗事件线程问题。
- 修复 Folia 图腾处理。
- 修复 Folia 交易处理。

# 5.11.0 {#5110}

## 通用设置 {#general-6}

- 添加对 1.21.10 的支持。
- 停止支持 1.19.X、1.20.2、1.20.6 和 1.21.3。
- 继续支持 1.20.1、1.20.4、1.21.1 和 1.21.4+。
- 重写 `/mm i import`，改进 NBT、显示内容和 MiniMessage 物品描述的导入。
- 将大部分自定义菜单逻辑移入基础插件；菜单现在需要 Premium 或 RPG。
- 将自定义命令处理从 RPG 移入 Premium。

## 优化 {#optimiations}

- 添加 `ShareComponents` 选项，对相同的机制、目标选择器和条件去重。
- 通过享元共享优化占位符和组件的内存使用。

## 兼容性 {#compatibility-3}

- 改进模型应用时机，进一步减少闪烁。
- 将 Lands 支持更新到最新版本。
- 更新 LibsDisguises 集成，在生成前为生物应用伪装，以减少闪烁。
- 移除 mcstats.org 数据上报。
- 暂时禁用 ShopGUIPlus 支持。

## 技能机制 {#mechanics-4}

### 新增：fear {#new-fear}

- 添加 `fear` 光环机制，使目标（包括玩家）不受控制地四处奔跑。

### 新增：TRAIL 粒子 {#new-trail-particle}

- 添加 `TRAIL` 粒子，支持 `color`、`duration` 和 `source=@targeter`。

### 新增：forEachPin {#new-foreachpin}

- 添加 `forEachPin{pin=X;skill=Y}`，在每个标记点位置各执行一次机制。
- 当前标记点位置通过 `@Pin` 提供。

### 新增：VariableMove {#new-variablemove}

- 添加 `VariableMove` 机制，在不同名称／注册表之间移动变量，可选择使用 `createnew`。

### 新增：determineCondition {#new-determinecondition}

- 添加 `determineCondition` 机制，在元技能中动态判断条件。

### Velocity {#velocity}

- `velocity` 机制不再改动未指定的分量。
- 进一步平滑后坐力移动。

### 其他 {#misc-7}

- 眩晕机制现在默认使用类型 `#stun`。
- 未指定材料时，`blockwave` 现在使用目标方块的材料。
- 为 `VariableMove` 添加 `inheritExpirationTime`。
- 改进弹射物对子碰撞箱的命中检测。

## 条件 {#conditions-5}

### 新增：MetaskillCondition {#new-metaskillcondition}

- 添加 `MetaskillCondition`，让元技能决定条件结果。

### 新增：isSibling {#new-issibling}

- 添加 `isSibling` 条件，检查生物的同级关系。

### Targets 条件 {#targets-condition}

- `targets` 条件现在可以指定目标选择器，不再只依赖继承的目标。

### 改进 {#enhancements}

- 为 `TargetWithin` 和 `TargetNotWithin` 添加占位符支持。
- 元技能条件现在可以解析技能参数。
- 为 `BlockType` 添加错误捕获。

## 目标选择器 {#targeters-4}

### 新增：@EscapeLocation {#new-at-escapelocation}

- 添加目标选择器，查找附近类似末影人传送的逃离位置。

### 新增：@EntitiesNearPin {#new-at-entitiesnearpin}

- 添加选择标记点位置周围实体的目标选择器。

### 位置目标选择器 {#location-targeters}

- 添加 `surface` 和 `surfaceTolerance`。

## 生物 {#mobs-3}

### 新增：铜傀儡（1.21.10） {#new-copper-golem-12110}

- `Options.WeatheringState`
- `Options.Waxed`

### 新增：假人（1.21.10） {#new-mannequin-12110}

- `MannequinOptions.Immovable`
- `MannequinOptions.Description`
- `MannequinOptions.Pose`
- `MannequinOptions.Skin`
- `MannequinOptions.Cape`
- `MannequinOptions.Elytra`
- `MannequinOptions.Model: CLASSIC/SLIM`
- `MannequinOptions.Player`

### 其他生物新增内容 {#other-mob-additions}

- 为牛、鸡和猪添加 `Options.Variant`。
- 添加 `Options.RandomizeProperties`，用于禁用原版生物随机变种。

## 触发器 {#triggers-5}

### 新增：onDismounted {#new-ondismounted}

- 添加实体被解除骑乘时的触发器。

## 占位符 {#placeholders-3}

### 数值占位符改进 {#numeric-placeholder-improvements}

- 添加 `Long` 变量类型。
- 添加 `.round` 和 `.precision.X` 元关键字。

### 静态占位符优化 {#static-placeholder-optimization}

- 添加静态占位符预解析。
- 改进运行时性能和重载后缓存。

### 其他 {#misc-8}

- 添加实验性 `<centertext>` 占位符。

## 物品 {#items-4}

- 添加 `ItemVariable` 掉落类型，供物品处理机制使用。
- 改进 `/mm i import` 对 NBT 和 MiniMessage 内容的处理。
- 为头颅物品添加 `Options.SkinID`。
- 将物品版本格式改为 `major.minor.patch`（最高 255.255.255）。
- 为物品变量添加 `drop:` 前缀。

## API {#api-4}

- 添加 RandomDouble 偏置（仅限 API）。
- 为自定义菜单添加图标模板 API。
- 扩展模板化菜单图标功能。
- 添加更多占位符／变量 API，以及 RandomDouble 偏置配置。
- 尝试在生成前附加 Mythic 类型，使其在 CreateSpawnEvent 中可用。

## 问题修复与优化 {#bug-fixes-optimizations-2}

- 为弹射物重力添加占位符支持。
- 为额外伤害字段添加占位符支持。
- 为伤害机制添加 `bonusDamageModifiers/bdm`。
- 改进 BlockMatcher 错误处理。
- 修复生物生成原因错误地显示为 `PATROL` 的问题。
- 修复重新加载区块时，原版覆盖设置覆写生物选项的问题。
- 修复较新版本上的 owner 和 parent AI 目标。
- 修复不存在任何 `~onSpawn` 触发器时，`~onSpawnOrLoad` 不触发的问题。
- 修复较新版本中的多个粒子问题。
- 修复极端坐标处弹射物不准确的问题。
- 修复弹射物子碰撞箱检测。
- 修复光环到期后未移除其附着对象的问题。
- 修复 Folia 上的光环错误和并发问题。
- 修复 Folia 的多处回归问题（弹射物、光环、延迟、召唤）。
- 修复物品属性叠加问题。
- 修复 1.21.10 上的玩家头颅。
- 通过自动补齐填充字符，修复无效的 Base64 头颅纹理。
- 修复元技能、没有掉落表的生物，以及 onKnockbackEntity 中的 NPE。
- 修复 BlockMatcher 的多个问题，并改进错误日志。
- 修复导入命令在非 Paper 服务器上失败的问题。
- 修复缺少换行符导致的配置加载问题。
- 修复占位符刷屏和属性占位符时机问题。
- 修复后坐力机制问题。
- 修复 meleeattack 目标产生过多调试信息的问题。
- 修复前一个构建中伤害失效的问题。
- 修复 look 机制对无 AI 实体的处理。
- 修复生物类型中的头颅纹理导致崩溃的问题。
- 修复插件无法在 1.21.10 上加载的问题。
- 对各系统进行常规重构和内部清理。

# 5.10.0（正式版） {#5100-release}

## 通用设置 {#general-7}

- 添加对 **1.21.7** 和 **1.21.8** 的支持。
- 添加 `HAPPY_GHAST` 实体类型。
- 性能：加快第二遍处理，并改进重新加载时的实体查找和物品解析缓存。
- 默认配置：添加多个缺少的选项。

## API 与事件 {#api-events}

- 新增：`MythicReloadCompleteEvent`。
- 新增（核心）：`ReloadEvent`。
- 新增：`MythicPlayerVariableSetEvent`、`MythicPlayerVariableRemoveEvent`。
- `MythicHealMechanicEvent` 现在还会调用 `EntityRegainHealthEvent`。
- 添加对 `DamageMetadata` 的元数据访问。
- 在 `SkillTriggerMetadata` 中添加对旧元数据的访问。
- 添加供 RPG 交叉兼容使用的 API 基础。

## 占位符 {#placeholders-4}

- 添加 `<target.armor>`、`<&lt>`、`<&gt>`、`<^dot>`、`<^dot2>`。
- 添加 `PlaceholderAngle`。
- 更多位置现在支持占位符（例如物品浏览器解析）。
- 修复通用 `int`、`float` 和 `double` 占位符不解析变量的问题。
- 修复 PlaceholderVector 在复杂情况下不生效的问题。
- 修复带物品 NBT（string/int/float/double）的占位符不解析的问题。

## 变量 {#variables}

- 新增变量类型：`Set`、`List`、`Map`、`Boolean`、`Vector`、`Time`、**Item**、**MetaSkill**。
- [变量元占位符](../skills/placeholders/meta-placeholders.md)：`<[scope].var.[name].keyword>`，支持串联关键字。
- 更新 `Variable.ofType`；添加 `PolymorphicPlaceholder`。
- 生物变量可以设置所有已注册的变量类型。
- 内部：调整默认变量处理器的位置，供 Crucible 使用。

## 技能机制 {#mechanics-5}

- **新增**：[`ForEach`](../skills/mechanics/foreach.md) 和 [`ForEachValue`](../skills/mechanics/foreachvalue.md)。
- **新增**：`ClearTarget` 机制。
- 更新 `variableadd` / `variablesubtract`，支持新的变量类型。
- 弹射物系列：
  - 添加许多缺少的弹射物选项。
  - 为 `shoot` 和 `volley` 添加 `startYOffset`、`startForwardOffset`、`startSideOffset`。
- 轨道系列：
  - 为 `ParticleOrbital` 半径添加占位符支持。
  - 添加 `immuneDelay`；修复多次命中免疫。
  - 移除 `hugSurface` 的 `hs` 别名。
  - 改进轨道对象的目标选择逻辑。
- 光环：`sync=true` 现在会强制使用同步调度器。
- Look 机制：对行为作出细微调整。
- Summon：修复 `useTargetYaw`/`useTargetPitch`。
- Stun：修复 `freezeFacing` 反转；修复较新版本上的问题。

## Teleport（仅限 Paper） {#teleport-paper-only}

- 为所有传送机制（Paper）**添加**以下选项：
  - 传送原因
  - 保留载具
  - 支持 Paper `TeleportFlag`
- 修复：处理导致传送机制失效的回归问题；进一步完善新选项。

## 目标选择器与触发器 {#targeters-triggers}

- Targeters:
  - 为 `@EntitiesInRadius` 和 `@EntitiesNearOrigin` 添加 `shape`。
  - 添加通用位置属性 `upoffset`。
- Triggers:
  - 潜影贝现在支持 `onShoot` 和 `onBowHit`。
  - 修复下落方块生物的 `onDeath`。

## 条件 {#conditions-6}

- **新增**：[`VariableContains`](../skills/conditions/variablecontains.md)。
- **新增**：`projectileHasEnded`。
- **新增**：`isSkill{name=...}`。
- `mythicMobType` 条件：添加 `exactmatch=false` 选项。
- 添加 `xdiff` 和 `zdiff` 条件。
- 修复生命值条件解析触发器。

## 物品与装备 {#items-equipment}

- 物品标志：允许在 `Hide` 字段中使用完整标志名（例如 `HIDE_ATTRIBUTES`）。
- 兼容性：在 > 1.20.5 上移除不支持的 `HIDE_POTION_EFFECTS`。
- 物品系统：
  - 加快重新加载时的物品缓存（也会解析占位符／变量）。
  - 修复工具规则（关闭 #2027）。
  - 修复物品机制可能失败的情况。
  - 尝试修复 `ItemMatcher` 中的 `vanillaonly=true`。

## 生物与生成 {#mobs-spawning}

- Options:
  - `Options.Aware: false`
  - `Options.PreventKnockback`
  - 添加 `Hidden: true`（使生物不出现在列表中），并修复继承导致该选项无效的问题。
- 数据包：修复通过数据包生成的生物的生成位置。

## 全息文字与展示实体 {#holograms-displays}

- 全息文字：修复前几个构建中的多处回归问题。
- 文本展示弹体：
  - 添加 `bulletRotation`。
  - 修复 1.20_R1 上的旋转代码。

## 兼容性与其他改动 {#compatibility-misc}

## 问题修复与其他改动 {#bug-fixes-other-3}

- 为召唤半径属性添加占位符支持。
- 修复以下位置的 NPE：启动（#2029）、`MythicConfig`、`ForEach`、`Summon`、带 `DisplayItem` 图腾的向量，以及目标设置。
- 修复 1.21.4+ 上的后坐力机制。
- 修复其他插件在加载前调用某些方法时发生的错误。
- 修复某开发构建引入的光环 `IllegalStateException`。
- 修复等级修正错误（少见情况）。
- 修复 `Log` 机制的消息解析。
- 修复目标变量不存在时 `variableequals` 的警告。
- 修复 `onShoot` 光环未设置 `<skill.var.bow-tension>` 的问题。
- 修复 missile 的多个 `verticalOffset` 问题。
- 修复 1.21.8 上发光效果引起的不可变列表错误。
- 修复所有可驯服类型的 `setOwner`/`removeOwner`。

# Older 更新记录 {#older-changelogs}

- [5.10.X 更新记录](https://wiki.mythiccraft.io/mythicmobs/changelogs/5.10.x_changelogs)
- [5.9.X 更新记录](5.9.x_changelogs.md)
- [5.8.X 更新记录](5.8.x_changelogs.md)
- [5.7.X 更新记录](5.7.x_changelogs.md)
- [5.6.X 更新记录](5.6.x_changelogs.md)
- [5.5.X 更新记录](5.5.x_changelogs.md)
- [5.4.X 更新记录](5.4.x_changelogs.md)
- [5.3.X 更新记录](5.3.x_changelogs.md)
- [5.2.X 更新记录](5.2.x_changelogs.md)
- [5.1.X 更新记录](5.1.x_changelogs.md)
- [5.0.X 更新记录](5.0.x_changelogs.md)
- [4.14.X 更新记录](4.14.x_changelogs.md)
- [4.13.X 更新记录](4.13.x_changelogs.md)
- [4.12.X 更新记录](4.12.x_changelogs.md)
- [4.11.X 更新记录](4.11.x_changelogs.md)
- [4.10.X 更新记录](4.10.x_changelogs.md)
- [4.9.X 更新记录](4.9.x_changelogs.md)
- [4.8.X 更新记录](4.8.x_changelogs.md)
- [4.7.X 更新记录](4.7.x_changelogs.md)
- [4.6.X 更新记录](4.6.x_changelogs.md)
- [4.5.X 更新记录](4.5.x_changelogs.md)
- [4.4.X 更新记录](4.4.x_changelogs.md)
- [4.3.X 更新记录](4.3.x_changelogs.md)
- [4.2.X 更新记录](4.2.x_changelogs.md)
- [4.1.X 更新记录](4.1.x_changelogs.md)
- [4.0.X 更新记录](4.0.x_changelogs.md)
- [2.5.X 更新记录](2.5.x_changelogs.md)
- [2.4.X 更新记录](2.4.x_changelogs.md)
- [2.3.X 更新记录](2.3.x_changelogs.md)
- [2.2.X 更新记录](2.2.x_changelogs.md)
- [2.1.X 更新记录](2.1.x_changelogs.md)
- [2.0.X 更新记录](2.0.x_changelogs.md)
- [2.0 之前的更新记录](pre-2.0_changelogs.md)
