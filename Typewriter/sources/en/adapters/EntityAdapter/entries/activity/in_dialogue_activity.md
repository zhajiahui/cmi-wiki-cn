# In Dialogue Activity

The `InDialogueActivityEntry` is an activity that activates child activities when a player is in a dialogue with the NPC.

The activity will only activate when the player is in a dialogue with the NPC.

## How could this be used? {#how-could-this-be-used}

This can be used to stop a npc from moving when a player is in a dialogue with it.

## Fields {#fields}

## Dialogue Idle Duration

Required

The duration a player can be idle in the same dialogue before the activity deactivates.

When set to 0, it won't use the timer.

**info**

When the dialogue priority is higher than this activity's priority, this timer will be ignored.
And will only exit when the dialogue is finished.

Durations can be specified in the following format: `1d 2h 3m 4s`. The following units are supported: `d` for days, `h` for hours,`m` for minutes and `s` for seconds.

## Talking Activity

Required

The activity that will be used when the npc is in a dialogue

## Idle Activity

Required

The activity that will be used when the npc is not in a dialogue
