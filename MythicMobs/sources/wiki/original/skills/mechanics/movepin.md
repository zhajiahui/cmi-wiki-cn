# Move Pin

## Description {#description}

Moves the given [pin](https://wiki.mythiccraft.io/mythicmobs/Pins) to the target location.  
Cannot move MultiPins.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| pin | p | The pin to move |  |

## Examples {#examples}

```yaml
  Skills:
  - movepin{pin=example} @selflocation
```

> Moves the pin named "example" to the current location of the caster
