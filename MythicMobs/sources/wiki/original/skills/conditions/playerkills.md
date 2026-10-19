# Playerkills

## Description {#description}

Matches how many players the target mob has killed.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| kills | k | The number range to match | 0 |

## Examples {#examples}

```yaml
  Conditions:
  - playerkills{k=>10} true
```
