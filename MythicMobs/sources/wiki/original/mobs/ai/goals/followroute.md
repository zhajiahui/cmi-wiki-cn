# Follow Route

## Description {#description}

Makes the mob follow a specific path, one time only.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| points | p | The points of the path, in a x1,y1,z1;x2,y2,z2;x3,y3,z3; syntax |  |
| speed | s | The speed of the movement |  |
| tolerance | t | The minimum distance the mob must be from a point before moving to the next one | 3 |

## Examples {#examples}

```yaml
  AIGoalSelectors:
  - clear
  - followRoute{p=1,0,0;12,0,10}
```

## Aliases {#aliases}

- followPath
