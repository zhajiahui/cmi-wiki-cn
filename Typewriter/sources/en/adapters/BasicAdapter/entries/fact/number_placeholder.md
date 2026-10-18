# Number Placeholder Fact

A [fact](https://docs.typewritermc.com/docs/creating-stories/facts) that is computed from a placeholder.
This placeholder is evaluated when the fact is read and must return a number or boolean.

This fact can only be **read**, not written to. Hence, it is only suitable for criteria.

## How could this be used? {#how-could-this-be-used}

Make sure the player has a high enough level.
Then allow them to start a quest or enter a dungeon.

## Fields {#fields}

## Comment

Inherited Optional

A comment to keep track of what this fact is used for.

## Group

Required

## Placeholder

Required Placeholders

The placeholder to parse.
For example %player_level%.

**caution**

Only placeholders that return a number or boolean are supported!
If you want to use a placeholder that returns a string,
use the [ValuePlaceholderFactEntry](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/value_placeholder) instead.

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.
