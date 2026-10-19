# Set Interaction Size

## Description {#description}

Sets the size of the target `INTERACTION` [Type](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#type) entity.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| height | h | The value to set the height to | 1 |
| width | w | The value to set the width to | 1 |

## Examples {#examples}

The following would set the size of the casting interaction entity to a 2x3 when right clicked

```yaml
ExampleInteractionEntity:
  Type: INTERACTION
  Skills:
  - setInteractionSize{height=2;width=3} @self ~onInteract
```

## Aliases {#aliases}

- interactionSize
