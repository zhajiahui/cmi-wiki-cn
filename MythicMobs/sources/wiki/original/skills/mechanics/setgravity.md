# Setgravity

## Description {#description}

Sets whether gravity affects the target entity.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| gravity | g, b, bool, u, use | Sets whether the entity uses gravity | true |

## Examples {#examples}

```yaml
  Skills:
  - setgravity{g=false} @self ~onSpawn
  - setusegravity{g=false} @self ~onSpawn
  - ...
```

## Aliases {#aliases}

- setusegravity
