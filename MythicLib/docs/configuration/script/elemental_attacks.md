---
title: script/elemental_attacks.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: script/elemental_attacks.yml
source_version: 1.7.1-SNAPSHOT
---

# script/elemental_attacks.yml

文件：`script/elemental_attacks.yml`。版本：`1.7.1-SNAPSHOT`。

随包脚本。

## `fire_elemental_attack` { #fire_elemental_attack }

```yaml title="script/elemental_attacks.yml · fire_elemental_attack"
# 火
fire_elemental_attack:
    mechanics:
        display_particles:
            type: particle
            particle: FLAME
            amount: 8
            speed: .05
```

## `fire_critical_strike` { #fire_critical_strike }

```yaml title="script/elemental_attacks.yml · fire_critical_strike"
fire_critical_strike:
    mechanics:
        ignite:
            type: set_on_fire
            ticks: '<stat.fire_damage> * 2'
        play_sound:
            type: sound
            sound: ENTITY_BLAZE_HURT
        fireparticles:
            type: particle
            particle: FLAME
            amount: 8
            speed: .05
        lavaparticles:
            type: particle
            particle: LAVA
            amount: 14
            speed: 0
```

## `ice_elemental_attack` { #ice_elemental_attack }

```yaml title="script/elemental_attacks.yml · ice_elemental_attack"
# 冰
ice_elemental_attack:
    mechanics:
        display_particles:
            type: particle
            particle: BLOCK_CRACK
            amount: 16
            speed: .07
            block: ICE
```

## `ice_critical_strike` { #ice_critical_strike }

```yaml title="script/elemental_attacks.yml · ice_critical_strike"
ice_critical_strike:
    mechanics:
        display_particles:
            type: particle
            particle: BLOCK_CRACK
            amount: 16
            speed: .07
            block: ICE
        play_sound:
            type: sound
            sound: BLOCK_GLASS_BREAK
            pitch: 0
        apply_root:
            type: potion
            effect: SLOW
            duration: '<attack.damage> * 1.5'
            level: 5
        draw_helix:
            type: helix
            height: 3
            source:
                type: target
                position: FEET
            radius: 1
            tick: ice_crit_strike_subskill
```

## `ice_crit_strike_subskill` { #ice_crit_strike_subskill }

```yaml title="script/elemental_attacks.yml · ice_crit_strike_subskill"
ice_crit_strike_subskill:
    mechanics:
        showparticle:
            type: particle
            particle: REDSTONE
            color:
                red: 0
                green: 0
                blue: 0
```

## `wind_elemental_attack` { #wind_elemental_attack }

```yaml title="script/elemental_attacks.yml · wind_elemental_attack"
# 风
wind_elemental_attack:
    mechanics:
        display_particles:
            type: particle
            particle: EXPLOSION_NORMAL
            amount: 8
            speed: .06
```

## `wind_critical_strike` { #wind_critical_strike }

```yaml title="script/elemental_attacks.yml · wind_critical_strike"
wind_critical_strike:
    mechanics:
        display_particles:
            type: particle
            particle: EXPLOSION_NORMAL
            amount: 8
            speed: .06
        play_sound:
            type: sound
            sound: ENTITY_ENDER_DRAGON_GROWL
            pitch: 2

        # 计算击退
        init_vector:
            type: set_vector
            x: '<target.location.x> - <caster.location.x>'
            y: '<target.location.y> - <caster.location.y>'
            z: '<target.location.z> - <caster.location.z>'
            variable: knockback
        norm_vector:
            type: normalize_vector
            variable: knockback
        multiply_vector:
            type: multiply_vector
            variable: knockback
            coef: 2
        set_y:
            type: set_y
            y: '0.5'
            variable: knockback
        knockback:
            type: set_velocity
            vector: knockback
        subskill:
            type: script
            name: wind_crit_sub_skill
            target:
                type: nearby_entities
                radius: 3
                height: 1
```

## `wind_crit_sub_skill` { #wind_crit_sub_skill }

```yaml title="script/elemental_attacks.yml · wind_crit_sub_skill"
wind_crit_sub_skill:
    conditions: # 过滤无法选中的实体
        cantarget:
            type: can_target
            interaction_type: OFFENSE_ACTION
    mechanics:
        knockback:
            type: set_velocity
            vector: knockback
        play_hurt_effect:
            type: entity_effect
            effect: HURT
```

## `earth_elemental_attack` { #earth_elemental_attack }

```yaml title="script/elemental_attacks.yml · earth_elemental_attack"
# 土
earth_elemental_attack:
    mechanics:
        display_particles:
            type: particle
            particle: BLOCK_CRACK
            amount: 24
            speed: .05
            block: DIRT
```

## `earth_critical_strike` { #earth_critical_strike }

```yaml title="script/elemental_attacks.yml · earth_critical_strike"
earth_critical_strike:
    mechanics:
        display_particles:
            type: particle
            particle: BLOCK_CRACK
            amount: 64
            target:
                type: target
                position: FEET
            x: 1
            z: 1
            speed: .05
            block: DIRT
        play_sound:
            type: sound
            sound: BLOCK_GRASS_BREAK
            pitch: 0
        define_vel:
            type: set_vector
            x: 0
            y: 1
            z: 0
            variable: knockup
        knockup:
            type: set_velocity
            vector: knockup
        subskill:
            type: script
            name: earth_crit_subskill
            target:
                type: nearby_entities
                radius: 3
                height: 1
```

## `earth_crit_subskill` { #earth_crit_subskill }

```yaml title="script/elemental_attacks.yml · earth_crit_subskill"
earth_crit_subskill:
    conditions: # 过滤无法选中的实体
        cantarget:
            type: can_target
            interaction_type: OFFENSE_ACTION
    mechanics:
        knockup:
            type: set_velocity
            vector: knockup
```

## `thunder_elemental_attack` { #thunder_elemental_attack }

```yaml title="script/elemental_attacks.yml · thunder_elemental_attack"
# 雷
thunder_elemental_attack:
    mechanics:
        display_particles:
            type: particle
            particle: FIREWORKS_SPARK
            amount: 8
            speed: .05
```

## `thunder_critical_strike` { #thunder_critical_strike }

```yaml title="script/elemental_attacks.yml · thunder_critical_strike"
thunder_critical_strike:
    mechanics:
        play_sound:
            type: sound
            sound: ENTITY_FIREWORK_ROCKET_LARGE_BLAST
            pitch: 0
        spawnparticle:
            type: particle
            particle: FIREWORKS_SPARK
            target:
                type: circle
                radius: 1
                amount: 32
        subskill:
            type: script
            name: thunder_crit_subskill_1
            target:
                type: nearby_entities
                radius: 3
```

## `thunder_crit_subskill_1` { #thunder_crit_subskill_1 }

```yaml title="script/elemental_attacks.yml · thunder_crit_subskill_1"
thunder_crit_subskill_1:
    conditions: # 过滤无法选中的实体
        cantarget:
            type: can_target
            interaction_type: OFFENSE_ACTION
    mechanics:
        dealdamage:
            type: damage
            amount: '<attack.damage> * .2'
```

## `water_elemental_attack` { #water_elemental_attack }

```yaml title="script/elemental_attacks.yml · water_elemental_attack"
# 水
water_elemental_attack:
    mechanics:
        display_particles:
            type: particle
            particle: BLOCK_CRACK
            amount: 32
            speed: .07
            block: WATER
```

## `water_critical_strike` { #water_critical_strike }

```yaml title="script/elemental_attacks.yml · water_critical_strike"
water_critical_strike:
    mechanics:
        init_variable:
            type: set_double
            variable: angle
            value: 0
        draw_helix:
            type: helix
            height: 3
            source:
                type: target
                position: FEET
            radius: 'sin(<angle>)'
            tick: water_crit_subskill_2
        subskill:
            type: script
            name: water_crit_subskill_1
            target:
                type: nearby_entities
                radius: 3
```

## `water_crit_subskill_2` { #water_crit_subskill_2 }

```yaml title="script/elemental_attacks.yml · water_crit_subskill_2"
water_crit_subskill_2:
    mechanics:
        increase_angle:
            type: set_double
            variable: angle
            value: '<angle> + 0.02618'
        showparticle:
            type: particle
            particle: WATER_DROP
```

## `water_crit_subskill_1` { #water_crit_subskill_1 }

```yaml title="script/elemental_attacks.yml · water_crit_subskill_1"
water_crit_subskill_1:
    conditions: # 过滤无法选中的实体
        cantarget:
            type: can_target
            interaction_type: OFFENSE_ACTION
    mechanics:
        slow_down:
            type: potion
            effect: SLOW
            duration: '<attack.damage> * 2'
            level: 1
```
