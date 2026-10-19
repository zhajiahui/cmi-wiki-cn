# Pin

## Description {#description}

Targets the location of a [Pin](https://wiki.mythiccraft.io/mythicmobs/Pins).
If the Pin is a Multi-Pin made via a Pin Wand, this targets all of the associated locations.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| name | n, pin, p, key, k | The name of the [pin](https://wiki.mythiccraft.io/mythicmobs/Pins) to target |  |
| random | r | Whether to select a single and random location, if the specified pin is a Multi-Pin | false |

## Examples {#examples}

```yaml
  Skills:
  - teleport @Pin{p=mypin}
```
