---
title: mitigation_types.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: mitigation_types.yml
source_version: 1.7.1-SNAPSHOT
---

# mitigation_types.yml

文件：`mitigation_types.yml`。版本：`1.7.1-SNAPSHOT`。

随包配置。

## `block` { #block }

```yaml title="mitigation_types.yml · block"
######################################
# 格挡
#
# 格挡攻击会按一定百分比降低受到的伤害
######################################
block:

  # 仅用于向后兼容。
  # 如果所有插件都没有使用旧的 MythicLib 伤害减免
  # 事件，可以移除此选项或将其注释掉。
  legacy: block

  # 两次连续格挡之间的冷却时间公式(单位：秒)
  # 删除此行或将其注释掉可禁用冷却
  # 注意：默认情况下，冷却缩减上限为 80%(见 stats.yml)
  cooldown: '3 * (1 - <stat.block_cooldown_reduction> / 100)'

  # 成功格挡攻击的概率
  # 此公式应返回 0 到 1 之间的数值(0 表示 0% 概率，1 表示 100% 概率)
  # 注意：默认情况下，格挡几率上限为 80%(见 stats.yml)
  roll: '<stat.block_rating> / 100'

  # 受到伤害时执行的技能
  on_damage: 'mythiclib:mitigation_on_block'
```

## `dodge` { #dodge }

```yaml title="mitigation_types.yml · dodge"
######################################
# 闪避
#
# 闪避攻击会完全抵消所有受到的伤害
######################################
dodge:

  # 仅用于向后兼容。
  # 如果所有插件都没有使用旧的 MythicLib 伤害减免
  # 事件，可以移除此选项或将其注释掉。
  legacy: dodge

  cooldown: '3 * (1 - <stat.dodge_cooldown_reduction> / 100)' # 连续两次闪避之间的冷却时间（秒）
  roll: '<stat.dodge_rating> / 100' # 成功闪避攻击的概率
  on_damage: 'mythiclib:mitigation_on_dodge' # 受到伤害时执行的技能
```

## `parry` { #parry }

```yaml title="mitigation_types.yml · parry"
######################################
# 招架
#
# 招架攻击会完全抵消所有受到的伤害，并将
# 一部分伤害反弹给攻击者
######################################
parry:

  # 仅用于向后兼容。
  # 如果所有插件都没有使用旧的 MythicLib 伤害减免
  # 事件，可以移除此选项或将其注释掉。
  legacy: parry

  cooldown: '3 * (1 - <stat.parry_cooldown_reduction> / 100)' # 连续两次招架之间的冷却时间（秒）
  roll: '<stat.parry_rating> / 100' # 成功招架攻击的概率
  on_damage: 'mythiclib:mitigation_on_parry' # 受到伤害时执行的技能

# 可以编辑已有的伤害减免类型、添加自定义类型，或复制已有类型等。
# 伤害减免类型的数量没有限制。
# MythicLib 内置 3 种伤害减免类型：block、parry 和 dodge，它们是 RPG 游戏中最常见的类型
```
