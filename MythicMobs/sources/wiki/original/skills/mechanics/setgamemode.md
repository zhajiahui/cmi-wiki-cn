# Setgamemode

## Description {#description}

Sets the gamemode of the target player. Does nothing if the target is
not a player. Requires the `sync=true` attribute.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| mode | m | The gamemode to change the target to. | SURVIVAL |

## Examples {#examples}

```yaml
  Skills:
  - setgamemode{m=CREATIVE;sync=true} @PlayersInRadius{r=10} ~onSpawn
  - ...
```
