# Material Is On Cooldown

## Description {#description}

Checks if the target player's specified material is on cooldown.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| material | mat, m | The material to check for | enderpearl |

## Examples {#examples}

```yaml
  TargetConditions:
  - materialIsOnCooldown{mat=STONE} true
```

## Aliases {#aliases}

- materialCooldown
- matCooldown
