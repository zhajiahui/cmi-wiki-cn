---
title: 阵营
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/Factions
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 阵营

# 自定义生物 AI {#customizing-mob-ai}

MythicMobs 可以为生物编写自定义 AI，大幅扩展对生物攻击方式、攻击目标选择以及其他行为的自定义。

以下各节将举例说明，如何配置几种服务器中可能需要的常见场景。

**关于玩家：**
默认情况下，MythicMobs 使用权限系统判断玩家所属阵营。玩家拥有 `faction.(factionname)` 权限时，就会被视为属于该阵营。

可以通过 API 注册自定义阵营提供器，覆盖这一行为。

## AI 目标、攻击目标与派系 {#ai-goals-targets-and-factions}

- 自定义 AI 通常需要配置两项内容才能生效：**AI 行为目标**决定生物如何行动，**AI 攻击目标**决定生物如何选择目标。
- **阵营**用于将生物分组，稍后会用于更高级的配置。
- 默认情况下，大多数（并非所有）Minecraft 生物都有一组内部 AI 行为目标，用于决定其 AI 如何运作。例如，骷髅 AI 会以玩家为目标，并在攻击玩家时使用射箭攻击。
- 要通过 MythicMobs 重新编写 AI，必须先清除其 AI 行为目标和攻击目标，再为这两部分添加新的目标。
- 自定义 AI 并非对所有生物都有效。末影龙等生物的行为是硬编码的，无法更改。**尝试修改它们的 AI 甚至可能导致服务器崩溃，请谨慎操作，并使用测试环境！**

```yaml
DecayingSkeleton:
  Type: skeleton
  Display: '&aa decaying skeleton'
  Health: 15
  Damage: 1
  Faction: Undead
  AIGoalSelectors:
  - clear
  - arrowattack
  AITargetSelectors:
  - clear
  - players
  Options:
    FollowRange: 10
    MovementSpeed: 0.2
    PreventOtherDrops: true
```

- 这个示例展示了骷髅 AI 通常如何攻击，省略了随机行走等无关行为。

```
    * The **AIGoalSelectors** section tells the Skeleton Mob to use the **arrowattack** action when it is going about its day to day goals.
    * The **AITargetSelectors** section tells the Skeleton Mob that it should look to target players to use the **arrowattack** action on.
    * As you see **clear** is always first, which in this case wipes the mobs AI so you have a clean slate to work with. This is important otherwise your AI may not function the way you would expect.
* Now lets say we want the skeleton to attack other mobs instead and we want him to use a melee attack instead of a ranged attack. See below for how we accomplish this.
```

```yaml
DecayingSkeleton:
  Type: skeleton
  Display: '&aa decaying skeleton'
  Health: 15
  Damage: 1
  Faction: Undead
  AIGoalSelectors:
  - clear
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - otherfactionmonsters
  Equipment:
  - COS_WoodSword HAND
  Options:
    FollowRange: 10
    MovementSpeed: 0.2
    PreventOtherDrops: true
```

- 现在，骷髅 AI 被设为攻击其他生物，以及任何先攻击它的生物。此外，它会使用近战攻击，而非远程攻击。

```
    * The **AIGoalSelectors** section now has the **meleeattack** goal which says to attack using melee. It should be noted that you must equip the skeleton with a sword now so he can use the melee attack since you can't melee with a bow equipped (the skeletons default weapon) This would not be required however for a zombie.
    * The **AITargetSelectors** section now has the **players** target removed so the skeleton will not actively engage players. Instead it has the **otherfactionmonsters** target, which tells it that it should attack any monsters that are not in its own faction (in this case Undead). There is also **hurtbytarget** selector with a priority of 1 which says that if any other entities attacks the skeleton first (such as a player) then it will retaliate. This target selector is a common one that should be set as a higher priority so that mobs don't end up being exploitable. Without this here, the player could kill the skeleton without it attacking back which generally is not wanted.
```

- 所有攻击目标选择器和行为目标选择器的列表见[生物的自定义 AI](custom-ai.md)。

- 以下两节会针对服务器中两种常见场景，提供 AI 配置示例。

## 示例 1：守卫攻击附近的怪物 {#example-1-guards-attack-nearby-monsters}

- 这个场景中，我们想在城门口设置守卫，驱赶靠得太近的怪物。可以使用伪装成村民的铁傀儡，但其 AI 较难控制，而且特殊的击飞攻击对怪物不太公平。因此，这里用 MythicMobs 的自定义 AI 更好地实现相同功能。
- 首先需要一名强壮的守卫生物来保护城镇。创建一个伪装成村民的骷髅，并为它装备一把剑。

```yaml
SummonedGuard1:
  Type: skeleton
  Display: '&Ea town guard'
  Health: 500
  Damage: 5
  Equipment:
  - COS_StoneSword HAND
  Options:
    Despawn: true
    FollowRange: 5
    AlwaysShowName: false
    MovementSpeed: 0.35
    PreventOtherDrops: true
    KnockbackResistance: 1
    PreventMobKillDrops: true
  Disguise: villager
```

- 如果直接把这个生物关联到城门口的刷怪点，它会攻击城里的所有玩家，因此需要调整设置，让它友好对待玩家。

```yaml
SummonedGuard1:
  Type: skeleton
  Display: '&Ea town guard'
  Health: 500
  Damage: 5
  Equipment:
  - COS_StoneSword HAND
  Faction: Guard
  AIGoalSelectors:
  - clear
  - opendoors
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - otherfactionmonsters
  Options:
    Despawn: true
    FollowRange: 5
    AlwaysShowName: false
    MovementSpeed: 0.35
    PreventOtherDrops: true
    KnockbackResistance: 1
    PreventMobKillDrops: true
  Disguise: Villager
```

- 现在，这个生物会攻击自身阵营以外的怪物阵营，也会攻击任何伤害它的人，以免有些玩家无缘无故杀死守卫。追击目标时，它还会打开沿途的门。
- 所以这是问题的前半部分。接下来，我们需要确保在墙外漫游的怪物会反击我们的守卫。
- 下面以 Decaying Skeleton 生物为例，按以下方式配置。

```yaml
DecayingSkeleton:
  Type: skeleton
  Display: '&aa decaying skeleton'
  Health: 15
  Damage: 1
  Faction: Undead
  AIGoalSelectors:
  - clear
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - players
  Equipment:
  - COS_RawHead HEAD
  - COS_WoodSword HAND
  Options:
    Despawn: true
    FollowRange: 10
    AlwaysShowName: false
    MovementSpeed: 0.2
    PreventOtherDrops: true
```

- Decaying Skeleton 现在属于 Undead 阵营，与 Guard 阵营不同，因此守卫会攻击它。加入 **hurtbytarget** 目标选择器后，它在与守卫交战时也会反击，最终被击杀。
- 城镇附近生成的其他生物，也应加入上面为骷髅配置的 AI 行为和攻击目标，并确保它们与守卫不属于同一阵营。

- 现在，当我们在门口为城镇守卫设置刷怪点时，他会击退怪物但忽略玩家（只要他们不打扰守卫）
- 此时还可以缩短守卫的跟随范围（本例为 5），并缩短刷怪点的牵引范围，避免守卫跑出去杀光本该留给玩家获取经验和掉落物的怪物。还应把守卫的 **PreventMobKillDrops** 设为  true ，防止它击杀的怪物为玩家掉落经验或物品。

## 示例 2：兽人与哥布林互相攻击 {#example-2-orcs-and-goblins-attack-each-other}

- 假设世界中有哥布林和兽人两个阵营，彼此敌对。我们设置了一处让它们持续交战的战场，但目前双方都使用骷髅类型和默认 AI，并没有怎么打起来。
- 我们想用 Mythic Mobs 自定义 AI，让它们既攻击进入战场的玩家，也在靠近时互相攻击。
- 让我们创建一个兽人生物和一个哥布林生物。

```yaml
OrcCenturion:
  Type: villagezombie
  Display: '&aan orc centurion'
  Health: 50
  Damage: 4
  Faction: Orcs
  AIGoalSelectors:
  - clear
  - opendoors
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - specificfactionmonsters Goblin
  - players
  Equipment:
  - C_DeathfistSkullcap HEAD
  - C_DeathfistTunic CHEST
  - C_DeathfistLeggings LEGS
  - C_DeathfistBoots FEET
  - COS_WoodSword HAND
  Options:
    Despawn: true
    FollowRange: 10
    AlwaysShowName: false
    MovementSpeed: 0.25
    PreventOtherDrops: true
    PreventItemPickup: true
    KnockbackResistance: 0.25
    PreventMobKillDrops: true
```

```yaml
GoblinBattlemaster:
  Type: zombie
  Display: '&aa goblin battlemaster'
  Health: 80
  Damage: 4
  Faction: Goblin
  AIGoalSelectors:
  - clear
  - opendoors
  - meleeattack
  AITargetSelectors:
  - clear
  - hurtbytarget
  - specificfactionmonsters Orcs
  - players
  Equipment:
  - COS_BronzeHead HEAD
  - COS_BronzeChest CHEST
  - COS_BronzeLegs LEGS
  - COS_BronzeFeet FEET
  - COS_WoodAxe HAND
  Skills:
  - skill{s=BashI} ~onAttack >0 0.25
  Options:
    Despawn: true
    FollowRange: 10
    AlwaysShowName: false
    MovementSpeed: 0.25
    PreventOtherDrops: true
    PreventItemPickup: true
    KnockbackResistance: 0.4    
    PreventMobKillDrops: true
```

- 这里有几项值得注意的配置。

```
    * First we have set the orc mob on the **Orc Faction** and the Goblin mob on the **Goblin Faction**. This will logically separate the two mob types.
    * Next we configure both of the mobs with the standard **clear, opendoors, and meleeattack** actions which is common for most melee type mobs.
    * Lastly we clear our AI then setup three AI target selectors. 

        * First is the **hurtbytarget** selector which as mentioned before is a good fall back option so that mobs can not be exploited by other mobs or players that they will not retaliate against.
    * Next is the **specifictargetfaction** selector with the opposing faction in it. This is set to priority 2 so the goblins and orcs will target each other first when they aren't already in combat 
        * Last is the **players** target selector which tells that mobs to attack players if there are no goblins/orcs nearby.
* Lastly remember to set the **PreventMobKillDrops** to true so that warring npc factions don't drop exp / loots for players that happen to wander by.
* If we have other goblin or orc mob types, we need only copy and paste these AI configurations into their mob setups and they should react similarly to the two mobs above.
```
