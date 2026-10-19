# Oxygen

## Description {#description}

Gives the target player an amount of oxygen.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | the amount of oxygen to give the player | 1 |

## Examples {#examples}

```yaml
  Skills:
  - oxygen{amount=10} @trigger ~onInteract
```
