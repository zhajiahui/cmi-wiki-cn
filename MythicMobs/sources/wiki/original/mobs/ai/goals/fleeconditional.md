# Fleeconditional

## Description {#description}

****This is a Premium only feature****  
Causes the mob to flee based on provided conditions.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| distance | d | The distance for mobs to be from the mob itself | 4 |
| speed | s | The speed at which to flee | 1.2 |
| safespeed | ss | The speed at which to flee once a safe distance (50 blocks) away | 1 |
| targetconditions | fleeconditions, conditions, cond, c | The conditions an entity must match for the mob to flee from it |  |
| mobconditions | mconditions, mcond, mc | The conditions the mob itself must match for it to flee |  |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleeConditional{distance=5;speed=2;safespeed=2;conditions=[ - inlineofsight true ]}
```

## Aliases {#aliases}

- fleeif
