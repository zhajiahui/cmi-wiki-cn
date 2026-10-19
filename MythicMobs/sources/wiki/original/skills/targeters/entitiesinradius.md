# Entities In Radius

## Description {#description}

Targets all entities in the given radius around the caster

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| shape |  | The "shape" in which to fetch entities. Can be any [shape](https://wiki.mythiccraft.io/mythicmobs/Enum/Shape) | SPHERE |
| livingonly | living, l | Whether the targeter should target only living entities | true |

## Examples {#examples}

```yaml
  Skills:
  - ignite @EIR{r=10}
```

## Aliases {#aliases}

- livingEntitiesInRadius
- livingInRadius
- allInRadius
- EIR
- entitiesnearby
- nearbyentities
