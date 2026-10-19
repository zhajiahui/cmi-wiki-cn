# Nearclaim

## Description {#description}

Checks if the target location is near any claims of any supported plugins.

Supported Plugins:

- GriefPrevention
- Lands
- CrashClaim

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The given range to check | 16 |

## Example {#example}

```yaml
  Conditions:
  - nearclaim{r=20} false
```

## Aliases {#aliases}

- nearClaims
