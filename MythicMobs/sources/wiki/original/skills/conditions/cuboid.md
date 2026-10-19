# Cuboid

## Description {#description}

Whether the target is within a cuboid that has `location1` and `location2` as opposite vertices

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| location1 | loc1, l1, a | x,y,z coordinates for the 1st point. |  |
| location2 | loc2, l2, b | x,y,z coordinates for the 2nd point. |  |
| relative | r | Whether or not the coordinates should be relative to the caster | false |

## Examples {#examples}

```yaml
  TargetConditions:
  - cuboid{location1=x,y,z;location2=x,y,z;relative=true}
```

## Aliases {#aliases}

- incuboid
