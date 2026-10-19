# Fleesun

## Description {#description}

Causes the mob to flee from the sun and hide in shade.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speed | s | The speed at which to move towards shade | 1 |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleesun{s=2}
```
