# Boss Bar

The `BossBarEntry` is a display that shows a bar at the top of the screen.

## How could this be used? {#how-could-this-be-used}

This could be used to show objectives in a quest, or to show the progress of a task.

## Fields {#fields}

## Title

Required Colored Placeholders

The title of the boss bar

Colors and formatting from the [`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html) can be used. So for example, you can use `<red>Some Text</red>` for red text.

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.

## Progress

Required

How filled up the bar is. 0.0 is empty, 1.0 is full.

## Color

Required

The color of the boss bar

## Style

Required

If the bossbar has notches

## Flags

Required List

Any flags to apply to the boss bar
