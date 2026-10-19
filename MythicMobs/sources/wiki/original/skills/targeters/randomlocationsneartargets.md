# Random Locations Near Targets

## Description {#description}

Targets random locations near the inherited targets

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The amount of points | 5 |
| radius | r, maxradius, maxr | The radius in which target points will be generated | 5 |
| minradius | minr | The minimum radius in which target points will be generated | 0 |
| spacing | s | The minimum amount of space between selected targets | 0 |
| onsurface | surface | Whether the selected location should be on a surface that is not air | false |

## Examples {#examples}

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @PIR{r=10}

ExampleSkill2:
  Skills:
  - effect:particles @RandomLocationsNearTargets{a=5;r=2}
```

## Aliases {#aliases}

- randomLocationsNearTarget
- randomLocationsNearTargetEntities
- randomLocationsNearTargetLocations
- RLNT
- RLNTE
- RLNTL
