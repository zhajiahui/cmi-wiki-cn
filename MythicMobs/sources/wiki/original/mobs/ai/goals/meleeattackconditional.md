# Melee Attack Conditional

## Description {#description}

Causes the mob to move to and melee attack its target, but only while the target matches the given conditions. Pair it with [MoveTowardsTargetConditional](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveTowardsTargetConditional) and its `minrange` to make a mob keep its distance until the target comes close.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speedmodifier | speed, s | The speed modifier for the mob while this action is being taken | 1 |
| followUnseen | fu | Should the target be followed even if it is hidden from view | false |
| targetconditions | conditions, cond, c | The conditions the target entity must match for the attack to start and continue |  |
| mobconditions | mconditions, mcond, mc | The conditions the mob itself must match for the attack to start and continue |  |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
  - 0 clear
  - 1 meleeAttackConditional{targetConditions=[ - distance{d=<3} ]}
  - 2 MoveTowardsTargetConditional{s=1;minrange=10;maxrange=80;targetConditions=[ - isPlayer true ]}
```

## Aliases {#aliases}

- meleeAttackCond
