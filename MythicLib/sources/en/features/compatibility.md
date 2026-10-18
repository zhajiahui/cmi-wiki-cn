# 🦾 Plugin Compatibility {#🦾-plugin-compatibility}

This section lists all plugin hooks implemented by MythicLib.

## RPG Plugins {#rpg-plugins}

> **INFO**
>
> While we recommend using [MMOCore](https://www.spigotmc.org/resources/70575/) for full native plugin compatibility, the MMO plugin suite also works when using other RPG core plugins.

The MMO plugins support the following RPG plugins. Player levels and classes apply to MMOItems item requirements and MMOInventory slot restrictions. Mana and stamina apply to MMOItems and MMOCore item and skill resource costs.

| Plugin | Level | Class | Mana | Stamina | Note |
| --- | --- | --- | --- | --- | --- |
| [MMOCore](https://www.spigotmc.org/resources/70575/) | ✔ | ✔ | ✔ | ✔ |  |
| [Heroes](https://www.spigotmc.org/resources/24734/) | ✔ | ✔ | ✔ | ✔ |  |
| [Fabled](https://www.spigotmc.org/resources/91913/) | ✔ | ✔ | ✔ | ❌ |  |
| [Skills](https://www.spigotmc.org/resources/8981/) / [SkillsPro](https://www.spigotmc.org/resources/skills-pro.8981/) | ✔ | ✔ | ✔ | ❌ |  |
| [RacesAndClasses](https://www.spigotmc.org/resources/28029/) | ✔ | ✔ | ✔ | ❌ |  |
| [RPGPlayerLeveling](https://www.spigotmc.org/resources/11096/) | ✔ | ❌ | ✔ | ✔ | Stamina is *power* |
| [AureliumSkills](https://www.spigotmc.org/resources/81069/) / [AuraSkills](https://www.spigotmc.org/resources/81069/) | ✔ | ❌ | ✔ | ❌ | Level is *power level* |
| [BattleLevels](https://www.spigotmc.org/resources/battlelevels.2218/) | ✔ | ❌ | ❌ | ❌ |  |
| [mcMMO](https://www.spigotmc.org/resources/official-mcmmo.64348/) | ✔ | ❌ | ❌ | ❌ | Level is *power level* |
| [McRPG](https://www.spigotmc.org/resources/mcrpg.63020/) | ✔ | ❌ | ❌ | ❌ | Level is *power level* |
| MythicLib | ❌ | ❌ | ✔ | ✔ | Read more [here](https://docs.phoenixdevt.fr/mythiclib/misc/mana-stamina) |
| Placeholders | ✔ | ✔ | ❌ | ❌ | Read more [below](https://docs.phoenixdevt.fr/mythiclib/features/compatibility#using-placeholders) |

### Notes {#notes}

MythicLib has a built-in module for mana and stamina. When running the MMO plugin suite, Mana is usually provided by MMOCore. For users who would like to use MMOItems without MMOCore, we provide this barebones Mana/Stamina solution. This built-in module replaces the old [Mana & Stamina Addon](https://github.com/mmopluginteam/mmoitems-mana) (no longer maintained).

Some plugins like [mcMMO](https://www.spigotmc.org/resources/official-mcmmo.64348/) or [McRPG](https://www.spigotmc.org/resources/mcrpg.63020/) have a *power level*, which is usually the sum of the individual player's skill levels. MythicLib interprets this power level as the player's level.

Several plugins only have one type of player resource, which is usually Mana. In that case, Stamina is replaced by food level. The second player resource is almost always Stamina.

### Using Placeholders {#using-placeholders}

You can also provide player classes and levels to MMO plugins using PlaceholderAPI placeholders. MythicLib will parse the placeholders using PlaceholderAPI and forward the results to the MMO plugins.

For example, if your RPG plugin `SomeRpgCore` is not natively supported by MMOCore but provides a `%somerpgcore_class%` placeholder for the class name, set `class-plugin` to `%somerpgcore_class%`. MythicLib will then use the placeholder output as the player's current class name. Similarly, if your RPG plugin provides a `%somerpgcore_level%` placeholder, you can use it for `level-plugin`.

> **WARNING**
>
> Note that the placeholder used to provide the player's level must return a properly formatted integer, as MythicLib will parse it as an integer.

### Configuration {#configuration}

MythicLib allows to separately choose the class, level, and mana plugins. For instance, you can simultaneously use classes from MMOCore, levels from mcMMO and mana/stamina from Fabled. You can use the same plugin for levels, classes and/or mana/stamina.

In order to choose your class plugin, go to your MythicLib `config.yml` and set the `class-plugin` option.

```yml
# Plugin providing classes. This will propagate to MMOItems for
# item requirements and MMOInventory for class slot requirements.
#
# Supported Plugins:
# ...
class-plugin: MMOCORE
```

In order to choose your level plugin, go to your MythicLib `config.yml` and set the `level-plugin` option.

```yml
# Plugin providing player levels. This will propagate to MMOItems
# for items requirements and MMOInventory for level slot requirements.
#
# Supported Plugins:
# ...
level-plugin: MMOCORE
```

## Flag Plugins {#flag-plugins}

Supported flag plugins:

- WorldGuard
- Residence

Here is the full list of all the available flags for both MMOCore and MMOItems.

| Flag | Description | Default |
| --- | --- | --- |
| `MI_WEAPONS` | Disables MMOItems weapons | Enabled |
| `MI_COMMANDS` | Disables MMOItems commands | Enabled |
| `MI_CONSUMABLES` | Disable MI consumables | Enabled |
| `MI_TOOLS` | Disables MI tools | Enabled |
| `MMO_ABILITIES` | Disable MMOCore/MI skills | Enabled |
| `PVP_MODE` | Disables PvP | Disabled |

## ~~Dual Wield Plugins~~ {#dual-wield-plugins}

~~MythicLib (and therefore MMOItems and MMOCore) features full compatibility (damage calculation and off hand attack effects application) with the following dual wield plugins:~~

- ~~[DualWield](https://www.spigotmc.org/resources/dualwield.82349/)~~
- ~~[RealDualWield](https://www.spigotmc.org/resources/%E2%9C%85-real-dualwield-attack-with-both-hands-with-real-animation-without-mods.30816/)~~

## Hologram Plugins {#hologram-plugins}

The following plugins are compatible with MythicLib and are used to display damage and regen indicators for example. Note that with the addition of text displays in 1.20.6, MythicLib now provides a stable and lag-free basic implementation of holograms.

- [HolographicDisplays](https://dev.bukkit.org/projects/holographic-displays)
- [DecentHolograms](https://modrinth.com/plugin/decentholograms)
- [CMI](https://www.spigotmc.org/resources/3742/)
- [TrHologram](https://www.spigotmc.org/resources/trhologram-outdated.75503/)
- [Holograms](https://www.spigotmc.org/resources/holograms.4924/)
