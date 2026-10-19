# Moisturelevel

## Description {#description}

Checks if the target block of farmland has the specified level of hydratation.

- `0` means that the farmland is not hydratated
- `1-6` means that a once hydratated farmland is gradualy losing its hydratation after removing its access to water
- `7` is for a fully hydratated farmland.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| l | moistness, m | The level of hydratation to check for |  |

## Examples {#examples}

```yml
  TargetConditions:
  - moisturelevel{l=3} true
```

```yml
  TargetConditions:
  - moistureness{l=1to6} true
```

## Aliases {#aliases}

- moistureness
- moistness
