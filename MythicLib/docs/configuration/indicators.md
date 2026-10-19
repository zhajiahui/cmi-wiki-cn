---
title: indicators.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: indicators.yml
source_version: 1.7.1-SNAPSHOT
---

# indicators.yml

文件：`indicators.yml`。版本：`1.7.1-SNAPSHOT`。

随包配置。

## `damage_indicators` { #damage_indicators }

```yaml title="indicators.yml · damage_indicators"
damage_indicators:

  # 完全启用或禁用伤害显示
  enabled: true

  # 伤害低于 0.1 时不显示
  min_damage: 0.1

  # 使用格式：'ᜌ{icon} &f{value}ᜌ'，并搭配 Wiki 中
  # 提供的资源包，即可移除灰色背景
  format: '{icon} &f{value}'
  decimal_format: '0.#'

  custom_font:
    enabled: false
    normal:
      '0': 'ᜀ'
      '1': 'ᜁ'
      '2': 'ᜂ'
      '3': 'ᜃ'
      '4': 'ᜄ'
      '5': 'ᜅ'
      '6': 'ᜆ'
      '7': 'ᜇ'
      '8': 'ᜈ'
      '9': 'ᜉ'
      'dot': 'ᜊ'
      'inter': 'ᜍ'
    crit:
      '0': 'ᜐ'
      '1': 'ᜑ'
      '2': 'ᜒ'
      '3': 'ᜓ'
      '4': '᜔'
      '5': '᜕'
      '6': '᜖'
      '7': '᜗'
      '8': '᜘'
      '9': '᜙'
      'dot': 'ᜋ'
      'inter': 'ᜍ'

  # single => 仅显示一个数值
  # packet => 每个伤害包显示一个数值(!!)
  # type   => 每种伤害类型显示一个数值
  group_by: packet
  damage_type_splits: [weapon, skill]
  damage_type_icon_join: '' # 用空格连接

  icon:
    weapon:
      normal: '&c🗡'
      crit: '&c&l🗡'
    skill:
      normal: '&6☄'
      crit: '&6&l☄'
    projectile:
      normal: '&a➶'
      crit: '&a&l➶'
    physical:
      normal: '&4✘'
      crit: '&4&l✘'
    magic:
      normal: '&9✩'
      crit: '&9&l✩'

  split_holograms: true
  holograms_join: ' ' # 按空格拆分

  move: true
  radial_velocity: 1
  gravity: 1
  initial_upward_velocity: 1
  y_offset: 0.1
  entity_height_percent: 0.75
  r_offset: 0.5
  entity_width_percent: 0.75
  tick_period: 3
  lifespan: 20
```

## `regen_indicators` { #regen_indicators }

```yaml title="indicators.yml · regen_indicators"
regen_indicators:

  # 完全启用或禁用伤害显示
  enabled: false

  # 恢复生命值低于 0.1 时不显示
  min_regen: 0.1

  # 使用格式：'ᜌ{icon} &f{value}ᜌ'，并搭配 Wiki 中
  # 提供的资源包，即可移除灰色背景
  format: '&a+{value}'
  decimal_format: '0.#'

  custom_font:
    enabled: false
    '0': 'ᜀ'
    '1': 'ᜁ'
    '2': 'ᜂ'
    '3': 'ᜃ'
    '4': 'ᜄ'
    '5': 'ᜅ'
    '6': 'ᜆ'
    '7': 'ᜇ'
    '8': 'ᜈ'
    '9': 'ᜉ'
    'dot': 'ᜊ'
    'inter': 'ᜍ'

  move: true
  radial_velocity: 1
  gravity: 1
  initial_upward_velocity: 1
  y_offset: 0.1
  entity_height_percent: 0.75
  r_offset: 0.5
  entity_radius_percent: 0.75
  tick_period: 3
  lifespan: 20
```
