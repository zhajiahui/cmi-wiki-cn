# Playersinworld

## Description {#description}

Matches the number of players in the caster's world

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The number of players to check for. Can be a range | 0 |

## Examples {#examples}

```yaml
  Conditions:
  - playersInWorld{amount=>5}
```
