# Message Action

The `Send Message Action` is an action that sends a message to a player.
You can specify the speaker, and the message to send.

This should not be confused with the (Message Dialogue)[../dialogue/message].
(Message Dialogue)[../dialogue/message] will replace the current dialogue with the message, while this action will not.

## How could this be used? {#how-could-this-be-used}

This action can be useful in a variety of situations.
You can use it to create text effects in response to specific events, such as completing actions or anything else.
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

## Speaker

Required

The speaker of the message

## Message

Required Multi-Line Placeholders

The message to send

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.
