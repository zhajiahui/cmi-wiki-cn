# Living In Radius

## Description {#description}

Matches a range to how many living entities are in the given radius

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The amount to check for | 1 |
| radius | r | The radius of the search | 5 |

## Examples {#examples}

```yaml
  Conditions:
  - livinginradius{a=<5;r=10} true
```
