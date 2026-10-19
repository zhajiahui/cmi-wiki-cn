---
title: 自定义 AI
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 自定义 AI

1. [AI 行为目标选择器](custom-ai.md#ai-goal-selectors)
   1. [所有生物](custom-ai.md#all-mobs)
   2. [仅限生物类实体](custom-ai.md#creatures-only)
   3. [仅限动物](custom-ai.md#animals-only)
   4. [仅限苦力怕](custom-ai.md#creepers-only)
   5. [仅限远程实体](custom-ai.md#ranged-entities-only)
   6. [仅限猪灵和掠夺者](custom-ai.md#piglins-and-pillagers-only)
2. [AI 攻击目标选择器](custom-ai.md#ai-target-selectors)
   1. [所有生物类实体](custom-ai.md#all-creatures)
   2. [所有生物类实体（支持阵营）](custom-ai.md#all-creatures-faction-support)
3. [AI 寻路代价](custom-ai.md#ai-pathfinding-malus)
   1. [示例](custom-ai.md#examples)
   2. [路径类型](custom-ai.md#path-types)

# AI 行为选择器 {#ai-goal-selectors}

行为目标选择器通过 AIGoalSelectors 字段使用，决定生物想“做什么”。如果某些自定义行为目标不属于所创建生物的基础 AI，它们可能无法生效。例如，僵尸无法使用 “EatGrass” AI 行为目标，因为僵尸本来就不会使用这个行为目标。可以自行尝试，了解哪些有效、哪些无效！

注意：世界处于和平模式时，某些行为目标无法正常生效。

Example:

```yaml
SuperMob:
  Type: zombie
  Health: 200
  Display: 'Superb Zombie'
  AIGoalSelectors:
  - clear
  - meleeattack
  - randomstroll
```

这个僵尸会攻击玩家，在没有锁定敌人时随机四处行走。

## 所有生物 {#all-mobs}

| AI 行为 | 别名 | 说明 |
| --- | --- | --- |
| clear | reset | 移除生物的 AI。 |
| [breakdoors](ai/goals/breakdoor.md) |  | 让生物破坏遇到的门。 |
| [eatgrass](ai/goals/eatgrass.md) |  | 让生物偶尔吃草。 |
| [float](ai/goals/float.md) | swim | 让生物在水中游泳/不游泳。 |
| [lookatplayers](ai/goals/lookatplayers.md) |  | 生物会看向附近的玩家。 |
| [LookAtTarget](ai/goals/lookattarget.md) |  | 生物会看向自己的目标。 |
| [opendoor](ai/goals/opendoor.md) | opendoors | 生物会打开遇到的门，并在通过后关门。 |
| [randomlookaround](ai/goals/randomlookaround.md) | lookaround | 生物会随机环顾四周。 |
| [gotospawnlocation](ai/goals/gotospawn.md) | gotospawn | 生物会寻路前往自己的出生位置。 |
| [doNothing](ai/goals/donothing.md) **[仅 Premium 版]** |  | 满足条件时，让生物不执行任何动作。 |

## 仅生物 {#creatures-only}

| AI 行为 | 别名 | 说明 |
| --- | --- | --- |
| [meleeattack](ai/goals/meleeattack.md) |  | 让生物移动到目标身边并进行近战攻击。 |
| [meleeAttackConditional](ai/goals/meleeattackconditional.md) | meleeAttackCond | 目标满足指定条件时，让生物移动到目标身边并进行近战攻击。 |
| [movetowardstarget](ai/goals/movetowardstarget.md) |  | 让生物向目标移动。 |
| [randomstroll](ai/goals/randomstroll.md) |  | 生物会随机走动。 |
| [restrictsun](ai/goals/restrictsun.md) |  | 阻止生物进入阳光下。 |
| [fleeplayers](ai/goals/fleeplayers.md) | runfromplayers | 让生物避开玩家。 |
| [fleegolems](ai/goals/fleegolems.md) | runfromgolems | 让生物避开铁傀儡。 |
| [fleevillagers](ai/goals/fleevillagers.md) | runfromvillagers | 让生物避开村民。 |
| [fleewolf](ai/goals/fleewolf.md) | runfromwolves | 让生物避开狼。 |
| [fleefaction](ai/goals/fleefaction.md) | runfromfaction | 让生物避开指定阵营的实体。 |
| [fleesun](ai/goals/fleesun.md) |  | 有阳光时，生物会躲到阴影中。 |
| [fleeConditional](ai/goals/fleeconditional.md) **[仅 Premium 版]** | fleeIf | 让生物根据提供的条件逃离。距离大于 5 时必须设置安全距离下的速度。 |
| [spiderattack](ai/goals/spiderattack.md) |  | 使用蜘蛛的攻击方式。 |
| [zombieattack](ai/goals/zombieattack.md) |  | 僵尸近战攻击。 |
| [leapattarget](ai/goals/leapattarget.md) |  | 让生物向目标跳跃。 |
| [movethroughvillage](ai/goals/movethroughvillage.md) |  |  |
| [movetoblock](ai/goals/movetoblock.md) |  | 让生物向特定类型的方块移动。 |
| [movetolava](ai/goals/movetolava.md) |  | 让生物向熔岩移动。 |
| [movetowater](ai/goals/movetowater.md) |  | 让生物向水移动。 |
| [movetowardsrestriction](ai/goals/movetowardsrestriction.md) |  | 让某些实体的生物向其“限制点”移动，例如村民所属的村庄。 |
| [MoveWithinDistanceOfTarget](ai/goals/movewithindistanceoftarget.md) |  | 向目标移动，直到进入指定距离范围。 |
| [MoveWithinDistanceOfTargetConditional](ai/goals/movewithindistanceoftargetconditional.md) | moveWithinConditional, moveWithinCond | 目标满足指定条件时，向其移动，直到进入指定距离范围。 |
| [MoveTowardsTargetConditional](ai/goals/movetowardstargetconditional.md) |  | 寻路前往满足指定条件的实体。 |
| [FollowRoute](ai/goals/followroute.md) | followpath | 让生物沿指定路径移动，仅执行一次。 |
| [patrol](ai/goals/patrol.md) x1,y1,z1;x2,y2,z2;x3,y3,z3;… | patrolroute | 让生物在指定位置之间巡逻。 |
| [gotolocation](ai/goals/gotolocation.md) x,y,z | goto | 让生物前往指定位置（注意：Followrange 必须大于该位置与生物之间的距离）。 |
| [goToLocationConditional](ai/goals/gotolocationconditional.md) | gotoConditional, goToLocationCond, gotoCond | 位置和生物满足指定条件时，让生物前往该位置。 |
| [gotoowner](ai/goals/gotoowner.md) # |  | 超过指定距离时，让生物向其[所有者](../skills/targeters/owner.md)移动，默认距离为 5 格。[Followrange](options.md#followrange) 必须大于所有者与生物之间的距离。 |
| [gotoparent](ai/goals/gotoparent.md) |  | 让生物向其父生物移动。 |
| [Panic](ai/goals/panic.md) | panicWhenOnFire | 着火时惊慌地四处奔跑，并寻找水。 |
| [randomFly](ai/goals/randomfly.md) |  | 随机四处飞行。 |
| [randomNod](ai/goals/randomnod.md) |  | 让生物随机点头。 |
| [horrified](ai/goals/horrified.md) |  | 疯狂地四处奔跑。 |

## 仅动物 {#animals-only}

| AI 行为 | 别名 | 说明 |
| --- | --- | --- |
| [breed](ai/goals/breed.md) |  | 让生物可以与其他生物繁殖。 |

## 仅苦力怕 {#creepers-only}

| AI 行为 | 别名 | 说明 |
| --- | --- | --- |
| [creeperswell](ai/goals/creeperswell.md) | creeperexplode | 让苦力怕准备在目标身边爆炸。 |

## 仅远程攻击实体 {#ranged-entities-only}

| AI 行为 | 别名 | 说明 |
| --- | --- | --- |
| [rangedattack](ai/goals/arrowattack.md) | arrowattack | 基础的远程/弹射物攻击。 |
| [bowattack](ai/goals/bowattack.md) | bowshoot, bowmaster | 高级弓箭攻击。 |
| [arrowAttackConditional](ai/goals/arrowattackconditional.md) | rangedAttackConditional, arrowAttackCond | 目标满足指定条件时，进行基础的远程/弹射物攻击。 |
| [bowAttackConditional](ai/goals/bowattackconditional.md) | bowAttackCond | 目标满足指定条件时，进行高级弓箭攻击。 |

## 仅猪灵和掠夺者 {#piglins-and-pillagers-only}

| AI 行为 | 别名 | 说明 |
| --- | --- | --- |
| [crossbowAttack](ai/goals/crossbowattack.md) |  | 使用弩攻击。 |
| [crossbowAttackConditional](ai/goals/crossbowattackconditional.md) | crossbowAttackCond | 目标满足指定条件时，使用弩攻击。 |

# AI 目标选择器 {#ai-target-selectors}

攻击目标选择器通过 AITargetSelectors 字段使用，决定生物尝试以什么为目标。

> 如果生物设置了 AITargets，却没有能根据目标采取行动的 AIGoal，*仍然*会被视为拥有根据所用 AITargets 选出的有效目标。因此，仍然可以使用 @target 目标选择器等。

示例

```yaml
SuperMob:
  Type: zombie
  Health: 200
  Display: 'Superb Zombie'
  AIGoalSelectors:
  - clear
  - meleeattack
  - randomstroll
  AITargetSelectors:
  - clear
  - players
  - golems
```

## 所有生物 {#all-creatures}

| AI 目标 | 别名 | 说明 |
| --- | --- | --- |
| clear |  | 特殊选项。清除生物的所有 AI。 |
| [hurtbytarget](ai/targets/hurtbytarget.md) | attacker, damager | 以攻击该生物的对象为目标。 |
| [monsters](ai/targets/monsters.md) | monster | 以怪物为目标。 |
| [Players](ai/targets/players.md) | player | 以玩家为目标。 |
| [Villagers](ai/targets/villagers.md) | villager | 以村民为目标。 |
| [irongolem](ai/targets/irongolems.md) | irongolem, iron_golems, iron_golem | 以傀儡为目标。 |
| [nearestConditionalTarget](ai/targets/nearestconditionaltarget.md) **[仅 Premium 版]** | nearestConditional, nearestIf | 以满足所提供条件的最近实体为目标。 |
| [OwnerAttacker](ai/targets/ownerattacker.md) | ownerHurtBy, ownerHurtByTarget, ownerDamager | 以攻击生物所有者的对象为目标。 |
| [OwnerTarget](ai/targets/ownertarget.md) | ownerAttack, ownerhurt | 以生物所有者攻击的对象为目标。 |
| [ParentHurtBy](ai/targets/parenthurtby.md) | parentHurtByTarget, parentDamager, parentAttacker | 以攻击生物父实体的实体为目标。 |
| [ParentTarget](ai/targets/parenttarget.md) | parentHurt, parentAttack | 以施法者父实体正在攻击的实体为目标。 |

## 所有生物（支持[派系](factions.md)） {#all-creatures-faction-support}

| AI 目标 | 别名 | 说明 |
| --- | --- | --- |
| [NearestOtherFaction](ai/targets/nearestotherfaction.md) | OtherFaction | 以任何属于不同阵营的实体为目标。 |
| [NearestOtherFactionMonsters](ai/targets/nearestotherfactionmonsters.md) | OtherFactionMonsters | 以任何属于不同阵营的怪物为目标。 |
| [SpecificFaction](ai/targets/specificfaction.md) [faction_name] |  | 以任何属于指定阵营的实体为目标。 |
| [SpecificFactionMonsters](ai/targets/specificfactionmonsters.md) [faction_name] |  | 以任何属于指定阵营的怪物为目标。 |

# AI 寻路惩罚值 {#ai-pathfinding-malus}

AIPathfindingMalus 字段用于覆盖生物计算路径时对特定路径类型的权重。每个条目由路径类型名称和数值组成，用空格分隔。这些数值会在生物生成时应用，并在加载时重新应用。

- 负值（例如 -1）会使该路径类型不可通行。
- 值为 0 表示没有额外代价。
- 正值会提高穿过该路径类型的代价，因此存在其他路线时，会避开经过它的路径。

自行选择目的地的移动行为目标（例如 randomstroll 或逃跑行为目标），只接受路径类型代价恰好为 0 的候选位置。只要代价为正，该位置就不能被选为目的地，即使生物沿路径移动时仍会经过它。

## 示例 {#examples}

让陆地生物在池塘中游荡。陆地生物的 WATER 默认值为 8，因此 randomstroll 等行为目标永远不会选择水上的位置，而漂浮在池塘中央的生物也完全不会移动：

```yaml
PondWanderer:
  Type: pig
  AIPathfindingMalus:
  - WATER 0
  AIGoalSelectors:
  - clear
  - randomstroll
  - float
```

让生物在寻路时始终避开水。负的寻路代价会使水对其导航系统变得不可通行，但生物仍可能被击退或推入水中：

```yaml
DuneStalker:
  Type: husk
  AIPathfindingMalus:
  - WATER -1
```

让免疫火焰的生物不再绕开燃烧的地面。FIRE（火、岩浆块、点燃的营火）的默认值为 16，火或熔岩旁可行走方块的默认值为 8：

```yaml
CinderBrute:
  Type: zombified_piglin
  AIPathfindingMalus:
  - FIRE 0
  - FIRE_IN_NEIGHBOR 0
```

让生物直接穿过仙人掌地和浆果丛。DAMAGING 方块默认不可通行，因此生物通常会绕开。除非生物对此免疫，否则仍会受到这些方块的伤害：

```yaml
BrambleBoar:
  Type: hoglin
  AIPathfindingMalus:
  - DAMAGING 0
  - DAMAGING_IN_NEIGHBOR 0
```

让生物穿过矿车轨道。生物尚未站在其上的铁轨会被视为 UNPASSABLE_RAIL（默认值为 -1），这就是生物拒绝走过铁轨的原因：

```yaml
RailRunner:
  Type: zombie
  AIPathfindingMalus:
  - UNPASSABLE_RAIL 0
```

将树冠视为可行走的地面。即使生物实际上可以站在树叶上，寻路系统默认也会将树叶方块视为不可通行：

```yaml
CanopyStalker:
  Type: spider
  AIPathfindingMalus:
  - LEAVES 0
```

## 路径类型 {#path-types}

有效名称来自服务器版本的 PathType 枚举。当前版本中包括：

| 路径类型 | 默认值 | 适用对象 |
| --- | --- | --- |
| `BLOCKED` | -1 | 无法穿过的实心方块。 |
| `OPEN` | 0 | 下方没有地面的空气。 |
| `WALKABLE` | 0 | 普通的可行走地面。 |
| `WALKABLE_DOOR` | 0 | 关闭的木门，适用于 AI 能够开门的生物。 |
| `TRAPDOOR` | 0 | 活板门、睡莲、大型垂滴叶。 |
| `POWDER_SNOW` | -1 | 细雪。 |
| `ON_TOP_OF_POWDER_SNOW` | 0 | 站在细雪上。 |
| `FENCE` | -1 | 栅栏、墙、关闭的栅栏门。 |
| `LAVA` | -1 | Lava |
| `WATER` | 8 | Water |
| `WATER_BORDER` | 8 | 水边可行走的方块。 |
| `RAIL` | 0 | 生物已经位于铁轨上时的铁轨。 |
| `UNPASSABLE_RAIL` | -1 | 生物当前未站在其上的铁轨。 |
| `FIRE_IN_NEIGHBOR` | 8 | 火或熔岩旁可行走的方块。 |
| `FIRE` | 16 | 火、灵魂火、岩浆块、点燃的营火、装有熔岩的炼药锅。 |
| `DAMAGING_IN_NEIGHBOR` | 8 | 会造成伤害的方块旁可行走的方块。 |
| `DAMAGING` | -1 | 仙人掌、甜浆果丛。 |
| `DOOR_OPEN` | 0 | 打开的门。 |
| `DOOR_WOOD_CLOSED` | -1 | 可以徒手打开的关闭状态的门。 |
| `DOOR_IRON_CLOSED` | -1 | 需要红石打开的关闭状态的门。 |
| `BREACH` | 4 | 水面正上方的空气（用于游泳导航和跃出水面）。 |
| `LEAVES` | -1 | 树叶方块。 |
| `STICKY_HONEY` | 8 | 蜂蜜块。 |
| `COCOA` | 0 | 可可果。 |
| `DAMAGE_CAUTIOUS` | 0 | 凋灵玫瑰、滴水石锥。 |
| `ON_TOP_OF_TRAPDOOR` | 0 | 站在活板门上。 |
| `BIG_MOBS_CLOSE_TO_DANGER` | 4 | 宽度超过一格、碰撞箱与危险方块相交的生物。 |

旧版服务器对其中一些类型使用不同的名称（[SetPathfindingMalus](../skills/mechanics/setpathfindingmalus.md) 机制页面提供了旧版表格）。名称无效时，会记录配置错误并跳过该条目。

[setpathfindingmalus](../skills/mechanics/setpathfindingmalus.md) 机制可以在运行时通过技能修改相同的数值。
