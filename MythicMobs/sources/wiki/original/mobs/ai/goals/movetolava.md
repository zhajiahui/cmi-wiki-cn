# Movetolava

## Description {#description}

Causes the mob to move towards lava.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speed | s | The speed at which to move | 0.9 |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - movetolava{s=2}
```

## Aliases {#aliases}

- gotolava
