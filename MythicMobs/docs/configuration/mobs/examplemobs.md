---
title: mobs/ExampleMobs.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: mobs/ExampleMobs.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# mobs/ExampleMobs.yml

文件：`mobs/ExampleMobs.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包示例配置。

## `SkeletalKnight` { #skeletalknight }

```yaml title="mobs/ExampleMobs.yml · SkeletalKnight"
# 更多信息请查看插件手册，或加入 Discord：
# http://www.mythicmobs.net
#  

#
# 一只非常强壮的凋灵骷髅
#
SkeletalKnight:
  Type: WITHER_SKELETON
  Display: "&a骷髅骑士"
  Health: 40
  Damage: 8
  Equipment:
  - IRON_HELMET HEAD
  - IRON_CHESTPLATE CHEST
  - IRON_LEGGINGS LEGS
  - IRON_BOOTS FEET
  - IRON_SWORD HAND
  - SHIELD OFFHAND
  Drops:
  - "GOLD_NUGGET{display=\"金币\"} 1to2 0.5"
  LevelModifiers:
  - health 5
  - damage 0.5
  Options:
    MovementSpeed: 0.1
```

## `SkeletonKing` { #skeletonking }

```yaml title="mobs/ExampleMobs.yml · SkeletonKing"
#
# 骷髅之王！会召唤骷髅随从，
# 并使用传送砸击攻击。
# 
SkeletonKing:
  Type: WITHER_SKELETON
  Display: "&6骷髅王"
  Health: 500
  Damage: 10
  Skills:
  - "speak{m=\"无人能挑战骷髅王！\";cooldown=20} @PlayersInRadius{r=40} ~onCombat 0.2"
  - "speak{m=\"啊哈哈哈哈！受死吧，<trigger.name>！\"} @PlayersInRadius{r=40} ~onPlayerKill"
  - skill{s=SummonSkeletons} @self 0.1
  - skill{s=SmashAttack} @target 0.2
  Equipment:
  - KingsCrown HEAD
  - SkeletonKingSword HAND
  Drops:
  - SkeletonKingDrops
  Options:
    AlwaysShowName: true
    MovementSpeed: 0.2
    MaxCombatDistance: 25
    PreventOtherDrops: true
```

## `SkeletalMinion` { #skeletalminion }

```yaml title="mobs/ExampleMobs.yml · SkeletalMinion"
#
# 骷髅王的一名弱小随从
#
SkeletalMinion:
  Type: SKELETON
  Display: "&2骷髅随从"
  Health: 10
  Damage: 2
  Options:
    MovementSpeed: 0.1
```

## `StaticallyChargedSheep` { #staticallychargedsheep }

```yaml title="mobs/ExampleMobs.yml · StaticallyChargedSheep"
#
# 一只带电的绵羊，会用闪电
# 攻击附近的一切！同时免疫
# 闪电伤害，火焰伤害减半。
#
StaticallyChargedSheep:
  Type: SHEEP
  Display: "&a带静电的绵羊"
  Health: 100
  Damage: 2
  Options:
    MovementSpeed: 0.3
  DamageModifiers:
  - LIGHTNING 0
  - FIRE 0.5
  Skills:
  - lightning @LivingInRadius{r=10} ~onTimer:100
```

## `AngrySludge` { #angrysludge }

```yaml title="mobs/ExampleMobs.yml · AngrySludge"
#
# 一只暴怒的巨型史莱姆，会向
# 附近所有玩家释放一波波毒素！
#
AngrySludge:
  Type: SLIME
  Display: "&a暴怒污泥怪"
  Health: 100
  Damage: 2
  Options:
    Size: 20
    MovementSpeed: 0.1
    PreventSlimeSplit: true
    PreventOtherDrops: true
    MaxCombatDistance: 30
    KnockbackResistance: 1
  Skills:
  - skill{s=AngrySludgePoison} 0.2
  - blockmask{material=SLIME_BLOCK;r=1;duration=100} @self ~onTimer:20
```
