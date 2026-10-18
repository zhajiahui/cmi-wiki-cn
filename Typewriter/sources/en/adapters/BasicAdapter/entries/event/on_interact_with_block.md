# Interact Block Event

The `Interact Block Event` is triggered when a player interacts with a block by right-clicking it.

## How could this be used? {#how-could-this-be-used}

This could be used to create special interactions with blocks, such as opening a secret door when you right-click a certain block, or a block that requires a key to open.

## Fields {#fields}

## Triggers

Required List

## Block

Required

The block that was interacted with.

## Location

Optional

The location of the block that was interacted with.

## Item In Hand

Required

The item the player must be holding when the block is interacted with.

## Cancel

Required

Cancel the event when triggered.
It will only cancel the event if all the criteria are met.
If set to false, it will not modify the event.

## Interaction Type

Required

The type of interaction that should trigger the event.

## Shift Type

Required

The type of shift that should trigger the event.
