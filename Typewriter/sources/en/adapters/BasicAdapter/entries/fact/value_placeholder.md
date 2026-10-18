# Value Placeholder Fact

A [fact](https://docs.typewritermc.com/docs/creating-stories/facts) that is computed from a placeholder.
This placeholder is evaluated when the fact is read and can return anything.
The value will be computed based on the `values` specified.

This fact can only be **read**, not written to. Hence, it is only suitable for criteria.

## How could this be used? {#how-could-this-be-used}

If you only want to run certain actions if the player is in creative mode.
Or depending on the weather, change the dialogue of the NPC.

## Fields {#fields}

## Comment

Inherited Optional

A comment to keep track of what this fact is used for.

## Group

Required

## Placeholder

Required Placeholders

Placeholder to parse (e.g. %player_gamemode%

Placeholders from the [`PlaceholderApi`](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) can be used. So for example, you can use `%player_name%` for the player name.

## Values

Required Regex

The values to match the placeholder with and their corresponding fact value.

An example would be:

```yaml
values:
SURVIVAL: 0
CREATIVE: 1
ADVENTURE: 2
SPECTATOR: 3
```

If the placeholder returns `CREATIVE`, the fact value will be `1`.
If no value matches, the fact value will be `0`.

Values can have placeholders inside them.

[`Regular expressions`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) can be used to match a pattern. For example, `^.*$` will match any string.
