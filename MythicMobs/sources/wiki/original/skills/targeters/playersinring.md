# Players In Ring

## Description {#description}

Targets all players in a ring around the caster.  
The targeted players will be the ones at a distance from the caster between the minimum and the maximum range.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| minrange | min | The minimum range of the ring | 5 |
| maxrange | max | The maximum range of the ring | 10 |

## Examples {#examples}

```yaml
  Skills:
  - ignite @PlayersInRing{min=2;max=10}
```

## Aliases {#aliases}

- pring
