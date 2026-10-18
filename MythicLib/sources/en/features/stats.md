# 💪 Player Stats {#💪-player-stats}

MMOItems and MMOCore share the same stat system. Any stat that you gain through an MMOItems item, MMOCore class, or item placed inside a MMOInventory inventory, will propagate to all MMO plugins.

In this page, we look at the `MythicLib/stats.yml` config file. Unless specified otherwise, all YML snippets are to be used inside of this config file.

## Temporary Stats {#temporary-stats}

Temporary stats, or *stat modifiers*, are stats boosts/debuffs that are given to players for a limited/unlimited amount of time. In either way, these stats are removed when the server restarts.

### Using a script {#using-a-script}

Note that you can give temporary stats to players using the `add_stat` script mechanic. You will find more information on [this wiki page](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/buffs#add-temporary-stats). These stats will be removed when the server restarts.

### Using commands {#using-commands}

The easiest way to provide temporary stats to players is through commands.

```cmd
/ml stat add <player> <stat> <amount> (duration) (key) (unique)
/ml stat remove <player> <stat> <key>
/ml stat clear <player> <key>
```

Using the `add` subcommand, you can provide a stat modifier to a player.

- If you provide a duration through the `duration` parameter (in ticks), the stat will be temporary and removed after that time.
- If you provide a `key`, you can later remove this stat modifier using the `remove` subcommand. If you do not provide any, it will use the default key `default`.
- If you set `unique` to true, only one modifier with the same key will be active at a time; adding a new one will replace the previous one. This is useful for buffs that you want to refresh periodically.

> **Example**
>
> The following command provides a flat +10 Attack Damage stat to the player `Notch` for 5 seconds (100 ticks), using the key `my_custom_buff`. If you execute the same command again, it will not override the previous one since `unique` is set to false, and it will stack with itself.
>
```cmd
/ml stat add Notch ATTACK_DAMAGE 10 100 my_custom_buff false
```

Using the `remove` subcommand, you can remove a specific stat modifier from a player using its `key`.

> **Example**
>
> The following command unregisters the stat modifier given in the previous example.
>
```cmd
/ml stat remove Notch ATTACK_DAMAGE my_custom_buff
```

Using the `clear` subcommand, you can remove all stat modifiers with the associated `key` from a player.

> **Example**
>
> The following command removes all stat modifiers with the key `my_custom_buff` from the player `Notch`.
>
```cmd
/ml stat clear Notch my_custom_buff
```

## Min/Max Stat Values {#min-max-stat-values}

Minimum and maximum values for the stat values. This means using '0 = 100' for CRITICAL_STRIKE_CHANCE means that you cannot have less than 0% and cannot have more than 100% critical strike chance. This is an important tool for server balance. You can balance stats like block rating, defense, max health, damage reduction etc.

- General format is `{min_value} = {max_value}`
- Using only `= {max_value}` will disable the lower bound.
- Using only `{min_value} =` will disable the upper bound.
- If nothing is specified, there are no upper nor lower bounds.

> **INFO**
>
> There is a slight difference between base stat value and minimal value. Min/max values are used to clamp the total stat value. The total stat value is the sum of the base stat value and all modifiers. In other words, the base stat value is like a permanent stat buff.

You will find the following code snippet inside the `MythicLib/stats.yml` config file.

```yml
min-max-values:

  # Crits
  CRITICAL_STRIKE_CHANCE: '0 = 80'
  CRITICAL_STRIKE_POWER: '0 = 500'
  SKILL_CRITICAL_STRIKE_CHANCE: '0 = 80'
  SKILL_CRITICAL_STRIKE_POWER: '0 = 500'

  # Mitigation
  BLOCK_RATING: '0 = 80'
  DODGE_RATING: '0 = 80'
  PARRY_RATING: '0 = 80'
  BLOCK_POWER: '25 = 75'

  BLOCK_COOLDOWN_REDUCTION: '0 = 80'
  DODGE_COOLDOWN_REDUCTION: '0 = 80'
  PARRY_COOLDOWN_REDUCTION: '0 = 80'

  # Other
  MOVEMENT_SPEED: '0 = .3'
  DEFENSE: '0 = 10000'
  SPEED_MALUS_REDUCTION: '0=80'

  # Add as many as you want.
```

## Base Stat Values {#base-stat-values}

Modifying the base value of a stat inside `MythicLib/stats.yml` has the same effect as applying a permanent flat stat buff or debuff to the player. If your MMOCore class has 20 base *Max Health*, and you set the base value of the *Max Health* stat to 10, the resulting *Max Health* is `10 + 20 = 30`.

This feature is most useful when you want to adjust the base stat values of all players on your server by a flat amount. If you are using MMOCore, you might not need this feature at all, as you may find it easier to simply edit the base stat values of your classes.

Note that default Minecraft stats like *Max Health*, *Armor*, *Attack Damage*, and *Attack Speed* naturally have non-zero base values defined by vanilla Minecraft. For instance, *Max Health* has a base value of 20, *Movement Speed* is 0.1, *Attack Speed* is 4, *Attack Damage* is 1, etc. These vanilla base values **add up to** the base values specified in this configuration file; they are not overridden by them.

Note that the base stat values specified inside `MMOCore/stats.yml` override the vanilla base stat values, while the MythicLib base stat values act as **stat value adjustments (offsets)**. Lastly, stat formulas provided inside [MMOCore class configs](https://docs.phoenixdevt.fr/mmocore/features/classes#class-stats) override formulas provided inside `MMOCore/stats.yml`.

```yml
base-stat-value:

  # Crits. By default, crits deal 2x damage
  CRITICAL_STRIKE_POWER: 200
  SKILL_CRITICAL_STRIKE_POWER: 200

  # Mitigation
  BLOCK_POWER: 25

  # Add as many as you want.
```

## Stat Proxies {#stat-proxies}

Stat proxies are a very useful feature, that allows you to create **stats that provide other stats**. For instance, you can create a *Strength* stat that, for every point, increases *Max Health* by 4% and *Atk Damage* by 1 point.

If you are running MMOCore, you might recognize similarities with [attributes](https://docs.phoenixdevt.fr/mmocore/features/attributes). You would not be wrong, as MMOCore attributes are internally implemented using stat proxies. Stat proxies can be seen as an extension of MMOCore attributes, while MMOCore attributes can be thought of as a user-friendly way to interact with stat proxies.

Let us take a look at the following YML snippet, which you will find inside the `MythicLib/stats.yml` config file.

```yml
proxies:
  
  POWER:
    # 1 pt in Power gives +2% max health
    # and +1% atk damage 
    MAX_HEALTH:
      type: RELATIVE
      multiplier: 2
    ATTACK_DAMAGE:
      type: RELATIVE
      multiplier: 1

  MAX_HEALTH_PERCENT:
    # One unit in MAX_HEALTH_PERCENT increases
    # MAX_HEALTH by 1%, linearly
    MAX_HEALTH:
      multiplier: 1
      type: RELATIVE
```

This syntax defines two stat proxies. The first one resembles the *Strength* stat we mentionned earlier. This stat proxy is configured so that, each point in the `POWER` stat automatically provides +2% *Max Health* and +1% *Atk Damage*.

`multiplier` is the amount of stat points transferred to the target stat, for each point in the source stat. `type` can be set to `FLAT` for a flat bonus, `RELATIVE` for a %-based bonus or `COMPOUND` for a geometric/compound %-based bonus. When type is set to `RELATIVE` or `COMPOUND`, `multiplier` should be provided as a percent (that is, MythicLib will multiply the given value by `1/100` to express it as a scalar).

### %-Based Stats {#based-stats}

The second proxy defined by the snippet above presents another potential use case for stat proxies. In case a specific stat, say `MAX_HEALTH`, as no %-stat equivalent in MMOItems, you can create an intermediate/proxy stat, that transforms linear buffs to the `MAX_HEALTH_PERCENT` stat into %-based buffs to the `MAX_HEALTH` stat.
