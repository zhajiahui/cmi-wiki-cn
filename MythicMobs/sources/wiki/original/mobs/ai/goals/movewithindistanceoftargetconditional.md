# Move Within Distance Of Target Conditional

## Description {#description}

Works like [MoveWithinDistanceOfTarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveWithinDistanceOfTarget), but the mob only moves while the target and the mob match the given conditions.

## Attributes {#attributes}

Takes every attribute of [MoveWithinDistanceOfTarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveWithinDistanceOfTarget), plus:

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| targetconditions | conditions, cond, c | The conditions the target must match for the mob to start and keep moving |  |
| mobconditions | mconditions, mcond, mc | The conditions the mob itself must match for it to start and keep moving |  |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
  - 0 clear
  - 1 moveWithinDistanceOfTargetConditional{s=1;minrange=4;maxrange=24;targetConditions=[ - isPlayer true ]}
```

## Aliases {#aliases}

- moveWithinConditional
- moveWithinDistanceOfTargetCond
- moveWithinCond
