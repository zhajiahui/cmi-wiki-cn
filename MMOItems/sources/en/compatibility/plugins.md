# 🦾 Built-in Compatibility {#🦾-built-in-compatibility}

This section lists all built-in compatibilities implemented into MMOItems.

## WorldGuard Flags {#worldguard-flags}

MythicLib implements new flags that work for both MMOCore and MMOItems. See the [full list here](https://docs.phoenixdevt.fr/mythiclib/features/compatibility#flag-plugins).

Like any other plugin, [WorldGuard](http://www.enginehub.org/worldguard) should be detected automatically by MMOItems when the server is booting. You can check the console when the plugin is loading to make sure it was detected.

## Custom Enchantments plugins {#custom-enchantments-plugins}

MMOItems is compatible with EcoEnchants, MythicEnchants and AdvancedEnchants (not recommended). It is most likely not natively compatible with other enchantment plugins, though well designed enchantment plugins should have no issues (for instance, EcoEnchants). More information over [this wiki page](https://docs.phoenixdevt.fr/mmoitems/compatibility/enchant-plugins).

## RPG Plugins {#rpg-plugins}

> **TIP**
>
> We recommend using [MMOCore](https://www.spigotmc.org/resources/70575/) for full native plugin compatibility.

MMOItems supports levels, classes and mana/stamina from the [following plugins](https://docs.phoenixdevt.fr/mythiclib/features/compatibility#rpg-plugins). Levels and classes from these plugins are forwarded to MMOItems in order to apply class and level requirements for items.

While most RPG core plugins feature Mana, the *Max Mana* stat ONLY works with MMOCore, Heroes and the built-in MythicLib Mana/Stamina module. Other plugins do not allow providing temporary stats to players, so it is impossible for MythicLib to provide Max Mana/Stamina to players.

## AureliumSkills {#aureliumskills}

MMOItems introduces a new stat to give the player more skills as well as item restrictions which prevent players from using specific items unless they have at least X levels in a skill. In order to have these stats display in the item lore, add this to your `stats.yml` config file:

```yml
additional-wisdom: '&3 &7■ Extra Wisdom: &f{value}'
additional-health: '&3 &7■ Extra Health: &f{value}'
additional-regeneration: '&3 &7■ Extra Regeneration: &f{value}'
additional-luck: '&3 &7■ Extra Luck: &f{value}'
additional-toughness: '&3 &7■ Extra Toughness: &f{value}'
additional-strength: '&3 &7■ Extra Strength: &f{value}'
additional-crit-damage: '&3 &7■ Extra Crit Damage: &f{value}'
additional-crit-chance: '&3 &7■ Extra Crit Chance: &f{value}'
required-farming: '&eRequires {value} in Farming'
required-foraging: '&eRequires {value} in Foraging'
required-mining: '&eRequires {value} in Mining'
required-fishing: '&eRequires {value} in Fishing'
required-excavation: '&eRequires {value} in Excavation'
required-archery: '&eRequires {value} in Archery'
required-defense: '&eRequires {value} in Defense'
required-fighting: '&eRequires {value} in Fighting'
required-endurance: '&eRequires {value} in Endurance'
required-agility: '&eRequires {value} in Agility'
required-alchemy: '&eRequires {value} in Alchemy'
required-enchanting: '&eRequires {value} in Enchanting'
required-sorcery: '&eRequires {value} in Sorcery'
required-healing: '&eRequires {value} in Healing'
required-forging: '&eRequires {value} in Forging'
```

And then this to your `lore-format.yml`:

```yml
  ...
  - '#additional-wisdom#'
  - '#additional-health#'
  - '#additional-regeneration#'
  - '#additional-luck#'
  - '#additional-toughness#'
  - '#additional-strength#'
  - '#additional-crit-chance#'
  - '#additional-crit-damage#'
  - '#required-farming#'
  - '#required-foraging#'
  - '#required-mining#'
  - '#required-fishing#'
  - '#required-excavation#'
  - '#required-archery#'
  - '#required-defense#'
  - '#required-fighting#'
  - '#required-endurance#'
  - '#required-agility#'
  - '#required-alchemy#'
  - '#required-enchanting#'
  - '#required-sorcery#'
  - '#required-healing#'
  - '#required-forging#'
  - '#required-forging#'
```

## MythicMobs {#mythicmobs}

MMOItems lets your mythic mobs drop items from MI. Please refer to [this wiki page](https://docs.phoenixdevt.fr/mmoitems/items/drop-tables).

## PlaceholderAPI {#placeholderapi}

See the full list of placeholders on [this wiki page](https://docs.phoenixdevt.fr/mmoitems/general/placeholders).

## RPGInventory {#rpginventory}

MMOItems supports [RPGInventory](https://www.spigotmc.org/resources/12498/): players can equip items from MMOItems in their custom inventory and benefit from their stats. However since RPGInventory does not support item attribute modifiers, stats based on vanilla attribute modifiers like attack speed, max health & movement speed won't apply on non-armor/hand item slots (i.e extra slots like accessory slots). Any other item effect will work fine.

MMOInventory however works flawlessly with MMOItems.

## BossShopPro {#bossshoppro}

MMOItems adds a special type of reward to BossShopPro. This reward type can be used to give players an item when they click an item. Here is the format you need to use in order to setup an MMOItem reward type:

```yml
RewardType: MMOITEM
Reward:
- <ITEM_TYPE>.<ITEM_ID>
- <ITEM_TYPE>.<ITEM_ID>
- etc.
```

## MythicMobs {#mythicmobs-1}

You can add items from MI to MythicMobs drop tables: more info on [this page](https://docs.phoenixdevt.fr/mmoitems/items/drop-tables#adding-mmoitems-to-mythicmobs-drop-tables).
