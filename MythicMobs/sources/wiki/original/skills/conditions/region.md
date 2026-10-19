# Region

## Description {#description}

Checks if the target is within the given WorldGuard region.

> When creating a region via the `/rg create` command the name will *always* be lowercase, regardless of what you wrote in the command. So, when you need to check against such a region via this condition, remember to write its name in lowercase too

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| region | r, name, n | The region to check |  |

## Examples {#examples}

```yaml
  Conditions:
  - region{r=someregion} true
```

## Aliases {#aliases}

- inregion
