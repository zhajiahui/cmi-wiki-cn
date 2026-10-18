# 💧 Mana & Stamina {#💧-mana-stamina}

MMOItems and MMOCore use mana and stamina for item/skill resource costs. Many RPG plugins that implement Mana and/or Stamina are natively supported by the MMO plugins. Please see [this wiki page](https://docs.phoenixdevt.fr/mythiclib/features/compatibility#rpg-plugins) for the full list of supported plugins.

In order to choose your mana/stamina plugin, go to your MythicLib `config.yml` and set the `mana-plugin` option.

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

## Built-in Solution {#built-in-solution}

If you are not using any RPG plugin, you can stick to the built-in mana and stamina module that comes with MythicLib. This module/addon adds two resources, Mana and Stamina, as well as the following stats:

- *Mana and Stamina Regeneration*, which is the amount of resource passively regenerated every second,
- *Max Mana and Stamina*, which is the maximum amount of resource a player can have.

This module also supports MMOProfiles. When switching profiles, mana and stamina are temporarily stored. When switching back to a previously opened profile, the old mana and stamina values are restored.

> **INFO**
>
> To enable this module, go to your MythicLib `config.yml` and set `mana-plugin` to `MYTHICLIB`.

### Configuration {#configuration}

Once enabled, you can edit mana/stamina options in the `builtin_mana` config section of your MythicLib `config.yml`. Note that these options are useless when using any other mana plugin.

<details markdown="1">

<summary>Full Config (Last Updated, 3.2026)</summary>

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

You can also edit the base/min/max values of resource stats (Max Mana, Stamina Regen...) inside your MythicLib `stats.yml`. Note that this syntax also works when using MMOCore as your mana plugin.

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

## Placeholders {#placeholders}

The following PAPI placeholders are available when using the built-in MythicLib mana module.

| Placeholder | Description |
| --- | --- |
| `%mythiclib_mana%` | Current mana of the player. |
| `%mythiclib_stamina%` | Current stamina of the player. |
| `%mythiclib_mana_bar%` | Displays the player's mana, as a bar using display options provided in the MythicLib `config.yml`. |
| `%mythiclib_stamina_bar%` | Displays the player's stamina as a bar, using display options provided in the MythicLib `config.yml`. |
