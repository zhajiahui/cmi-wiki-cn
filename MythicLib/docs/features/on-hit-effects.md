---
title: 命中效果
source: https://docs.phoenixdevt.fr/mythiclib/features/on-hit-effects
source_snapshot: '2026-10-19'
---

# 命中效果 {#🗡️-on-hit-effects}

*On-Hit效果* 是当玩家对另一个实体（怪物或玩家）造成伤害时触发的特殊效果。

例如，*技能* 和 *武器暴击* 被视为on-hit效果。 *吸血*根据造成的伤害百分比来治疗攻击者，这是on-hit效果的另一个例子。 *Manasteal*，根据造成的伤害百分比为攻击者恢复魔力，也是on-hit效果。

大多数on-hit效果直接取决于数值玩家属性，例如*暴击几率*或*吸血百分比*。在本页中，我们将介绍MythicLib提供的built-inon-hit效果，以及如何创建自定义效果。

## 内置On-Hit效果器 {#builtin-on-hit-effects}

MythicLib内置了多种on-hit效果器，包括：

- *武器* & *技能暴击*
- *吸血*，*技能吸血鬼*

## 自定义On-Hit效果器 {#custom-on-hit-effects}

你可以通过向`MythicLib/on_hit_effects.yml`文件添加新部分来创建自己的自定义on-hit效果。每个部分应遵循与built-inon-hit效果相同的结构。下一节将介绍可用于on-hit效果的不同参数，以 *武器暴击* 为例。

虽然你当然可以使用其他插件或脚本解决方案重新创建类似的 *On-Hit效果*，但MythicLib旨在提供针对RPG服务器用例进行微调的easy-to-use框架。

## 一个例子 {#an-example}

所有on-hit效果均在`MythicLib/on_hit_effects.yml`文件中配置。每个on-hit效果在文件中都有自己的部分，你可以在其中自定义其行为和参数。让我们以 *武器暴击* 的built-in配置部分为例：

```yml
weapon_crits:

  pre_attack: skill_crit_script_check

  # Formula for cooldown between two consecutive weapon crits (in seconds)
  # To disable cooldown, delete this line, or comment it out
  cooldown: '3 * (1 - <stat.critical_strike_cooldown_reduction> / 100)'

  # Chance to successfully perform a weapon crit
  # This formula should return a value between 0 and 1 (0 being 0% chance, 1 being 100% chance)
  # Note that, by default, weapon crit strike is capped at 80% (see stats.yml)
  roll: '<stat.critical_strike_chance> / 100'

  # Script/skill ran on weapon crit
  on_attack: weapon_crit_script
```

### 冷却时间 {#cooldown}

选项`cooldown`表示此类on-hit效果具有冷却时间。它发生的频率不能超过每 X 秒一次，其中 X 是公式返回的值。 *武器暴击* 的默认公式是`3 * (1 - <stat.critical_strike_cooldown_reduction> / 100)`，这意味着基础冷却时间是3秒，但可以通过玩家的 *暴击冷却时间减少*属性。

这是一个可选参数。如果你希望禁用冷却时间以获得on-hit效果，只需删除`cooldown`行或将其注释掉即可。

### 卷 {#roll}

选项`roll`是一个公式，返回成功执行on-hit效果的机会。该公式应返回0和1之间的值，其中0表示0%机会，1表示100%机会。对于 *武器暴击*，默认公式为`<stat.critical_strike_chance> / 100`，这意味着如果玩家具有25%*暴击几率*，则它们有25%机会执行武器每次攻击时为暴击。

这是一个可选参数。如果你希望on-hit效果始终触发（不在冷却时间上时），只需将该值设置为`1`即可。

### Pre-Attack脚本 {#pre-attack-script}

在滚动on-hit效果之前执行脚本`pre_attack`。它可用于为on-hit效果设置任何必要的变量或条件。对于 *武器暴击*，默认脚本是`skill_crit_script_check`，这确保攻击包含 *武器* 或 *徒手* 伤害，因为武器暴击仅适用于这些伤害类型。

```yml
skill_crit_script_check:
  conditions:
    - 'has_damage_type{types="skill"}'
```

这是一个可选参数。如果你不需要任何pre-attack设置，则可以简单地省略`pre_attack`行。

> **信息**
>
> 请注意，on-hit效果使用的所有built-in脚本均位于`MythicLib/script/on_hit_effects`配置文件中。你可以根据需要查看和编辑它们。

### 攻击脚本 {#attack-script}

最后但并非最不重要的一点是，当on-hit效果成功触发时，将执行脚本`on_attack`。该脚本仅在满足以下条件时执行：

- on-hit效果不适用于冷却时间，
- 滚动检查成功，
- 满足`pre_attack`脚本中指定的任何条件，
- Bukkit事件`OnHitEffectEvent`不会被任何插件取消。

对于 *武器暴击*，默认脚本是`weapon_crit_script`，它将暴击伤害乘数应用于攻击。

```yml
weapon_crit_script:
  mechanics:
    # increase weapon/unarmed damage by crit power
    - 'set_double{var=crit_coef;val="<stat.critical_strike_power> / 100"}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=WEAPON}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=UNARMED}'

    # play sound and particle effect
    #Uncomment for an action bar message
    #- 'action_bar{m="&6You landed a crit for &c<attack.damage> &6damage!";target=caster;priority=40;duration=30}'
    - "play_sound{sound=ENTITY_PLAYER_ATTACK_CRIT;volume=1;pitch=1}"
    - "particle{particle=CRIT;amount=32;offset_x=.5;offset_y=.5;offset_z=.5;speed=0.5;target_location={type=target;position=BODY}}"
```

### 跳过事件 {#skip-event}

这是性能的可选参数。将`skip_event`设置为`true`，以在该on-hit效果触发时跳过触发`OnHitEffectEvent`Bukkit事件。这样，这个on-hit事件就无法被任何插件监听或取消。

---

原文：[🗡️ On-Hit Effects](https://docs.phoenixdevt.fr/mythiclib/features/on-hit-effects) · 原文归档：2026-10-19
