# Food Level

## Description {#description}

Checks the food amount of the target

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a, food, f | Range of amount of food to check for | 0 |

## Examples {#examples}

```yaml
  TargetConditions:
  - FoodLevel{a=<10} true
```

## Aliases {#aliases}

- hunger
- food
- hungerlevel
