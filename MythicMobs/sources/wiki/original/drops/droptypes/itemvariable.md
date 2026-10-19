# Item Variable

## Description {#description}

Drops the item defined in the specified item variable

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| variable | var, name, n | The scope and name of the item variable to fetch, in the scope.name format |  |

## Examples {#examples}

```yaml
  Drops:
  - itemvariable{variable=caster.stolenitem} 1 1
```

## Aliases {#aliases}

- itemvar
