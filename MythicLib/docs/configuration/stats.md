---
title: stats.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: stats.yml
source_version: 1.7.1-SNAPSHOT
---

# stats.yml

文件：`stats.yml`。版本：`1.7.1-SNAPSHOT`。

随包配置。

## `decimal-format` { #decimal-format }

```yaml title="stats.yml · decimal-format"
# 各项属性在界面中
# 显示的小数位数 (例如玩家属性界面)。
# https://docs.oracle.com/javase/7/docs/api/java/text/DecimalFormat.html
#
# 未指定时默认为 "0.#"，此默认值无法修改。
decimal-format:
  MOVEMENT_SPEED: '0.##'
  ARMOR_TOUGHNESS: '0.###'
  KNOCKBACK_RESISTANCE: '0.##'
  HEALTH_REGENERATION: '0.##'
  MANA_REGENERATION: '0.##'
  STELLIUM_REGENERATION: '0.##'
```

## `min-max-values` { #min-max-values }

```yaml title="stats.yml · min-max-values"
  # 可以按需添加任意数量……

# 属性值的最小值和最大值。例如，为 CRITICAL_STRIKE_CHANCE 设置 '0 = 100'
# 意味着暴击几率不能低于 0%，
# 也不能超过 100%。这是调整服务器平衡的
# 重要工具。可以调整格挡几率、防御、
# 最大生命值、伤害减免等属性。
#
# * 通用格式为 '{MINIMUM VALUE} = {MAXIMUM VALUE}'
# * 使用 '= {MAXIMUM VALUE}' 可禁用下限。
# * 使用 '{MINIMUM VALUE} =' 可禁用上限。
# * 默认情况下，大多数属性没有上限或下限。
#   以下部分内容仅作为示例。
# * !! 最小值不是基础属性值。它仅表示
#   该属性不能低于 X(只对属性值进行限幅)。
#
# 生命值、护甲、攻击伤害等原版 Minecraft 属性
# 仅得到部分支持。只有 MMO 插件
# 提供的那部分属性值会受到这些上下限影响。
min-max-values:

  # 暴击
  CRITICAL_STRIKE_CHANCE: '0 = 80'
  CRITICAL_STRIKE_POWER: '0 = 500'
  SKILL_CRITICAL_STRIKE_CHANCE: '0 = 80'
  SKILL_CRITICAL_STRIKE_POWER: '0 = 500'

  # 伤害减免
  BLOCK_RATING: '0 = 80'
  DODGE_RATING: '0 = 80'
  PARRY_RATING: '0 = 80'
  BLOCK_POWER: '25 = 75'

  BLOCK_COOLDOWN_REDUCTION: '0 = 80'
  DODGE_COOLDOWN_REDUCTION: '0 = 80'
  PARRY_COOLDOWN_REDUCTION: '0 = 80'

  # 其他
  MOVEMENT_SPEED: '0 = .3'
  DEFENSE: '0 = 10000'
  SPEED_MALUS_REDUCTION: '0=80'
```

## `base-stat-value` { #base-stat-value }

```yaml title="stats.yml · base-stat-value"
  # 可以按需添加任意数量……

# 在此可编辑任意属性的基础值。这与施加
# 永久属性增益的效果完全相同。例如，MMOCore 职业提供
# 20 点基础生命值，此配置节中的基础值设为
# 10，则最终得到 20 + 10 = 30 点生命值。
# 对 MMOItems 物品也是如此。
#
# 这也是平衡玩家属性的重要工具。
# 所有属性的默认基础值均为 0。
#
# !! 对基于原版属性的数值(最大生命值、移动速度、护甲等)，
# !! 此基础属性值会加到玩家原版的基础属性值上
# !! (最大生命值为 20，移动速度为 0.1，护甲为 0 等)
base-stat-value:

  # 暴击。默认造成 2x 伤害
  CRITICAL_STRIKE_POWER: 200
  SKILL_CRITICAL_STRIKE_POWER: 200

  # 伤害减免
  BLOCK_POWER: 25

  # MMOItems 武器属性
  BLUNT_POWER: 2
  BLUNT_RATING: 33

  # 可以按需添加任意数量……
```
