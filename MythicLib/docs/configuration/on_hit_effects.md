---
title: on_hit_effects.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: on_hit_effects.yml
source_version: 1.7.1-SNAPSHOT
---

# on_hit_effects.yml

文件：`on_hit_effects.yml`。版本：`1.7.1-SNAPSHOT`。

随包配置。

## `lifesteal_and_spellsteal` { #lifesteal_and_spellsteal }

```yaml title="on_hit_effects.yml · lifesteal_and_spellsteal"
######################################
# 生命偷取与法术吸血
#
# 按造成伤害的一定比例治疗攻击者。
# 生命偷取在造成武器伤害时触发，法术吸血
# 在造成技能伤害时触发。
######################################

lifesteal_and_spellsteal:
  skip_event: true # 用于性能优化
  # 无冷却，不进行概率判定
  on_attack: 'mythiclib:lifesteal_and_spellsteal_script'
```

## `weapon_crits` { #weapon_crits }

```yaml title="on_hit_effects.yml · weapon_crits"
######################################
# 武器暴击
######################################

weapon_crits:

  pre_attack: 'mythiclib:weapon_crit_script_check'

  # 两次连续武器暴击之间的冷却时间公式(单位：秒)
  # 删除此行或将其注释掉可禁用冷却
  cooldown: '3 * (1 - <stat.critical_strike_cooldown_reduction> / 100)'

  # 成功触发武器暴击的概率
  # 此公式应返回 0 到 1 之间的数值(0 表示 0% 概率，1 表示 100% 概率)
  # 注意：默认情况下，武器暴击几率上限为 80%(见 stats.yml)
  roll: '<stat.critical_strike_chance> / 100'

  # 武器暴击时执行的技能
  on_attack: 'mythiclib:weapon_crit_script'
```

## `skill_crits` { #skill_crits }

```yaml title="on_hit_effects.yml · skill_crits"
######################################
# 技能暴击
######################################

skill_crits:

  pre_attack: 'mythiclib:skill_crit_script_check'

  # 两次连续技能暴击之间的冷却时间公式(单位：秒)
  # 删除此行或将其注释掉可禁用冷却
  cooldown: '3 * (1 - <stat.skill_critical_strike_cooldown_reduction> / 100)'

  # 成功触发技能暴击的概率
  # 此公式应返回 0 到 1 之间的数值(0 表示 0% 概率，1 表示 100% 概率)
  # 注意：默认情况下，技能暴击几率上限为 80%(见 stats.yml)
  roll: '<stat.skill_critical_strike_chance> / 100'

  # 技能暴击时执行的技能
  on_attack: 'mythiclib:skill_crit_script'
```
