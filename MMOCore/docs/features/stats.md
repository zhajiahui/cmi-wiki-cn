---
title: 玩家属性
source: https://docs.phoenixdevt.fr/mmocore/features/stats
source_snapshot: '2026-10-19'
---

# 玩家属性 {#💪-player-stats}

玩家属性是 MMOCore 的基础，可以由职业、基础属性、队伍增益、临时技能和物品等提供。为便于兼容，MMOItems 与 MMOCore 共用属性系统，因此 MMOItems 中的任意属性都可以用于 MMOCore。

## 属性使用原版基础属性修饰符处理 {#stats-handled-with-vanilla-attribute-modifiers}

|属性名称 |描述 |
| --- | --- |
| `attack_damage` | 近战攻击造成的伤害 |
| `attack_speed` | 玩家的攻击速度 |
| `max_health` | 玩家的最大生命值 |
| `movement_speed` | 玩家的行走速度 |
| `knockback_resistance` | 从0到1否定击退(原版玩家基础属性) 的几率 |
| `armor` | 减少受到的伤害，原版玩家基础属性 |
| `armor_toughness` | 原版护甲韧性，减少受到的伤害（参见 MC wiki） |

根据Minecraftwiki，默认玩家移动速度设置为0.1，即4.317m/s。由于一格的测量值为1m^3，因此玩家移动速度的公式为`<attribute_value> * 43.17 m/s`。

### Minecraft1.20.2+ {#minecraft-1-20-2}

| 属性名称 | 描述 |
| --- | --- |
| `max_absorption` | 最大吸收心数 |

### Minecraft1.20.5+ {#minecraft-1-20-5}

| 属性名称 | 描述 |
| --- | --- |
| `block_break_speed` | 玩家的破块速度 |
| `block_interaction_range` | 玩家可以打破或与方块互动多远？ |
| `entity_interaction_range` | 玩家可以击中实体或与实体交互多远 |
| `fall_damage_multiplier` | 增加/减少坠落伤害 |
| `gravity` | 重力有多大 |
| `jump_strength` | 玩家能跳多高（基本上是Jump Boost） |
| `safe_fall_distance` | 玩家可以从多高的地方跌落而不会受到坠落伤害？ |
| `scale` | 玩家有多大（增加玩家的尺寸并偏移相机位置） |
| `step_height` | 玩家行走时无需跳跃可以爬多少个街区 |

### Minecraft1.21+ {#minecraft-1-21}

| 属性名称 | 描述 |
| --- | --- |
| `burning_time` | 实体被点燃后保持着火状态的时间量作为倍数。 |
| `explosion_knockback_resistance` | 由于爆炸而抵抗击退。 |
| `mining_efficiency` | 增加/减少采矿速度的因素 |
| `movement_efficiency` | 在减慢移动速度的方块上行走时的移动速度因素。 |
| `oxygen_bonus` | 确定在水下时不消耗空气的机会。 |
| `sneaking_speed` | 潜行时的移动速度。 |
| `submerged_mining_speed` | 水下采矿速度系数。 |
| `sweeping_damage_ratio` | 扫掠攻击转移的伤害百分比。 |
| `water_movement_efficiency` | 淹没时的移动速度系数。 |

## 资源 {#resources}

| 属性名称 | 描述 |
| --- | --- |
| `max_mana` | 玩家可能具有的最大魔力。 |
| `max_stamina` | 玩家可能具有的最大耐力。 |
| `max_stellium` | Sttellium 是一种用于使用航路点旅行的资源。 |
| `health_regeneration` | 生命值 [再生](combat.md)（以点/秒为单位）。 |
| `mana_regeneration` | 魔力恢复点数/秒 |
| `stamina_regeneration` | 耐力恢复点数/秒 |
| `stellium_regeneration` | 群星回复 (pts/sec) |
| `max_health_regeneration` | 生命恢复百分比（最大生命值/秒） |
| `max_mana_regeneration` | 魔力再生，以最大魔力/秒的百分比表示 |
| `max_stamina_regeneration` | 耐力再生，以最大耐力/秒的百分比表示 |
| `max_stellium_regeneration` | 群星再生（以最大群星/秒的百分比表示） |

## 实用性 {#utility}

| 属性名称 | 描述 |
| --- | --- |
| `additional_experience` | 玩家获得额外经验。 |
| `cooldown_reduction` | 将技能冷却时间减少特定% |
| `speed_malus_reduction` | 减少（%）缓慢的减益效果。 |
| `luck` | 在掉落物宝箱和钓鱼掉落台中获得稀有物品的几率更大。事实上，物品的掉落几率为1%，而10%的幸运几率为100。 |

速度恶意减少不会直接增加玩家的移动速度。它会减少一定量的速度减益效果，例如MMOItems造成的减益效果。通过在MMOItems上注册负移动速度增益，你可以营造物品很重的感觉，并降低玩家佩戴/手持时的移动速度。速度恶意减少可以减少这种缓慢的减益效果。

## 暴击 {#critical-strikes}

| 属性名称 | 描述 |
| --- | --- |
| `critical_strike_chance` | 有机会用武器处理暴击。 |
| `critical_strike_power` | 武器暴击造成额外伤害。 |
| `skill_critical_strike_chance` | 有机会用技能处理暴击。 |
| `skill_critical_strike_power` | 技能暴击造成额外伤害。 |

## 损坏属性 {#damage-stats}

以下属性为伤害倍数*e.g*当设置为50时，指定的攻击伤害会增加50%。

| 属性名称 | 描述 |
| --- | --- |
| `magic_damage` | 额外的魔法技能伤害。 |
| `physical_damage` | 额外物理技能/武器伤害。 |
| `projectile_damage` | 基于武器和技能的额外射弹伤害。 |
| `weapon_damage` | 附加武器基于攻击伤害。 |
| `skill_damage` | 额外技能（魔法/物理）伤害。 |
| `undead_damage` | 对不死生物造成额外伤害。 |
| `pvp_damage` | 对玩家造成额外伤害。 |
| `pve_damage` | 对除玩家之外的任何物体都会造成额外伤害。 |

---

原文：[💪 Player Stats](https://docs.phoenixdevt.fr/mmocore/features/stats) · 原文归档：2026-10-19
