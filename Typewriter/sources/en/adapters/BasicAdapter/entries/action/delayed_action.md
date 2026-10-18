# Delayed Action

The `Delayed Action Entry` is an entry that fires its triggers after a specified duration. This entry provides you with the ability to create time-based actions and events.

## How could this be used? {#how-could-this-be-used}

This entry can be useful in a variety of situations where you need to delay an action or event.
You can use it to create countdown timers, to perform actions after a certain amount of time has elapsed, or to schedule events in the future.

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Modifiers

Inherited List

A list of facts that will be modified for the player when this entry is triggered.

## Triggers

Required List

## Duration

Required

The duration before the next triggers are fired.

Durations can be specified in the following format: `1d 2h 3m 4s`. The following units are supported: `d` for days, `h` for hours,`m` for minutes and `s` for seconds.
