# Level

## Description {#description}

Checks the target MythicMob's level

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| level | l | The level range to match |  |

## Examples {#examples}

```yaml
  Conditions:
  - level{l=10} true
```

```yaml
  Conditions:
  - level{l=>10} true
```

```yaml
  Conditions:
  - level{l=1to10} true
```

```yaml
  Conditions:
  - level{l=<10} true
```
