# Playersonline

## Description {#description}

Matches the number of players online

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The number of players to check for. Can be a range | 0 |

## Examples {#examples}

```yaml
  Conditions:
  - playersOnline{amount=>5}
```

## Aliases {#aliases}

- onlineplayercount
- onlineplayers
