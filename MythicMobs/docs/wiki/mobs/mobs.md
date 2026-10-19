---
title: 生物
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 生物 {#mobs}

MythicMobs 完全基于自定义实体/生物，并且有很多选项和属性可供你使用。你可以在下面找到可添加到你的自定义创作中的选项/属性的完整列表。

下面的大多数选项都是可选的，这意味着你不必每次创建新生物时都配置整个列表。真正需要的是 `Internal_Name` 和 `Type`。

目录：

1. [分解怪物配置](mobs.md#breaking-down-the-mob-configuration)
2. [示例](mobs.md#examples)

## 生物配置详解 {#breaking-down-the-mob-configuration}

#### Internal_Name {#internal-name}

这个字符串用于在 MythicMobs 内部引用生物，可自行命名。名称必须唯一，不得与其他生物的内部名称冲突，且**不允许包含空格**。

```yml
example_name:
```

#### 类型 {#type}

该字段确定你的创建将基于哪种实体类型。可用[实体类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html)的完整列表可以在spigot javadocs上找到，而[此处](types.md)你可以找到显式实现的类型列表。

> Minecraft 新增实体类型的部分生物选项，要等 Mythic 加入对应实体支持后才能生效。

> 某些实体类型存在不易发现的问题。建议查阅[不稳定实体类型](mobs/unstable-entity-types.md)，再判断哪种实体适合当前用途。

```yml
example_mob:
  Type: zombie
```

```yml
another_mob:
  Type: ZOMBIE
```

#### 显示名称 {#display}

设置生物的显示名称。此选项支持颜色代码和[占位符](../skills/placeholders.md)。 **生物的名字不会自行改变或更新，你必须使用[setname](../skills/mechanics/setname.md)机制来改变或更新它。**

```yml
example_mob:
  Type: zombie
  Display: Example Mob
```

```yml
example_mob:
  Type: zombie
  Display: Example Mob <caster.hp> <red><&heart></red>
```

#### Health {#health}

设置生物最大生命值属性的基础值。 Mythic 对最大生命值没有任何限制，但 Spigot 将最大生命值限制为`2048`。这可以在 spigot 的配置文件 `server_root\spigot.yml` 中轻松更改。每当生物持有或佩戴带有属性修饰符的物品时，也会影响总最大生命值。

```yml
example_mob:
  Type: zombie
  Display: Example Mob
  Health: 30
```

#### Damage {#damage}

设置生物近战攻击伤害属性的基础值。1 点伤害等于 0.5 颗心，因此 6 点伤害相当于 3 颗完整的心。此属性不影响箭、药水等远程攻击。手持或穿戴带有属性修饰符的物品，也会影响生物的近战伤害。

```yml
example_mob:
  Type: zombie
  Display: Example Mob
  Damage: 20
```

#### Armor {#armor}

设置生物的护甲属性的基础值。 Minecraft 将最大护甲值限制为 30。每当生物持有或穿着带有属性修饰符的物品时，也会影响总护甲值。

```yml
example_mob:
  Type: zombie
  Display: Tanker
  Armor: 25
```

#### HealthBar {#healthbar}

一旦生物受到损坏，就会在生物上方创建一个基本的生命条全息图。

```yml
example_mob:
  Type: zombie
  Display: HealthyBoi
  Health: 1000
  HealthBar:
    Enabled: true
    Offset: 1.45
```

#### BossBar {#bossbar}

定义并控制生物的生命值。看起来像末影龙或凋灵的生命条，但外观是可配置的。参见[BossBar](bossbar.md)

```yml
example_mob:
  Type: zombie
  Armor: 25
  BossBar:
    Enabled: true
    Title: Tanker
    Range: 20
    Color: RED
    Style: NOTCHED_6
    CreateFog: true
    DarkenSky: true
    PlayMusic: true
```

#### Faction {#faction}

设置生物的阵营，可用于高级[自定义AI](custom-ai.md)配置或[目标过滤](../skills/targeters.md#targeter-options)。阵营区分大小写，因此使用阵营条件时要小心。

```yml
example_mob:
  Type: zombie
  Armor: 25
  Faction: Tank
```

#### Mount {#mount}

设置你的生物的坐骑。一定是另一个MythicMob。生物在生成时会自动骑在定义的坐骑上。

```yml
another_example:
  Type: chicken
  Mount: example_mo
```

#### 展示实体选项 {#display-options}

设置显示实体选项。可用的显示选项列表可以在[显示选项](displayoptions.md)页面中找到

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
```

#### 选项 {#options}

这是一个特殊的字段，带有许多子选项，例如确定生物是否应该消失、设置击退抗性、跟随范围、移动速度等等。可用的生物选项列表可以在[生物选项](options.md)页面中找到

```yml
slow_persistent_mob:
  Type: husk
  Options:
    MovementSpeed: 0.025
    Despawn: PERSISTENT
```

#### Modules {#modules}

此字段允许你启用或禁用模块，例如 [仇恨表](threattables.md) 和/或 [免疫表](immunitytables.md)

```yml
example_mob:
  Type: husk
  Modules:
    ThreatTable: false
    ImmunityTable: false
```

#### AIGoalSelectors {#aigoalselectors}

修改和自定义生物的 [AI 行为](custom-ai.md#ai-goal-selectors)。

```yml
dummy_mob:
  Type: zombie
  AIGoalSelectors:
    - clear
```

```yml
passive_mob:
  Type: zombie
  AIGoalSelectors:
    - clear
    - randomstroll
    - randomlookaround
```

#### AITargetSelectors {#aitargetselectors}

修改和自定义生物的 [AI 攻击目标](custom-ai.md#ai-target-selectors)。

```yml
neutral_mob:
  Type: zombie
  AIGoalSelectors:
    - clear
    - meleeattack
    - randomstroll
    - randomlookaround
  AITargetSelectors:
    - clear
    - attacker
```

#### AIPathfindingMalus {#aipathfindingmalus}

覆盖生物对特定路径类型的寻路代价，改变计算路径时这些方块的权重。每项填写路径类型名称和对应值。数值含义及有效类型见 [AI 寻路代价](custom-ai.md#ai-pathfinding-malus)。

```yml
pond_wanderer:
  Type: pig
  AIPathfindingMalus:
    - WATER 0
  AIGoalSelectors:
    - clear
    - randomstroll
    - float
```

#### 掉落物 {#drops}

添加或完全修改生物战利品掉落。可以是原版物品、Mythic 物品、经验值、跨插件物品（如果支持），甚至是具有自己的条件系统的自定义掉落表。有关更多信息，请参阅[掉落和DropTables](../drops/drops.md)。

```yml
example_mob:
  Type: zombie
  Options:
    PreventOtherDrops: true
  Drops:
    - diamond 32 1
    - netherite_ingot 12 0.5
```

#### DamageModifiers {#damagemodifiers}

修改生物因不同的伤害原因而受到的伤害。例如，DamageModifiers可用于使生物免疫近战攻击，但对远程攻击较弱。请参阅[伤害修正](damagemodifiers.md) 了解更多信息。

```yml
example_mob:
  Type: zombie
  DamageModifiers:
    - ENTITY_ATTACK 0
    - PROJECTILE 1.25
```

#### 装备 {#equipment}

当生物第一次出现时，为它配备原版物品或Mythic 物品。更多信息请参见[装备](equipment.md)。

```yml
example_mob:
  Type: zombie
  Options:
    PreventRandomEquipment: true
  Equipment:
    - diamond_sword HAND
    - diamond_helmet{name=<green>COMMON</green> helmet} HEAD
```

#### KillMessages {#killmessages}

自定义怪物杀死玩家时出现的[杀死消息](killmessages.md)。

```yml
example_mob:
  Type: zombie
  Display: Tanker
  KillMessages:
    - <caster.name> yeeted <target.name>!!
    - You're too weak <target.name>!!
```

#### Level {#level}

设置生物的默认[等级](levels.md)。接受固定数字或范围，如`3to7`，每次生物生成时都会滚动一个随机级别。每当生成生物而未指定级别时，都会使用此级别。

```yml
example_mob:
  Type: zombie
  Level: 5
```

#### LevelModifiers {#levelmodifiers}

MythicMobs 生物可以拥有[等级](levels.md)，此字段用于指定等级变化时增加哪些属性。

```yml
example_mob:
  Type: zombie
  Display: Dummy
  LevelModifiers:
    Damage: 2
    Health: 0.25
```

#### Disguise {#disguise}

将生物的外观更改为像其他实体类型一样。需要在你的服务器上安装并运行插件 [LibsDisguises](https://www.spigotmc.org/resources/libs-disguises-free.81/)。请参阅[附加组件：伪装](disguises.md) 了解更多信息。

```yml
#This mob acts like a zombie but looks like a chicken
example_mob:
  Type: zombie
  Disguise: chicken
```

#### 技能 {#skills}

技能是 Mythic 的重要功能。所有生物都可以拥有各种技能，在不同条件和场景下触发。熟悉后，Mythic 技能系统使用起来很直观，可以制作简单生物，也可以制作极其复杂的 Boss。请从[技能](../skills/skills.md)开始创建自己的技能。

```yml
#swaps locations with the player that right-clicked the mob
example_mob:
  Type: zombie
  Skills:
    - swap @trigger ~onInteract
```

#### 名称显示 {#nameplate}

如果使用 `Enabled: true` 选项，则强制在生物上使用Mythic 名牌。   这使得像 `Display: "Hello\nWorld!"` 这样的显示名称显示在两个单独的行上。

```yaml
ExampleMob:
  Type: PIG
  Display: "Hello\nWorld!"
  Nameplate:
    Enabled: true

    # The Offset of the nameplate
    Offset: 1.8 
    
    # The Scale of the nameplate
    Scale: 1,1,1

    # If set, forces the nameplate to work with modeled entities from the ModelEngine plugin
    Mounted: true
```

#### Hearing {#hearing}

允许生物像监守者一样“听到”声音。   打开此选项将启用新的 [~onHear](../skills/triggers/onhear.md) 触发器。

```yaml
ICanHearYou:
  Type: ZOMBIE
  Hearing:
    Enabled: true
  Skills:
  - message{m="I can hear you <trigger.name>! <skill.var.volume>? Way too loud!"} @trigger ~onHear
```

#### Totem {#totem}

允许你配置自定义结构，一旦构建，就会召唤生物

```yaml
ExampleMob:
  Type: ZOMBIE
  Totem:

    # The block that once placed will prompt the plugin to check for a totem
    Head: player_head

    # A list of offset vectors and materials that define what the totem should look like
    Pattern:
    - 1,2,0 player_head
    - 0,2,0 player_head
    - -1,2,0 player_head
    - 1,1,0 NETHERITE_BLOCK
    - -1,1,0 NETHERITE_BLOCK
    - 0,1,0 NETHERITE_BLOCK
    - 0,0,0 NETHERITE_BLOCK

    # Optional list of replacements blocks for the pattern.
    # If a replacement for them is not set, every block in the pattern will be replaced with AIR
    Replacement:
    - 0,0,0 AIR
```

Head 的值是用于触发检查的实际方块类型：在世界中放置这种方块时，插件会检查图腾结构是否搭建完成，因此建议使用不常见的方块类型。

方块偏移采用 x,y,z 格式，以面向 yaw=0 的方向配置；0,0,0 位于图腾最底部，也就是生物生成的位置。

![生物图腾](https://i.imgur.com/yOc8Hnm.gif)

#### 变量 {#variables}

无需在 `~onSpawn` 时大量使用 `setvariable` 机制。可以通过生物的 Variables 字段，让生物生成时就具有已设置的[变量](../skills/variables.md)。

```yaml
VariableZombie:
     Type: ZOMBIE
     Variables:
       SomeVariable: something
       AnIntVariable: int/2
       AFloatVariable: float/420.69
```

> 上面的例子将设置
>

> - 类型为 `STRING` 且值为 `something` 的 `SomeVariable` 变量
> - 类型为 `INTEGER` 且值为 `2` 的 `AnIntVariable` 变量
> - 类型为 `FLOAT` 且值为 `420.69` 的 `AFloatVariable` 变量

可能的前缀：

- `int/`
- `float/`
- `set/`
- `list/`
- `map/`

#### Trades {#trades}

自定义村民交易。村民必须具有职业，且职业等级达到 2，才能保留自定义交易。

```yml
MerchantTest:
  Type: VILLAGER
  Display: '&6Merchant Test'
  Options:
    Profession: CLERIC
    Type: DESERT
    Level: 2
  Trades:
    1:
      Item1: 5 EMERALD
      Item2: 5 DIAMOND
      Result: DIAMOND_SWORD
    2:
      Item1: 64 EMERALD
      Result: mmoitems.SWORD.CUTLASS
      MaxUses: 1
    3:
      Item1: 32 EMERALD
      Item2: 1 PAPER
      Result: 1 CUSTOM_ITEM
      MaxUses: 1
```

> 如果不设置`MaxUses`，则默认为`10000`

## 示例 {#examples}

更多生物示例可以在[示例](../examples/common-examples.md#mobs)部分找到。
