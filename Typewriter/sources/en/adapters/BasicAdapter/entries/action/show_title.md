# Show Title Action

The `Show Title Action` is an action that shows a title to a player. You can specify the subtitle, and durations if needed.

## How could this be used? {#how-could-this-be-used}

This action can be useful in a variety of situations. You can use it to create text effects in response to specific events, such as completing questions or anything else. The possibilities are endless!

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Modifiers

Inherited List

A list of facts that will be modified for the player when this entry is triggered.

## Triggers

Required List

## Title

Required Colored Placeholders

The title text to show.

Colors and formatting from the [`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html) can be used. So for example, you can use `<red>Some Text</red>` for red text.

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.

## Subtitle

Required Colored Placeholders

The subtitle text to show.

Colors and formatting from the [`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html) can be used. So for example, you can use `<red>Some Text</red>` for red text.

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.

## Durations

Optional

Duration of the title: Fade in, how long it stays, fade out.
