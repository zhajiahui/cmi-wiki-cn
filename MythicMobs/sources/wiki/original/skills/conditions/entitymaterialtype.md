# Entity Material Type

## Description {#description}

Tests the material of the targeted entity item

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| material | mat, m, type, types, t | A list of materials to match |  |

## Examples {#examples}

```yaml
  TargetConditions:
  - entityMaterialType{mat=STONE,DIRT} true
```
