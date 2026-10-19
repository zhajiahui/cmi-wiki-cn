# Random Locations Near Caster

## Description {#description}

Targets random locations near the caster

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The amount of points | 5 |
| radius | r, maxradius, maxr | The radius in which target points will be generated | 5 |
| minradius | minr | The minimum radius in which target points will be generated | 0 |
| spacing | s | The minimum amount of space between selected targets | 0 |
| onSurface | onsurf, os | Only target locations above solid blocks | false |

## Examples {#examples}

```yaml
ExampleSkill:
  Skills:
  - effect:particles @RandomLocationsNearCaster{a=5;r=2}
```

## Aliases {#aliases}

- randomLocations
- RLNC
