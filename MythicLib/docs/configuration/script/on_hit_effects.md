---
title: script/on_hit_effects.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: script/on_hit_effects.yml
source_version: 1.7.1-SNAPSHOT
---

# script/on_hit_effects.yml

文件：`script/on_hit_effects.yml`。版本：`1.7.1-SNAPSHOT`。

随包脚本。

## `weapon_crit_script_check` { #weapon_crit_script_check }

```yaml title="script/on_hit_effects.yml · weapon_crit_script_check"
######################################
# 武器暴击
######################################

weapon_crit_script_check:
  conditions:
    # 武器伤害和徒手伤害均可暴击
    - 'has_damage_type{types="weapon,unarmed"}'
```

## `weapon_crit_script` { #weapon_crit_script }

```yaml title="script/on_hit_effects.yml · weapon_crit_script"
weapon_crit_script:
  mechanics:
    # 根据暴击伤害提高武器或徒手伤害
    - 'set_double{var=crit_coef;val="<stat.critical_strike_power> / 100"}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=WEAPON}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=UNARMED}'
    - 'mark_crit{dtype="WEAPON,UNARMED"}'
    - 'call_trigger{trigger=WEAPON_CRIT}'

    # 播放音效和粒子效果
    #取消注释可发送快捷栏消息
    #- 'action_bar{m="&6你造成了一次暴击，伤害为 &c<attack.damage>&6！";target=caster;priority=40;duration=30}'
    - "play_sound{sound=ENTITY_PLAYER_ATTACK_CRIT;volume=1;pitch=1}"
    - "particle{particle=CRIT;amount=32;offset_x=.5;offset_y=.5;offset_z=.5;speed=0.5;target_location={type=target;position=BODY}}"
```

## `skill_crit_script_check` { #skill_crit_script_check }

```yaml title="script/on_hit_effects.yml · skill_crit_script_check"
######################################
# 技能暴击
######################################

skill_crit_script_check:
  conditions:
    # 只有技能伤害可以暴击
    - 'has_damage_type{types="skill"}'
```

## `skill_crit_script` { #skill_crit_script }

```yaml title="script/on_hit_effects.yml · skill_crit_script"
skill_crit_script:
  mechanics:
    - 'multiply_damage{scalar="<stat.skill_critical_strike_power> / 100";dtype=SKILL}'
    - 'mark_crit{dtype=SKILL}'

    # 播放音效和粒子效果
    - "play_sound{sound=ENTITY_PLAYER_ATTACK_CRIT;volume=1;pitch=1}"
    - "particle{particle=TOTEM_OF_UNDYING;amount=32;offset_x=.5;offset_y=.5;offset_z=.5;speed=0.5;target_location={type=target;position=BODY}}"
```

## `lifesteal_and_spellsteal_script` { #lifesteal_and_spellsteal_script }

```yaml title="script/on_hit_effects.yml · lifesteal_and_spellsteal_script"
######################################
# 生命偷取与技能吸血
######################################

lifesteal_and_spellsteal_script:
  mechanics:
    - 'set_double{var=heal;val="<stat.lifesteal> / 100 * <attack.damage_weapon> + <stat.spell_vampirism> / 100 * <attack.damage_skill>"}'
    - 'script{s=lifesteal_and_spellsteal_script_heal}'
```

## `lifesteal_and_spellsteal_script_heal` { #lifesteal_and_spellsteal_script_heal }

```yaml title="script/on_hit_effects.yml · lifesteal_and_spellsteal_script_heal"
lifesteal_and_spellsteal_script_heal:
  conditions:
    - 'bool{expr=" <heal> > 0 "}' # 仅在治疗量为正数时
  mechanics:
    #- 'message{m="&a你恢复了 &2<heal> &a点生命值！";target=caster}'
    - 'heal{amount="<heal>";reason=MAGIC;target=caster}' # 治疗玩家
```
