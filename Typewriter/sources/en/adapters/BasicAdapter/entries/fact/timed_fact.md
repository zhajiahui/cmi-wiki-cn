# Timed Fact

This fact is stored for a certain amount of time.
After that time, it is reset.

## How could this be used? {#how-could-this-be-used}

This fact could serve as a timer, and when the fact runs out, it could be used to trigger an action.

## Fields {#fields}

## Comment

Inherited Optional

A comment to keep track of what this fact is used for.

## Group

Required

## Duration

Required

The duration after which the fact expires.

Durations can be specified in the following format: `1d 2h 3m 4s`. The following units are supported: `d` for days, `h` for hours,`m` for minutes and `s` for seconds.
