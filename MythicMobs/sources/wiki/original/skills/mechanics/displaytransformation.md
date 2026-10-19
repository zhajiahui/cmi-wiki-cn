# Display Transformation

## Description {#description}

Sets the targeted display entity's transformations

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| action | a | The action to use. Can be `SET`, `ADD`, `MULTIPLY`, `DIVIDE` | SET |
| transformationtype | transformation, type, tt | The type of the transformation. Can be `TRANSLATION`, `SCALE`, `RIGHT_ROTATION`, `LEFT_ROTATION` | TRANSLATION |
| value | val | The value of the transformation | 0,0,0 |

## Examples {#examples}

```yaml
ExampleDisplayEntity:
  Type: block_display
  Skills:
  # sets the translation transform to `0,0,1` after 10 seconds the entity spawns
  - displaytransformation{action=set;transformation=translation;value=0,0,1;delay=200} @self ~onSpawn

  # rotates the item display along the y-axis (similar to a dropped item)
  - displaytransformation{action=MULTIPLY;transformation=LEFT_ROTATION;val=0,0.707,0,0.707} @self ~onTimer:10
```

## Aliases {#aliases}

- settransformation
- transformation
