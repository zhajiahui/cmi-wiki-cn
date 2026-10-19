# Entity Item Type

## Description {#description}

Tests the type of the targeted entity item

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| material | mat, m, type, types, t | A list of items to match |  |

## Examples {#examples}

```yaml
  TargetConditions:
  - entityItemType{m=STONE} true
```
