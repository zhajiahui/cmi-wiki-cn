# Spoken Dialogue

The `Spoken Dialogue Action` is an action that displays an animated message to the player. This action provides you with the ability to display a message with a specified speaker, text, and duration.

## How could this be used? {#how-could-this-be-used}

This action can be useful in a variety of situations. You can use it to create storylines, provide instructions to players, or create immersive roleplay experiences. The possibilities are endless!

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Modifiers

Inherited List

A list of facts that will be modified for the player when this entry is triggered.

## Triggers

Required List

## Speaker

Required

## Text

Required Colored Multi-Line Placeholders

The text to display to the player.

Colors and formatting from the [`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html) can be used. So for example, you can use `<red>Some Text</red>` for red text.

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.

## Duration

Required

The duration it takes to type out the message.

Durations can be specified in the following format: `1d 2h 3m 4s`. The following units are supported: `d` for days, `h` for hours,`m` for minutes and `s` for seconds.
