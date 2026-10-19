# Playersinradius

## Description {#description}

Checks how many players are in a radius.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The given range value to check | >0 |
| radius | r, distance, d | The given radius to check | 32 |
| ignorespectator | is | Whether players in spectator mode should be ignored | true |

## Examples {#examples}

```yaml
  Conditions:
  - playersinradius{a=>3;r=16}
```

## Aliases {#aliases}

- pir
- playerInRadius
