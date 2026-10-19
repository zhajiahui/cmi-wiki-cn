# Mobsinchunk

## Description {#description}

Matches a range to how many mobs are in the target location's chunk

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The number range to match | 0 |

## Examples {#examples}

```yaml
  Conditions:
  - mobsinchunk{a=1to5} true
```

```yaml
  Conditions:
  - mobsinchunk{a=<5} true
```
