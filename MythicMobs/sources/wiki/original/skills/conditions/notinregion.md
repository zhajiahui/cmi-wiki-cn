# Notinregion

## Description {#description}

Checks if the target location is **not** within the given WorldGuard region

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| region | r, name, n | The region's name |  |

## Examples {#examples}

```yaml
  Conditions:
  - notinregion{r=BossZone} true
```
