# Worldtime

## Description {#description}

Matches a range against the target location's world's time.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| time | t | A range of time to check | 0 |

## Examples {#examples}

```yaml
  Conditions:
  - worldtime{t=0to6000} true
```
