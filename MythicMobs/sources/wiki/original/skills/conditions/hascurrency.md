# Hascurrency

## Description {#description}

If the target has the given amount of vault currency

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The amount of currency |  |

## Examples {#examples}

```yaml
  Conditions:
  - hascurrency{a=1000} true
```

## Aliases {#aliases}

- hasmoney
