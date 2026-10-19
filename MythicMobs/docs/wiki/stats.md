---
title: 属性
source_url: https://wiki.mythiccraft.io/mythicmobs/Stats
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 属性

# 介绍 {#introduction}

属性是影响玩家、生物、物品、技能等各种机制的数值。属性系统一开始可能不太容易掌握，但它支持多种用法，可用于调整战斗机制、实现技术性功能，以及设计新的游戏玩法元素。

属性在 `stats.yml` 文件中定义。该文件可放在 MythicMobs 根目录（`/plugins/MythicMobs/`）或[包](packs.md)文件夹中。

> **警告：要在物品上使用属性，必须安装 [Crucible](https://wiki.mythiccraft.io/mythiccrucible/home)**

- [自定义属性选项](stats.md#custom-stat-options)
  - [自定义属性类型](stats.md#custom-stat-types)
  - [具体类型选项](stats.md#specific-type-options)
  - [工具提示格式](stats.md#tooltips-formatting)
- [修正项](stats.md#modifiers)
- [内置属性](stats.md#built-in-stats)
- [配置实现](stats.md#implementations-with-configurations)
  - [生物](stats.md#mobs)
  - [物品](stats.md#items)
- [示例](https://wiki.mythiccraft.io/mythicmobs/Stats#Examples)
  - [自定义属性示例](stats.md#example-custom-stats)

# 自定义属性选项 {#custom-stat-options}

可用于属性的选项，用于进一步自定义属性

| 选项 | 说明 |
| --- | --- |
| Enabled | 此属性当前是否启用。 |
| AlwaysActive | 是否将此属性强制应用到每个实体的每个注册表中。 |
| Type | 属性的[类型](stats.md#custom-stat-types)。 |
| Display | 属性显示时使用的名称。 |
| Formatting | 属性在物品上的显示方式，取决于所用的 Modifier。 |
| ShowInLore | 是否显示各修饰符的提示框格式。 |
| Priority | 相对于其他属性，此属性生效的优先级。值*越小*，越会*先于*值较大的属性触发。 |
| MinValue | 属性的最小值。 |
| MaxValue | 属性的最大值。 |
| Triggers | 触发属性效果的触发器。可使用任意 MythicMobs 触发器，但要去掉“on”部分，例如使用 `onAttack` 时，触发器应写为 `ATTACK`。截至 v.5.4.0，仅支持造成伤害的触发器；扩展功能请关注开发版。 |
| ParentStats | 此属性依赖的其他属性列表。 |
| TriggerStats | 触发实体可能具有的属性及其 FormulaKey 列表，两者用空格分隔。随后可在其他公式中使用 FormulaKey，获取触发实体上的对应属性值。[示例见此处](https://wiki.mythiccraft.io/mythicmobs/Stats#ice_damage)。 |
| Formula | 此属性具有父属性时，用于计算基础值的公式。 |
| FormulaKey | 当此属性是其他属性的父属性时，可在公式中使用的键。 |
| BaseValue | 没有父属性时使用的固定基础值。 |
| ExecutionPoint | 对于修改触发器的属性，可设为 `PRE` 或 `POST`，决定在所有机制执行之前还是之后计算此属性。 |
| Skills | 属性激活时执行的技能。 |

## 自定义属性类型 {#custom-stat-types}

`Type` 选项可设置的值

| 类型 | 说明 |
| --- | --- |
| `STATIC` | 一个固定值，本身不产生效果，但可通过占位符引用。 |
| `DAMAGE_BONUS` | 此属性增加固定数值的额外伤害。 |
| `DAMAGE_MODIFIER` | 使用公式修改伤害。 |
| `PROC` | 执行技能的概率。 |

## 特定类型选项 {#specific-type-options}

仅在属性使用指定类型时可用的选项列表

### DAMAGE_MODIFIER {#damage-modifier}

| 选项 | 说明 |
| --- | --- |
| DamageType | 指定自定义伤害类型。使用 `ALL` 可修改技能的最终总伤害。 |
| Conditions | 指定能够影响 Modifier 的条件。 |
| DamageFormula | 定义伤害修改公式，示例见[此处](https://wiki.mythiccraft.io/mythicmobs/Stats#fire_resistance)。伤害公式还可以使用以下键：- `d` 表示原始伤害值 - `v` 表示此属性的值。 |

### DAMAGE_BONUS {#damage-bonus}

| 选项 | 说明 |
| --- | --- |
| DamageType | 指定自定义伤害类型。 |

## 提示信息格式 {#tooltips-formatting}

| 格式 | 说明 |
| --- | --- |
| Additive | 加法修饰符显示的提示文本。 |
| Multiply | 乘法修饰符显示的提示文本。 |
| Compound | 复合修饰符显示的提示文本。 |
| Setter | 设值修饰符显示的提示文本。 |
| Rounding | 属性数值保留的小数位数。 |
| ShowInItemLore | 使用 `{stats-each}` 时，是否在物品描述中显示提示文本。默认为 true；若设置了 ShowInLore 选项，则以其为准。 |

| ShowInLore | 说明 |
| --- | --- |
| Additive | 是否在物品描述中显示 Additive 修饰符的提示文本。 |
| Multiply | 是否在物品描述中显示 Multiply 修饰符的提示文本。 |
| Compound | 是否在物品描述中显示 Compound 修饰符的提示文本。 |
| Setter | 是否在物品描述中显示 Setter 修饰符的提示文本。 |

```yml
EXAMPLE_STAT:
  Enabled: true
  AlwaysActive: false
  Type: STATIC
  FormulaKey: 'SPD'
  Formatting:
    Additive: '+<value> Speed'
    Multiply: '+<value>% Speed'
    Compound: 'x<value>% Speed'
    Static: 'Force <value> <display>'
    Rounding: 2
  ShowInLore:
    Compound: false # optional
```

# 修正器 {#modifiers}

定义属性基础值后，可以使用修正项调整属性。

| 修正器 | 说明 |
| --- | --- |
| `ADDITIVE` | 为属性的基础值增加数值。 |
| `ADDITIVE_MULTIPLIER` | 为属性的基础值增加倍率。 |
| `COMPOUND_MULTIPLIER` | 将属性基础值乘以指定值，再将结果加到基础值上。 |
| `SETTER` | 覆盖所有修饰符和基础值，强制将属性设为所定义的值。 |

生物、玩家、物品、附魔和光环均可施加属性修正，也可受到属性修正影响。例如，物品可以增加或倍增持有者的攻击速度；一次攻击也可以临时施加 COMPOUND MULTIPLIER，将目标的攻击速度减半。

##  {#section}

#### `ADDITIVE` {#additive}

`ADDITIVE` 修正项很直观：直接加到基础属性值上。

#### `ADDITIVE_MULTIPLIER` {#additive-multiplier}

`ADDITIVE_MULTIPLIER` 将基础属性值乘以指定值。

#### `COMPOUND_MULTIPLIER` {#compound-multiplier}

最后，`COMPOUND_MULTIPLIER` 会再乘算所有 ADDITIVE 计算的结果。它适合用于减益等效果，因为这类修正通常应在属性加值和加算倍率之后计算。

##  {#section-2}

## 属性计算 {#stat-calculation}

`ADDITIVE_MULTIPLIER` 和 `COMPOUND_MULTIPLIER` 容易混淆，下面的示例可以帮助理解：

假设有以下修正项：

```rb
 8 base value
 10 additive
 2 additive
 5 multiply
 3 multiply
 2 compound   (effectively x2)
 0.4 compound (effectively -60%)
```

……MythicMobs 会按以下方式计算：

```rb
(8 + 10 + 2) * (5 + 3) * (2 * 0.4) = 128

(base + additive + additive) * (additive_multiplier + additive_multiplier) * (compound_multiplier * compound_multiplier) = final stat
```

普通倍率之间相加，复合倍率之间相乘。可以将加算倍率理解为 "+10%"，将复合倍率理解为 "x10%"。

# 内置属性 {#built-in-stats}

这些属性由 MythicMobs 内置支持，可在插件根目录（`/plugins/MythicMobs/`）或包目录（`/plugins/MythicMobs/Packs/CoolPack/`）中的 `stats.yml` 文件内配置。玩家继承这些属性的 `BaseValue`；生物也将其作为默认值，除非在自身配置的 `Stats:` 小节中另行覆盖。

| 属性 | 说明 |
| --- | --- |
| [ATTACK_DAMAGE](https://wiki.mythiccraft.io/mythicmobs/Stats#attack_damage) | 基础伤害输出。 |
| [ATTACK_SPEED](https://wiki.mythiccraft.io/mythicmobs/Stats#attack_speed) | 攻击冷却频率，通常仅用于玩家。 |
| [BONUS_DAMAGE](https://wiki.mythiccraft.io/mythicmobs/Stats#bonus_damage) | 用于造成额外伤害的附加修饰符。 |
| [CRITICAL_STRIKE_CHANCE](https://wiki.mythiccraft.io/mythicmobs/Stats#critical_strike_chance) | 触发暴击的概率，即基于概率的暴击。 |
| [CRITICAL_STRIKE_DAMAGE](https://wiki.mythiccraft.io/mythicmobs/Stats#critical_strike_damage) | 暴击造成的伤害。 |
| [CRITICAL_STRIKE_RESILIENCE](https://wiki.mythiccraft.io/mythicmobs/Stats#critical_strike_resilience) | 暴击抗性。 |
| [DAMAGE_REDUCTION](https://wiki.mythiccraft.io/mythicmobs/Stats#damage_reduction) | 通用伤害减免。 |
| [DEFENSE](stats.md#defense) | 防御 |
| [DODGE_CHANCE](https://wiki.mythiccraft.io/mythicmobs/Stats#dodge_chance) | 尝试造成伤害时攻击失败的概率，会被对手的 [DODGE_NEGATION](https://wiki.mythiccraft.io/mythicmobs/Stats#dodge_negation) 降低。 |
| [DODGE_NEGATION](https://wiki.mythiccraft.io/mythicmobs/Stats#dodge_negation) | 降低对手的 [DODGE_CHANCE](https://wiki.mythiccraft.io/mythicmobs/Stats#dodge_chance)。 |
| [HEALTH](stats.md#health) | 生命值。 |
| [HEALTH_REGENERATION](https://wiki.mythiccraft.io/mythicmobs/Stats#health_regeneration) | 生命恢复速率。 |
| [LIFESTEAL_CHANCE](https://wiki.mythiccraft.io/mythicmobs/Stats#lifesteal_chance) | 造成伤害时治疗攻击者的概率。 |
| [LIFESTEAL_POWER](https://wiki.mythiccraft.io/mythicmobs/Stats#lifesteal_power) | LifeSteal 的治疗量。 |
| [MOVEMENT_SPEED](https://wiki.mythiccraft.io/mythicmobs/Stats#movement_speed) | 移动速度。 |
| [PARRY_CHANCE](https://wiki.mythiccraft.io/mythicmobs/Stats#parry_chance) | 减免并反弹来自正面近战攻击伤害的概率，会被对手的 [PARRY_NEGATION](https://wiki.mythiccraft.io/mythicmobs/Stats#parry_negation) 降低。 |
| [PARRY_COUNTERATTACK](https://wiki.mythiccraft.io/mythicmobs/Stats#parry_counterattack) | 招架时返还给对手的伤害量。 |
| [PARRY_POWER](https://wiki.mythiccraft.io/mythicmobs/Stats#parry_power) | 招架减免的伤害量。 |
| [PARRY_NEGATION](https://wiki.mythiccraft.io/mythicmobs/Stats#parry_negation) | 降低对手的 [PARRY_CHANCE](https://wiki.mythiccraft.io/mythicmobs/Stats#parry_chance)。 |
| [SCALE](stats.md#scale) | 实体的缩放比例。 |
| STEP_HEIGHT | 跨步高度属性。 |
| ARMOR | 护甲属性。 |
| ARMOR_TOUGHNESS | 护甲韧性属性。 |
| BURNING_TIME | 燃烧时间属性。 |
| EXPLOSION_KNOCKBACK_RESISTANCE | 爆炸击退抗性属性。 |
| FALL_DAMAGE_MULTIPLIER | 摔落伤害倍率属性。 |
| GRAVITY | 重力属性。 |
| JUMP_STRENGTH | 跳跃力度属性。 |
| KNOCKBACK_RESISTANCE | 击退抗性属性。 |
| MOVEMENT_EFFICIENCY | 移动效率属性。 |
| OXYGEN_BONUS | 氧气加成属性。 |
| SAFE_FALL_DISTANCE | 安全摔落距离属性。 |
| SNEAKING_SPEED | 潜行速度属性。 |
| WATER_MOVEMENT_EFFICIENCY | 水中移动效率属性。 |
| BLOCK_BREAK_SPEED | 方块破坏速度属性。 |
| BLOCK_INTERACTION_RANGE | 方块交互范围属性。 |
| ENTITY_INTERACTION_RANGE | 实体交互范围属性。 |
| FLYING_SPEED | 实体的飞行速度。 |
| FOLLOW_RANGE | 实体的跟随范围。 |
| LOOT_BIAS | 提高掉落表中稀有物品获取机会的额外幸运值。 |

# 内置属性详解 {#built-in-stats-breakdown}

以下详细介绍 MythicMobs 提供的内置属性。自定义属性请参阅[自定义属性示例](stats.md#example-custom-stats)。

#### `DODGE_NEGATION` {#dodge-negation}

攻击命中并造成伤害的概率，会降低对手的 [DODGE_CHANCE](https://wiki.mythiccraft.io/mythicmobs/Stats#dodge_chance)。如下所示，可以自定义属性的显示名称和描述文本，例如用 'Accuracy' 替代 'Dodge Negation'

```yml
DODGE_NEGATION:
  Enabled: false
  AlwaysActive: false
  Display: 'Accuracy'
  Formatting:
    Additive: '+<value> Accuracy'
    Multiply: '+<value> Accuracy'
    Compound: 'x<value> Accuracy'
  BaseValue: 0
```

##  {#section-3}

#### `ATTACK_DAMAGE` {#attack-damage}

基础伤害输出

```yml
ATTACK_DAMAGE:
  Enabled: true
  AlwaysActive: false
  Display: 'Damage'
  Formatting:
    Additive: '+<value> Damage'
    Multiply: '+<value> Damage'
    Compound: 'x<value> Damage'
  BaseValue: 1
```

##  {#section-4}

#### `ATTACK_SPEED` {#attack-speed}

攻击冷却频率。通常仅用于玩家。

```yml
ATTACK_SPEED:
  Enabled: true
  AlwaysActive: false
  Display: 'Attack Speed'
  Formatting:
    Additive: '+<value> Attack Speed'
    Multiply: '+<value> Attack Speed'
    Compound: 'x<value> Attack Speed'
  BaseValue: 4.0
```

##  {#section-5}

#### `BONUS_DAMAGE` {#bonus-damage}

用于造成额外伤害的附加修饰符

```yml
BONUS_DAMAGE:
  Enabled: false
  AlwaysActive: false
  Display: 'Bonus Damage'
  Formatting:
    Additive: '+<value> Bonus Damage'
    Multiply: '+<value> Bonus Damage'
    Compound: 'x<value> Bonus Damage'
  BaseValue: 0
```

##  {#section-6}

#### `CRITICAL_STRIKE_CHANCE` {#critical-strike-chance}

触发暴击的概率（基于概率的暴击）

```yml
CRITICAL_STRIKE_CHANCE:
  Enabled: false
  AlwaysActive: false
  Display: 'Critical Strike'
  Formatting:
    Additive: '+<value> Critical Strike'
    Multiply: '+<value> Critical Strike'
    Compound: 'x<value> Critical Strike'
  BaseValue: 0
  MinValue: 0
  Skills:
  - particles{p=crit;a=50;hS=1;y=1;s=1} @trigger
```

##  {#section-7}

#### `CRITICAL_STRIKE_DAMAGE` {#critical-strike-damage}

通过暴击造成的伤害

```yml
CRITICAL_STRIKE_DAMAGE:
  Enabled: false
  AlwaysActive: true
  Display: 'Critical Damage'
  Formatting:
    Additive: '+<value> Critical Damage'
    Multiply: '+<value> Critical Damage'
    Compound: 'x<value> Critical Damage'
  BaseValue: 1
```

##  {#section-8}

#### `CRITICAL_STRIKE_RESILIENCE` {#critical-strike-resilience}

抵抗暴击

```yml
CRITICAL_STRIKE_RESILIENCE:
  Enabled: false
  Display: 'Resilience'
  AlwaysActive: false
  Formatting:
    Additive: '+<value> Resilience'
    Multiply: '+<value> Resilience'
    Compound: 'x<value> Resilience'
  BaseValue: 0
```

##  {#section-9}

#### `DAMAGE_REDUCTION` {#damage-reduction}

通用伤害减免

```yml
DAMAGE_REDUCTION:
  Enabled: false
  AlwaysActive: false
  Display: 'Damage Reduction'
  Formatting:
    Additive: '+<value> Damage Reduction'
    Multiply: '+<value> Damage Reduction'
    Compound: 'x<value> Damage Reduction'
  BaseValue: 0
```

##  {#section-10}

#### `DEFENSE` {#defense}

防御

```yml
DEFENSE:
  Enabled: false
  AlwaysActive: false
  Display: 'Defense'
  Formatting:
    Additive: '+<value> Defense'
    Multiply: '+<value> Defense'
    Compound: 'x<value> Defense'
  BaseValue: 0
```

##  {#section-11}

#### `DODGE_CHANCE` {#dodge-chance}

攻击未能造成伤害的概率，会降低对手的 [ACCURACY](https://wiki.mythiccraft.io/mythicmobs/Stats#accuracy)。

```yml
DODGE_CHANCE:
  Enabled: false
  AlwaysActive: false
  Display: 'Dodge'
  Formatting:
    Additive: '+<value> Dodge Chance'
    Multiply: '+<value> Dodge Chance'
    Compound: 'x<value> Dodge Chance'
  BaseValue: 0
  Skills: []
```

##  {#section-12}

#### `HEALTH` {#health}

生命值

```yml
HEALTH:
  Enabled: false
  AlwaysActive: true
  Display: 'Health'
  Formatting:
    Additive: '+<value> Health'
    Multiply: '+<value> Health'
    Compound: 'x<value> Health'
  BaseValue: 20
  MinValue: 1
```

##  {#section-13}

#### `HEALTH_REGENERATION` {#health-regeneration}

生命恢复率

```yml
HEALTH_REGENERATION:
  Enabled: false
  AlwaysActive: false
  Display: 'Health Regeneration'
  Formatting:
    Additive: '+<value> Regeneration'
    Multiply: '+<value> Regeneration'
    Compound: 'x<value> Regeneration'
  BaseValue: 0
  MaxValue: 1000000
  MinValue: 0
  Frequency: 60
```

##  {#section-14}

#### `LIFESTEAL_CHANCE` {#lifesteal-chance}

造成的伤害转化为攻击者治疗量的概率

```yml
LIFESTEAL_CHANCE:
  Enabled: false
  AlwaysActive: false
  Display: 'Lifesteal Chance'
  Formatting:
    Additive: '+<value> Lifesteal Chance'
    Multiply: '+<value> Lifesteal Chance'
    Compound: 'x<value> Lifesteal Chance'
  BaseValue: 0
```

##  {#section-15}

#### `LIFESTEAL_POWER` {#lifesteal-power}

生命偷取提供的治疗量。

```yml
LIFESTEAL_POWER:
  Enabled: true
  AlwaysActive: false
  Display: 'Lifesteal Power'
  Formatting:
    Additive: '+<value> Lifesteal Power'
    Multiply: '+<value> Lifesteal Power'
    Compound: 'x<value> Lifesteal Power'
  BaseValue: 0.1
```

##  {#section-16}

#### `MOVEMENT_SPEED` {#movement-speed}

移动速度。

```yml
MOVEMENT_SPEED:
  Enabled: false
  AlwaysActive: true
  Display: 'Movement Speed'
  Formatting:
    Additive: '+<value> Movement Speed'
    Multiply: '+<value>% Movement Speed'
    Compound: 'x<value>% Movement Speed'
  ParentStats:
  - SPEED
  Formula: '0.2 + (0.2 / (1 + e^(-0.005 * (SPD - 1000))))'
```

##  {#section-17}

#### `PARRY_CHANCE` {#parry-chance}

减免并反弹来自正面近战攻击的伤害的概率。

```yml
PARRY_CHANCE:
  Enabled: false
  AlwaysActive: false
  Display: 'Parry Chance'
  BaseValue: 0
  Priority: 0
  Formatting:
    Additive: '+<value> Parry Chance'
    Multiply: '+<value> Parry Chance'
    Compound: 'x<value> Parry Chance'
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

##  {#section-18}

#### `PARRY_COUNTERATTACK` {#parry-counterattack}

招架时返还给对手的伤害量。

```yml
PARRY_COUNTERATTACK:
  Enabled: false
  AlwaysActive: false
  Display: 'Parry Counterattack'
  BaseValue: 1
  Formatting:
    Additive: '+<value> Parry Counterattack'
    Multiply: '+<value> Parry Counterattack'
    Compound: 'x<value> Parry Counterattack'
```

##  {#section-19}

#### `PARRY_NEGATION` {#parry-negation}

影响并降低对手的 [PARRY_CHANCE](https://wiki.mythiccraft.io/mythicmobs/Stats#parry_chance)。如下所示，可以自定义属性的显示名称和描述文本，例如用 'Expertise' 替代 'Parry Negation'

```yml
PARRY_NEGATION:
  Enabled: false
  AlwaysActive: false
  Display: 'Expertise'
  Formatting:
    Additive: '+<value> Expertise'
    Multiply: '+<value> Expertise'
    Compound: 'x<value> Expertise'
  BaseValue: 0
```

##  {#section-20}

#### `PARRY_POWER` {#parry-power}

招架减免的伤害量。

```yml
PARRY_POWER:
  Enabled: false
  AlwaysActive: false
  Display: 'Parry Power'
  BaseValue: 0.5
  Formatting:
    Additive: '+<value> Parry Power'
    Multiply: '+<value> Parry Power'
    Compound: 'x<value> Parry Power'
```

##  {#section-21}

#### `SCALE` {#scale}

实体的缩放比例

```yml
SCALE:
  Enabled: false
  AlwaysActive: false
  Display: 'Scale'
  BaseValue: 1
  Formatting:
    Additive: '+<value> Scale'
    Multiply: '+<value> Scale'
    Compound: 'x<value> Scale'
```

##  {#section-22}

#### `LOOT_BIAS` {#loot-bias}

从 Mythic 掉落表获得稀有物品的额外幸运值。**仅对带权重的物品有效！**

- 默认值：0 - 稀有物品保持正常掉落概率
- -100：只会掉落加权列表中最常见的物品
- 100：稀有物品的掉落概率变为正常的两倍
- 1000：稀有物品的掉落概率变为正常的 10 倍

```yml
LOOT_BIAS:
  Enabled: true
  Type: STATIC
  Display: 'Loot Bias'
  BaseValue: 0
  MinValue: -100
  Formatting:
    Rounding: 1
    Additive: '+<value> Loot Bias'
    Multiply: '+<value> Loot Bias'
    Compound: 'x<value> Loot Bias'
```

##  {#section-23}

# 配置实现示例 {#implementations-with-configurations}

请注意，玩家的所有基础属性值均来自 `stats.yml` 文件，而生物只有部分基础值来自 `stats.yml`。如果生物自身配置中为某项属性指定了其他值，则采用该值。

## 生物 {#mobs}

此示例中的 `Some_Mob` 配置了三项属性：`Stats:` 部分的 `CRITICAL_STRIKE_CHANCE`，以及 `Health` 和 `Damage`。生命值和伤害属性由生物配置的常规写法直接处理。此外，该生物还配置了 `ATTACK_DAMAGE`、`ATTACK_SPEED` 和 `MOVEMENT_SPEED`。

```yml
Some_Mob:
  Health: 50
  Damage: 10
  Stats:
  - CRITICAL_STRIKE_CHANCE 0.2
```

## 物品 {#items}

```yaml
ExampleItem:
  Id: BLAZE_ROD
  Display: 'Test'
  Stats:
  - CRITICAL_STRIKE_CHANCE 0.5 ADDITIVE
  - CRITICAL_STRIKE_DAMAGE 2.0 ADDITIVE
  - HEALTH 20to30 ADDITIVE
```

> **警告：要在物品上使用属性，必须安装 [Crucible](https://wiki.mythiccraft.io/mythiccrucible/home)**

# 示例 {#examples}

## 自定义属性示例 {#example-custom-stats}

这些属性由用户自定义，以下提供了一些示例。

#### `ARMOR_GENERIC` {#armor-generic}

基于护甲的通用伤害减免，可用于装备。

```yml
ARMOR_GENERIC:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  ExecutionPoint: PRE
  Display: 'Generic Armor'
  DamageFormula: 'd - v'
  BaseValue: 0
  Formatting:
    Additive: '+<value> Generic Armor'
    Multiply: '+<value> Generic Armor'
    Compound: 'x<value> Generic Armor'
```

#### `ARMOR_BLUNT` {#armor-blunt}

针对 `BLUNT` [伤害类型](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/damagetag)的护甲伤害减免。

```yml
ARMOR_BLUNT:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  ExecutionPoint: PRE
  Display: 'Blunt Armor'
  DamageType: BLUNT
  DamageFormula: 'd - v'
  BaseValue: 0
  Formatting:
    Additive: '+<value> Blunt Armor'
    Multiply: '+<value> Blunt Armor'
    Compound: 'x<value> Blunt Armor'
```

#### `ARMOR_SHARP` {#armor-sharp}

针对 `SHARP` [伤害类型](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/damagetag)的护甲伤害减免。

```yml
ARMOR_SHARP:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_MODIFIER
  Triggers:
    - DAMAGED
  ExecutionPoint: PRE
  Display: 'Sharp Armor'
  DamageType: SHARP
  DamageFormula: 'd - v'
  BaseValue: 0
  Formatting:
    Additive: '+<value> Sharp Armor'
    Multiply: '+<value> Sharp Armor'
    Compound: 'x<value> Sharp Armor'
```

#### `DAMAGE_BLUNT` {#damage-blunt}

`BLUNT` [伤害类型](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/damagetag)的伤害输出。

```yml
DAMAGE_BLUNT:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_BONUS
  Priority: 1
  Triggers:
    - ATTACK
  ExecutionPoint: PRE
  Display: 'Blunt Damage'
  DamageType: BLUNT
  BaseValue: 0
  Formatting:
    Additive: '+<value> Blunt Damage'
    Multiply: '+<value> Blunt Damage'
    Compound: 'x<value> Blunt Damage'
```

#### `DAMAGE_SHARP` {#damage-sharp}

`SHARP` [伤害类型](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/damagetag)的伤害输出。

```yml
DAMAGE_SHARP:
  Enabled: false
  AlwaysActive: false
  Type: DAMAGE_BONUS
  Priority: 2
  Triggers:
    - ATTACK
  ExecutionPoint: PRE
  Display: 'Sharp Damage'
  DamageType: SHARP
  BaseValue: 0
  Formatting:
    Additive: '+<value> Sharp Damage'
    Multiply: '+<value> Sharp Damage'
    Compound: 'x<value> Sharp Damage'
```

#### `FIRE_RESISTANCE` {#fire-resistance}

配置为抵抗 FIRE、FIRE_TICK [伤害来源](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/conditions/DamageCause)。

```yml
FIRE_RESISTANCE:
  Enabled: false
  AlwaysActive: false
  Display: 'Fire Resistance'
  Formatting:
    Additive: '+<value> Fire Resistance'
    Multiply: '+<value> Fire Resistance'
    Compound: 'x<value> Fire Resistance'
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

#### `SPEED` {#speed}

可用于 [MOVEMENT_SPEED](https://wiki.mythiccraft.io/mythicmobs/Stats#movement_speed) 属性计算，通过公式影响速度。

```yml
SPEED:
  Enabled: true
  AlwaysActive: false
  Type: STATIC
  FormulaKey: 'SPD'
  Formatting:
    Additive: '+<value> Speed'
    Multiply: '+<value>% Speed'
    Compound: 'x<value>% Speed'
```

#### `ICE_DAMAGE` {#ice-damage}

以下是一个还涉及 TriggerStats 的更复杂示例

```yaml
ICE_DAMAGE:
  Enabled: true
  Type: DAMAGE_MODIFIER
  Priority: 50
  Triggers:
    - ATTACK
  ExecutionPoint: PRE
  Display: '&f֍'
  DamageType: ALL
  BaseValue: 0
  TriggerStats:
  - LIGHTNING_DEFENSE LD
  - AIR_DEFENSE AD
  - EARTH_DEFENSE ED
  - FIRE_DEFENSE FD
  - AETHER_DEFENSE AE
  - VOID_DEFENSE VD
  DamageFormula: '1 + d * ( LD + AD - ED - FD + 0.5 * ( AE - VD ) ) / 100'
  Formatting:
    Rounding: 2
    Additive: '&a+<value>'
    Multiply: '&a+<value>%'
    Compound: '&ax<value>%'
```
