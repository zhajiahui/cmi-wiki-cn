# Disengage

## Description {#description}

Causes the caster to leap backwards away from the target entity

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| velocity | v, magnitude | The velocity of the leap | 1 |
| velocityy | yvelocity, vy, yv | The y component of the velocity of the leap | 0.01337 |

## Examples {#examples}

```yaml
ExampleMob:
  Skills:
  - disengage @trigger ~onDamaged
```
