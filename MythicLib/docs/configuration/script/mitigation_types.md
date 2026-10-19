---
title: script/mitigation_types.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: script/mitigation_types.yml
source_version: 1.7.1-SNAPSHOT
---

# script/mitigation_types.yml

文件：`script/mitigation_types.yml`。版本：`1.7.1-SNAPSHOT`。

随包脚本。

## `mitigation_on_block` { #mitigation_on_block }

```yaml title="script/mitigation_types.yml · mitigation_on_block"
######################################
# 格挡
######################################

mitigation_on_block:
  mechanics:

    # 先计算格挡系数并降低伤害
    - 'set_double{variable="block_coef";value="<stat.block_power>/100"}'
    - 'multiply_damage{amount="1 - <block_coef>"}'

    # 发送消息并播放音效
    - 'set_double{variable="damaged_blocked";value="<attack.damage> * <block_coef>"}'
    - "action_bar{m=\"&c你格挡了 <damaged_blocked.round.2> 点伤害！\";target=caster;priority=31}"
    - 'play_sound{sound=ENTITY_ZOMBIE_ATTACK_IRON_DOOR;volume=1;pitch=2}'
    - 'set_double{variable=max_angle;value=120}'
    - 'script{name=mitigation_block_particle_effect}'
```

## `mitigation_block_particle_effect` { #mitigation_block_particle_effect }

```yaml title="script/mitigation_types.yml · mitigation_block_particle_effect"
# 同时用于斩击和穿刺
mitigation_block_particle_effect:
  conditions:
    - 'variable_exists{var=target}' # 仅在目标存在时
  mechanics:
    - 'copy_vector{variable=dir;value=target.location}'
    - 'copy_vector{variable=src;value=caster.location}'
    - 'subtract_vector{variable=dir;value=caster.location}'
    - 'script{name=mitigation_block_particle_effect_1;counter=counter_a;iterations=10}'
```

## `mitigation_block_particle_effect_1` { #mitigation_block_particle_effect_1 }

```yaml title="script/mitigation_types.yml · mitigation_block_particle_effect_1"
mitigation_block_particle_effect_1:
  mechanics:
    - 'script{name=mitigation_block_particle_effect_2;counter=counter_z;iterations=8}'
```

## `mitigation_block_particle_effect_2` { #mitigation_block_particle_effect_2 }

```yaml title="script/mitigation_types.yml · mitigation_block_particle_effect_2"
mitigation_block_particle_effect_2:
  mechanics:
    - 'set_double{variable=angle;value="pi / 180.0 * (<dir.yaw> + 90 + <max_angle> * ( <counter_a> / 10 - 0.5))"}'
    - 'copy_vector{variable=inter;value=src}'
    - 'add_vector{variable=inter;x="cos(<angle>)";y=".25 + <counter_z> * 1.5/8";z="sin(<angle>)"}'
    - 'particle{particle=REDSTONE;target={type=variable;name=inter};color={red=128;green=128;blue=128}}'
    - 'script{name=mitigation_block_particle_effect_3;target_location={type=variable;name=inter}}'
```

## `mitigation_block_particle_effect_3` { #mitigation_block_particle_effect_3 }

```yaml title="script/mitigation_types.yml · mitigation_block_particle_effect_3"
mitigation_block_particle_effect_3:
  conditions:
    - 'chance{c=0.1}'
  mechanics:
    - 'particle{particle=CRIT;speed=.3}'
```

## `mitigation_on_dodge` { #mitigation_on_dodge }

```yaml title="script/mitigation_types.yml · mitigation_on_dodge"
######################################
# 闪避
######################################

mitigation_on_dodge:
  mechanics:

    - 'cancel_event{}' # 抵消全部伤害
    - 'set_no_damage_ticks{target=caster;ticks=10}' # 短暂使玩家无敌，避免伤害叠加

    # 发送消息，并播放音效和粒子效果
    - "action_bar{m=\"&c你闪避了 <attack.damage> 点伤害！\";target=caster;priority=31}"
    - 'play_sound{sound=ENTITY_ENDER_DRAGON_FLAP;volume=1;pitch=1}'
    - 'particle{particle=POOF;target=caster;amount=16;x=.5;y=.5;z=.5}'
    - 'script{name=mitigation_dodge_knockback}'
```

## `mitigation_dodge_knockback` { #mitigation_dodge_knockback }

```yaml title="script/mitigation_types.yml · mitigation_dodge_knockback"
mitigation_dodge_knockback:
  conditions:
    - 'variable_exists{var=target}' # 仅在目标存在时
  mechanics:
    - 'copy_vector{var=dir;val=target.location}'
    - 'sub_vector{var=dir;val=caster.location}'
    - 'multiply_vector{var=dir;value=-1}'
    - 'set_y{var=dir;y=0}'
    - 'normalize_vector{var=dir}'
    - 'set_y{var=dir;y=0.35}'
    - 'set_velocity{vector=dir;target=caster}'
```

## `mitigation_on_parry` { #mitigation_on_parry }

```yaml title="script/mitigation_types.yml · mitigation_on_parry"
######################################
# 招架
######################################

mitigation_on_parry:
  mechanics:

    - 'cancel_event{}' # 抵消全部伤害
    - 'set_no_damage_ticks{target=caster;ticks=10}' # 短暂使玩家无敌，避免伤害叠加

    # 发送消息，并播放音效和粒子效果
    - "action_bar{m=\"&c你招架了 <attack.damage> 点伤害！\";target=caster;priority=31}"
    - 'play_sound{sound=ENTITY_ENDER_DRAGON_FLAP;volume=1;pitch=1}'
    - 'particle{particle=POOF;target=caster;amount=16;x=.5;y=.5;z=.5}'
    - 'script{name=mitigation_parry_knockback}'
```

## `mitigation_parry_knockback` { #mitigation_parry_knockback }

```yaml title="script/mitigation_types.yml · mitigation_parry_knockback"
mitigation_parry_knockback:
  conditions:
    - 'variable_exists{var=target}' # 仅在目标存在时
  mechanics:
    - 'copy_vector{var=dir;val=target.location}'
    - 'sub_vector{var=dir;val=caster.location}'
    - 'set_y{var=dir;y=0}'
    - 'normalize_vector{var=dir}'
    - 'set_y{var=dir;y=0.35}'
    - 'set_velocity{vector=dir}'
```
