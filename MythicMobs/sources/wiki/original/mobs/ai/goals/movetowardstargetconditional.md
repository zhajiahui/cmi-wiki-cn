# Move Towards Target Conditional

## Description {#description}

Paths to an entity that checks some conditions

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speed | s | The speed modifier | 1 |
| minrange | minr, mr | The minimum range from the target entity. The mob stops moving once it is within this distance | 0 |
| maxrange | range, r | The maximum range from the target entity | 32.0 |
| targetconditions | conditions, cond, c | The conditions the target entity must match |  |
| mobconditions | mconditions, mcond, mc | The conditions the mob itself must match |  |

## Examples {#examples}

```yaml
  AIGoalSelectors:
  - clear
  - MoveTowardsTargetConditional{s=2;maxrange=6;targetConditions=[
    - isPlayer true
    ]}
```

## Aliases {#aliases}

- moveTowardsTargetCond
