# Crossbowattack

## Description {#description}

Attack with a crossbow. Only Piglins and Pillagers can use crossbowAttack goal as long as they're holding a crossbow.

### Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speed | s | Movement speed modifier | 1 |
| attackradius | radius, r | The distance from which the mob starts shooting | 8 |

### Examples {#examples}

```yaml
ExampleMob:
  Type: Piglins
  Equipment:
    - crossbow HAND
  AIGoalSelectors:
    - clear
    - crossbowAttack
```
