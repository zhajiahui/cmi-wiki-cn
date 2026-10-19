# Altitude

## Description {#description}

This condition tests how far above the ground the target entity is.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| height | altitude, a, h | The height range to check |  |
| maxHeight | mH | Limits the maximum height this condition can checks for | 30 |

## Examples {#examples}

```yaml
Conditions:
- altitude{h=3-5} true
```

## Aliases {#aliases}

- heightfromsurface
