# Zdiff

## Description {#description}

Checks the difference in z value between the target entity and the caster.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| difference | diff, d | The z difference to check |  |

## Examples {#examples}

```yaml
  TargetConditions:
  - zDiff{diff=>5} true
```
