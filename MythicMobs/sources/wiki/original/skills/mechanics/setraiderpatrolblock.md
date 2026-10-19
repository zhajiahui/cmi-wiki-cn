# Setraiderpatrolblock

## Description {#description}

Sets the target raider to patrol the given location

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| location | block, l, b | A [Location Targeter](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#single-location-targeters), whose targeted location will be the specified one |  |

## Examples {#examples}

```yaml
  Skills:
  - setRaiderPatrolBlock{l=@TrackedLocation} @self
```

## Aliases {#aliases}

- setRaiderBlock
