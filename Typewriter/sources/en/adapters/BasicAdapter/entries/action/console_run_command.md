# Console Command Action

The Console Command Action is an action that sends a command to the server console. This action provides you with the ability to execute console commands on the server in response to specific events.

## How could this be used? {#how-could-this-be-used}

This action can be useful in a variety of situations. You can use it to perform administrative tasks, such as sending a message to all players on the server, or to automate server tasks, such as setting the time of day or weather conditions. The possibilities are endless!

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
