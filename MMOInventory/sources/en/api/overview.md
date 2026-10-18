# 🔌 Overview {#🔌-overview}

Access the `MMOInventory` plugin singleton instance using Bukkit's plugin manager after making sure the plugin is installed.

```java
MMOInventory plugin = (MMOInventory) Bukkit.getPluginManager().getPlugin("MMOInventory");
```

## Inventories {#inventories}

Every inventory has an instance of `Inventory` stored in memory. This abstract interface has two implementations, `CustomInventory` for custom inventories, and `VanillaInventory` for the vanilla inventory. Recall that there can be at most one vanilla inventory registered.

The `Inventory` instances contain configuration information about the inventory: items and slots inside it, commands bound to them, scripts when opening or closing the inventory...

First, access MMOInventory's inventory manager using the following syntax:

```java
MMOInventory plugin = /* see above */
InventoryManager inventories = plugin.getInventoryManager();
```

Then access instances of `Inventory` using the following methods:

```java
CustomInventory someCustomInv = inventories.getCustom("custom_inventory_id");
VanillaInventory theVanillaInv = inventories.getVanilla();

Collection<Inventory> all = inventories.getAll();
Collection<Inventory> customInvs = inventories.getAllCustom();
```

## Slots {#slots}

The `Inventory#getSlots` method returns a collection of instances of class `CustomSlot`. A custom slot corresponds to a slot in chest UIs where players can place items.

The key feature of these custom slots is their list of restrictions (one `SlotRestriction` object per restriction use). There are multiple implementations of the `SlotRestriction` abstract interface, like `LevelRestriction` or `TypeRestriction` when MMOItems is installed.

## Registering new restriction types {#registering-new-restriction-types}

Say you have a custom plugin with player data, and you want to restrict certain slots to players who have a specific boolean flag toggled on in their player data object, `SomePlayerData`.

First, provide an implementation of `SlotRestriction`:

```java
public class MyRestriction extends SlotRestriction {
  public MyRestriction(MMOLineConfig config) {
    // No config options needed?
  }

  @Override
  public boolean isVerified(InventoryData player, CustomSlot ignore2, ItemStack ignore1) {
    // does not depend on the custom slot in which item is placed.
    // does not depend on the item placed either.

    SomePlayerData yourPlayerData = SomePlayerData.get(player.getPlayer());
    return yourPlayerData.canUseThisSlot();
  }
}
```

Then register this slot restriction type with MMOInventory's slot manager. Let's call this restriction `my_restriction`.

```java
MMOInventory plugin = /* see above */
InventoryManager inventories = plugin.getInventoryManager();
```

> **WARNING**
>
> Make sure you call this code after MMOInventory loads, but before it enables. You can either put this in your `#onLoad` if you make MMOInventory a *(soft)depend*, or in `#onEnable` if you make MMOInventory a *loadbefore*.

You can then use this restriction inside inventory configs to create slots that are only usable when a certain condition is met. This can be combined with other existing restrictions to create interesting perks for players.

```yml
slots:
  ...
  SPECIAL_RING_SLOT:
    type: accessory
    material: GOLD_NUGGET
    custom_model_data_string: "ring1"
    name: "&6Special Ring Slot"
    slot: 34
    restrictions:
      - "mmoitemstype{type=RING}"
      - "my_restriction{}" # <<==== HERE!
    lore:
      - 'Drag & drop an item to equip it.'
      - ''
      - 'This slot is only available after'
      - 'completing the quest XXXXX.'
```

## Player Data {#player-data}

First, access player data objects using the following syntax:

```java
Player yourPlayer = /* see above */
MMOInventory plugin = /* see above */
PlayerDataManager manager = plugin.getDataManager();

PlayerData playerData = manager.get(yourPlayer);
```

Each player has a `PlayerData` object stored in memory, and an `InventoryData` object for each registered inventory. The `InventoryData` abstract interface is implemented for both custom inventories (`CustomInventoryData`) and vanilla inventories (`VanillaInventoryData`).

You can obtain instances of `InventoryData` using the following methods:

```java
PlayerData playerData = /* see above */
CustomInventory customInv = /* see above */
Inventory someInv = /* see above */

VanillaInventoryData vanillaInvData = playerData.getVanilla();
CustomInventoryData customInvData = playerData.getCustom(customInv);
InventoryData invData = playerData.get(someInv); // either custom or vanilla
```

You can obtain the current list of equipped items of a player using the following method. Using lookup mode `NORMAL` will ignore items that have been placed in an invalid inventory slot. Using lookup mode `IGNORE_RESTRICTIONS` will return all items, including the items present in the player's vanilla inventory.

```java
List<InventoryItem> items = playerData.getItems(InventoryLookupMode.NORMAL);
```

The `InventoryData` abstract interface exposes mainly two important methods for getting and updating inventory content. Note that calls to `#setItem` trigger an `InventoryUpdateEvent`.

```java
InventoryData invData = /* see above */
CustomSlot someSlot = /* ... */

invData.setItem(someSlot, new ItemStack(Material.DIAMOND_SWORD));
invData.setItem(someSlot, null); // remove item

Collection<InventoryItem> content = invData.retrieveItems();
```

The class `InventoryItem` stores information about the item and its position in the inventory.
