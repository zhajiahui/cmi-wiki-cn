---
title: 生物示例
source_url: https://wiki.mythiccraft.io/mythicmobs/examples/Mob-Examples
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 生物示例 {#mob-examples}

## 敌对生物 {#hostile-mobs}

### 恶魔 {#demon}

恶魔会敌视玩家、攻击它的实体，以及属于 "good" 阵营的所有 MythicMob。它还装备了下界合金斧，带有火焰粒子，可以悬浮和发射火球（因为它以烈焰人为基础生物！）。它使用了自定义皮肤，需要[伪装](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Mobs/Disguises)功能。

难度：`⭐⭐⭐`（中等）

### 教程 {#tutorial}

先为生物添加一些基本选项：

```yml
Demon:
  Type: blaze # Mob Type
  Display: 'Demon' # Mob Display name
  Damage: 6 # The amount of Damage it deals
  Health: 60 # The amount of Health it has
  Faction: bad # Set the Demon's faction as "bad".
  Disguise: Player 164_ setCustomName Demon setCustomNameVisible false # Disguise it as a player with a skin. Requires LibsDisguises.
```

然后添加自定义 AI，防止它攻击不应攻击的实体：

```yml
  # ...
  AIGoalSelectors:  # We will not clear the mob's base AI, instead adding to it
  - meleeattack # Uses melee attacks
  - randomstroll # Randomly walks
  - float # floats on water
  AITargetSelectors:
  - clear # Clears the mob's base AI
  - players # Firstly targets players
  - attacker # Targets whatever attacks it
  - specificfaction good # Targets mobs from the faction "good"
```

给这个生物配上一把斧：

```yml
  # ...
  Equipment:
  - NETHERITE_AXE HAND # Makes the mob hold a netherite axe in its hand
```

现在进一步自定义这个生物：

1. 让生物的名称只在特定时候显示。
2. 然后，禁止生物死亡时掉落烈焰人的原版掉落物。
3. 此外，禁止被这个烈焰人击杀的生物掉落战利品。
4. 将生物的移动速度设为 `0.35`。
5. 让生物发出声音。

最终配置如下：

```yml
  # ...
  Options:
    AlwaysShowName: false # Don't always show name unless hovered
    PreventOtherDrops: true # Don't drop default blaze drops on death
    PreventMobKillDrops: true # Prevent mobs that the demon kills from dropping loot
    MovementSpeed: 0.35 # Sets movement speed
    Silent: false # Play the default blaze sound effects
```

最后，添加一些能力，让这个生物更有趣。

```yml
  # ...
  Skills:
  # PARTICLE EFFECTS
  - effect:flames @self ~onTimer:100 # Every 100 ticks (5 seconds), show a spawner flame effect on mob's location.
  # SOUND EFFECTS
  - effect:sound{s=entity.elder_guardian.ambient;v=1;p=2} @self 0.5 ~onTimer:150 # Every 150 ticks (7.5 seconds), 50% chance to play the entity.elder_guardian.ambient sound with volume 1 and pitch 2
  - effect:sound{s=entity.elder_guardian.hurt;v=1;p=0.7} @self ~onDamaged # When the mob gets damaged, play the entity.elder_guardian.hurt sound with volume 1 and pitch 0.7
  - effect:sound{s=entity.elder_guardian.death;v=1;p=0.7} @self ~onDeath # When the mob dies, play the entity.elder_guardian.death sound with volume 1 and pitch 0.7
  - effect:sound{s=entity.blaze.death;v=0.3;p=0.7} @self ~onDeath # When the mob dies, also play the entity.blaze.death sound with volume 0.3 and pitch 0.7
```

这些技能主要为生物添加自定义声音和效果，让它更加生动。

```yml
Demon:
  Type: blaze # Mob Type
  Display: 'Demon' # Mob Display name
  Damage: 6 # The amount of Damage it deals
  Health: 60 # The amount of Health it has
  Faction: bad # Set the Demon's faction as "bad".
  Disguise: Player 164_ setCustomName Demon setCustomNameVisible false # Disguise it as a player with a skin. Requires LibsDisguises.
  AIGoalSelectors:  # We will not clear the mob's base AI, instead adding to it
  - meleeattack # Uses melee attacks
  - randomstroll # Randomly walks
  - float # Randomly floats
  AITargetSelectors:
  - clear # Clears the mob's base AI
  - players # Firstly targets players
  - attacker # Targets whatever attacks it
  - specificfaction good # Targets mobs from the faction "good"
  Equipment:
  - NETHERITE_AXE HAND # Makes the mob hold a netherite axe in its hand
  Options:
    AlwaysShowName: false
    PreventOtherDrops: true
    PreventMobKillDrops: true
    MovementSpeed: 0.35
    Silent: false
  Skills:
  # PARTICLE EFFECTS
  - effect:flames @self ~onTimer:100 # Every 100 ticks (5 seconds), show a spawner flame effect on mob's location.
  # SOUND EFFECTS
  - effect:sound{s=entity.elder_guardian.ambient;v=1;p=2} @self 0.5 ~onTimer:150 # Ever 150 ticks (7.5 seconds), 50% chance to play the entity.elder_guardian.ambient sound with volume 1 and pitch 2
  - effect:sound{s=entity.elder_guardian.hurt;v=1;p=0.7} @self ~onDamaged # When the mob gets damaged, play the entity.elder_guardian.hurt sound with volume 1 and pitch 0.7
  - effect:sound{s=entity.elder_guardian.death;v=1;p=0.7} @self ~onDeath # When the mob dies, play the entity.elder_guardian.death sound with volume 1 and pitch 0.7
  - effect:sound{s=entity.blaze.death;v=0.3;p=0.7} @self ~onDeath # When the mob dies, also play the entity.blaze.death sound with volume 0.3 and pitch 0.7
```

---

### 哨兵 {#the-sentinel}

一个迅捷而危险的小 Boss，会发出恐怖的声音，带有粒子效果，头戴命令方块，并使用下界合金剑击败挡路的所有目标。

```yaml
Sentinel:
  Type: wither_skeleton # Base mob wither skeleton. Keep note that this means that when the mob attacks other entities, they will receive the WITHER effect.
  Display: 'Sentinel' # The name of the mob.
  Damage: 10 # Deals 10 damage on hit
  Health: 120 # Has 120 HP.
  Faction: bad # Sets the mob to be in the faction 'bad'
  AIGoalSelectors: # What's the mob going to do?
  - clear # Clears the mob's AI
  - meleeattack # Melee-attacks its targets
  - lookatplayers # Looks at players.
  - randomstroll # Randomly walks around when off-combat.
  AITargetSelectors:
  - clear # Clears the mob's AI
  - players # Targets players
  - attacker # Then targets whatever attacks it
  - otherfaction # Targets whatever is not in the 'bad' faction
  Options: # Additional mob options
    PreventSunburn: true # Prevents the mob from burning in daylight
    AlwaysShowName: false # Prevents the mob from showing its name all the time. (Players will have to look at the mob to show the name)
    PreventOtherDrops: true # Prevents vanilla wither skeleton drops.
    PreventMobKillDrops: true # Prevents mobs that the Sentinel kills from dropping loot.
    MovementSpeed: 0.45 # Fast movement speed.
    Silent: true # Disables its default sounds. Useful if you are going to use custom sounds.
  Equipment: # Things that the mob will wear.
  - COMMAND_BLOCK HEAD # Wears a Command Block on its head.
  - NETHERITE_SWORD HAND # Holds a Netherite Sword in its hand
  Skills:
  # SOUNDS
  - effect:sound{s=entity.enderman.scream;v=1;p=0.2} @self ~onDeath
  - effect:sound{s=entity.enderman.hurt;v=1;p=0.2} @self ~onDamaged
  - effect:sound{s=entity.enderman.stare;v=.2;p=0.2} @self ~onTimer:150 0.5
  # PARTICLES
  - effect:particles{particle=spell;amount=50;hS=1;vS=1;speed=5} @self ~onTimer:2 0.8
  # ABILITIES
  - throw{velocity=8;velocityY=4} @EIR{r=4} ~onDamaged 0.2 # When damaged, the mob has a 20% chance to launch nearby players in a radius of 4.
```

## 中立生物 {#neutral-mobs}

### 冒险者 {#the-adventurer}

一个简单的生物，会保护这片土地，用铁剑攻击敌对生物，随机说话，在遭到攻击时自卫，并在获胜后庆祝。它使用了自定义皮肤，需要[伪装](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Mobs/Disguises)功能。

```yaml
Adventurer:
  Type: zombie
  Display: 'Adventurer'
  Damage: 6
  Health: 65
  Faction: good
  Disguise: Player Refreshin setCustomName Adventurer setCustomNameVisible true
  AIGoalSelectors:
  - clear
  - meleeattack
  - lookatplayers
  - randomstroll
  - float
  AITargetSelectors:
  - clear
  - attacker
  - otherfactionmonsters
  Equipment:
  - IRON_SWORD HAND
  Options:
    PreventSunburn: true
    AlwaysShowName: false
    PreventOtherDrops: true
    PreventMobKillDrops: true
    MovementSpeed: 0.26
    Silent: true
  Skills:
  - effect:sound{s=entity.villager.ambient;v=.6;p=0.7} @self ~onTimer:60 0.6
  - effect:sound{s=entity.villager.yes;v=.6;p=0.7} @self ~onKill
  - effect:sound{s=entity.villager.hurt;v=.6;p=0.7} @self ~onDamaged
  Drops:
  - IRON_SWORD 1
```

## 被动生物 {#passive-mobs}

### 平民 {#the-civilian}

平民是温顺、不喜欢战斗的 NPC 生物。他们会逃离战斗，玩家右键点击时会与玩家交谈。他们也会像普通村民一样获得职业。此生物使用了自定义皮肤，需要[伪装](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Mobs/Disguises)功能；还使用了需要 [Mythicmobs Premium](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Premium-Features) 的 AIGoalSelectors。

```yaml
Citizen:
  Type: VILLAGER
  Display: 'Civilian'
  Damage: 6
  Health: 20
  Faction: good
  Disguise: Player Refreshin setCustomName Civilian setCustomNameVisible true
  AIGoalSelectors:
  - fleeConditional{distance=15;speed=1;safespeed=1;conditions=[ - incombat true ]}
  AITargetSelectors:
  - clear
  - attacker
  Options:
    PreventItemPickup: false
    AlwaysShowName: false
    Despawn: true
    PreventOtherDrops: true
    PreventMobKillDrops: true
    MovementSpeed: 0.35
    Silent: true
  Skills:
  - effect:sound{s=entity.villager.yes;v=.6;p=0.8} @self ~onInteract
  - effect:sound{s=entity.villager.hurt;v=.6;p=0.8} @self ~onDamaged
  - effect:sound{s=entity.villager.death;v=.6;p=0.8} @self ~onDeath
  Drops:
  - BREAD 1-3 0.4
  - CARROT 1-3 0.4
  - BEETROOT 1-3 0.4
  - POTATO 1-3 0.4
  - EMERALD 1-2 0.1
  - GOLD_NUGGET 1-6 0.2
  - DIAMOND 1 0.01
```
