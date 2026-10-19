# Entity Item Is Similar

## Description {#description}

Tests if the item entity is similar to an itemstack

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| item | i, material, m, mm, mythicitem | The item to check against | DIRT |

## Examples {#examples}

```yaml
  TargetConditions:
  - entityitemissimilar{i=MyCustomItem} true
```
