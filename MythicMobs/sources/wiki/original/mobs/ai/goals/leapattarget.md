# Leapattarget

## Description {#description}

Causes the mob to leap towards its target.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speed | s | The speed at which to leap at the target | 1.2 |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - leapattarget{s=4}
```

## Aliases {#aliases}

- leaptowardstarget
