# Random Spoken Dialogue

The `Random Spoken Dialogue` action displays a randomly selected animated message to the player.

## How could this be used? {#how-could-this-be-used}

Let's say you have an NPC in your game who tells jokes to the player.
You could use the Random Spoken Dialogue action
to randomly select a joke from a list of possible jokes and have the NPC "tell"
it to the player using an animated message.

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

## Messages

Required List Colored Placeholders

A list of messages to display to the player. Every time the dialogue is triggered, one of these messages will be picked at random.

Colors and formatting from the [`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html) can be used. So for example, you can use `<red>Some Text</red>` for red text.

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.

## Duration

Required

The duration it takes to type out the message.

Durations can be specified in the following format: `1d 2h 3m 4s`. The following units are supported: `d` for days, `h` for hours,`m` for minutes and `s` for seconds.
