# Match Rotation

## Description {#description}

Sets the target's yaw and pitch to the same value of the specified target attribute

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| target | to, t, location, loc, l, of | The [targeter](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters) |  |

## Examples {#examples}

```yaml
  Skills:
  - matchrotation{target=@Parent} @self
```

## Aliases {#aliases}

- matchrot
