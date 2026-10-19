# Bow Attack Conditional

## Description {#description}

Works like [bowattack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/bowattack), but the mob only shoots while the target and the mob match the given conditions. When the conditions stop matching, the mob stops shooting and keeps its target.

## Attributes {#attributes}

Takes every attribute of [bowattack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/bowattack), plus:

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
  - 1 bowAttackConditional{targetConditions=[ - isPlayer true ];mobConditions=[ - health{h=>10} ]}
```

## Aliases {#aliases}

- bowAttackCond
- skeletonBowAttackConditional
- bowshootConditional
- bowmasterConditional
