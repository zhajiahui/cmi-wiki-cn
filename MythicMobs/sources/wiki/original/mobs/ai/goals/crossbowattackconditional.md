# Crossbow Attack Conditional

## Description {#description}

Works like [crossbowAttack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/crossbowattack), but the mob only shoots while the target and the mob match the given conditions. When the conditions stop matching, the mob stops shooting and keeps its target. Only Piglins and Pillagers can use it.

## Attributes {#attributes}

Takes every attribute of [crossbowAttack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/crossbowattack), plus:

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| targetconditions | conditions, cond, c | The conditions the target must match for the attack to start and continue |  |
| mobconditions | mconditions, mcond, mc | The conditions the mob itself must match for the attack to start and continue |  |

## Examples {#examples}

```yaml
ExampleMob:
  Type: PILLAGER
  Equipment:
  - crossbow HAND
  AIGoalSelectors:
  - 0 clear
  - 1 crossbowAttackConditional{attackradius=16;targetConditions=[ - isPlayer true ]}
```

## Aliases {#aliases}

- crossbowAttackCond
