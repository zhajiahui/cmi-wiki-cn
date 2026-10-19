# Damagetag

## Description {#description}

Checks whether the damage that caused the current skill tree has a specific tag

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| tag | t | The tag to check against |  |
| value | val, v, b, bool, boolean | If true, checks for the presence of the tag If false, checks for its absence | true |

## Examples {#examples}

```yaml
Conditions:
- damageTag{tag=WITCHCURSES}
```

Used to check the damage tag specified in the [Damage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/damage) mechanic or mechanics inheriting its attributes

## Aliases {#aliases}

- damagehastag
