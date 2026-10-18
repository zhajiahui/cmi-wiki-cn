# Timed Activity

The `TimedActivityEntry` is an activity that allows child activities for a limited amount of time.

When the duration is up, the activity will deactivate.
Then the activity will be on cooldown for a set amount of time before it can be activated again.

## How could this be used? {#how-could-this-be-used}

This could be used to make an entity do something for a limited amount of time.

## Fields {#fields}

## Duration

Required

The duration child activities will be active for.

Durations can be specified in the following format: `1d 2h 3m 4s`. The following units are supported: `d` for days, `h` for hours,`m` for minutes and `s` for seconds.

## Cooldown

Required

The cooldown time before the activity can be activated again.

Durations can be specified in the following format: `1d 2h 3m 4s`. The following units are supported: `d` for days, `h` for hours,`m` for minutes and `s` for seconds.

## Active Activity

Required

The activity that will be used when the duration is active.

## Cooldown Activity

Required

The activity that will be used when it is on cooldown.
