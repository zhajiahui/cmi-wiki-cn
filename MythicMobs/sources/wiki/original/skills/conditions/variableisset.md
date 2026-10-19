# Variableisset

## Description {#description}

Checks if the given [variable](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables) is set.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| variable | name, n, var, key, k | The name of the variable. Can optionally be prefixed with scope |  |
| scope | s | The [scope](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-scopes) of the variable, e.g. where the variable is located |  |

## Examples {#examples}

```yaml
  Conditions:
  - variableisset{var=target.dazed} true
```

## Aliases {#aliases}

- varisset
- varset
