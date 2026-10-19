# Food Saturation

## Description {#description}

Checks the food saturation amount of the target

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a, food, f, saturation, s | Range of amount of food saturation to check for | 0 |

## Examples {#examples}

```yaml
  TargetConditions:
  - FoodSaturation{a=<1} true
```

## Aliases {#aliases}

- hungerSaturation
