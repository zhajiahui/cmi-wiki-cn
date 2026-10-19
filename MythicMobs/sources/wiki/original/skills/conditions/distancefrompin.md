# Distance From Pin

## Description {#description}

Checks if the target is within a certain distance of a specified [pin](https://wiki.mythiccraft.io/mythicmobs/Pins)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| pin | p | The pin to check against |  |
| distance | d | The distance to check against. Can be a range. |  |

## Examples {#examples}

```yaml
  Conditions:
  - distanceFromPin{pin=example_pin;d=>10} true
```
