---
title: 变量
source: https://docs.phoenixdevt.fr/mythiclib/scripts/variables
source_snapshot: '2026-10-19'
---

# 变量 {#📚-variables}

当提供的机制没有提供足够的可配置性时，你始终可以使用变量来重新编码一些更复杂的脚本。例如，变量可用于存储临时数据，甚至可以为高级粒子效果进行复杂的数值或矢量计算。

## 内部和自定义变量 {#internal-custom-variables}

有两种类型的变量。首先，**内部变量**或**保留变量**具有由MythicLib保留的名称。它们始终由MythicLib使用，并且你无法使用保留的变量名称创建自定义变量。例如，你可以使用`<caster>`或`<target_location>`访问这些变量。

|变量|类型 |用途 |
| --- | --- | --- |
| `source` | position | 剧本拍摄地点 |
| `target_location` | position | 目标位置**如果存在** |
| `caster` | player | 玩家剧本是谁选的？ |
| `attack` | attackMetadata | 触发技能的攻击**如果存在** |
| `stat` | statMap | 施法者施放此脚本时的属性映射。 |
| `target` | entity | 技能目标**如果存在** |
| `random` | random | 用于生成随机数的额外模块。见下文 |

另一方面，**自定义变量**被初始化并且可以由用户操作。你可以使用`<your_variable_name>`访问它们，在数值公式中使用它们，或者就像在任何机制或条件下使用 PAPI占位符一样。MythicLib附带许多机制，可让你初始化和编辑自定义变量。完整列表可在[此处](mechanics/intro.md)。

## 范围 {#scopes}

自定义变量具有**范围**。此功能非常重要，因为它确定变量是否特定于玩家、是否可以由任何玩家访问以及在脚本最终运行其最后一个机制时是否应该保存它。

内部变量不需要作用域。

共有三个可用变量范围：

- `SERVER`（服务器变量对于所有玩家和所有脚本都是相同的）
- `PLAYER`（玩家变量对于特定玩家运行的所有脚本都是相同的）
- `SKILL`（默认范围。当脚本运行最后一个机制时，技能/script 变量将丢失）。

你只需在编辑或初始化变量时提供变量的范围。使用`<var.custom_var_name>`获取自定义变量的值时，可能有多个具有相同名称但作用域不同的变量（每个作用域最多一个）。在这种情况下，优先级为`SKILL`>`PLAYER`>`SERVER`（范围最低的优先）。

## 类型 {#types}

输入变量：`<source>`是一个位置（运行脚本的位置），而`<target>`是一个实体（技能目标，如果存在）。变量也有**子变量**：例如，你可以使用`<entity_variable.location>`访问实体的位置，这具有将实体变量转换为位置变量的效果。

子变量也是一个变量，这意味着你可以使用多个点来访问子变量的子变量等以获得所需的数据：`<caster.location.world.name>`

这是当前支持的所有变量类型及其子变量的列表

## 变量类型 {#variable-types}

### 攻击元数据 {#attackmetadata}

| Subvariable | Type | 描述 |
| --- | --- | --- |
| `damage` | double | 造成的伤害量 |
| `damage_<type>` | double | 给定伤害类型造成的伤害量 |

### 属性图 {#attributemap}

如果你想访问某些玩家的普通基础属性值，这非常有用。使用示例：`<caster.attribute.max_health>`。

原版基础属性不得误认为是 MMO 插件添加的玩家属性。其中一些属性基于原版基础属性，但不是全部。例如，武器暴击几率是自定义的属性，它不基于任何原版基础属性，因此你无法使用此变量类型访问它。你需要使用`statMap`变量类型：`<caster.stat.critical_strike_chance>`。然而，由于攻击伤害基于原版基础属性，`<caster.stat.attack_damage>`将不会返回正确的值，因为它只考虑在MythicLib中注册的属性修正器而不是外部基础属性修饰符！

| Subvariable | Type | 描述 |
| --- | --- | --- |
| `max_health` | double | 玩家基础属性值 |
| `follow_range` | double | 玩家基础属性值 |
| `knockback_resistance` | double | 玩家基础属性值 |
| `movement_speed` | double | 玩家基础属性值 |
| `flying_speed` | double | 玩家基础属性值 |
| `attack_damage` | double | 玩家基础属性值 |
| `attack_knockback` | double | 玩家基础属性值 |
| `attack_speed` | double | 玩家基础属性值 |
| `armor` | double | 玩家基础属性值 |
| `armor_toughness` | double | 玩家基础属性值 |
| `luck` | double | 玩家基础属性值 |
| `armor_toughness` | double | 玩家基础属性值 |

### 冷却图 {#cooldownmap}

冷却时间映射用于存储玩家的冷却时间值。冷却时间由MythicLib用于伤害减免（格挡、格挡、闪避）和技能冷却时间，由MMOItems用于物品冷却时间。你可以使用`<caster.cooldown>`访问玩家投射脚本的冷却时间映射。

使用子变量`some_key`将返回与给定冷却时间密钥的剩余冷却时间相对应的双精度值。例如，`<caster.cooldown.mmoitem_small_mana_pot>`返回ID`SMALL_MANA_POT`的 MMOItem 的剩余冷却时间，`<caster.cooldown.hello>`返回技能/物品/ 等的剩余冷却时间。与冷却时间钥匙`hello`。

下表列出了MMOCore和MMOItems使用的所有密钥。你几乎可以在脚本或插件中使用任何冷却时间密钥，如果你愿意，你还可以混乱/干扰MMOItems和MMOCore内部使用的冷却时间密钥。

> **信息**
>
> 你还可以使用`%mythiclib_cooldown_<cooldown_key>%`从PlaceholderAPI中使用占位符检索玩家的当前冷却时间。示例：`%mythiclib_cooldown_skill_fireball%`

| Subvariable | Type | 描述 |
| --- | --- | --- |
| `mmoitem_<lower_case_item_id>` | double | 剩余物品冷却时间或0 |
| `<cooldown_reference>` | double | 如果 MMOItem 有冷却时间引用，请使用它而不是上面的引用。 |
| `skill_<lower_case_skill_id>` | double | 剩余技能冷却时间或0 |
| `dodge` | double | 剩余躲避冷却时间或0 |
| `parry` | double | 剩余招架冷却时间或0 |
| `block` | double | 剩余闪避冷却时间或0 |
| `weapon_crit` | double | 剩余武器暴击冷却时间或0 |
| `skill_crit` | double | 剩余技能暴击冷却时间或0 |

### 双人间 {#double}

数值。

| Subvariable | Type | 描述 |
| --- | --- | --- |
| `int` | integer | 该数字的整个部分 |
| `round.xxx` | string | 将双精度舍入到小数点后 N 位 |

### 实体 {#entity}

**不是玩家** 的任何实体。玩家与实体变量类型共享许多子变量，但有一些额外的属性。

| Subvariable | Type | 描述 |
| --- | --- | --- |
| `id` | integer | 实体 ID |
| `uuid` | string | 实体UUID |
| `type` | string | 实体类型（ZOMBIE、GHAST 等[完整列表](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html)） |
| `location` | position | 实体当前位置 |
| `bb_center` | position | 给定边界框的该实体的中心位置 |
| `eye_location` | position | 实体眼睛的位置 |
| `health` | double | 当前实体生命条 |
| `looking` | position | 指向实体正在寻找的位置的向量 |
| `velocity` | position | 瞬时实体速度 |
| `height` | double | 实体高度 |
| `attribute` | attributeMap | 实体基础属性图 |
| `fire_ticks` | int | 实体着火的时间间隔（如果没有着火，则为0） |

### 整数 {#integer}

一个整数。没有子变量！

### 玩家 {#player}

玩家实体。玩家与`Entity`变量类型共享许多子变量，但有一些额外的属性。

| Subvariable | Type | 描述 |
| --- | --- | --- |
| - | - | 任何来自`Entity`变量类型的 |
| `stat` | statMap | 玩家的属性图 |
| `cooldown` | cooldownMap | 玩家的冷却时间图 |
| `name` | string | 玩家名称 |

### 职位 {#position}

位置/位置/向量都是*几乎*同义词。位置由世界 + 三个坐标（X、Y 和 Z）定义。位置既用于描述玩家位置（在这种情况下，你使用的是`world`子变量），也用于进行向量计算（因此`world`子变量无用）。

| Subvariable | Type | 描述 |
| --- | --- | --- |
| `world` | world | 定位世界 |
| `x` | double | X坐标 |
| `y` | double | Y坐标 |
| `z` | double | Z坐标 |
| `length` | double | 向量长度计算 |
| `biome` | string | 生物群落名称 |
| `altitude` | double | 计算位置高度 |

### 统计图 {#statmap}

属性映射用于存储来自特定玩家的所有属性修正器。你可以使用`<caster.stat>`访问脚本运行程序的属性映射。然后使用`<caster.stat.skill_critical_strike_chance>`检索属性值。

原版基础属性不得误认为是 MMO 插件添加的玩家属性。其中一些属性基于原版基础属性，但不是全部。例如，武器暴击几率是自定义的属性，它不基于任何原版基础属性，因此你无法使用此变量类型访问它。你需要使用`StatMap`变量类型：`<caster.stat.critical_strike_chance>`。然而，由于攻击伤害基于原版基础属性，`<caster.stat.attack_damage>`将不会返回正确的值，因为它只考虑在MythicLib中注册的属性修正器而不是外部基础属性修饰符！

### 字符串 {#string}

| Subvariable | Type | 描述 |
| --- | --- | --- |
| `uppercase` | string | 相同的大写字符串 |
| `lowercase` | double | 小写的相同字符串 |

### 随机 {#random}

| Subvariable | Type | 描述 |
| --- | --- | --- |
| `uniform` | double | 0和1之间统一采样的十进制数 |
| `int` | int | 随机整数 |
| `bool` | boolean | 随机布尔值（true或false），统一 |
| `gaussian` | double | 从标准高斯分布中采样的十进制数 |

### 世界 {#world}

| Subvariable | Type | 描述 |
| --- | --- | --- |
| `time` | int | 世界当前时间 |
| `name` | string | 世界名称 |

---

原文：[📚 Variables](https://docs.phoenixdevt.fr/mythiclib/scripts/variables) · 原文归档：2026-10-19
