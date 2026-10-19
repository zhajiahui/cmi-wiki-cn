# Lunge

## Description {#description}

Applies forward directional velocity to the target.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| velocity | v, magnitude | The horizontal velocity at which the entity is moved forward | 1 |
| velocityY | vy, yv, yvelocity | The vertical velocity at which the entity is moved forward | 1 |
| oldmath | old, o | If the lunge mechanic should use the old math formula | false |

## Examples {#examples}

```yaml
  Skills:    
  - lunge{velocity=15;velocityY=5} @Self
```
