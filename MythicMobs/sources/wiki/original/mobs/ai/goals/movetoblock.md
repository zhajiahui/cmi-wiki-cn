# Movetoblock

## Description {#description}

Makes the mob move towards the specified block type.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| material | m, mat | The block type to target | IRON_ORE |
| radius | r, search, searchrange | The radius in which to search for the block | 8 |
| radiusy | ry, verticalsearchrange, vsearch, yr, yradius | The y radius in which to search for the block | 2 |
| speed | s | The speed of movement | 0.9 |

### Examples {#examples}

```yaml
ExampleMob:
  Type: Pig
  AIGoalSelectors:
    - clear
    - moveToBlock{material=STONE;radius=8;radiusY=2;speed=0.9}
```

## Aliases {#aliases}

- gotoblock
