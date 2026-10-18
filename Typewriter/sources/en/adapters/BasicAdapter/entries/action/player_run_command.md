# Player Command Action

The `Player Command Action` is an action that runs a command as if the player entered it.
This action provides you with the ability to execute commands on behalf of the player in response to specific events.

## How could this be used? {#how-could-this-be-used}

This action can be useful in a variety of situations.
You can use it to provide players with a custom command that triggers a specific action,
such as teleporting the player to a specific location or giving them an item.
You can also use it to automate repetitive tasks,
such as sending a message to the player when they complete a quest or achievement.
The possibilities are endless!

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Modifiers

Inherited List

A list of facts that will be modified for the player when this entry is triggered.

## Triggers

Required List

## Command

Required Multi-Line Placeholders

Every line is a different command. Commands should not be prefixed with `/`.

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.
