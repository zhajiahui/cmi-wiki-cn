# Random Locations Near Origin

## Description {#description}

Targets random locations near the origin of the metaskill

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
  - projectile{...;
    onEnd=[
      - effect:particles @RandomLocationsNearOrigin{a=10;r=4;minr=1}
    ]}
```

## Aliases {#aliases}

- RLO
- randomLocationsOrigin
- RLNO
