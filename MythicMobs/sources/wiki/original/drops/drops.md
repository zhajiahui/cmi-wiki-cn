# Drops

The Drops tag can be added to your custom mobs to allow them to drop items of your choice upon their death. There are three types of custom drops available in MythicMobs to distinguish between.

1. [Drops Configuration](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#drops-configuration)
   1. [Drop](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#drop)
   2. [Amount](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#amount)
   3. [Chance](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#chance)
   4. [Dynamic Chances](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#dynamic-chances)
2. [Drop Types](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#drop-types)
   1. [Example](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#example)
3. [In-line Drops](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#in-line-drops)
   1. [Example](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#example-2)

Drops are the simplest way to implement custom drops.

## Drops Configuration {#drops-configuration}

```yaml
internal_mobname:
  Type: <mobtype>
  Drops:
  - <drop> <amount> <chance>
  - <drop> <amount> <chance>
  - ...
```

### Drop {#drop}

Can be either an item from MythicMobs, a vanilla item, exp, a drop table or an item/experience for a supported plugin. The list of available [Drop Types](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#drop-types) is displayed below

### Amount {#amount}

The amount of items to be dropped.

Can be a number range, for example: `1-3` or `1to3`.  
In this case, the number of dropped items will never be smaller than the leftmost number and never be **equal or greater** to the rightmost number

> Writing `1to3` will drop at least 1 item and at most 2 items

### Chance {#chance}

The chance for the specified item to be dropped.

- Must be a number between 0 and 1
- **Note:** allows percentage chances. (10% instead of 0.1).

### Dynamic Chances {#dynamic-chances}

> Requires MythicMobs Premium (math and variables in numeric values are a Premium feature).

The chance may also be a math expression, placeholder, or variable that resolves to a number. It is evaluated for the dropping mob every time loot is rolled, so drop rates can scale with level, stats, or a variable. A resolved value of `1` or higher always drops; `0` or lower never drops. The roll happens during loot generation, so dynamic chances also work with [FancyDrops](https://wiki.mythiccraft.io/mythicmobs/drops/FancyDrops).

```yaml
YourMob:
  Type: ZOMBIE
  Drops:
  # 5% per mob level (reaches 100% at level 20+)
  - diamond 1 0.05*<caster.level>
  # chance pulled from a variable set elsewhere on the mob
  - emerald 1 <caster.var.scaledDrop>
```

> On the free version these expressions cannot be evaluated: the drop is treated as a guaranteed (100%) drop and a warning is logged on load.

## Drop Types {#drop-types}

| **Type** | **Explanation** | **Example** |
| --- | --- | --- |
| [MythicMob](https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/MythicMob) | Will drop a MythicMob |  |
| [Mythic Item](https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/MythicItem) | Will drop a Mythic Item |  |
| [VanillaLootTable](https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/VanillaLootTable) | Drop items from vanilla loot tables and datapacks | `- vanillaLootTable minecraft:table_name` |
| **champions-exp** | Will drop experience points for the plugin `Champions`. |  |
| [skillapi-exp](https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/SkillAPIExp) | Will drop experience points for the plugin `SkillAPI` |  |
| **heroesexp** | Will drop experience points for the plugin `Heroes`. |  |
| [mcmmo-exp](https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/McMMOExp) | Will drop experience points for the plugin `MCMMO`. | `- mcmmo-exp 69` |
| **exp** | Will drop regular Minecraft experience points. | `- exp 420` |
| [money](https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/Money) | Will drop money for the plugin `Vault`. | `- money 1500` |
| **mythicdrop <item>** | Will drop an <item> from the plugin `MythicDrops`. | `- mythicdrop CoolSword 1` |
| [phatloot](https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/PhatLoot) | Will drop an &item from the plugin `PhatLoot`. | `- phatloot LootTableName 1` |
| [command](https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/Command) | Will run a command in console. | `- cmd{cmd="warp <trigger.name> spawn"} 1` |
| [mmoitems](https://gitlab.com/phoenix-dvpmt/mmoitems/-/wikis/Item%20Drop%20Tables#adding-mmoitems-to-mythicmobs-drop-tables) | Drops a `mmoitems` item | `- mmoitems{type=SWORD;id=CUTLASS} 1 1` |
| **nothing** | Will drop nothing. Can help while creating weighted droptables | `- nothing` |
| [ItemVariable](https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/ItemVariable) | Drops the item defined in the specified item variable | `- itemvariable{variable=caster.stolenitem} 1 1` |

### Example {#example}

This example will have a 20% chance of dropping 3 diamonds, a 60% chance to run a command and a 12% chance to drop between 100 and 600 exp

```yaml
YourMob:
  Type: ZOMBIE
  Drops:
  - diamond 3 0.2
  - cmd{cmd="crate give <trigger.name> RewardCrate 1"} 1 0.6
  - exp 100to600 0.12
```

## In-line Drops {#in-line-drops}

For very basic equipment, you can add some inline item data so that you don't always have to create a mythic item.
You can use all the item data from [Inline Item Configurations](https://wiki.mythiccraft.io/mythicmobs/Mobs/Equipment#in-line-items)!

```yaml
 Drops:
 - leather_chestplate{name="Dark Leather";lore="&8A vest made of darkened leather";color=BLACK} 1 1
```

### Example {#example-2}

The below drops section will drop a Panda player head item that has 2 enchants on it, and will drop 3 pieces of diamond armor that all have names, lore, and enchantments on them!

```yaml
  Drops:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==;enchants=WATER_WORKER:1,OXYGEN:3} 1 1
  - DIAMOND_CHESTPLATE{name="Panda<&sq>s Will";lore="A Panda must be vigilant";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_LEGGINGS{name="Panda<&sq>s Strength";lore="A Panda must be strong";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_BOOTS{name="Panda<&sq>s Speed";lore="A Panda must be fast";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,PROTECTION_FALL:4,DEPTH_STRIDER:3} 1 1
```
