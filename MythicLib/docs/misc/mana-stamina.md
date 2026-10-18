---
title: 魔力与耐力
source: https://docs.phoenixdevt.fr/mythiclib/misc/mana-stamina
source_snapshot: '2026-10-19'
---

# 魔力与耐力 {#💧-mana-stamina}

MMOItems和MMOCore使用魔力和耐力来计算物品/技能资源成本。 MMO 插件本身支持许多实现魔力和/或耐力的RPG插件。请参阅[此 wiki 页面](../features/compatibility.md#rpg-plugins)以获取受支持插件的完整列表。

要选择魔力/耐力插件，请转到MythicLib`config.yml`并设置`mana-plugin`选项。

```yml
# Plugin providing mana and stamina. This works on MMOItems item
# requirements and skill costs for MMOItems/MMOCore.
#
# For plugins that features only one resource, which is then
# usually named Mana, Stamina is replaced by food level.
#
# Supported Plugins:
# ...
mana-plugin: MMOCORE
```

## Built-in解决方案 {#built-in-solution}

如果你没有使用任何RPG插件，你可以坚持使用MythicLib附带的built-in魔力和耐力模块。此模块/插件添加了两个资源，魔力和耐力，以及以下属性：

- *魔力和耐力再生*，即每秒被动再生的资源量，
- *Max魔力和耐力*，这是玩家可以拥有的最大资源量。

该模块还支持MMOProfiles。切换档案时，临时存储魔力和耐力。当切换回之前打开的档案时，旧的魔力和耐力值将恢复。

> **信息**
>
> 要启用此模块，请转到MythicLib`config.yml`并将`mana-plugin`设置为`MYTHICLIB`。

### 配置 {#configuration}

启用后，你可以在MythicLib`config.yml`的`builtin_mana`配置部分中编辑魔力/耐力选项。请注意，当使用任何其他魔力插件时，这些选项是无用的。

<details markdown="1">

<summary>完整配置（最后更新，3.2026）</summary>

```yml
# MythicLib features a default mana/stamina module if you are not using
# MMOCore nor any RPG plugin that has mana/stamina.
# Set 'resource-plugin' to 'MYTHICLIB' to enable. Otherwise, these settings
# are useless.
builtin_mana:

  # Change default stat values inside MythicLib/stats.yml
  # Stat names are MAX_MANA, MANA_REGENERATION, MAX_STAMINA, STAMINA_REGENERATION

  # The interval at which regeneration should happen in ticks.
  # Default value is 10 ticks which is the same as half a second.
  refresh_rate: 10

  # The percentage of their max mana/stamina which players
  # get as mana/stamina when logging in for the first time
  login_ratio:
    mana: 75
    stamina: 75

  # Edit here the character used in the resource bars
  # in the %mmoitems_mana_<mana/stamina>_bar% placeholder.
  bar:
    mana:
      char: █
      length: 20
      color:
        full: AQUA
        half: DARK_AQUA
        empty: WHITE
    stamina:
      char: █
      length: 20
      color:
        full: GREEN
        half: DARK_GREEN
        empty: WHITE
```

</details>

你还可以在MythicLib`stats.yml`内编辑资源属性（最大魔力、耐力再生...）的基本/最小/最大值。请注意，当使用MMOCore作为魔力插件时，此语法也适用。

```yml
#Min/max values of stats
min-max-values:
  ...
  MAX_MANA: '0 = 1000'
  MAX_STAMINA: '0 = 1000'
  ...

# Base stat values
base-stat-value:
  ...
  MAX_MANA: 20
  MAX_STAMINA: 20
  STAMINA_REGENERATION: 1
  MANA_REGENERATION: .3
```

## 占位符 {#placeholders}

使用built-inMythicLib魔力模块时，以下 PAPI占位符可用。

|占位符|描述 |
| --- | --- |
| `%mythiclib_mana%` | 玩家的当前魔力。 |
| `%mythiclib_stamina%` | 玩家的当前耐力。 |
| `%mythiclib_mana_bar%` | 使用MythicLib`config.yml`中提供的显示选项将玩家的魔力显示为条形。 |
| `%mythiclib_stamina_bar%` | 使用MythicLib`config.yml`中提供的显示选项将玩家的耐力显示为条形。 |

---

原文：[💧 Mana & Stamina](https://docs.phoenixdevt.fr/mythiclib/misc/mana-stamina) · 原文归档：2026-10-19
