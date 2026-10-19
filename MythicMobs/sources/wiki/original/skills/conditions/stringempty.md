# String Empty

## Description {#description}

Checks if the provided string is empty

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| value | val, v, string, s | The string to check |  |

## Example {#example}

```yaml
  Conditions:
  - stringEmpty{value=<caster.var.examplevariable>}
```

> Checks if the value of the <caster.var.examplevariable> placeholder is an empty string

## Aliases {#aliases}

- isEmpty
