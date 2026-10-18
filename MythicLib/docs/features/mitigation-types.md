---
title: 伤害减免
source: https://docs.phoenixdevt.fr/mythiclib/features/mitigation-types
source_snapshot: '2026-10-19'
---

# 伤害减免 {#🛡️-damage-mitigation}

*伤害减免* 指的是玩家可以减少或避免攻击造成的伤害的各种方式。虽然MythicLib提供了多种built-in缓解类型（*Block*、*Dodge* 和 *Parry*），但你还可以创建自定义缓解类型以满足服务器的需求。

## Built-in缓解类型 {#built-in-mitigation-types}

### 阻塞 {#blocking}

当格挡近战或射弹攻击时，玩家会大幅减少受到的伤害。物品可以增加格挡几率和格挡威力（你格挡的伤害百分比）。格挡能力有默认值和上限，这意味着如果玩家没有物品给予他额外的格挡能力，他将至少格挡20%所受到的伤害。阻挡能力不能超过75%。阻止攻击的机会由 *阻止等级*属性决定。

```yml
STEEL_BREASTPLATE:
  material: IRON_CHESTPLATE
  block-power: 10
  block-rating: 5
```

### 闪避 {#dodging}

当躲避近战或射弹攻击时，玩家会完全**抵消**受到的伤害，并快速向后冲刺，让他逃离战斗。躲避攻击的几率上限为80%。

```yml
SWIFT_LEATHER_BOOTS:
  material: LEATHER_BOOTS
  dodge-rating: 10
```

### 招架 {#parrying}

就像躲避一样，格挡会完全否定攻击伤害并将攻击者击退。

可以在主MythicLib配置文件中编辑击退强制。

```yml
DWARVEN_SHIELD:
  material: SHIELD
  parry-rating: 10
```

### 缓解措施冷却时间减少 {#mitigation-cooldown-reduction}

每个缓解属性还具有冷却时间缓解属性。默认情况下，玩家每隔几秒无法闪避、招架或格挡一次以上攻击。这些冷却时间属性降低了延迟，如果玩家运行状况不佳，这可能非常有用。

```yml
ROGUE_AMULET:
  material: RED_DYE
  dodge-cooldown-reduction: 40
```

## 自定义缓解类型 {#custom-mitigation-types}

你可以通过向`MythicLib/mitigation_types.yml`文件添加新部分来创建自己的自定义缓解类型。每个部分应遵循与built-in缓解类型相同的结构。以下部分以*阻止*为例介绍可用于缓解类型的不同参数。

虽然你当然可以使用其他插件或脚本解决方案重新创建类似的“缓解类型”，但MythicLib旨在提供针对RPG服务器用例进行微调的easy-to-use框架。

## 一个例子 {#an-example}

```yml
block:

  # For backwards compatibility only.
  # If none of your plugins use the old MythicLib mitigation
  # events, you can safely remove/comment out this option.
  legacy: block

  # Formula for cooldown between two consecutive blocks (in seconds)
  # To disable cooldown, delete this line, or comment it out
  # Note that, by default, cooldown reduction is capped at 80% (see stats.yml)
  cooldown: '3 * (1 - <stat.block_cooldown_reduction> / 100)'

  # Chance to successfully block an attack
  # This formula should return a value between 0 and 1 (0 being 0% chance, 1 being 100% chance)
  # Note that, by default, block rating is capped at 80% (see stats.yml)
  roll: '<stat.block_rating> / 100'

  # Script/skill ran on damage
  on_damage: mitigation_on_block
```

### 冷却时间 {#cooldown}

选项`cooldown`指示此类缓解类型具有冷却时间。它发生的频率不能超过每 X 秒一次，其中 X 是公式返回的值。 *Blocking* 的默认公式是`3 * (1 - <stat.block_cooldown_reduction> / 100)`，这意味着基本冷却时间是3秒，但可以通过玩家的 *Block冷却时间Reduction*属性来减少。

### 卷 {#roll}

选项`roll`是一个返回成功执行缓解的机会的公式。该公式应返回0和1之间的值，其中0表示0%机会，1表示100%机会。在 *阻止* 的情况下，默认公式为`<stat.block_rating> / 100`，这意味着如果玩家具有25%*阻止评级*，则它们有25%机会阻止每个传入攻击。

### Pre-Damage脚本 {#pre-damage-script}

脚本`pre_damage`在缓解措施推出之前执行。它可用于设置任何必要的变量或缓解条件。对于 *Blocking*，默认情况下没有pre-damage脚本，但你可以根据需要使用以下语法添加一个脚本：

```yml
my_mitigation_type:
  pre_damage: my_custom_pre_damage_script
```

> **信息**
>
> 请注意，缓解类型使用的所有built-in脚本均位于`MythicLib/script/mitigation_types`配置文件中。你可以根据需要查看和编辑它们。

### On-Damage脚本 {#on-damage-script}

最后但并非最不重要的一点是，当缓解成功触发时，将执行脚本`on_damage`。该脚本仅在满足以下条件时执行：

- 缓解措施不在冷却时间上，
- 缓解滚动成功，
- 满足pre-damage脚本中的所有条件（如果有），
- `DamageMitigationEvent`Bukkit事件未被其他插件取消。

对于*阻止*，默认的on-damage脚本是`mitigation_on_block`，它根据玩家的*阻止功率*属性减少传入伤害的百分比。

```yml
mitigation_on_block:
  mechanics:

    # First, compute block coefficient and reduce damage
    - 'set_double{variable="block_coef";value="<stat.block_power>/100"}'
    - 'multiply_damage{amount="1 - <block_coef>"}'

    # Send message and play sound effect
    - 'set_double{variable="damaged_blocked";value="<attack.damage> * <block_coef>"}'
    - 'action_bar{m="&cYou blocked <damaged_blocked> damage!";target=caster;priority=31}'
    - 'play_sound{sound=ENTITY_ZOMBIE_ATTACK_IRON_DOOR;volume=1;pitch=2}'
    - 'set_double{variable=max_angle;value=120}'
    - 'script{name=mitigation_block_particle_effect}'

mitigation_block_particle_effect:
  # Sound and particle effect logic
  # [...]
```

---

原文：[🛡️ Damage Mitigation](https://docs.phoenixdevt.fr/mythiclib/features/mitigation-types) · 原文归档：2026-10-19
