# Detect Command Ran Event

The `Detect Command Ran Event` event is triggered when an **already existing** command is ran.

**caution**

This event only works if the command already exists. If you are trying to make a new command that does not exist already, use the [`Run Command Event`](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_run_command) instead.

## How could this be used? {#how-could-this-be-used}

This event could be used to trigger a response when a specific command has been run.
For example, you could have a command that sends a message to a channel when a command has been run,
which could be used as an audit log for your admins.

## Fields {#fields}

## Triggers

Required List

## Command

Required Regex

The command to listen for.
This can be partial, so if you wanted to listen for any warp command,
you could use `warp` as the command.
However, this can also include parameters, so if you
wanted to listen if the player warps to spawn, you could use
`warp spawn` as the command.

  

**caution**

Do not include the `/` at the start of the command.
This will be added automatically.

[`Regular expressions`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) can be used to match a pattern. For example, `^.*$` will match any string.

## Cancel

Required

Cancel the event when triggered
