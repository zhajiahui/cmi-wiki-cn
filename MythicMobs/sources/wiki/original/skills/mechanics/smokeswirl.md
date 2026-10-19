# Smoke Swirl

## Description {#description}

Creates a swirling vortex of smoke at the targeted entity or location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| duration | d | How many intervals the swirl will last | 5 |
| interval | i | How many ticks there are between each pulse of smoke | 1 |

## Examples {#examples}

```yaml
SmokeSwirlSkill:
  Skills:
  - smokeswirl{duration=10;interval=10} @TargetLocation
```

## Aliases {#aliases}

- effect:smokeswirl
- e:smokeswirl
