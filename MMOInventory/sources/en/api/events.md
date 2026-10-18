# 📮 Events {#📮-events}

This page describes the Bukkit events fired by MMOInventory.

## `InventoryUpdateEvent` {#inventoryupdateevent}

This event is called every time inventory content is changed. `#getPreviousItem` returns the previous item, or `null` if there wasn't one. `#getNewItem` returns the item being "equipped", or `null` if it is being removed. `#getInventoryData` returns the player's inventory data. `#getSlot` returns the clicked slot.

This event cannot be canceled. It is notably used for broadcasting inventory updates to MMOItems.

## `ItemEquipEvent` {#itemequipevent}

This is the cancelable counterpart of `InventoryUpdateEvent`. It is only called when players click from inside the chest inventory. Note that this event is also called when players interact with custom slots inside their vanilla inventory.

Note that editing items on clicks is not trivial, as it can lead to inconsistent behaviors with MMOItems inventory updates. Here are some solutions:

- either listen to one of the previous events, and schedule a task to edit it on the next tick using `InventoryData#setItem`,
- or edit the equipped item *in place*, by setting its item type and item meta. Note that MMOItems sometimes does that for features like *in place* durability losses and item downgrades. You will need to resolve MMOItems modifiers from the inventory again afterward.
