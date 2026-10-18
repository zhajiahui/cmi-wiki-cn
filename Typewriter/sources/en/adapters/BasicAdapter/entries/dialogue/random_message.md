# Random Message Dialogue

The `Random Message Dialogue` action displays a random message from a list to the player. This action provides you with the ability to create interactive dialogues with randomized responses.

## How could this be used? {#how-could-this-be-used}

This action can be useful in a variety of situations. You can use it to create randomized NPC dialogue, quests with multiple randomized outcomes, or to add a level of unpredictability to your game. The possibilities are endless!

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

Required List Colored Multi-Line Placeholders

The text to display to the player. One will be picked at random.

Colors and formatting from the [`MiniMessage Adventure Api`](https://docs.advntr.dev/minimessage/format.html) can be used. So for example, you can use `<red>Some Text</red>` for red text.

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.
