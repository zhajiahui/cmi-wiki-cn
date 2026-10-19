# Move Within Distance Of Target

## Description {#description}

Moves towards the target to be within a certain range

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speed | s | The speed modifier | 1 |
| minrange | minrange, range, r, distance, d | The minimum range from the target entity | 10.0 |
| maxrange | maxrange, maxr | The maximum range from the target entity | 32.0 |

## Examples {#examples}

```yaml
  AIGoalSelectors:
  - clear
  - MoveWithinDistanceOfTarget{s=2;minrange=3;maxrange=6}
```

## Aliases {#aliases}

- moveWithin
