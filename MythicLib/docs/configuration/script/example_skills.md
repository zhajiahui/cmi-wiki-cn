---
title: script/example_skills.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: script/example_skills.yml
source_version: 1.7.1-SNAPSHOT
---

# script/example_skills.yml

文件：`script/example_skills.yml`。版本：`1.7.1-SNAPSHOT`。

随包脚本。

## `none` { #none }

```yaml title="script/example_skills.yml · none"
# 不执行任何操作
none:
    public: true
```

## `empty_skill` { #empty_skill }

```yaml title="script/example_skills.yml · empty_skill"
empty_skill:
    public: true
```

## `staff_attack` { #staff_attack }

```yaml title="script/example_skills.yml · staff_attack"
# 一种魔法法杖攻击
staff_attack:
    public: true
    mechanics:
        raycast:
            type: raytrace
            hit_entity: staff_attack_hit_entity
            tick: staff_attack_tick
            size: 1
```

## `staff_attack_hit_entity` { #staff_attack_hit_entity }

```yaml title="script/example_skills.yml · staff_attack_hit_entity"
staff_attack_hit_entity:
    conditions:
        cantarget:
            type: can_target
    mechanics:
        dealdamage:
            type: damage
            amount: 10
            ignore_immunity: true
        showparticles:
            type: particle
            particle: LAVA
            amount: 32
```

## `staff_attack_tick` { #staff_attack_tick }

```yaml title="script/example_skills.yml · staff_attack_tick"
staff_attack_tick:
    mechanics:
        showparticles:
            type: particle
            particle: REDSTONE
            amount: 4
            x: .5
            y: .5
            z: .5
```
