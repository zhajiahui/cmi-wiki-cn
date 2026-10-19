# Localdifficulty

## Description {#description}

Tests the difficulty scale at the target location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| difficulty | diff, d | The difficulty range to check |  |

## Examples {#examples}

```yaml
  Conditions:
  - localdifficulty{d=>0}
```
