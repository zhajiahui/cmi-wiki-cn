# Group Trigger Action

The `Group Trigger Action` is an action that triggers the next entries for everyone in the same group as the player.

**caution**

The modifiers will only be applied to the player that triggered the action.
If you want to modify the other players, you will need to do it in the next entries.

## How could this be used? {#how-could-this-be-used}

This could be used to trigger the next entries for everyone in the same group as the player,
when a player joins a faction, all the other players in the same faction could be notified.

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Modifiers

Inherited List

A list of facts that will be modified for the player when this entry is triggered.

## Triggers

Required List

## Group

Required

## Force Group

Optional

The group to trigger the next entries for. If not set, the action will trigger for the group of the player that triggered the action.
