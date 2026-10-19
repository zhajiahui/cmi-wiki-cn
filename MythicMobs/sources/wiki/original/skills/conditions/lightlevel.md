# Lightlevel

## Description {#description}

Tests the light level at the target location

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| level | l | The level range to match | 0 |

## Examples {#examples}

```yaml
  Conditions:
  - lightlevel{l=10} true
```

```yaml
  Conditions:
  - lightlevel{l=>10} true
```

```yaml
  Conditions:
  - lightlevel{l=1to10} true
```
