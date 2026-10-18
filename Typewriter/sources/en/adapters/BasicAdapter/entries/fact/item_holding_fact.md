# Item Holding Fact

The `Item Holding Fact` is a fact that returns the amount of a specific item the player is currently holding.
When no properties for the item are set, the fact will return the amount of the item the player is holding.

This fact can only be **read**, not written to. Hence, it is only suitable for criteria.

## How could this be used? {#how-could-this-be-used}

Show PathStreams when the player is holding a specific item.
Like showing a path to a location when the player is holding a map.

## Fields {#fields}

## Comment

Inherited Optional

A comment to keep track of what this fact is used for.

## Group

Required

## Item

Required

The item to check for.
