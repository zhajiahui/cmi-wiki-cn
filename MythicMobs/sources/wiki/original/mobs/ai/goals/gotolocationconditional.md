# Go To Location Conditional

## Description {#description}

Makes the mob go to a location, but only while the location and the mob match the given conditions. The location can use placeholders, such as a location variable, and the mob follows the new location when the value changes. The mob stops when it gets within `minrange` of the location, when a condition stops matching, or when the location can no longer be read.

A location written as `x,y,z` is in the world the mob is currently in. A location written as `world,x,y,z` only applies while the mob is in that world; in any other world the mob does not move toward it. If a location written directly in the config cannot be read, for example because the world does not exist, the console shows a warning.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| location | loc, l | The location to go to, as `x,y,z` or `world,x,y,z`. Supports placeholders |  |
| speed | s | The speed modifier | 1 |
| minrange | minr, mr | The mob stops moving once it is within this distance of the location | 2 |
| cooldown | cd, interval, i | How often, in ticks, the mob recalculates its path while moving | 5 |
| locationconditions | locconditions, lconditions, lcond, lc | The conditions the location must match |  |
| mobconditions | mconditions, mcond, mc | The conditions the mob itself must match |  |

## Examples {#examples}

Walk to a location stored in a variable, but only while the mob's `state` variable is `returning`:

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
  - 0 clear
  - 1 goToLocationConditional{location=<caster.var.home>;minrange=3;mobConditions=[ - variableEquals{var=caster.state;value=returning} ]}
  Skills:
  - setvariable{var=caster.home;type=LOCATION;value=world,100,64,100} @self ~onSpawn
```

Walk to a fixed location only while it is less than 30 blocks away, at speed 1.5:

```yaml
  AIGoalSelectors:
  - clear
  - gotoCond{location=100,64,100;speed=1.5;locationConditions=[ - distance{d=<30} ]}
```

The location and speed can also be given after the goal name:

```yaml
  AIGoalSelectors:
  - clear
  - gotoCond 100,64,100 1.5
```

## Aliases {#aliases}

- gotoConditional
- goToLocationCond
- gotoCond
