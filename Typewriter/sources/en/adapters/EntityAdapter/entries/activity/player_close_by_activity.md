# Player Close By Activity

The `PlayerCloseByActivityEntry` is an activity that activates child activities when a viewer is close by.

The activity will only activate when the viewer is within the defined range.

When the maximum idle duration is reached, the activity will deactivate.
If the maximum idle duration is set to 0, then it won't use the timer.

## How could this be used? {#how-could-this-be-used}

When the player has to follow the NPC and walks away, let the NPC wander around (or stand still) around the point the player walked away. When the player returns, resume its path.

When the npc is walking, and a player comes in range Stand still.

## Fields {#fields}

## Range

Required

The range in which the player has to be close by to activate the activity.

## Max Idle Duration

Required

The maximum duration a player can be idle in the same range before the activity deactivates.

Durations can be specified in the following format: `1d 2h 3m 4s`. The following units are supported: `d` for days, `h` for hours,`m` for minutes and `s` for seconds.

## Close By Activity

Required

The activity that will be used when there is a player close by.

## Idle Activity

Required

The activity that will be used when there is no player close by.
