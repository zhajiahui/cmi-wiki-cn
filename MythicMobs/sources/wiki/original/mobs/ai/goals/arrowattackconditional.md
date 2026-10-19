# Arrow Attack Conditional

## Description {#description}

Works like [rangedAttack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/arrowattack), but the mob only shoots while the target and the mob match the given conditions. When the conditions stop matching, the mob stops shooting and keeps its target.

## Attributes {#attributes}

Takes every attribute of [rangedAttack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/arrowattack), plus:

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| targetconditions | conditions, cond, c | The conditions the target must match for the attack to start and continue |  |
| mobconditions | mconditions, mcond, mc | The conditions the mob itself must match for the attack to start and continue |  |

## Examples {#examples}

```yaml
ExampleMob:
  Type: SKELETON
  AIGoalSelectors:
  - 0 clear
  - 1 arrowAttackConditional{targetConditions=[ - isPlayer true ]}
```

## Aliases {#aliases}

- arrowAttackCond
- rangedAttackConditional
- rangedAttackCond
