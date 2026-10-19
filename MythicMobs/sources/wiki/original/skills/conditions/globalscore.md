# Globalscore

## Description {#description}

Checks a global scoreboard value (the value associated with the fake player **GLOBAL**)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| objective | obj, o | The objective |  |
| value | val, v | The value to match |  |

## Examples {#examples}

```yaml
  Conditions:
  - globalscore{o=KillCount;value=5} true
```

## Aliases {#aliases}

- scoreglobal
