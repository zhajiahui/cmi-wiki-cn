# Remove Item Action

The `Remove Item Action` is an action that removes an item from the player's inventory.
This action provides you with the ability to remove items from the player's inventory in response to specific events.

**caution**

This action will try to remove "as much as possible" but does not verify if the player has enough items in their inventory.
If you want to guarantee that the player has enough items in their inventory, add an
[Inventory Item Count Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/inventory_item_count_fact) to the criteria.

## How could this be used? {#how-could-this-be-used}

This can be used when `giving` an NPC an item, and you want to remove the item from the player's inventory.
Or when you want to remove a key from the player's inventory after they use it to unlock a door.

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Modifiers

Inherited List

A list of facts that will be modified for the player when this entry is triggered.

## Triggers

Required List

## Item

Required

The item to remove.
