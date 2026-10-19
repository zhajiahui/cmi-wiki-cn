---
title: stats.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: stats.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# stats.yml

文件：`stats.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包配置。

## `ARMOR` { #armor }

```yaml title="stats.yml · ARMOR"
################################################################
# 内置固定属性
################################################################

ARMOR:
  Enabled: true
  Display: "护甲"
  Formatting:
    Additive: "<white><value> 护甲"
    Multiply: "<white><value>% 护甲"
    Compound: "<white><value>x 护甲"
  PlayerBaseValue: 0
```

## `ARMOR_TOUGHNESS` { #armor_toughness }

```yaml title="stats.yml · ARMOR_TOUGHNESS"
ARMOR_TOUGHNESS:
  Enabled: true
  Display: "盔甲韧性"
  Formatting:
    Additive: "<white><value> 盔甲韧性"
    Multiply: "<white><value>% 盔甲韧性"
    Compound: "<white><value>x 盔甲韧性"
  PlayerBaseValue: 0
```

## `ATTACK_DAMAGE` { #attack_damage }

```yaml title="stats.yml · ATTACK_DAMAGE"
ATTACK_DAMAGE:
  Enabled: true
  AlwaysActive: false
  Display: "伤害"
  Type: STATIC
  Formatting:
    Additive: "<white><value> 攻击伤害"
    Multiply: "<white><value>% 攻击伤害"
    Compound: "<white><value>x 攻击伤害"
  PlayerBaseValue: 1
```

## `ATTACK_SPEED` { #attack_speed }

```yaml title="stats.yml · ATTACK_SPEED"
ATTACK_SPEED:
  Enabled: true
  Display: "攻击速度"
  Type: STATIC
  Formatting:
    Additive: "<white><value> 攻击速度"
    Multiply: "<white><value>% 攻击速度"
    Compound: "<white><value>x 攻击速度"
  PlayerBaseValue: 4
  MinValue: -200
```

## `BLOCK_BREAK_SPEED` { #block_break_speed }

```yaml title="stats.yml · BLOCK_BREAK_SPEED"
BLOCK_BREAK_SPEED:
  Enabled: true
  Display: "方块破坏速度"
  Formatting:
    Additive: "<white><value> 方块破坏速度"
    Multiply: "<white><value>% 方块破坏速度"
    Compound: "<white><value>x 方块破坏速度"
  PlayerBaseValue: 1.0
```

## `BLOCK_INTERACTION_RANGE` { #block_interaction_range }

```yaml title="stats.yml · BLOCK_INTERACTION_RANGE"
BLOCK_INTERACTION_RANGE:
  Enabled: true
  Display: "方块交互距离"
  Formatting:
    Additive: "<white><value> 方块交互距离"
    Multiply: "<white><value>% 方块交互距离"
    Compound: "<white><value>x 方块交互距离"
  PlayerBaseValue: 4.5
```

## `BONUS_DAMAGE` { #bonus_damage }

```yaml title="stats.yml · BONUS_DAMAGE"
BONUS_DAMAGE:
  Enabled: false
  Display: "额外伤害"
  Formatting:
    Additive: "<white>+<value> 额外伤害"
    Multiply: "<white>+<value> 额外伤害"
    Compound: "<white>x<value> 额外伤害"
  PlayerBaseValue: 0
```

## `BURNING_TIME` { #burning_time }

```yaml title="stats.yml · BURNING_TIME"
BURNING_TIME:
  Enabled: true
  Display: "燃烧时间"
  Formatting:
    Additive: "<white><value> 燃烧时间"
    Multiply: "<white><value>% 燃烧时间"
    Compound: "<white><value>x 燃烧时间"
  PlayerBaseValue: 1
```

## `CRITICAL_STRIKE_CHANCE` { #critical_strike_chance }

```yaml title="stats.yml · CRITICAL_STRIKE_CHANCE"
CRITICAL_STRIKE_CHANCE:
  Enabled: false
  Display: "暴击"
  Formatting:
    Additive: "<white>+<value> 暴击"
    Multiply: "<white>+<value> 暴击"
    Compound: "<white>x<value> 暴击"
  PlayerBaseValue: 0
  MinValue: 0
  Skills:
    - particles{p=crit;a=50;hS=1;y=1;s=1} @trigger
```

## `CRITICAL_STRIKE_DAMAGE` { #critical_strike_damage }

```yaml title="stats.yml · CRITICAL_STRIKE_DAMAGE"
CRITICAL_STRIKE_DAMAGE:
  Enabled: false
  Display: "暴击伤害"
  Formatting:
    Additive: "<white>+<value> 暴击伤害"
    Multiply: "<white>+<value> 暴击伤害"
    Compound: "<white>x<value> 暴击伤害"
  PlayerBaseValue: 1
```

## `CRITICAL_STRIKE_RESILIENCE` { #critical_strike_resilience }

```yaml title="stats.yml · CRITICAL_STRIKE_RESILIENCE"
CRITICAL_STRIKE_RESILIENCE:
  Enabled: false
  Display: "暴击抗性"
  Formatting:
    Additive: "<white>+<value> 暴击抗性"
    Multiply: "<white>+<value> 暴击抗性"
    Compound: "<white>x<value> 暴击抗性"
  PlayerBaseValue: 0
```

## `DAMAGE_REDUCTION` { #damage_reduction }

```yaml title="stats.yml · DAMAGE_REDUCTION"
DAMAGE_REDUCTION:
  Enabled: false
  Display: "伤害减免"
  Formatting:
    Additive: "<white>+<value> 伤害减免"
    Multiply: "<white>+<value> 伤害减免"
    Compound: "<white>x<value> 伤害减免"
  PlayerBaseValue: 0
```

## `DEFENSE` { #defense }

```yaml title="stats.yml · DEFENSE"
DEFENSE:
  Enabled: false
  Display: "防御"
  Formatting:
    Additive: "<white>+<value> 防御"
    Multiply: "<white>+<value> 防御"
    Compound: "<white>x<value> 防御"
  PlayerBaseValue: 0
```

## `DODGE_CHANCE` { #dodge_chance }

```yaml title="stats.yml · DODGE_CHANCE"
DODGE_CHANCE:
  Enabled: false
  Display: "闪避"
  Formatting:
    Additive: "<white>+<value> 闪避几率"
    Multiply: "<white>+<value> 闪避几率"
    Compound: "<white>x<value> 闪避几率"
  PlayerBaseValue: 0
  Skills: []
```

## `DODGE_NEGATION` { #dodge_negation }

```yaml title="stats.yml · DODGE_NEGATION"
DODGE_NEGATION:
  Enabled: false
  Display: "命中"
  Formatting:
    Additive: "<white>+<value> 命中"
    Multiply: "<white>+<value> 命中"
    Compound: "<white>x<value> 命中"
  PlayerBaseValue: 0
```

## `ENTITY_INTERACTION_RANGE` { #entity_interaction_range }

```yaml title="stats.yml · ENTITY_INTERACTION_RANGE"
ENTITY_INTERACTION_RANGE:
  Enabled: true
  Display: "攻击距离"
  Type: STATIC
  Formatting:
    Additive: "<white><value> 攻击距离"
    Multiply: "<white><value>% 攻击距离"
    Compound: "<white><value>x 攻击距离"
  PlayerBaseValue: 3.0
```

## `EXPLOSION_KNOCKBACK_RESISTANCE` { #explosion_knockback_resistance }

```yaml title="stats.yml · EXPLOSION_KNOCKBACK_RESISTANCE"
EXPLOSION_KNOCKBACK_RESISTANCE:
    Enabled: false
    Display: "爆炸击退抗性"
    Formatting:
        Additive: "<white>+<value> 爆炸击退抗性"
        Multiply: "<white>+<value> 爆炸击退抗性"
        Compound: "<white>x<value> 爆炸击退抗性"
    PlayerBaseValue: 0
```

## `FALL_DAMAGE_MULTIPLIER` { #fall_damage_multiplier }

```yaml title="stats.yml · FALL_DAMAGE_MULTIPLIER"
FALL_DAMAGE_MULTIPLIER:
  Enabled: true
  Display: "摔落伤害倍率"
  Formatting:
    Additive: "<white><value> 摔落伤害倍率"
    Multiply: "<white><value>% 摔落伤害倍率"
    Compound: "<white><value>x 摔落伤害倍率"
  PlayerBaseValue: 1
```

## `FLYING_SPEED` { #flying_speed }

```yaml title="stats.yml · FLYING_SPEED"
FLYING_SPEED:
  Enabled: true
  Display: "飞行速度"
  Formatting:
    Additive: "<white><value> 飞行速度"
    Multiply: "<white><value>% 飞行速度"
    Compound: "<white><value>x 飞行速度"
  PlayerBaseValue: 0.4
```

## `FOLLOW_RANGE` { #follow_range }

```yaml title="stats.yml · FOLLOW_RANGE"
FOLLOW_RANGE:
  Enabled: true
  Display: "跟随范围"
  Formatting:
    Additive: "<white><value> 跟随范围"
    Multiply: "<white><value>% 跟随范围"
    Compound: "<white><value>x 跟随范围"
  PlayerBaseValue: 16.0
```

## `GRAVITY` { #gravity }

```yaml title="stats.yml · GRAVITY"
GRAVITY:
  Enabled: true
  Display: "重力"
  Formatting:
    Additive: "<white><value> 重力"
    Multiply: "<white><value>% 重力"
    Compound: "<white><value>x 重力"
  PlayerBaseValue: 0.08
```

## `HEALTH` { #health }

```yaml title="stats.yml · HEALTH"
HEALTH:
  Enabled: true
  Display: "生命值"
  Formatting:
    Additive: "<white><value> 生命值"
    Multiply: "<white><value>% 生命值"
    Compound: "<white><value>x 生命值"
  PlayerBaseValue: 20
  MinValue: 1
```

## `HEALTH_REGENERATION` { #health_regeneration }

```yaml title="stats.yml · HEALTH_REGENERATION"
HEALTH_REGENERATION:
  Enabled: false
  Display: "生命恢复"
  Formatting:
    Additive: "<white>+<value> 生命恢复"
    Multiply: "<white>+<value> 生命恢复"
    Compound: "<white>x<value> 生命恢复"
  PlayerBaseValue: 0
  MaxValue: 1000000
  MinValue: 0
  Frequency: 60
```

## `JUMP_STRENGTH` { #jump_strength }

```yaml title="stats.yml · JUMP_STRENGTH"
JUMP_STRENGTH:
  Enabled: true
  Type: STATIC
  Display: "跳跃力度"
  Formatting:
    Additive: "<white><value> 跳跃力度"
    Multiply: "<white><value>% 跳跃力度"
    Compound: "<white><value>x 跳跃力度"
  PlayerBaseValue: 0.42
```

## `KNOCKBACK_RESISTANCE` { #knockback_resistance }

```yaml title="stats.yml · KNOCKBACK_RESISTANCE"
KNOCKBACK_RESISTANCE:
  Enabled: true
  Display: "击退抗性"
  Formatting:
    Additive: "<white><value> 击退抗性"
    Multiply: "<white><value>% 击退抗性"
    Compound: "<white><value>x 击退抗性"
  PlayerBaseValue: 0
```

## `LIFESTEAL_CHANCE` { #lifesteal_chance }

```yaml title="stats.yml · LIFESTEAL_CHANCE"
LIFESTEAL_CHANCE:
  Enabled: false
  Display: "吸血几率"
  Formatting:
    Additive: "<white>+<value> 吸血几率"
    Multiply: "<white>+<value> 吸血几率"
    Compound: "<white>x<value> 吸血几率"
  PlayerBaseValue: 0
```

## `LIFESTEAL_POWER` { #lifesteal_power }

```yaml title="stats.yml · LIFESTEAL_POWER"
LIFESTEAL_POWER:
  Enabled: true
  Display: "吸血强度"
  Formatting:
    Additive: "<white>+<value> 吸血强度"
    Multiply: "<white>+<value> 吸血强度"
    Compound: "<white>x<value> 吸血强度"
  PlayerBaseValue: 0.1
```

## `LOOT_BIAS` { #loot_bias }

```yaml title="stats.yml · LOOT_BIAS"
LOOT_BIAS:
  Enabled: true
  Display: "掉落偏向"
  Formatting:
    Additive: "<white>+<value> 掉落偏向"
    Multiply: "<white>+<value> 掉落偏向"
    Compound: "<white>x<value> 掉落偏向"
  PlayerBaseValue: 0.0
```

## `MINING_EFFICIENCY` { #mining_efficiency }

```yaml title="stats.yml · MINING_EFFICIENCY"
MINING_EFFICIENCY:
  Enabled: true
  Display: "挖掘效率"
  Formatting:
    Additive: "<white><value> 挖掘效率"
    Multiply: "<white><value>% 挖掘效率"
    Compound: "<white><value>x 挖掘效率"
  PlayerBaseValue: 0.0
```

## `MOVEMENT_EFFICIENCY` { #movement_efficiency }

```yaml title="stats.yml · MOVEMENT_EFFICIENCY"
MOVEMENT_EFFICIENCY:
  Enabled: true
  Display: "移动效率"
  Formatting:
    Additive: "<white><value> 移动效率"
    Multiply: "<white><value>% 移动效率"
    Compound: "<white><value>x 移动效率"
  PlayerBaseValue: 0
```

## `MOVEMENT_SPEED` { #movement_speed }

```yaml title="stats.yml · MOVEMENT_SPEED"
MOVEMENT_SPEED:
  Enabled: true
  Display: "移动速度"
  Formatting:
    Additive: "<white><value> 移动速度"
    Multiply: "<white><value>% 移动速度"
    Compound: "<white><value>x 移动速度"
  PlayerBaseValue: 0.2
```

## `OXYGEN_BONUS` { #oxygen_bonus }

```yaml title="stats.yml · OXYGEN_BONUS"
OXYGEN_BONUS:
  Enabled: true
  Display: "氧气加成"
  Formatting:
    Additive: "<white><value> 氧气加成"
    Multiply: "<white><value>% 氧气加成"
    Compound: "<white><value>x 氧气加成"
  PlayerBaseValue: 0
```

## `PARRY_CHANCE` { #parry_chance }

```yaml title="stats.yml · PARRY_CHANCE"
PARRY_CHANCE:
  Enabled: false
  Display: "招架几率"
  PlayerBaseValue: 0
  Priority: 0
  Formatting:
    Additive: "<white>+<value> 招架几率"
    Multiply: "<white>+<value> 招架几率"
    Compound: "<white>x<value> 招架几率"
  FrontAngle: 180
  UsableMaterials:
    - WOODEN_SWORD
    - STONE_SWORD
    - GOLDEN_SWORD
    - IRON_SWORD
    - DIAMOND_SWORD
    - NETHERITE_SWORD
  Skills: []
```

## `PARRY_COUNTERATTACK` { #parry_counterattack }

```yaml title="stats.yml · PARRY_COUNTERATTACK"
PARRY_COUNTERATTACK:
  Enabled: false
  Display: "招架反击"
  PlayerBaseValue: 1
  Formatting:
    Additive: "<white>+<value> 招架反击"
    Multiply: "<white>+<value> 招架反击"
    Compound: "<white>x<value> 招架反击"
```

## `PARRY_NEGATION` { #parry_negation }

```yaml title="stats.yml · PARRY_NEGATION"
PARRY_NEGATION:
  Enabled: false
  Display: "招架穿透"
  Formatting:
    Additive: "<white>+<value> 招架穿透"
    Multiply: "<white>+<value> 招架穿透"
    Compound: "<white>x<value> 招架穿透"
  PlayerBaseValue: 0
```

## `PARRY_POWER` { #parry_power }

```yaml title="stats.yml · PARRY_POWER"
PARRY_POWER:
  Enabled: false
  Display: "招架强度"
  PlayerBaseValue: 0.5
  Formatting:
    Additive: "<white>+<value> 招架强度"
    Multiply: "<white>+<value> 招架强度"
    Compound: "<white>x<value> 招架强度"
```

## `SAFE_FALL_DISTANCE` { #safe_fall_distance }

```yaml title="stats.yml · SAFE_FALL_DISTANCE"
SAFE_FALL_DISTANCE:
  Enabled: true
  Display: "安全摔落距离"
  Formatting:
    Additive: "<white><value> 安全摔落距离"
    Multiply: "<white><value>% 安全摔落距离"
    Compound: "<white><value>x 安全摔落距离"
  PlayerBaseValue: 3
```

## `SCALE` { #scale }

```yaml title="stats.yml · SCALE"
SCALE:
  Enabled: true
  AlwaysActive: false
  Display: "缩放"
  PlayerBaseValue: 1
  Formatting:
    Additive: "<white><value> 缩放"
    Multiply: "<white><value>% 缩放"
    Compound: "<white><value>x 缩放"
```

## `SNEAKING_SPEED` { #sneaking_speed }

```yaml title="stats.yml · SNEAKING_SPEED"
SNEAKING_SPEED:
  Enabled: true
  Display: "潜行速度"
  Formatting:
    Additive: "<white><value> 潜行速度"
    Multiply: "<white><value>% 潜行速度"
    Compound: "<white><value>x 潜行速度"
  PlayerBaseValue: 0.3
```

## `STEP_HEIGHT` { #step_height }

```yaml title="stats.yml · STEP_HEIGHT"
STEP_HEIGHT:
  Enabled: true
  Display: "跨越高度"
  Formatting:
    Additive: "<white><value> 跨越高度"
    Multiply: "<white><value>% 跨越高度"
    Compound: "<white><value>x 跨越高度"
  PlayerBaseValue: 0.5
```

## `WATER_MOVEMENT_EFFICIENCY` { #water_movement_efficiency }

```yaml title="stats.yml · WATER_MOVEMENT_EFFICIENCY"
WATER_MOVEMENT_EFFICIENCY:
  Enabled: true
  Display: "水中移动效率"
  Formatting:
    Additive: "<white><value> 水中移动效率"
    Multiply: "<white><value>% 水中移动效率"
    Compound: "<white><value>x 水中移动效率"
  PlayerBaseValue: 0
```

## `AGILITY` { #agility }

```yaml title="stats.yml · AGILITY"
################################################################
#
# 自定义属性示例
#
################################################################

AGILITY:
  Enabled: false
  Type: MUTATOR
  AlwaysActive: true
  Display: "敏捷"
  PlayerBaseValue: 0
  MaxValue: 100
  MinValue: 0
  Formatting:
    Additive: "<white>+<value> 敏捷"
    Multiply: "<white>+<value> 敏捷"
    Compound: "<white>x<value> 敏捷"
    Rounding: 2
  Components:
    - Stat: BONUS_DAMAGE
      Formula: 'v / 5'
      Operation: ADDITIVE
    - Stat: CRITICAL_STRIKE_CHANCE
      Formula: 'v / 1000'
      Operation: ADDITIVE
    - Stat: DODGE_CHANCE
      Formula: 'v / 2000'
      Operation: ADDITIVE
```

## `ARMOR_GENERIC` { #armor_generic }

```yaml title="stats.yml · ARMOR_GENERIC"
ARMOR_GENERIC:
  Enabled: false
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  ExecutionPoint: PRE
  Display: "通用护甲"
  DamageFormula: 'd - v'
  PlayerBaseValue: 0
  Formatting:
    Additive: "<white>+<value> 通用护甲"
    Multiply: "<white>+<value> 通用护甲"
    Compound: "<white>x<value> 通用护甲"
```

## `ARMOR_BLUNT` { #armor_blunt }

```yaml title="stats.yml · ARMOR_BLUNT"
ARMOR_BLUNT:
  Enabled: false
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  ExecutionPoint: PRE
  Display: "钝击护甲"
  DamageType: BLUNT
  DamageFormula: 'd - v'
  PlayerBaseValue: 0
  Formatting:
    Additive: "<white>+<value> 钝击护甲"
    Multiply: "<white>+<value> 钝击护甲"
    Compound: "<white>x<value> 钝击护甲"
```

## `ARMOR_SHARP` { #armor_sharp }

```yaml title="stats.yml · ARMOR_SHARP"
ARMOR_SHARP:
  Enabled: false
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  ExecutionPoint: PRE
  Display: "利刃护甲"
  DamageType: SHARP
  DamageFormula: 'd - v'
  PlayerBaseValue: 0
  Formatting:
    Additive: "<white>+<value> 利刃护甲"
    Multiply: "<white>+<value> 利刃护甲"
    Compound: "<white>x<value> 利刃护甲"
```

## `DAMAGE_BLUNT` { #damage_blunt }

```yaml title="stats.yml · DAMAGE_BLUNT"
DAMAGE_BLUNT:
  Enabled: false
  Type: DAMAGE_BONUS
  Priority: 1
  Triggers:
    - ATTACK
  ExecutionPoint: PRE
  Display: "钝击伤害"
  DamageType: BLUNT
  PlayerBaseValue: 0
  Formatting:
    Additive: "<white>+<value> 钝击伤害"
    Multiply: "<white>+<value> 钝击伤害"
    Compound: "<white>x<value> 钝击伤害"
```

## `DAMAGE_SHARP` { #damage_sharp }

```yaml title="stats.yml · DAMAGE_SHARP"
DAMAGE_SHARP:
  Enabled: false
  Type: DAMAGE_BONUS
  Priority: 2
  Triggers:
    - ATTACK
  ExecutionPoint: PRE
  Display: "利刃伤害"
  DamageType: SHARP
  PlayerBaseValue: 0
  Formatting:
    Additive: "<white>+<value> 利刃伤害"
    Multiply: "<white>+<value> 利刃伤害"
    Compound: "<white>x<value> 利刃伤害"
```

## `FIRE_RESISTANCE` { #fire_resistance }

```yaml title="stats.yml · FIRE_RESISTANCE"
FIRE_RESISTANCE:
  Enabled: false
  Display: "火焰抗性"
  Formatting:
    Additive: "<white>+<value> 火焰抗性"
    Multiply: "<white>+<value> 火焰抗性"
    Compound: "<white>x<value> 火焰抗性"
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  Conditions:
    - (damageCause FIRE || damageCause FIRE_TICK)
  ExecutionPoint: PRE
  DamageFormula: 'd * (1 - v)'
  MaxValue: 1
  MinValue: 0
```
