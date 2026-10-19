# Player Locations In Radius

## Description {#description}

Targets the locations of all players in a given radius around the caster

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the targeter | 5 |
| yoffset | y | The y offset of the targeted locations | 0 |

## Examples {#examples}

```yaml
  Skills:
  - effect:particles @PlayerLocationsInRadius{r=10}
```

## Aliases {#aliases}

- LocationRadius
- PLIR
- PLR
